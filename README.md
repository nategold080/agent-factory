# Agent Factory

A scaffolding system for running autonomous AI agents that research, build, test, and deliver structured data products at scale.

## What This Is

Agent Factory is a template for setting up a **multi-agent autonomous project generation system**. It provides the directory structure, state management, evaluation criteria, and workflow definitions needed to run multiple AI agents in parallel — each working on different projects within a unified framework.

The system is designed so you can:
- Open separate agent sessions in each project folder for parallel autonomous work
- Have agents research new project ideas while others build existing ones
- Track all project state, progress, and alerts in a central location
- Maintain consistent quality standards across all projects
- Generate outreach packages alongside the technical deliverables

## How It Works

### The 5-Phase Pipeline

1. **Research** (continuous) — Agents investigate domains, find unstructured public data, score ideas using a 6-dimension rubric
2. **Scaffold** — Accepted ideas get a standardized project directory with all the boilerplate
3. **Build** — Agents follow a 12-step build order: config → scrapers → extractors → normalization → validation → storage → pipeline → exports → dashboard → docs → tests
4. **Outreach** — Agents research and document 15+ targets per project (clients, employers, researchers, media, partners)
5. **Polish** — Final quality checks against a client-ready checklist

### State Management

All operational state lives in `state/`:
- `projects.json` — Tracks every project's status, metrics, and notes
- `research_queue.json` — Pipeline of ideas being evaluated
- `alerts.json` — Notifications for the operator (client-ready, needs-human, blocked, milestone)
- `research_briefs/` — Detailed briefs for each evaluated idea

### Per-Project Structure

Every project under `projects/` follows the same layout:
```
projects/{project-slug}/
├── CLAUDE.md           ← Project-specific agent instructions
├── PROBLEMS.md         ← Issue tracker
├── src/                ← Source code (scrapers, extractors, normalization, etc.)
├── tests/              ← 50+ tests required
├── data/               ← SQLite DB, raw cache, exports
├── docs/               ← Methodology documentation
├── outreach/           ← Targets, email templates, pitch materials
├── config/             ← YAML source/entity configs
└── .streamlit/         ← Dashboard theme config
```

## Getting Started

1. **Fork or clone this repo**
2. **Customize `CLAUDE.md`** — Fill in your name, background, goals, and preferred research domains
3. **Add reference projects** (optional) — Place examples of your best work in `references/existing_projects/` and write up `references/PROJECT_ANALYSIS.md`
4. **Start an agent session** at the repo root — it will read `CLAUDE.md` and begin Phase 1 research
5. **Monitor `state/`** — Check `alerts.json` for things that need your attention
6. **Open parallel sessions** — Launch agents in individual `projects/` folders for concurrent building

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Master orchestration instructions for the agent |
| `EVALUATION_CRITERIA.md` | 6-dimension scoring rubric for evaluating new project ideas |
| `OUTREACH_TEMPLATE.md` | Standards for outreach packages (targets, emails, pitch materials) |
| `state/projects.json` | Central project tracker |
| `state/research_queue.json` | Idea evaluation pipeline |
| `state/alerts.json` | Operator notifications |
| `scripts/sync_to_outreach.py` | Auto-syncs project updates to an external folder |
| `templates/` | Scaffolding templates for new projects and outreach packages |

## Technical Stack

Each project built by the factory uses:
- **Python 3.12+** with Click CLI
- **SQLite** (WAL mode) for storage
- **Streamlit + Plotly** for dashboards
- **Pydantic v2** for validation
- **pytest** for testing
- **Rule-based extraction** (zero LLM dependency in core pipelines)

## Customization

This is a **template** — customize it for your domain:

- Edit `CLAUDE.md` to define your identity, goals, and preferred research domains
- Modify `EVALUATION_CRITERIA.md` to weight dimensions differently
- Adjust `OUTREACH_TEMPLATE.md` for your outreach style
- Add your own technical standards to the build phase
- Place your existing projects in `references/` as quality benchmarks

## License

MIT
