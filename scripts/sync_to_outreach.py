#!/usr/bin/env python3
"""
Sync project status updates to an external Outreach folder.

Runs automatically via git post-commit hook. Detects which projects changed,
reads current state, and writes a manifest to ~/Desktop/Outreach/project_updates.json.

Can also be run manually: python scripts/sync_to_outreach.py

To set up as a post-commit hook:
    ln -sf ../../scripts/sync_to_outreach.py .git/hooks/post-commit
    chmod +x scripts/sync_to_outreach.py
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = REPO_ROOT / "state" / "projects.json"
OUTREACH_DIR = Path.home() / "Desktop" / "Outreach"
MANIFEST_FILE = OUTREACH_DIR / "project_updates.json"


def get_changed_files_from_commit():
    """Get files changed in the most recent commit."""
    try:
        result = subprocess.run(
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return result.stdout.strip().splitlines() if result.returncode == 0 else []
    except Exception:
        return []


def get_uncommitted_changes():
    """Get files with uncommitted changes (staged + unstaged, tracked files only)."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return result.stdout.strip().splitlines() if result.returncode == 0 else []
    except Exception:
        return []


def get_commit_info():
    """Get the latest commit hash and message."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H|%s|%ai"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        if result.returncode == 0 and result.stdout.strip():
            parts = result.stdout.strip().split("|", 2)
            return {
                "hash": parts[0][:8],
                "message": parts[1] if len(parts) > 1 else "",
                "date": parts[2] if len(parts) > 2 else "",
            }
    except Exception:
        pass
    return {"hash": "unknown", "message": "", "date": ""}


def detect_affected_projects(changed_files):
    """Map changed files to project IDs."""
    affected = set()
    for f in changed_files:
        if f.startswith("projects/"):
            parts = f.split("/")
            if len(parts) >= 2:
                affected.add(parts[1])
        elif f.startswith("state/"):
            affected.add("__state__")
    return sorted(affected)


def load_project_state():
    """Load current project status from state/projects.json."""
    if not STATE_FILE.exists():
        return []
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def categorize_changes(files):
    """Categorize changed files into meaningful buckets."""
    categories = set()
    for f in files:
        lower = f.lower()
        if "/dashboard/" in lower or "app.py" in lower:
            categories.add("dashboard")
        elif "/export/" in lower or "/exports/" in lower:
            categories.add("exports")
        elif "/scraper" in lower or "/downloader" in lower:
            categories.add("scrapers")
        elif "/test" in lower:
            categories.add("tests")
        elif "/outreach/" in lower or "pitch" in lower:
            categories.add("outreach_materials")
        elif "readme" in lower or "methodology" in lower or "/docs/" in lower:
            categories.add("documentation")
        elif "/normalization/" in lower or "cross_link" in lower:
            categories.add("data_processing")
        elif "/validation/" in lower or "schema" in lower or "quality" in lower:
            categories.add("validation")
        elif "/storage/" in lower or "database" in lower:
            categories.add("database")
        elif "/data/raw/" in lower:
            categories.add("raw_data")
        elif "cli.py" in lower:
            categories.add("cli")
        else:
            categories.add("other")
    return sorted(categories)


def build_manifest(projects, affected, commit_info, changed_files):
    """Build the manifest that gets written to the outreach folder."""
    project_summaries = []
    for p in projects:
        summary = {
            "id": p["id"],
            "name": p["name"],
            "status": p["status"],
            "record_count": p.get("record_count", 0),
            "test_count": p.get("test_count", 0),
            "data_sources": p.get("data_sources", []),
            "target_buyers": p.get("target_buyers", []),
            "target_researchers": p.get("target_researchers", []),
            "description": p.get("description", ""),
            "notes": p.get("notes", ""),
            "changed_in_this_commit": p["id"] in affected,
        }
        project_summaries.append(summary)

    changes_by_project = {}
    for proj_id in affected:
        if proj_id == "__state__":
            continue
        proj_files = [f for f in changed_files if f.startswith(f"projects/{proj_id}/")]
        categories = categorize_changes(proj_files)
        if categories:
            changes_by_project[proj_id] = categories

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(REPO_ROOT),
        "last_commit": commit_info,
        "affected_projects": [p for p in affected if p != "__state__"],
        "changes_by_project": changes_by_project,
        "total_projects": len(projects),
        "client_ready_count": sum(1 for p in projects if p["status"] == "client-ready"),
        "projects": project_summaries,
    }


def main():
    if not OUTREACH_DIR.exists():
        print(f"[sync] Outreach directory not found: {OUTREACH_DIR}")
        print(f"[sync] Create it with: mkdir -p {OUTREACH_DIR}")
        return 1

    projects = load_project_state()
    commit_changed = get_changed_files_from_commit()
    uncommitted = get_uncommitted_changes()
    commit_info = get_commit_info()

    all_changed = list(set(commit_changed + uncommitted))
    affected = detect_affected_projects(all_changed)

    manifest = build_manifest(projects, affected, commit_info, all_changed)

    # Add uncommitted changes section
    uncommitted_projects = detect_affected_projects(uncommitted)
    uncommitted_projects = [p for p in uncommitted_projects if p != "__state__"]
    if uncommitted_projects:
        uncommitted_detail = {}
        for proj_id in uncommitted_projects:
            proj_files = [f for f in uncommitted if f.startswith(f"projects/{proj_id}/")]
            uncommitted_detail[proj_id] = {
                "categories": categorize_changes(proj_files),
                "file_count": len(proj_files),
            }
        manifest["uncommitted_changes"] = {
            "projects": uncommitted_projects,
            "details": uncommitted_detail,
        }

    # Keep a rolling log of recent updates (last 50)
    existing_manifest = None
    if MANIFEST_FILE.exists():
        try:
            with open(MANIFEST_FILE) as f:
                existing_manifest = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    recent_updates = []
    if existing_manifest and "recent_updates" in existing_manifest:
        recent_updates = existing_manifest["recent_updates"]

    if affected and any(p != "__state__" for p in affected):
        recent_updates.insert(0, {
            "timestamp": manifest["generated_at"],
            "commit": commit_info["hash"],
            "message": commit_info["message"],
            "affected_projects": [p for p in affected if p != "__state__"],
        })
        recent_updates = recent_updates[:50]

    manifest["recent_updates"] = recent_updates

    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)

    project_names = [p for p in affected if p != "__state__"]
    if project_names:
        print(f"[sync] Updated {MANIFEST_FILE.name}: {', '.join(project_names)}")
    else:
        print(f"[sync] Updated {MANIFEST_FILE.name} (state refresh)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
