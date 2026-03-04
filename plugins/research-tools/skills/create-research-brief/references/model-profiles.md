# Model Profiles & Research Configuration Reference

**Version**: 2.0
**Last validated**: 2026-03-04
**Models**: Claude Opus 4.6 | Gemini 3.1 Pro Deep Research | GPT-5.2 Deep Research | GPT-5.2 Chat

---

## Section 1: Model Capability Matrix

| Capability | Claude Opus 4.6 | Gemini 3.1 Pro Deep Research | GPT-5.2 Deep Research | GPT-5.2 Chat |
|---|---|---|---|---|
| **Web research (BrowseComp)** | 84% | 85.9% | Strong (precision via site restriction) | Standard |
| **Reasoning (ARC-AGI-2)** | 68.8% | 77.1% | Strong (GPT-5.2 base) | Moderate |
| **Long-context retrieval** | 76% MRCR v2 | Strong (1M input) | Leading MRCRv2 at 128K-256K | Standard |
| **Output structure** | Analytical prose, reasoning chains | Structured reports, tables, TOC, citations | Full-screen reports with sections | Conversational |
| **Citation quality** | Web-sourced with URLs | High-density with source appendix | Site-specific with provenance | Light sourcing |
| **Context window** | 1M tokens (beta) | 1M tokens | 128K-256K (leading retrieval) | Standard |
| **Output limit** | 128K tokens | 64K tokens | ~60-80K per task | Standard |
| **Tool coordination** | Integrated web search | 69.2% MCP Atlas | MCP + site restrictions | Web search |
| **File ingestion** | Conversation context | file_search (uploaded docs as sources) | Multi-modal (text, images, PDFs) | Conversation context |
| **Site restrictions** | ✗ Not available | ✗ Not available | ✓ Limit to specific domains | ✗ Not available |
| **Thinking/effort** | Adaptive: low/medium/high/max | 3-tier: Low/Medium/High | thinking_effort: low/medium/high/extended | Instant or Thinking |
| **Autonomous research** | Per-query web search | 5-30 min autonomous agent | 5-30 min autonomous agent | Per-query |
| **Research volume** | Variable per-search | Std: ~80 searches, ~250K in, ~60K out. Complex: ~160 searches, ~900K in, ~80K out | Std: ~80-160 searches per task | Single-pass |
| **API interface** | Messages API | Interactions API (background exec) | ChatGPT Deep Research UI | ChatGPT / API |
| **Cost tier** | Highest per-token | $2/1M in, $12/1M out | Subscription-gated | Subscription-gated |

### Capability Uniqueness Map

Each model has exactly one capability the others lack:

| Model | Unique Capability | Consolidation Impact |
|---|---|---|
| **Claude** | Self-correction + cross-domain synthesis | Claims include reasoning chains; provenance: `analytical_synthesis` |
| **Gemini** | file_search (uploaded docs as research sources) | Claims grounded in internal docs; provenance: `internal_document` |
| **GPT-5.2 Deep** | Site-restricted search (limit to specific domains) | Claims from authoritative sources; provenance: `site_restricted` |

Web research is a **shared capability** (Claude 84%, Gemini 85.9%). Differentiate by *how* they research:
- **Claude**: Searches to ground reasoning. Analytical synthesis + causal chains.
- **Gemini**: Searches to comprehensively map. Breadth + structured cataloging.
- **GPT-5.2 Deep**: Searches authoritatively. Site-restricted precision.

---

## Section 2: Role Assignment Framework

### Role Definitions

