# [PROJECT NAME] — Project-Specific Instructions

## IDENTITY

This is the build instructions file for [PROJECT NAME]. You are building a structured data product that aggregates [DOMAIN] data from public sources.

---

## DATA SOURCES

| # | Source | URL | Format | Status |
|---|--------|-----|--------|--------|
| 1 | [Source Name] | [URL] | [API/HTML/PDF/CSV] | Not started |
| 2 | [Source Name] | [URL] | [API/HTML/PDF/CSV] | Not started |
| 3 | [Source Name] | [URL] | [API/HTML/PDF/CSV] | Not started |

---

## DATABASE SCHEMA

```sql
-- Core tables (customize per project)
CREATE TABLE IF NOT EXISTS entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    normalized_name TEXT NOT NULL,
    entity_type TEXT,
    source TEXT NOT NULL,
    source_id TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    quality_score REAL DEFAULT 0.0
);

CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER REFERENCES entities(id),
    source TEXT NOT NULL,
    raw_data TEXT,
    extracted_data TEXT,
    record_date TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    quality_score REAL DEFAULT 0.0
);

-- Add project-specific tables below
```

---

## CLI COMMANDS

```bash
# Scrape data from sources
python -m src.cli scrape --source [all|source1|source2]

# Extract and normalize
python -m src.cli extract
python -m src.cli normalize

# Validate and export
python -m src.cli validate
python -m src.cli export --format [csv|json|excel|markdown]

# Launch dashboard
python -m src.cli dashboard
# OR
streamlit run src/dashboard/app.py
```

---

## QUALITY SCORING

```python
# Customize weights per project (must sum to 1.0)
QUALITY_WEIGHTS = {
    "has_core_fields": 0.25,      # All required fields populated
    "has_source_data": 0.20,      # Raw source data preserved
    "has_normalized_name": 0.15,  # Entity name normalized
    "has_cross_link": 0.15,       # Linked to entity in another source
    "has_date": 0.10,             # Valid date field
    "has_location": 0.10,         # Geographic information
    "has_category": 0.05,         # Categorized/classified
}
```

---

## DASHBOARD SECTIONS

1. **Overview** — KPI cards (total records, sources, entities, avg quality score)
2. **Explorer** — Searchable/filterable data table
3. **Entity Analysis** — Cross-linked entity view
4. **Trends** — Time series charts
5. **Geographic** — Map or state/region breakdown
6. **[Custom Section]** — Domain-specific analysis
7. **Data Quality** — Quality score distribution, completeness metrics
8. **Export** — Download buttons for all formats

---

## BUILD CHECKLIST

- [ ] Config YAML files defined
- [ ] Scraper for Source 1
- [ ] Scraper for Source 2
- [ ] Scraper for Source 3
- [ ] Extractors built and tested
- [ ] Normalization pipeline
- [ ] Validation + quality scoring
- [ ] SQLite storage layer
- [ ] End-to-end pipeline working
- [ ] Full pipeline run completed
- [ ] Exports (CSV, JSON, Excel, Markdown)
- [ ] Dashboard (5+ sections)
- [ ] Methodology document
- [ ] 50+ tests passing
- [ ] All PROBLEMS.md issues resolved
- [ ] Outreach package complete
