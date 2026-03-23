"""Shared test fixtures."""

import pytest
import sqlite3
import tempfile
from pathlib import Path


@pytest.fixture
def tmp_db():
    """Provide a temporary SQLite database for testing."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    yield conn
    conn.close()
    Path(db_path).unlink(missing_ok=True)


@pytest.fixture
def sample_raw_data():
    """Provide sample raw data for testing extractors."""
    return {}


@pytest.fixture
def sample_records():
    """Provide sample structured records for testing validation."""
    return []
