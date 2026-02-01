# Evidence Strength Rubric

A 5-point scale for evaluating evidence quality in research findings. Use this rubric to score individual pieces of evidence and aggregate scores to determine overall confidence in research conclusions.

---

## Overview

### Purpose
Standardize evidence quality assessment across research findings to:
- Enable objective comparison between sources
- Support confidence tier assignment
- Identify weak areas requiring additional research
- Guide source prioritization during synthesis

### When to Apply
- During research consolidation
- When findings conflict
- Before making recommendations
- When assessing research completeness

---

## The 5-Point Scale

### Score 5: Primary Source

**Definition:** Direct, authoritative information from the original creator, participant, or official record-keeper.

**Indicators:**
- First-hand account or official documentation
- Published by the entity being researched
- Directly verifiable through official channels
- No interpretation layer between source and fact

**Typical Sources:**
| Category | Examples |
|----------|----------|
| Corporate | SEC filings, earnings transcripts, official press releases, annual reports |
| Government | Census data, regulatory filings, patent records, court documents |
| Academic | Original research papers, peer-reviewed studies, clinical trial data |
| Direct | Interviews with decision-makers, internal documents, API documentation |

**Examples:**
```
Finding: "Company X reported Q3 revenue of $2.4B"
Source: Q3 2025 earnings call transcript
Score: 5 (direct from company)

Finding: "Patent US20250123 covers autonomous vehicle navigation"
Source: USPTO patent database
Score: 5 (official government record)

Finding: "The API rate limit is 1000 requests/minute"
Source: Official API documentation
Score: 5 (publisher's own documentation)
```

**Caveats:**
- Primary ≠ unbiased (company may spin data)
- Still verify against other primary sources when possible
- Watch for selective disclosure

---

### Score 4: Authoritative Secondary

**Definition:** Analysis or reporting by recognized experts or major analysts who cite primary sources.

**Indicators:**
- Clear attribution to primary sources
- Author has domain expertise or institutional credibility
- Published through rigorous editorial process
- Methodology is transparent

**Typical Sources:**
| Category | Examples |
|----------|----------|
| Analyst Reports | Gartner, Forrester, McKinsey, IDC (with citations) |
| Quality Journalism | WSJ, Financial Times, The Economist (investigative pieces) |
| Expert Commentary | Domain experts citing specific data points |
| Meta-analyses | Systematic reviews combining multiple primary studies |

**Examples:**
```
Finding: "Enterprise AI adoption increased 47% YoY"
Source: Gartner 2025 AI Survey (n=3,200, methodology disclosed)
Score: 4 (major analyst with transparent methodology)

Finding: "Three executives confirmed the acquisition talks"
Source: WSJ investigative report with named sources
Score: 4 (authoritative journalism with verification)

Finding: "Across 47 studies, the effect size averaged 0.65"
Source: Peer-reviewed meta-analysis in Nature
Score: 4 (systematic review of primary literature)
```

**Caveats:**
- Check for potential conflicts of interest
- Verify the primary sources are correctly represented
- Consider the analyst's track record

---

### Score 3: Credible Secondary

**Definition:** Reporting from reputable sources that are well-sourced but lack the authority or rigor of Score 4.

**Indicators:**
- Generally reliable publication
- Some sourcing provided but not comprehensive
- May rely on other secondary sources
- Editorial oversight exists but varies

**Typical Sources:**
| Category | Examples |
|----------|----------|
| Industry Publications | TechCrunch, VentureBeat, Industry Dive verticals |
| Business News | Bloomberg (non-investigative), Reuters (wire reports) |
| Trade Associations | Industry group reports and surveys |
| Expert Blogs | Well-established domain experts with good track records |

**Examples:**
```
Finding: "The startup raised $50M Series B"
Source: TechCrunch article citing company spokesperson
Score: 3 (credible publication, single source)

Finding: "Market expected to reach $15B by 2028"
Source: Industry association annual report
Score: 3 (trade group data, methodology unclear)

Finding: "The new feature reduces latency by 30%"
Source: Product Hunt launch with company benchmarks
Score: 3 (company claims, limited verification)
```

**Caveats:**
- Verify critical claims through additional sources
- Be aware of publication biases (tech press favors certain narratives)
- Check publication date for currency

---

### Score 2: Weak Secondary

**Definition:** Information from sources with limited verification, unclear attribution, or significant age.

**Indicators:**
- No clear sourcing or "according to reports"
- Outdated information (>2 years for fast-moving domains)
- Anonymous sources without corroboration
- Aggregator sites without original reporting

**Typical Sources:**
| Category | Examples |
|----------|----------|
| Content Aggregators | Medium posts (non-expert), content farms |
| Outdated Reports | Any report >2 years old in technology domains |
| Anonymous Claims | Reddit, forums, anonymous tips |
| Press Releases | Self-serving announcements without verification |