| Role | Function | Claim Types Produced | Provenance Weight |
|---|---|---|---|
| **Primary Researcher** | Deepest analysis, cross-domain reasoning, web-grounded synthesis, self-correction | Causal, recommendation, cross-domain synthesis, reasoning chains | Highest on reasoning + recommendation claims |
| **Structured Cataloger** | Breadth coverage, systematic inventory, comparison matrices, quantitative data, citation volume | Factual, quantitative, structural artifacts (tables, matrices) | Highest on factual + quantitative claims |
| **Targeted Investigator** | Site-restricted deep dives on authoritative sources, precision verification | Factual (site-specific), temporal, quantitative (from primary sources) | Highest when `site_restricted` provenance active |
| **Recency Validator** | Quick check on recent developments, sentiment, momentum signals | Factual (recent), sentiment, trend signals | Moderate (`quick_validation` provenance) |
| **Deep Recency Investigator** | Extended investigation of recent developments with analytical depth | Causal (recent), trend analysis, emerging patterns | Moderate-High (`web_search` + recency focus) |

### Model → Role Mapping

| Model | Optimal Role | Secondary Role(s) | Not Suited For |
|---|---|---|---|
| **Claude Opus 4.6** | Primary Researcher | Deep Recency Investigator | Structured Cataloger (depth > breadth) |
| **Gemini 3.1 Pro** | Structured Cataloger | Primary Researcher (peer BrowseComp + strong reasoning) | Targeted Investigator (no site restrictions) |
| **GPT-5.2 Deep** | Targeted Investigator | Deep Recency Investigator, Primary Researcher | Structured Cataloger (less structured output) |
| **GPT-5.2 Chat** | Recency Validator | — | Any deep research role |

---

## Section 3: Research Pattern × Model Configuration Matrix

### Quick Reference Table

| Pattern | Claude Role | Gemini Role | GPT-5.2 Deep Role (FULL) | Gemini Thinking | Claude Effort | Default Consolidation |
|---|---|---|---|---|---|---|
| Landscape Mapping | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | breadth_first |
| Comparative Evaluation | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | confidence_weighted |
| Implementation Pattern | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | depth_first |
| Best Practices | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | gap_driven |
| Competitive Intelligence | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | adversarial |
| Market Research | Primary Researcher | Structured Cataloger | Deep Recency Investigator | High | max | standard |
| User Research | Primary Researcher | Structured Cataloger | Deep Recency Investigator | High | max | depth_first |
| Economic Analysis | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | confidence_weighted |
| Compliance & Requirements | Primary Researcher | Structured Cataloger | Targeted Investigator | High | max | gap_driven |

### Per-Pattern Configuration

---

#### 1. Landscape Mapping

**Goal**: Discover and categorize the complete universe of players, solutions, or approaches.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Market structure analysis, white space identification, cross-domain structural parallels, categorization rationale | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Comprehensive player inventory per category, funding/maturity data, taxonomy creation, ecosystem relationship maps | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Structure analysis, white space, cross-domain parallels | Exclude: comprehensive player inventory |
| Gemini | Structured Cataloger | Player inventory, taxonomy, quantitative landscape data | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent entrants (last 6 months), pivots, M&A, funding events | Exclude: structural analysis |

**SINGLE mode**: Claude covers full scope with expanded structured output directives.

**GPT-5.2 site restrictions**: Crunchbase, PitchBook, ProductHunt, TechCrunch, relevant trade publications, analyst firm sites
**Gemini file_search**: Upload prior research outputs, internal market assessments, partial landscape data
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: breadth_first

---

#### 2. Comparative Evaluation

**Goal**: Deep comparison of known options against weighted criteria for a selection decision.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Trade-off analysis, hidden dependencies, second-order effects, decision sensitivity, cross-domain pattern imports | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Feature-by-feature comparison matrix, pricing tables, benchmark data, customer review synthesis, adoption metrics | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Trade-offs, hidden dependencies, decision sensitivity | Exclude: feature-level comparison |
| Gemini | Structured Cataloger | Feature matrices, pricing, benchmarks, review synthesis | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent pricing changes, feature launches, sentiment shifts, breaking changes | Exclude: strategic analysis |

**SINGLE mode**: Claude covers full scope; add explicit "create comparison tables" directive.

