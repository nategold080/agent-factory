# Project Evaluation Criteria

## Scoring Rubric

Score each dimension 1-5. **Minimum threshold to pursue: 20/30.**

---

### 1. Data Gap Reality (Weight: 5)

Does this data truly not exist in structured, aggregated form?

| Score | Meaning |
|-------|---------|
| 1 | Multiple commercial providers already sell this exact data |
| 2 | Data exists but is expensive or hard to access — marginal improvement |
| 3 | Data is partially aggregated by some players but with significant gaps |
| 4 | Data is public but scattered — nobody has built a comprehensive structured database |
| 5 | Data is completely unstructured and nobody has attempted aggregation at scale |

**How to verify:** Search for "[domain] database", "[domain] tracker", "[domain] data provider". Check Crunchbase for startups in the space. Search academic papers for datasets. If you find a comprehensive existing product, score 1-2.

---

### 2. Buyer Clarity (Weight: 5)

Can you name specific organizations AND specific people who would pay?

| Score | Meaning |
|-------|---------|
| 1 | Vague sense that "someone might want this" |
| 2 | Can name an industry vertical but no specific companies |
| 3 | Can name 3+ companies but unclear who specifically to contact |
| 4 | Can name 5+ companies AND the relevant roles (VP Data, Head of Product) |
| 5 | Can name specific people at specific companies with clear budget authority |

**How to verify:** Search for companies in the vertical. Check their product pages — does this data fit their offering? Look for job postings mentioning this data type. Find named individuals on LinkedIn.

---

### 3. Technical Feasibility (Weight: 5)

Can the data be scraped/extracted reliably from public sources?

| Score | Meaning |
|-------|---------|
| 1 | Sources require authentication, CAPTCHA, or are behind paywalls |
| 2 | Sources are accessible but highly fragile (PDF pixel positions, JS-heavy sites) |
| 3 | Mix of easy and hard sources — most require custom adapters |
| 4 | Sources have stable HTML or semi-structured formats, moderate scraping effort |
| 5 | Sources have public APIs or very stable, well-structured HTML/data formats |

**How to verify:** Actually visit 2-3 target sources. Try to fetch a page. Check if there's an API. Look at the HTML structure.

---

### 4. Cross-Linking Value (Weight: 5)

Can you connect the same entity across multiple sources for unique analytical value?

| Score | Meaning |
|-------|---------|
| 1 | Single-source data with no cross-referencing opportunity |
| 2 | Multiple sources but entities don't overlap meaningfully |
| 3 | Some entity overlap but cross-linking is optional/nice-to-have |
| 4 | Significant entity overlap — cross-linking reveals actionable patterns |
| 5 | Cross-linking IS the core value proposition — the data is only valuable because you connected sources |

---

### 5. Scale Demonstration (Weight: 3)

Can you realistically achieve enough records to prove viability?

| Score | Meaning |
|-------|---------|
| 1 | Unlikely to reach 100 records |
| 2 | 100-500 records achievable |
| 3 | 500-2,000 records achievable |
| 4 | 2,000-10,000 records achievable |
| 5 | 10,000+ records achievable |

---

### 6. Credibility Signal (Weight: 2)

Does this project open doors to notable researchers, publications, or organizations?

| Score | Meaning |
|-------|---------|
| 1 | Unlikely to generate any external interest |
| 2 | Might get a blog post or minor attention |
| 3 | Could lead to conversations with interesting people/orgs |
| 4 | Clear path to research collaboration or media coverage |
| 5 | Could lead to publication, major media coverage, or partnership with prestigious institution |

---

## Quick Rejection Criteria

Reject immediately (score 0, do not pursue) if ANY of these are true:
- Data requires paid subscriptions or API keys costing > $0 for core pipeline
- Primary sources are behind authentication that the operator hasn't approved
- A well-funded startup already sells this exact data at scale
- Data involves personal/private information about non-public individuals
- Fewer than 3 independent sources are accessible
- No identifiable buyer would pay more than $1,000 for the complete dataset
