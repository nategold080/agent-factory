# Outreach Package Standards

## Overview

Every project requires a complete outreach package before it can be marked client-ready. This document defines the standards.

---

## targets.json Schema

Each entry in `targets.json` must include:

```json
{
  "name": "Full Name",
  "title": "Job Title",
  "organization": "Company/University Name",
  "email": "email@example.com",
  "linkedin": "linkedin.com/in/profile",
  "website": "https://example.com",
  "category": "potential_client | potential_employer | research_collaborator | media_contact | strategic_partner",
  "relevance": "Why this person/org would care about this specific data",
  "priority": "high | medium | low",
  "source": "How you found this target",
  "outreach_angle": "The specific hook for your pitch",
  "notes": "Additional context",
  "status": "identified | researched | contacted | responded | converted"
}
```

---

## Minimum Targets Per Project

| Category | Minimum | Description |
|----------|---------|-------------|
| potential_client | 5 | SaaS companies, compliance platforms, data vendors who would license the data |
| potential_employer | 3 | Companies hiring for roles this project demonstrates capability for |
| research_collaborator | 3 | Academics publishing in related fields |
| media_contact | 2 | Journalists covering this domain |
| strategic_partner | 2 | Distribution or integration partners |
| **Total** | **15** | |

---

## Email Templates

### Structure (applies to all templates)
1. **Hook** — Reference something specific about the recipient (recent article, product gap, research paper)
2. **Value Prop** — What the data is and why it matters to them specifically
3. **Proof Point** — Key stat or finding from the data (e.g., "We've aggregated X records from Y sources")
4. **Ask** — Clear, low-friction next step (15-min call, share sample data, send methodology doc)
5. **Sign-off** — Brief, professional

### Template Categories
Create one template per category:
- **Client pitch** — Focus on data gap their product has, how your data fills it
- **Researcher pitch** — Focus on novel dataset, methodology, collaboration opportunity
- **Employer pitch** — Focus on skills demonstrated, results achieved, role alignment
- **Media pitch** — Focus on newsworthy findings, exclusive access to data
- **Partner pitch** — Focus on mutual value, integration opportunity, shared audience

---

## Pitch Materials

### 1-Page Project Brief
- What the data is (1-2 sentences)
- Why it matters / the gap it fills
- Key statistics (record count, source count, coverage)
- 2-3 headline findings or insights
- How to access (dashboard URL, export options)
- Your contact information

### Sample Data Preview
- 5-10 curated records that showcase the most interesting/valuable data
- Clean formatting (table or structured JSON)
- Brief annotations explaining what makes these records noteworthy
- Include cross-linked records if applicable (this is the unique value)

---

## Research Notes

For each target, document in `research_notes.md`:
- How you found them and why they're relevant
- Their recent work/publications/products related to this domain
- The specific angle you'd use to pitch them
- Any mutual connections or warm introduction paths
- Timing considerations (conference season, budget cycles, etc.)