**GPT-5.2 site restrictions**: Vendor official sites, G2, Capterra, analyst firms, Hacker News
**Gemini file_search**: Upload RFP responses, vendor proposals, existing ADRs
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: confidence_weighted

---

#### 3. Implementation Pattern

**Goal**: Synthesize how-to knowledge from real-world implementations, architecture decisions, and production lessons.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Architecture decision rationale, pattern trade-offs at scale, cross-domain pattern imports, anti-pattern root cause analysis, decision trees | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Reference architecture catalog, code pattern examples, benchmark comparisons, open-source project analysis, dependency matrices | web_search, file_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Decision rationale, trade-offs, cross-domain, anti-patterns | Exclude: code-level pattern catalog |
| Gemini | Structured Cataloger | Reference architectures, code patterns, benchmarks, dependencies | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent production incidents, post-mortems, community workarounds, migration guides | Exclude: architectural reasoning |

**SINGLE mode**: Claude covers full scope; add "include code examples where relevant" directive.

**GPT-5.2 site restrictions**: GitHub repos + issues + discussions, Stack Overflow, official docs, engineering blogs (Netflix, Uber, Stripe, etc.)
**Gemini file_search**: Upload current architecture diagrams, ADRs, codebase samples, config files
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: depth_first

---

#### 4. Best Practices

**Goal**: 8-dimension technology knowledge base.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Idiomatic patterns with reasoning, anti-patterns with root cause, decision trees, escape hatches, cross-domain insights | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Documentation state, version compatibility matrices, community issues, benchmark data, practitioner sentiment | web_search, file_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Pattern reasoning, anti-patterns, decision trees, cross-domain | Exclude: version matrix, benchmark catalog |
| Gemini | Structured Cataloger | Version matrices, benchmarks, community issues, sentiment | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent breaking changes, deprecations, migration issues, community workarounds | Exclude: pattern reasoning |

**SINGLE mode**: Claude covers full scope with expanded structured table directives.

**Prompt assembly**: Load dimension-specific fragments from `best-practices-dimensions.md`. Assemble per technology family weighting from `technology-profiles.md`.

**GPT-5.2 site restrictions**: Official docs, GitHub repos + issues + discussions, Stack Overflow, community forums
**Gemini file_search**: Upload existing codebase samples, current config files, requirements.txt / package.json
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: gap_driven

---

#### 5. Competitive Intelligence

**Goal**: Strategic positioning analysis — moats, differentiation sustainability, competitive dynamics.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Moat sustainability analysis, positioning dynamics, competitive response scenarios, differentiation durability, cross-industry pattern imports | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Feature matrices, pricing comparison, market share data, funding history, team/hiring signals, positioning maps | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Moat analysis, positioning dynamics, competitive scenarios | Exclude: feature-level matrices |
| Gemini | Structured Cataloger | Feature matrices, pricing, market share, funding, hiring | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent strategic moves, product launches, pricing changes, partnership announcements, hiring signals | Exclude: strategic positioning analysis |

**SINGLE mode**: Claude covers full scope; add "include feature comparison table" directive.

**GPT-5.2 site restrictions**: Competitor domains, press/news sites (TechCrunch, The Information), G2, Capterra, analyst firms (Gartner, Forrester), LinkedIn
**Gemini file_search**: Upload competitor feature screenshots, teardown notes, sales battle cards
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: adversarial

---

#### 6. Market Research

**Goal**: Market sizing, segmentation, dynamics, entry strategy.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Market structure dynamics (winner-take-all vs. fragmented), segment attractiveness, entry barrier assessment, demand driver reasoning | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Market sizing data (TAM/SAM/SOM), growth rates, segment breakdown, geographic distribution, funding activity | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Structure dynamics, segment attractiveness, entry barriers | Exclude: quantitative sizing |
| Gemini | Structured Cataloger | Sizing, growth, segments, geographic, funding | Full scope |
| GPT-5.2 Deep | Deep Recency Investigator | Recent funding rounds, segment shifts, regulatory changes, emerging market signals | Exclude: structural analysis |