**Examples:**
```
Finding: "The company has 500 employees"
Source: LinkedIn company page (self-reported)
Score: 2 (unverified self-report)

Finding: "Market share is approximately 25%"
Source: 2022 industry report
Score: 2 (outdated for fast-moving market)

Finding: "Sources say a layoff is planned"
Source: Anonymous Glassdoor review
Score: 2 (unverified anonymous claim)
```

**Caveats:**
- Use only for directional indicators
- Actively seek better sources
- Flag uncertainty in outputs

---

### Score 1: Speculative

**Definition:** Information with no verifiable basis or clear speculation.

**Indicators:**
- No sourcing whatsoever
- Clearly labeled as speculation or prediction
- Contradicted by primary sources
- Logical inconsistencies or implausibility

**Typical Sources:**
| Category | Examples |
|----------|----------|
| Rumors | Unattributed "industry chatter" |
| Predictions | Forward-looking statements without data basis |
| Misinformation | Demonstrably false claims |
| Fabrications | AI hallucinations, made-up statistics |

**Examples:**
```
Finding: "The company will IPO in 2026"
Source: Analyst speculation with no insider knowledge
Score: 1 (pure prediction)

Finding: "Revenue will grow 200% next year"
Source: No source provided
Score: 1 (unverified, implausible claim)

Finding: "The CEO said they're pivoting to AI"
Source: Cannot locate any such statement
Score: 1 (potentially fabricated)
```

**Action:** Do not include Score 1 findings in research outputs without explicit "unverified speculation" labels.

---

## Scoring Guidelines

### Edge Case Handling

#### Multiple Sources for Same Finding
When multiple sources report the same finding, score based on the **strongest source**:
```
Finding: "Company acquired for $2B"
Sources:
  - WSJ report citing documents (Score 4)
  - TechCrunch citing WSJ (Score 3)
  - Company press release (Score 5)
Final Score: 5 (highest available)
```

#### Conflicting Information
When sources disagree, report the conflict with individual scores:
```
Finding: "Market size estimates vary significantly"
  - Source A (Gartner): $50B — Score 4
  - Source B (IDC): $35B — Score 4
  - Source C (Company estimate): $65B — Score 5
Note: 40% variance across authoritative sources
Recommendation: Use range ($35-65B) with confidence caveat
```

#### Time-Sensitive Information
Apply time decay for domains with rapid change:
| Domain | Decay Period | Effect |
|--------|--------------|--------|
| Technology | 6 months | -1 point |
| Market data | 1 year | -1 point |
| Financial metrics | 1 quarter | -1 point |
| Regulatory | On law change | Re-evaluate |
| Academic | 3-5 years | -1 point |

```
Finding: "Kubernetes adoption at 78%"
Source: CNCF Survey 2023 (originally Score 4)
Current Date: 2025
Adjusted Score: 3 (time decay applied)
```

#### Aggregated/Derived Data
For findings combining multiple data points:
- Score = lowest component score
- Flag as "derived" in output
```
Finding: "Total addressable market of $12B"
Components:
  - Segment A: $5B (Score 4)
  - Segment B: $4B (Score 3)
  - Segment C: $3B (Score 2)
Aggregated Score: 2 (lowest component)
Note: Segment C estimate is weak
```

---

## Special Cases

### Contradicting Sources

When authoritative sources directly conflict:

1. **Document both positions** with individual scores
2. **Identify methodology differences** that explain the gap
3. **Assess which methodology better fits your research question**
4. **Report the range** rather than picking a winner

**Template:**
```markdown
### Conflicting Finding: [Topic]

| Position | Source | Score | Methodology |
|----------|--------|-------|-------------|
| [Position A] | [Source] | [X] | [How measured] |
| [Position B] | [Source] | [X] | [How measured] |

**Reconciliation:** [Why they differ]
**Recommendation:** [Which to use or use range]
```

### Self-Reported Data

Company-provided data requires special handling:

| Data Type | Base Score | Adjustment |
|-----------|------------|------------|
| Audited financials | 5 | None |
| Unaudited metrics | 4 | -1 if incentive to inflate |
| Marketing claims | 3 | -1 to -2 based on verifiability |
| "Approximately" figures | 2-3 | Flag as estimate |

### AI-Generated Content

Treat LLM outputs as Score 1 unless:
- The LLM cites verifiable sources (then score the sources)
- Output is factual lookup from tool use (score the underlying source)
- Used for synthesis/analysis rather than facts (score inputs)

---

## Integration with Confidence Tiers

Map evidence scores to research confidence tiers:

| Confidence Tier | Required Evidence Profile |
|-----------------|--------------------------|
| **HIGH** | Majority Score 4-5, no critical findings below 3 |
| **MEDIUM** | Mix of 3-5, no critical findings below 2 |
| **LOW** | Contains Score 1-2 for critical findings |
| **INSUFFICIENT** | Unable to find Score 3+ for core questions |