**SINGLE mode**: Claude covers full scope; add "include sizing estimates with sources" directive.

**GPT-5.2 site restrictions**: Crunchbase, PitchBook, SEC/EDGAR, analyst reports, trade publications, Statista
**Gemini file_search**: Upload internal market assessments, segment definitions
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: standard

---

#### 7. User Research

**Goal**: Jobs-to-be-done, persona development, behavioral patterns, unmet needs.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | JTBD framework, unmet needs hierarchy, behavioral driver analysis, persona synthesis with psychological depth, workaround analysis | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Demographic data, usage pattern surveys, review/sentiment aggregation, satisfaction scores, community discussion synthesis | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | JTBD, unmet needs, behavioral drivers, persona synthesis | Exclude: demographic compilation |
| Gemini | Structured Cataloger | Demographics, usage patterns, review aggregation, satisfaction | Full scope |
| GPT-5.2 Deep | Deep Recency Investigator | Recent behavioral shifts, emerging pain points, community sentiment evolution | Exclude: persona synthesis |

**SINGLE mode**: Claude covers full scope; add "synthesize from forum discussions and reviews" directive.

**GPT-5.2 site restrictions**: Reddit (relevant subreddits), ProductHunt, G2, Capterra, community forums, Twitter/X
**Gemini file_search**: Upload user interview transcripts, survey results, support tickets
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: depth_first

---

#### 8. Economic Analysis

**Goal**: ROI modeling, TCO, cost-benefit, sensitivity analysis, financial feasibility.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Financial modeling framework, sensitivity analysis, cost-benefit reasoning, hidden cost identification, ROI scenario construction | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Pricing data, benchmark costs, industry financial metrics, comparable company data, TCO component catalog | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Financial modeling, sensitivity, cost-benefit reasoning | Exclude: pricing data compilation |
| Gemini | Structured Cataloger | Pricing data, benchmarks, financial metrics, comparables | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent pricing changes, cost trend data, updated financial benchmarks | Exclude: financial modeling |

**SINGLE mode**: Claude covers full scope; add "include quantitative estimates with confidence ranges" directive.

**GPT-5.2 site restrictions**: Vendor pricing pages, SEC/EDGAR, financial databases, cost calculators, cloud provider pricing pages
**Gemini file_search**: Upload current cost models, vendor quotes, financial projections
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: confidence_weighted

---

#### 9. Compliance & Requirements

**Goal**: Regulatory constraints, governance frameworks, audit requirements.

**DUAL mode**:

| Model | Role | Focus | Capabilities |
|---|---|---|---|
| Claude | Primary Researcher | Regulatory interpretation, cross-jurisdictional analysis, governance framework design, risk-impact reasoning, constraint interaction mapping | web_search, adaptive_thinking, thinking_max |
| Gemini | Structured Cataloger | Regulatory text catalog, compliance checklists, audit requirement matrices, deadline tracking, jurisdiction comparison tables | web_search, thinking_high |

**FULL mode** (add GPT-5.2):

| Model | Role | Focus | Exclusions |
|---|---|---|---|
| Claude | Primary Researcher | Regulatory interpretation, governance design, constraint interactions | Exclude: regulatory text catalog |
| Gemini | Structured Cataloger | Regulatory catalog, checklists, audit matrices, deadlines | Full scope |
| GPT-5.2 Deep | Targeted Investigator | Recent regulatory changes, enforcement actions, policy updates, pending legislation | Exclude: governance design |

**SINGLE mode**: Claude covers full scope; add "include compliance checklist" directive.

**GPT-5.2 site restrictions**: Regulatory body sites (.gov domains), legal databases, governance frameworks (ISO, NIST), compliance portals, industry-specific regulators
**Gemini file_search**: Upload regulatory requirements docs, policy documents, existing compliance matrices
**Gemini thinking**: High
**Claude effort**: max
**Default consolidation**: gap_driven

---

## Section 4: DUAL Mode Redistribution

### Core Principle

Both Claude (84%) and Gemini (85.9%) are strong web researchers. DUAL mode differentiates by **research approach**, not research capability.

### Redistribution Table

| Research Dimension | Route To | Rationale |
|---|---|---|
| Analytical synthesis + trade-off reasoning | **Claude** | Cross-domain pattern recognition, self-correction, causal chain construction |
| Breadth coverage + structured cataloging | **Gemini** | Systematic mapping, citation volume, comparison matrix generation |
| Quantitative data + benchmarks | **Gemini** | Structured output, table generation, data-dense coverage |
| Strategic implications + second-order effects | **Claude** | Deep reasoning about consequences and dynamics |
| Recent developments + trajectory analysis | **Split** | Claude for dynamics/implications, Gemini for structured timeline |
| Practitioner sentiment + community signals | **Gemini** | Breadth of community source surveying |
| Cross-domain pattern recognition | **Claude** | Novel synthesis capability (68.8% ARC-AGI-2) |
| Production learnings + post-mortems | **Claude** | Web search + deep reasoning about failure modes |

### DUAL Prompt Modifications

- **Claude**: Add explicit web search directives for recency. Add cross-domain synthesis section. Add self-review mandate. Set effort to `max`.
- **Gemini**: Add "Prioritize 2025-2026 sources". Add practitioner sentiment survey dimension. Add structured table directive. Set thinking to `High`.
- **Both**: No "Do NOT cover" exclusions. Full overlap for cross-validation. Differentiate by HOW, not WHAT.

### DUAL Recency Assessment

With both models having strong BrowseComp, DUAL has minimal recency risk. Use ℹ️ informational for most topics. Only flag ⚠️ for:
- Rapidly evolving regulatory environments
- Live market events (funding rounds, M&A in progress)
- Topics where site-restricted search on authoritative sources (GPT-5.2) would add meaningful precision

---

## Section 5: Prompt Templates

### Claude Opus 4.6 (Primary Researcher)

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000  # Increase up to 128000 for comprehensive output

You are researching [TOPIC] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified
sources. Prioritize 2025-2026 sources for rapidly evolving topics.

Focus your research and analysis on:

1. [DIMENSION 1]
   - [Specific question]
   - Search for: [specific evidence to find]
   - Analyze: [what to derive from evidence]

2. [DIMENSION 2]
   - [Specific question]
   - Search for: [specific evidence to find]
   - Analyze: [what to derive from evidence]

3. [DIMENSION 3]
   - [Specific question]
   - Search for: [specific evidence to find]

4. CROSS-DOMAIN SYNTHESIS
   After completing primary analysis:
   - What structural patterns from unrelated domains map to these findings?
   - Where does conventional framing miss something an outsider would catch?
   - What emergent properties arise from constraint interactions?
   - What would need to be true for the consensus view to be wrong?

5. IMPLICATION ANALYSIS
   - What are the second-order consequences of your key findings?
   - Which findings interact to create non-obvious opportunities or risks?
   - What decisions does this research enable or constrain?

Ground every claim in evidence. Distinguish between web-verified facts and
your analytical reasoning. Surface non-obvious dynamics.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Internal contradictions between sections
- Claims asserted without supporting evidence
- Reasoning chains that don't survive scrutiny
- Coverage gaps against the dimensions above
- Opportunities for cross-domain insight you missed
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research (Structured Cataloger)

```
Conduct a comprehensive, data-driven analysis of [TOPIC].

Provide systematic coverage of:

1. [COVERAGE AREA 1]
   - [Specific elements to catalog]
   - [Data points needed]
   - Create a comparison table including: [dimensions]

2. [COVERAGE AREA 2]
   For each [entity], document:
   - [Attribute 1]
   - [Attribute 2]
   - [Attribute 3]

3. [COVERAGE AREA 3]
   - [Specific question]
   - Include quantitative data where available
   - Survey practitioner sentiment from community discussions, forums,
     and conference talks

4. [COVERAGE AREA 4]
   - [Specific question]
   - Create a structured inventory with: [fields]

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Provide structured inventories with consistent fields
- Note where sources conflict
- Distinguish between well-sourced facts and practitioner opinions
- Organize with clear section headers for navigability
```