### Weighting by Finding Importance

Not all findings are equal. Weight evidence scores by importance:

| Finding Type | Weight | Minimum Score |
|--------------|--------|---------------|
| Core research question | 3x | 4 |
| Supporting detail | 2x | 3 |
| Context/background | 1x | 2 |
| Nice-to-have | 0.5x | 1 |

**Weighted Confidence Formula:**
```
Weighted Score = Σ(Finding Score × Finding Weight) / Σ(Weights)

Example:
- Core finding: Score 4, Weight 3 → 12
- Support 1: Score 5, Weight 2 → 10
- Support 2: Score 3, Weight 2 → 6
- Context: Score 2, Weight 1 → 2

Weighted Score = (12+10+6+2)/(3+2+2+1) = 30/8 = 3.75
Tier: MEDIUM (below 4.0 threshold for HIGH)
```

---

## Output Format Example

### Single Finding Format
```markdown
**Finding:** [Statement of fact]
**Evidence Score:** [1-5] — [Category name]
**Source:** [Full citation]
**Date:** [Publication/access date]
**Notes:** [Caveats, time decay, conflicts]
```

### Research Section Format
```markdown
## [Research Question]

### Key Findings

| Finding | Score | Source | Date |
|---------|-------|--------|------|
| [Finding 1] | 5 | [Source] | [Date] |
| [Finding 2] | 4 | [Source] | [Date] |
| [Finding 3] | 3 | [Source] | [Date] |

**Section Confidence:** HIGH
**Evidence Profile:** 1×Score 5, 1×Score 4, 1×Score 3
**Gaps:** [Any missing information]
```

### Full Research Output Header
```markdown
# Research Brief: [Topic]

## Evidence Summary

| Tier | Count | Critical Findings |
|------|-------|-------------------|
| Score 5 (Primary) | 3 | 2 |
| Score 4 (Auth. Secondary) | 5 | 1 |
| Score 3 (Credible Secondary) | 4 | 0 |
| Score 2 (Weak Secondary) | 2 | 0 |
| Score 1 (Speculative) | 0 | 0 |

**Overall Confidence:** HIGH
**Methodology:** Multi-source triangulation with primary verification
**Key Limitations:** [List any gaps or weak areas]
```

---

## Quick Reference Table

| Score | Name | Definition | Use |
|-------|------|------------|-----|
| **5** | Primary Source | Direct from entity being researched | Full confidence |
| **4** | Authoritative Secondary | Major analysts with citations | High confidence |
| **3** | Credible Secondary | Industry publications, well-sourced | Moderate confidence |
| **2** | Weak Secondary | Unsourced, outdated, anonymous | Directional only |
| **1** | Speculative | No verifiable basis | Do not rely on |

### Quick Scoring Decision Tree

```
Is the source the original creator/publisher of this information?
├─ YES → Score 5 (Primary)
└─ NO → Does the source cite primary sources?
         ├─ YES → Is the source a major analyst/publication?
         │        ├─ YES → Score 4 (Authoritative Secondary)
         │        └─ NO → Score 3 (Credible Secondary)
         └─ NO → Is there any verifiable sourcing?
                  ├─ YES → Score 2 (Weak Secondary)
                  └─ NO → Score 1 (Speculative)
```

### Minimum Scores by Research Type

| Research Type | Core Findings | Supporting | Context |
|---------------|---------------|------------|---------|
| Investment decisions | 5 | 4 | 3 |
| Strategic planning | 4 | 3 | 2 |
| Market exploration | 3 | 3 | 2 |
| Competitive monitoring | 3 | 2 | 2 |
| Trend scanning | 2 | 2 | 1 |

---

## Appendix: Common Source Score Reference

### Technology Domain
| Source Type | Typical Score |
|-------------|---------------|
| Official documentation | 5 |
| GitHub README/code | 5 |
| Gartner/Forrester with methodology | 4 |
| Hacker News discussion | 2 |
| Stack Overflow answers | 2-3 |
| LLM-generated without citations | 1 |

### Business/Finance Domain
| Source Type | Typical Score |
|-------------|---------------|
| SEC filings (10-K, 10-Q) | 5 |
| Earnings call transcripts | 5 |
| Equity research (bulge bracket) | 4 |
| Business news (WSJ, FT) | 3-4 |
| Press releases | 3 |
| Glassdoor/LinkedIn data | 2 |

### Market Research Domain
| Source Type | Typical Score |
|-------------|---------------|
| Census/government data | 5 |
| Major market research (Gartner, IDC) | 4 |
| Industry association reports | 3-4 |
| Company-commissioned studies | 2-3 |
| Blog posts/opinion pieces | 1-2 |