**Gemini API configuration** (configure via Interactions API, not in prompt):

```yaml
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true
# tools: [file_search]  # when file_search recommended
```

**File search preamble** (add when file_search is recommended per Section 7):

```
CONTEXT DOCUMENTS:
The following documents have been uploaded as research context. Use them
to ground your analysis in the specific situation being researched.
Cross-reference findings from web sources against these internal documents.
Flag where web-sourced best practices conflict with current implementation.

Uploaded: [DOCUMENT_LIST]
```

### GPT-5.2 Deep Research (Targeted Investigator)

```
Research [TOPIC] with focus on [ASPECT].

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- [SITE 1]
- [SITE 2]
- [SITE 3]
- [SITE 4]
- [SITE 5]

RESEARCH DIMENSIONS:
1. [TARGETED DIMENSION 1]
   - What to find: [specific evidence]
   - What to verify: [specific claims to check]

2. [TARGETED DIMENSION 2]
   - What to find: [specific evidence]
   - Recent changes: [what may have shifted in last 6 months]

3. [TARGETED DIMENSION 3]
   - What to find: [specific data points]

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth. You have access to restricted,
authoritative sources — use them for high-quality evidence.
```

**Mid-session intervention protocol** (include in FULL-mode research briefs):

```
MONITORING CHECKLIST (while GPT-5.2 Deep Research runs):
□ Drift: Research exploring tangential topics
  → Intervene: "Refocus on [SPECIFIC DIMENSION]"
□ Source quality: Results from low-authority sources
  → Intervene: "Prioritize [SPECIFIC SITES]"
□ Coverage gap: Missing a key dimension
  → Intervene: "Also investigate [MISSING AREA]"
□ Redundancy: Repeating findings already covered
  → Intervene: "Skip [COVERED AREA], focus on [UNCOVERED]"
□ Stale data: Using pre-2025 sources on fast-changing topics
  → Intervene: "Focus on 2025-2026 sources only"
```

### GPT-5.2 Chat (Recency Validator — FULL mode only)

```
Provide a recency validation check on [TOPIC], focusing on [ASPECT].

Cover:
1. Most notable developments in the last 6 months
2. Current sentiment and momentum signals
3. Emerging concerns or opportunities not yet in mainstream coverage
4. Where the current situation differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed developments and rumors.
```

---

## Section 6: Site Restriction Library

Recommended site restriction lists for GPT-5.2 Deep Research. These are starting templates — customize per topic.

### By Research Pattern

| Pattern | Site Categories | Example Sites |
|---|---|---|
| **Landscape Mapping** | VC databases, product directories, tech press, analyst firms | crunchbase.com, pitchbook.com, producthunt.com, techcrunch.com, gartner.com, g2.com |
| **Comparative Evaluation** | Vendor sites, review platforms, analyst firms, forums | [vendor-1].com, [vendor-2].com, g2.com, capterra.com, gartner.com, news.ycombinator.com |
| **Implementation Pattern** | Code repos, dev forums, official docs, eng blogs | github.com/[repos], stackoverflow.com, [official-docs], eng.uber.com, netflixtechblog.com |
| **Best Practices** | Official docs, code repos + issues, dev forums, community | [official-docs], github.com/[repos]/issues, github.com/[repos]/discussions, stackoverflow.com |
| **Competitive Intelligence** | Competitor sites, review platforms, news, analyst firms | [competitor-1].com, [competitor-2].com, g2.com, techcrunch.com, gartner.com, linkedin.com |
| **Market Research** | VC databases, SEC filings, analyst reports, trade pubs | crunchbase.com, pitchbook.com, sec.gov, statista.com, [trade-publications] |
| **User Research** | Review platforms, product directories, forums, social | reddit.com/r/[subs], producthunt.com, g2.com, capterra.com, [community-forums] |
| **Economic Analysis** | Vendor pricing, financial databases, cost tools | [vendor-pricing-pages], sec.gov, [cloud-pricing], [cost-calculators] |
| **Compliance & Requirements** | Regulatory bodies, legal databases, standards orgs | [regulatory].gov, iso.org, nist.gov, [compliance-portals], [industry-regulators] |

### High-Value Cross-Pattern Sites

| Site | Value For | Notes |
|---|---|---|
| github.com | Implementation, Best Practices, Competitive | Issues + Discussions are higher signal than README |
| stackoverflow.com | Implementation, Best Practices | Filter by votes and recency |
| g2.com / capterra.com | Comparative, Competitive, User Research | Verified user reviews |
| crunchbase.com | Landscape, Market | Funding, founding date, team size |
| sec.gov (EDGAR) | Market, Economic | Authoritative financial data |
| news.ycombinator.com | All technical patterns | High-signal technical community sentiment |

---

## Section 7: Gemini File Search Guidance

Gemini 3.1 Pro Deep Research supports `file_search` — uploaded documents serve as research context alongside web sources. This is **Gemini-specific**. Claude handles context via conversation window. GPT-5.2 handles context via multi-modal input.

### When to Recommend File Upload

| Pattern | Upload When | What to Upload | Research Value |
|---|---|---|---|
| **Best Practices** | User has existing codebase or config | Code samples, config files, requirements.txt, package.json | Gemini compares current implementation against discovered best practices |
| **Comparative Evaluation** | User has vendor proposals or RFPs | RFP responses, vendor proposals, existing ADRs | Gemini cross-references vendor claims against web-sourced evidence |
| **Competitive Intelligence** | User has competitor teardowns | Feature screenshots, teardown notes, sales battle cards | Gemini validates/extends competitor analysis with web data |
| **Implementation Pattern** | User has current architecture | Architecture diagrams, ADRs, codebase structure, config files | Gemini maps discovered patterns against existing architecture |
| **Compliance & Requirements** | User has regulatory docs | Regulatory requirements, policy documents, compliance matrices | Gemini builds compliance analysis grounded in actual requirements |
| **Economic Analysis** | User has financial models | Current cost models, vendor quotes, financial projections | Gemini benchmarks internal estimates against market data |
| **Landscape Mapping** | User has partial research | Prior research outputs, internal market assessments | Gemini builds on existing knowledge, avoids duplication |
| **User Research** | User has qualitative data | Interview transcripts, survey results, support tickets | Gemini synthesizes internal qualitative data with web-sourced behavioral data |
| **Market Research** | User has internal data | Internal market assessments, segment definitions | Gemini calibrates internal estimates against external sizing data |

### File Search Value by Technology Family

For **Best Practices** pattern, the value of file_search varies:

| Technology Family | File Search Value | What to Upload |
|---|---|---|
| Serverless | Medium | Function configs, deployment scripts |
| Databases | High | Schema files, migration scripts, query patterns |
| Frontend Frameworks | Medium | Component examples, build configs |
| Infrastructure as Code | High | Current Terraform/CDK files, state files |
| API Development | Low | Well-documented publicly; upload only custom middleware |
| CI/CD Pipelines | Medium | Pipeline configs, custom scripts |
| AI/ML Platforms | High | Agent configs, prompt files, orchestration code |
| Mobile | Low | Well-documented publicly |
| AI Agent Frameworks | High | Orchestration configs, agent definitions, tool specs |

### File Search Setup Instructions

Include in research brief when file_search is recommended:

```
GEMINI FILE SEARCH SETUP:
Before executing the Gemini prompt:
1. Upload the following documents to Gemini Deep Research:
   - [DOCUMENT_1]: [why this helps]
   - [DOCUMENT_2]: [why this helps]
2. The prompt includes instructions to cross-reference web findings
   against these internal documents.
3. In consolidation, claims grounded in uploaded documents receive
   provenance: internal_document (higher weight than web_search).
```

---

## Section 8: Effort & Thinking Directives

### Claude Opus 4.6

| Task | Effort Level | Rationale |
|---|---|---|
| Research execution prompt | `max` | Deepest reasoning for novel synthesis |
| Consolidation / merge | `max` | Highest-stakes reasoning task |
| Quick recency validation | `high` | Standard deep reasoning sufficient |
| Simple lookups | `medium` | Speed over depth |

```yaml
# Claude API Configuration
model: "claude-opus-4-6"
thinking:
  type: "adaptive"
effort: "max"
max_tokens: 16000  # Up to 128000
```

If over-thinking detected in output: add "Use deep reasoning for strategic analysis; move efficiently through factual compilation."

### Gemini 3.1 Pro Deep Research

| Task | Thinking Tier | Rationale |
|---|---|---|
| Primary research (any pattern) | High | Maximum reasoning for complex tasks |
| Follow-up verification | Medium | Balanced speed and depth |
| Quick fact checks | Low | Speed priority |

```yaml
# Gemini API Configuration (Interactions API)
agent: "deep-research-pro-preview-12-2025"
thinking: "High"
background: true
tools:
  - type: "file_search"
    file_search_store_names: ["fileSearchStores/[store-name]"]  # when applicable
```

### GPT-5.2 Deep Research

| Task | Thinking Setting | Rationale |
|---|---|---|
| Site-restricted deep investigation | Extended | Maximum depth on authoritative sources |
| Broad recency sweep | Standard | Balanced for broad coverage |
| Quick validation | Light | Speed priority |

### GPT-5.2 Chat

| Task | Mode | Rationale |
|---|---|---|
| Quick recency check | Instant | Speed is the primary value |
| Validation with reasoning | Thinking (Standard) | When reasoning matters |

---

## Section 9: Context Budget Planning

### Output Estimates by Model

| Model | Standard Output | Complex Output | Maximum |
|---|---|---|---|
| Claude Opus 4.6 | 15-40K tokens | 40-80K tokens | 128K tokens |
| Gemini 3.1 Pro | 30-60K tokens | 60-80K tokens | 64K tokens |
| GPT-5.2 Deep | 30-60K tokens | 60-80K tokens | ~80K tokens |
| GPT-5.2 Chat | 2-5K tokens | 5-10K tokens | ~15K tokens |

### Combined Budget by Mode

| Mode | Expected Combined | Context Tier | Strategy |
|---|---|---|---|
| SINGLE | 15-80K tokens | Standard | Single output, no consolidation needed |
| DUAL | 50-160K tokens | Standard | Both outputs unabridged, single consolidation pass |
| FULL | 80-250K tokens | Standard or Extended | All outputs unabridged |
| FULL (complex) | 150-300K+ tokens | Extended (beta) | Use 1M context, all unabridged |

**Principle**: Always prefer full unabridged outputs. Opus 4.6's 76% MRCR v2 means it attends throughout the context window.

---

## Section 10: FULL Mode Guidelines

When user requests FULL mode:

1. **Add "Do NOT cover" exclusions** to reduce redundancy across 3 models
2. **Claude**: Analytical synthesis + cross-domain reasoning + trade-off analysis
3. **Gemini**: Structured data retrieval + comprehensive cataloging + quantitative data
4. **GPT-5.2 Deep**: Site-restricted targeted investigation (default) OR quick recency validation (Chat)
5. Generate site restriction list per pattern from Section 6

### FULL Mode Default: GPT-5.2 Deep Research

GPT-5.2 Deep Research is the default for FULL mode. Site-restricted search is its unique differentiator. Use GPT-5.2 Chat only when:
- Topic doesn't benefit from site restrictions
- Time is constrained (< 30 min total research window)
- User explicitly requests "quick" or "lite" OpenAI coverage
