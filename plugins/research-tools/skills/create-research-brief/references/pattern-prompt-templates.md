# Pattern-Specific Prompt Templates

**Version**: 1.0
**Last validated**: 2026-03-04
**Consumed by**: create-research-brief (prompt generation per pattern x model x mode)

---

## How to Use This File

Each of the 9 research patterns has prompt templates for every model x mode combination:

| Model | DUAL variant | FULL variant |
|---|---|---|
| **Claude Opus 4.6** | Yes | Yes |
| **Gemini 3.1 Pro Deep Research** | Yes | Yes |
| **GPT-5.2 Deep Research** | No (FULL only) | Yes |
| **GPT-5.2 Chat/Lite** | No (FULL only) | Yes |

**DUAL templates**: No "Do NOT cover" exclusions. Both Claude and Gemini get full scope, differentiated by research approach (analytical vs. structured).

**FULL templates**: Include "Do NOT cover" exclusions to reduce redundancy across 3-4 models.

**Placeholders**: `[TOPIC]`, `[DOMAIN]`, `[PURPOSE]`, `[SPECIFIC_ASPECT]`, `[COMPETITOR_LIST]`, `[TECHNOLOGY]`, `[VERSION]`, `[MARKET_SEGMENT]`, `[REGULATORY_BODY]`, `[JURISDICTIONS]`, `[OPTIONS]`, `[CRITERIA]`, `[TIMEFRAME]`, `[USERS]`, `[SOLUTIONS]`, `[DOCUMENT_LIST]`

---

## 1. Landscape Mapping

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher mapping the landscape of [TOPIC] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources for rapidly evolving areas.

Focus your research and analysis on:

1. MARKET STRUCTURE ANALYSIS
   - What are the major categories of [TOPIC] in [DOMAIN], and what structural logic defines each category?
   - What determines whether a solution belongs in one category vs. another?
   - Search for: industry analyses, analyst reports, ecosystem overviews
   - Analyze: the underlying structural forces that created these categories

2. WHITE SPACE IDENTIFICATION
   - Where are the gaps — categories or segments with few or no solutions?
   - What demand signals suggest these gaps represent opportunities vs. genuinely unviable spaces?
   - Search for: user complaints about missing solutions, adjacent market entries, VC thesis posts
   - Analyze: why gaps exist (technical barriers, market timing, regulatory)

3. ECOSYSTEM DYNAMICS
   - What partnership, integration, and platform dynamics shape this landscape?
   - Where are network effects or lock-in creating winner-take-most dynamics?
   - What M&A trends signal category consolidation or expansion?
   - Search for: partnership announcements, integration directories, acquisition histories
   - Analyze: which structural forces are durable vs. transient

4. EVOLUTION TRAJECTORY
   - How is this landscape likely to evolve over the next 12-18 months?
   - What adjacent spaces or technologies could disrupt the current structure?
   - Search for: emerging technologies, regulatory changes, platform shifts
   - Analyze: which categories will grow, shrink, merge, or emerge

5. CROSS-DOMAIN SYNTHESIS
   After completing primary analysis:
   - What structural patterns from unrelated industry landscapes map to these findings?
   - Where does the conventional framing of this landscape miss something an outsider would catch?
   - What emergent properties arise from category interaction effects?
   - What would need to be true for the consensus landscape view to be wrong?

6. IMPLICATION ANALYSIS
   - What are the second-order consequences of the landscape structure you've identified?
   - Which structural dynamics interact to create non-obvious opportunities or risks?
   - What decisions does this landscape map enable or constrain?

Ground every claim in evidence. Distinguish between web-verified facts and your analytical reasoning. Surface non-obvious structural dynamics.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Internal contradictions between sections
- Claims about landscape structure asserted without supporting evidence
- Reasoning chains about market dynamics that don't survive scrutiny
- Coverage gaps against the dimensions above
- Opportunities for cross-domain structural insight you missed
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher mapping the landscape of [TOPIC] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources for rapidly evolving areas.

Do NOT cover: comprehensive player-by-player inventory (another model handles cataloging). Focus on structural analysis and dynamics.

Focus your research and analysis on:

1. MARKET STRUCTURE ANALYSIS
   - What are the major categories of [TOPIC] in [DOMAIN], and what structural logic defines each category?
   - What determines whether a solution belongs in one category vs. another?
   - Search for: industry analyses, analyst reports, ecosystem overviews
   - Analyze: the underlying structural forces that created these categories

2. WHITE SPACE IDENTIFICATION
   - Where are the gaps — categories or segments with few or no solutions?
   - What demand signals suggest these gaps represent opportunities vs. genuinely unviable spaces?
   - Search for: user complaints about missing solutions, adjacent market entries, VC thesis posts
   - Analyze: why gaps exist (technical barriers, market timing, regulatory)

3. ECOSYSTEM DYNAMICS AND EVOLUTION
   - What partnership, integration, and platform dynamics shape this landscape?
   - Where are network effects or lock-in creating winner-take-most dynamics?
   - How is this landscape likely to evolve over the next 12-18 months?
   - Search for: partnership announcements, integration directories, acquisition histories
   - Analyze: which structural forces are durable vs. transient

4. CROSS-DOMAIN SYNTHESIS
   After completing primary analysis:
   - What structural patterns from unrelated industry landscapes map to these findings?
   - Where does the conventional framing miss something an outsider would catch?
   - What would need to be true for the consensus landscape view to be wrong?

Ground every claim in evidence. Distinguish between web-verified facts and your analytical reasoning.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Internal contradictions between sections
- Claims asserted without supporting evidence
- Coverage gaps against the dimensions above
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger conducting a comprehensive inventory of the [TOPIC] landscape in [DOMAIN] to [PURPOSE].

Provide systematic, data-driven coverage of:

1. TAXONOMY CREATION
   - Define all major categories and subcategories of [TOPIC] in [DOMAIN]
   - Provide clear category definitions and boundary criteria
   - Create a taxonomy table with: category name, definition, estimated number of players, maturity level

2. COMPREHENSIVE PLAYER INVENTORY
   For each category in the taxonomy, create a structured table including:
   - Company/solution name
   - Founded/launched date
   - Funding stage and total raised (if applicable)
   - Target segment (enterprise, SMB, developer, consumer)
   - Key differentiator (one line)
   - Maturity level (early, growth, established)
   - Notable integrations/partnerships

3. FUNDING AND MATURITY DATA
   - Recent funding activity in this space (last 12 months)
   - M&A activity and consolidation trends
   - Create a funding timeline table for significant rounds
   - Include quantitative data where available

4. ECOSYSTEM RELATIONSHIP MAP
   - Key partnership and integration relationships
   - Platform dependencies and ecosystem alliances
   - Survey practitioner sentiment from community discussions, forums, and conference talks about ecosystem health
   - Create a relationship matrix showing which players integrate with which

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Provide structured inventories with consistent field sets per category
- Note where sources conflict on player details
- Distinguish between well-sourced facts and practitioner opinions
- Organize with clear section headers and navigable structure
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger conducting a comprehensive inventory of the [TOPIC] landscape in [DOMAIN] to [PURPOSE].

Provide systematic, data-driven coverage of:

1. TAXONOMY CREATION
   - Define all major categories and subcategories of [TOPIC] in [DOMAIN]
   - Provide clear category definitions and boundary criteria
   - Create a taxonomy table with: category name, definition, estimated number of players, maturity level

2. COMPREHENSIVE PLAYER INVENTORY
   For each category in the taxonomy, create a structured table including:
   - Company/solution name
   - Founded/launched date
   - Funding stage and total raised (if applicable)
   - Target segment (enterprise, SMB, developer, consumer)
   - Key differentiator (one line)
   - Maturity level (early, growth, established)
   - Notable integrations/partnerships

3. FUNDING AND MATURITY DATA
   - Recent funding activity in this space (last 12 months)
   - M&A activity and consolidation trends
   - Create a funding timeline table for significant rounds
   - Include quantitative data where available

4. ECOSYSTEM RELATIONSHIP MAP
   - Key partnership and integration relationships
   - Platform dependencies and ecosystem alliances
   - Survey practitioner sentiment from community discussions, forums, and conference talks
   - Create a relationship matrix showing integration patterns

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Provide structured inventories with consistent field sets
- Note where sources conflict
- Distinguish between well-sourced facts and practitioner opinions
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent developments in the [TOPIC] landscape in [DOMAIN].

Do NOT cover: structural market analysis or comprehensive player cataloging (other models handle those). Focus on recent events and authoritative source verification.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- crunchbase.com
- pitchbook.com
- producthunt.com
- techcrunch.com
- [DOMAIN-SPECIFIC trade publications]
- [DOMAIN-SPECIFIC analyst firm sites]

RESEARCH DIMENSIONS:

1. RECENT ENTRANTS (last 6 months)
   - What new players have entered this space since [6 months ago]?
   - What to find: launch announcements, Product Hunt launches, seed/Series A rounds
   - What to verify: are these genuinely new, or rebrands/pivots of existing players?

2. PIVOTS AND REPOSITIONING
   - Which existing players have significantly changed their positioning?
   - What to find: product rebrands, market repositioning announcements, leadership changes
   - Recent changes: pricing model shifts, target segment changes

3. M&A AND FUNDING EVENTS
   - What acquisitions or significant funding rounds have occurred?
   - What to find: acquisition announcements, funding round details, strategic investment signals
   - What these signal: consolidation trends, category validation, emerging segments

4. MOMENTUM SIGNALS
   - Which players are showing acceleration or deceleration signals?
   - What to find: hiring patterns, customer announcements, community growth metrics

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth. You have access to restricted, authoritative sources — use them for high-quality evidence.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on the [TOPIC] landscape in [DOMAIN].

Cover:
1. Most notable new entrants or exits in the last 6 months
2. Current momentum signals — which players are gaining or losing traction?
3. Emerging categories or segments not yet in mainstream coverage
4. Where the landscape today differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed developments and rumors.
```

---

## 2. Comparative Evaluation

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting a comparative evaluation of [OPTIONS] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Focus your research and analysis on:

1. TRADE-OFF ANALYSIS
   - For each option among [OPTIONS], what are the fundamental trade-offs?
   - Where does choosing one option foreclose future possibilities?
   - Search for: architecture decision records, migration stories, technology selection post-mortems
   - Analyze: which trade-offs are reversible vs. irreversible

2. HIDDEN DEPENDENCIES AND SECOND-ORDER EFFECTS
   - What are the non-obvious dependencies each option introduces?
   - What second-order effects emerge 6-12 months after adoption?
   - Search for: production experience reports, blog posts from teams who switched, "lessons learned" articles
   - Analyze: what costs and risks only become visible at scale or over time

3. DECISION SENSITIVITY ANALYSIS
   - Under what conditions does the optimal choice change?
   - Which evaluation criteria have the highest leverage — where a small weight shift flips the recommendation?
   - Search for: case studies of teams who chose differently and why
   - Analyze: what assumptions are embedded in each option's advantage

4. CROSS-DOMAIN PATTERN RECOGNITION
   - What analogous selection decisions in other domains illuminate this choice?
   - Where have similar trade-off structures led to surprising outcomes?
   - Search for: cross-industry technology adoption patterns
   - Analyze: what structural pattern does this selection decision follow

5. RECOMMENDATION AND ESCAPE ANALYSIS
   - Given the evidence, what is the defensible recommendation and why?
   - Under what conditions would the runner-up be the better choice?
   - What is the realistic cost of reversing this decision in 12 months?

Ground every claim in evidence. Distinguish between web-verified facts and your analytical reasoning. Surface non-obvious dynamics.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Confirmation bias toward any single option
- Trade-offs asserted without supporting evidence
- Missing consideration of less-popular options that may be superior
- Reasoning chains that don't survive scrutiny
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting a comparative evaluation of [OPTIONS] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: feature-by-feature comparison matrices or pricing table compilation (another model handles structured cataloging). Focus on strategic analysis and reasoning.

Focus your research and analysis on:

1. TRADE-OFF ANALYSIS
   - For each option among [OPTIONS], what are the fundamental trade-offs?
   - Where does choosing one option foreclose future possibilities?
   - Search for: architecture decision records, migration stories, post-mortems
   - Analyze: which trade-offs are reversible vs. irreversible

2. HIDDEN DEPENDENCIES AND SECOND-ORDER EFFECTS
   - What non-obvious dependencies does each option introduce?
   - What second-order effects emerge 6-12 months after adoption?
   - Search for: production experience reports, "lessons learned" articles
   - Analyze: costs and risks that only appear at scale

3. DECISION SENSITIVITY AND RECOMMENDATION
   - Under what conditions does the optimal choice change?
   - What is the defensible recommendation and why?
   - What would make the runner-up the better choice?
   - Search for: case studies of teams who chose differently
   - Analyze: embedded assumptions in each option's advantage

4. CROSS-DOMAIN SYNTHESIS
   - What analogous selection decisions in other domains illuminate this choice?
   - What would need to be true for the consensus recommendation to be wrong?

Ground every claim in evidence. Distinguish between facts and analytical reasoning.

SELF-REVIEW (mandatory before finalizing):
Review for confirmation bias, unsupported trade-offs, and missing considerations.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger conducting a data-driven comparison of [OPTIONS] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. FEATURE-BY-FEATURE COMPARISON MATRIX
   - Create a comprehensive comparison table of [OPTIONS] across all relevant feature dimensions
   - Include: feature availability (yes/no/partial), quality assessment, notable limitations
   - Organize features by category (core, integration, developer experience, enterprise, etc.)

2. PRICING AND COST COMPARISON
   - Create a pricing table showing all tiers for each option
   - Include: base price, usage-based costs, enterprise pricing (where available)
   - Note pricing model differences (seat-based vs. usage-based vs. flat)
   - Flag recent pricing changes

3. BENCHMARK DATA AND PERFORMANCE
   - Compile available benchmark comparisons across [OPTIONS]
   - Include: performance metrics, reliability data, scalability evidence
   - Create a benchmark comparison table with source attribution
   - Note benchmark methodology where available

4. CUSTOMER REVIEW SYNTHESIS
   - Aggregate customer sentiment from review platforms (G2, Capterra, etc.)
   - Include: overall scores, satisfaction by category, common praise/complaints
   - Create a sentiment comparison table
   - Survey practitioner sentiment from community discussions and forums

5. ADOPTION AND ECOSYSTEM METRICS
   - Usage/adoption metrics: market share, growth trends, community size
   - Ecosystem health: integrations, plugins, partner ecosystem
   - Create adoption metrics table with source dates

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Note where sources conflict on feature claims or pricing
- Distinguish between vendor-stated features and independently verified
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger conducting a data-driven comparison of [OPTIONS] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. FEATURE-BY-FEATURE COMPARISON MATRIX
   - Create a comprehensive comparison table of [OPTIONS] across all relevant feature dimensions
   - Include: feature availability (yes/no/partial), quality assessment, notable limitations
   - Organize features by category

2. PRICING AND COST COMPARISON
   - Create a pricing table showing all tiers for each option
   - Include: base price, usage-based costs, enterprise pricing (where available)
   - Note pricing model differences and recent pricing changes

3. BENCHMARK DATA AND PERFORMANCE
   - Compile available benchmark comparisons across [OPTIONS]
   - Create a benchmark comparison table with source attribution
   - Note benchmark methodology where available

4. CUSTOMER REVIEW SYNTHESIS
   - Aggregate customer sentiment from review platforms
   - Create a sentiment comparison table
   - Survey practitioner sentiment from community discussions and forums

5. ADOPTION AND ECOSYSTEM METRICS
   - Usage/adoption metrics: market share, growth trends, community size
   - Create adoption metrics table with source dates

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Note where sources conflict
- Distinguish between vendor-stated and independently verified features
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent developments affecting the comparison of [OPTIONS] in [DOMAIN].

Do NOT cover: strategic trade-off analysis or comprehensive feature cataloging (other models handle those). Focus on recent changes and authoritative verification.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- [VENDOR_1 official site]
- [VENDOR_2 official site]
- g2.com
- capterra.com
- gartner.com
- news.ycombinator.com

RESEARCH DIMENSIONS:

1. RECENT PRICING CHANGES
   - What pricing changes have any of [OPTIONS] made in the last 6 months?
   - What to find: pricing page updates, billing model changes, new tier introductions
   - What to verify: do current published prices match analyst reports?

2. RECENT FEATURE LAUNCHES
   - What significant features have been launched or deprecated?
   - What to find: changelog entries, release announcements, feature deprecation notices
   - Recent changes: beta features that have gone GA, features that have been sunset

3. SENTIMENT SHIFTS
   - How has user sentiment changed across review platforms?
   - What to find: recent review trends, community discussion sentiment, support quality signals
   - What to verify: are reported issues being resolved?

4. BREAKING CHANGES AND MIGRATION ISSUES
   - What breaking changes, API changes, or migration requirements have emerged?
   - What to find: migration guides, breaking change announcements, community workaround posts

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on the comparison of [OPTIONS] in [DOMAIN].

Cover:
1. Most notable pricing or feature changes in the last 6 months across [OPTIONS]
2. Current sentiment momentum — which option is gaining or losing favor?
3. Emerging concerns (security issues, reliability problems, vendor stability)
4. Where the comparison landscape today differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed developments and rumors.
```

---

## 3. Implementation Pattern

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher synthesizing implementation knowledge for [TOPIC] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources for evolving frameworks.

Focus your research and analysis on:

1. ARCHITECTURE DECISION RATIONALE
   - What are the key architecture decisions required for [TOPIC], and what factors determine the right choice for each?
   - What constraints (scale, latency, cost, team skill) shift the optimal decision?
   - Search for: architecture decision records (ADRs), tech blog posts explaining "why we chose X", migration retrospectives
   - Analyze: the decision space structure — which decisions are coupled, which are independent

2. PATTERN TRADE-OFFS AT SCALE
   - For each major implementation pattern, what works at small scale but breaks at production scale?
   - What operational surprises emerge only after deployment?
   - Search for: production post-mortems, scaling stories, performance optimization posts
   - Analyze: root causes of pattern failure — is it the pattern itself or misapplication?

3. ANTI-PATTERN ROOT CAUSE ANALYSIS
   - What anti-patterns have caused production failures for [TOPIC]?
   - What makes each anti-pattern tempting — why do teams fall into it?
   - Search for: incident reports, "what we learned" posts, Stack Overflow questions about common failures
   - Analyze: detection signals for each anti-pattern and correction strategies

4. CROSS-DOMAIN PATTERN IMPORTS
   - What proven implementation patterns from other domains apply to [TOPIC]?
   - Where have solutions to analogous problems in unrelated fields been overlooked?
   - Search for: cross-domain architecture discussions, patterns from adjacent technology areas
   - Analyze: which cross-domain patterns transfer cleanly vs. require adaptation

5. IMPLEMENTATION SEQUENCE AND DECISION TREES
   - What is the recommended implementation sequence, and what are the decision points?
   - At each decision point, what factors determine the right path?
   - Search for: implementation guides, step-by-step migration paths, starter templates
   - Analyze: common stumbling points and how to navigate them

6. IMPLICATION ANALYSIS
   - What are the second-order consequences of the key architecture decisions?
   - Which implementation choices interact to create non-obvious risks?

Ground every claim in evidence. Distinguish between web-verified facts and your analytical reasoning.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Architecture decisions asserted without trade-off analysis
- Anti-patterns listed without root cause explanation
- Missing consideration of operational concerns at scale
- Reasoning chains about pattern trade-offs that don't survive scrutiny
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher synthesizing implementation knowledge for [TOPIC] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: code-level pattern catalogs, reference architecture inventories, or benchmark compilations (another model handles structured cataloging). Focus on decision rationale, trade-offs, and anti-pattern analysis.

Focus your research and analysis on:

1. ARCHITECTURE DECISION RATIONALE
   - What are the key architecture decisions for [TOPIC], and what factors determine the right choice?
   - What constraints shift the optimal decision?
   - Search for: ADRs, tech blog posts explaining "why we chose X", migration retrospectives
   - Analyze: which decisions are coupled vs. independent

2. PATTERN TRADE-OFFS AT SCALE
   - What works at small scale but breaks at production scale?
   - What operational surprises emerge only after deployment?
   - Search for: production post-mortems, scaling stories
   - Analyze: root causes of pattern failure

3. ANTI-PATTERN ROOT CAUSE ANALYSIS
   - What anti-patterns have caused production failures?
   - Why are they tempting — what makes teams fall into them?
   - Search for: incident reports, "what we learned" posts
   - Analyze: detection signals and correction strategies

4. CROSS-DOMAIN SYNTHESIS
   - What implementation patterns from other domains apply?
   - What would need to be true for the conventional architecture approach to be wrong?

Ground every claim in evidence. Distinguish between facts and analytical reasoning.

SELF-REVIEW (mandatory before finalizing):
Review for unsupported architecture claims, missing trade-offs, and overlooked operational concerns.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive implementation reference for [TOPIC] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. REFERENCE ARCHITECTURE CATALOG
   - Document all major architecture patterns for [TOPIC]
   - For each pattern, create a structured entry with:
     - Pattern name and description
     - When to use (ideal conditions)
     - When to avoid (contraindications)
     - Key components and their interactions
     - Known production deployments (with evidence)
   - Create a pattern comparison table

2. CODE PATTERN EXAMPLES
   - Catalog idiomatic implementation patterns with examples
   - For each pattern:
     - Code structure or pseudocode
     - Configuration requirements
     - Common variations
   - Organize by implementation phase (setup, core logic, deployment, operations)

3. BENCHMARK COMPARISONS
   - Compile available performance benchmarks for different implementation approaches
   - Include: latency, throughput, resource consumption, cost-at-scale
   - Create a benchmark comparison table with methodology notes
   - Survey practitioner sentiment on real-world performance from community discussions

4. OPEN-SOURCE PROJECT ANALYSIS
   - Catalog relevant open-source projects, templates, and starter kits
   - For each, document: stars/forks, last update, maintenance status, key features
   - Create an inventory table with adoption and health metrics

5. DEPENDENCY MATRICES
   - Map the dependency relationships for [TOPIC] implementation
   - Version compatibility constraints
   - Create a dependency/compatibility matrix

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Include code examples where relevant
- Note where community opinions conflict on best approach
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive implementation reference for [TOPIC] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. REFERENCE ARCHITECTURE CATALOG
   - Document all major architecture patterns for [TOPIC]
   - For each pattern, create a structured entry with: name, when to use, when to avoid, key components, known deployments
   - Create a pattern comparison table

2. CODE PATTERN EXAMPLES
   - Catalog idiomatic implementation patterns with examples
   - Organize by implementation phase

3. BENCHMARK COMPARISONS
   - Compile available performance benchmarks for different approaches
   - Create a benchmark comparison table with methodology notes
   - Survey practitioner sentiment on real-world performance

4. OPEN-SOURCE PROJECT ANALYSIS
   - Catalog relevant open-source projects, templates, and starter kits
   - Create an inventory table with adoption and health metrics

5. DEPENDENCY MATRICES
   - Map dependency relationships and version compatibility
   - Create a dependency/compatibility matrix

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Include code examples where relevant
- Note where community opinions conflict
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent production experience and community knowledge for [TOPIC] implementation in [DOMAIN].

Do NOT cover: architectural reasoning or code pattern catalogs (other models handle those). Focus on recent incidents, community workarounds, and practitioner-sourced implementation intelligence.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- github.com (repos, issues, discussions for [TOPIC])
- stackoverflow.com
- [OFFICIAL_DOCS_SITE]
- eng.uber.com
- netflixtechblog.com
- [DOMAIN-SPECIFIC engineering blogs]

RESEARCH DIMENSIONS:

1. RECENT PRODUCTION INCIDENTS
   - What production incidents or failures related to [TOPIC] have been reported in the last 6 months?
   - What to find: post-mortems, incident reports, GitHub issues labeled "bug" or "critical"
   - What to verify: were root causes identified and fixes confirmed?

2. COMMUNITY WORKAROUNDS
   - What workarounds has the community developed for known issues?
   - What to find: GitHub discussions, Stack Overflow answers with high votes, blog posts about "how we fixed X"
   - Recent changes: newly discovered workarounds, official fixes that replace old workarounds

3. MIGRATION GUIDES AND BREAKING CHANGES
   - What migration guides or breaking change notices have been published?
   - What to find: version upgrade guides, deprecation notices, migration tools
   - What to verify: community success rate with recommended migration paths

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on [TOPIC] implementation in [DOMAIN].

Cover:
1. Most notable recent releases, breaking changes, or deprecations (last 6 months)
2. Current community sentiment — is momentum growing or declining?
3. Emerging implementation approaches not yet in mainstream guides
4. Known issues currently affecting production deployments

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed issues and anecdotal reports.
```

---

## 4. Best Practices

**Note**: Best Practices uses an 8-dimension framework. The templates below serve as wrappers. Dimension-specific prompt fragments are loaded from `best-practices-dimensions.md` and assembled per technology family weighting from `technology-profiles.md`.

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher building a practitioner knowledge base for [TECHNOLOGY] [VERSION] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources, especially for rapidly evolving technologies.

Your goal is to capture what expert practitioners know about [TECHNOLOGY] that goes BEYOND official documentation — the hard-won knowledge from production experience.

Organize your research across these dimensions (weighted by importance for this technology):

1. IDIOMATIC PATTERNS WITH REASONING
   - What are the idiomatic ways to use [TECHNOLOGY], and WHY are they idiomatic?
   - What makes a pattern "idiomatic" vs. "merely functional"?
   - Search for: style guides, expert blog posts, conference talks, highly-voted Stack Overflow answers
   - Analyze: the reasoning behind each convention — is it performance, maintainability, or historical accident?

2. ANTI-PATTERNS WITH ROOT CAUSE ANALYSIS
   - What are the known anti-patterns for [TECHNOLOGY], and what root causes drive teams toward them?
   - What detection signals indicate an anti-pattern is forming?
   - Search for: "don't do this" posts, production failure stories, code review guidelines
   - Analyze: why each anti-pattern is tempting and what structural forces create it

3. DECISION TREES
   - What are the critical decision points when working with [TECHNOLOGY]?
   - At each decision point, what factors determine the right path?
   - Search for: "when to use X vs. Y" discussions, configuration guides, architecture guidance
   - Analyze: decision criteria that are context-dependent vs. universal

4. ESCAPE HATCHES AND WORKAROUNDS
   - What are the known limitations of [TECHNOLOGY], and what are the proven escape hatches?
   - When should you work around the framework vs. fight through it?
   - Search for: workaround posts, "how I solved X" blog entries, GitHub issues with workaround labels
   - Analyze: which workarounds are stable vs. likely to break with updates

5. CROSS-DOMAIN INSIGHTS
   After completing primary analysis:
   - What patterns from other technology ecosystems apply to [TECHNOLOGY]?
   - What would an expert in an analogous technology notice that [TECHNOLOGY] practitioners miss?
   - Where does the community consensus have blind spots?

[DIMENSION_FRAGMENTS]

Ground every claim in evidence. Distinguish between web-verified facts and your analytical reasoning. Capture the "why" behind every practice.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Practices listed without reasoning ("do X" without "because Y")
- Anti-patterns without root cause analysis
- Decision trees that don't account for context variation
- Coverage gaps across the 8 dimensions
- Opportunities for cross-domain insight
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher building a practitioner knowledge base for [TECHNOLOGY] [VERSION] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: version compatibility matrices, benchmark data compilations, or community issue catalogs (another model handles structured cataloging). Focus on pattern reasoning, anti-pattern analysis, decision trees, and cross-domain insights.

Organize your research across these dimensions:

1. IDIOMATIC PATTERNS WITH REASONING
   - What are the idiomatic ways to use [TECHNOLOGY], and WHY?
   - Search for: style guides, expert blog posts, conference talks
   - Analyze: the reasoning behind each convention

2. ANTI-PATTERNS WITH ROOT CAUSE ANALYSIS
   - What are the known anti-patterns, and what root causes drive teams toward them?
   - Search for: "don't do this" posts, production failure stories
   - Analyze: why each anti-pattern is tempting

3. DECISION TREES
   - What are the critical decision points when working with [TECHNOLOGY]?
   - Search for: "when to use X vs. Y" discussions, architecture guidance
   - Analyze: context-dependent vs. universal decision criteria

4. ESCAPE HATCHES AND WORKAROUNDS
   - What are the known limitations and proven escape hatches?
   - Search for: workaround posts, GitHub issues with workaround labels
   - Analyze: which workarounds are stable vs. fragile

5. CROSS-DOMAIN SYNTHESIS
   - What patterns from other ecosystems apply?
   - What would need to be true for the community consensus to be wrong?

[DIMENSION_FRAGMENTS]

Ground every claim in evidence. Capture the "why" behind every practice.

SELF-REVIEW (mandatory before finalizing):
Review for practices without reasoning, anti-patterns without root causes, and dimension gaps.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive data-driven knowledge base for [TECHNOLOGY] [VERSION] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. DOCUMENTATION STATE ASSESSMENT
   - Current official documentation quality and completeness
   - Known documentation gaps or outdated sections
   - Community-maintained documentation and guides
   - Create a documentation coverage table: area, official doc quality, community supplement quality

2. VERSION COMPATIBILITY MATRIX
   - Create a comprehensive version compatibility table for [TECHNOLOGY] with its ecosystem
   - Include: [TECHNOLOGY] version, dependency versions, known incompatibilities, support status
   - Flag end-of-life dates and upcoming version transitions
   - Note migration path availability between versions

3. COMMUNITY ISSUES AND SENTIMENT
   - Catalog the most common issues from GitHub issues, Stack Overflow, and forums
   - Create a "top issues" table: issue, frequency, severity, status (open/resolved/workaround)
   - Survey practitioner sentiment from community discussions, forums, and conference talks
   - Note where practitioner opinion diverges from official guidance

4. BENCHMARK DATA AND PERFORMANCE CHARACTERISTICS
   - Compile available performance benchmarks for [TECHNOLOGY]
   - Include: metric, value, conditions, methodology, source
   - Create a performance characteristics table
   - Compare against alternatives where data is available

5. OPERATIONAL PATTERNS
   - Monitoring and observability approaches
   - Deployment patterns and configuration management
   - Create a structured inventory of operational tooling

[DIMENSION_FRAGMENTS]

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Provide structured inventories with consistent fields
- Note where sources conflict
- Distinguish between well-sourced facts and practitioner opinions
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a data-driven knowledge base for [TECHNOLOGY] [VERSION] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. VERSION COMPATIBILITY MATRIX
   - Create a comprehensive version compatibility table for [TECHNOLOGY]
   - Include: dependency versions, known incompatibilities, support status
   - Flag end-of-life dates and upcoming version transitions

2. COMMUNITY ISSUES AND SENTIMENT
   - Catalog the most common issues from GitHub, Stack Overflow, forums
   - Create a "top issues" table: issue, frequency, severity, status
   - Survey practitioner sentiment from community discussions

3. BENCHMARK DATA
   - Compile available performance benchmarks
   - Create a performance characteristics table

4. DOCUMENTATION AND OPERATIONAL PATTERNS
   - Documentation coverage assessment
   - Monitoring, deployment, and configuration patterns
   - Create structured inventories

[DIMENSION_FRAGMENTS]

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Note where sources conflict
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent changes and community-sourced intelligence for [TECHNOLOGY] [VERSION] in [DOMAIN].

Do NOT cover: pattern reasoning, anti-pattern analysis, or decision tree construction (other models handle those). Focus on recent breaking changes, deprecations, and community workarounds.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- [OFFICIAL_DOCS_SITE]
- github.com/[REPO]/issues
- github.com/[REPO]/discussions
- stackoverflow.com (tagged [TECHNOLOGY])
- [COMMUNITY_FORUM]

RESEARCH DIMENSIONS:

1. RECENT BREAKING CHANGES AND DEPRECATIONS
   - What breaking changes have been introduced in the last 6 months?
   - What to find: release notes, migration guides, deprecation notices
   - What to verify: are migration paths documented and tested by community?

2. RECENTLY DISCOVERED ISSUES AND WORKAROUNDS
   - What new issues have emerged with recent versions?
   - What to find: new GitHub issues with high engagement, Stack Overflow questions on new problems
   - Recent changes: official fixes vs. community workarounds

3. COMMUNITY MIGRATION EXPERIENCES
   - How are teams migrating between versions or from alternatives?
   - What to find: migration blog posts, GitHub discussion threads about upgrade experiences
   - What to verify: success rate of recommended migration paths

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on [TECHNOLOGY] [VERSION] best practices in [DOMAIN].

Cover:
1. Most notable recent releases, deprecations, or breaking changes (last 6 months)
2. Current community sentiment — growing enthusiasm or growing frustration?
3. Emerging best practices not yet in official documentation
4. Known issues currently under active discussion

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed changes and community speculation.
```

---

## 5. Competitive Intelligence

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting competitive intelligence analysis of [COMPETITOR_LIST] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Focus your research and analysis on:

1. MOAT SUSTAINABILITY ANALYSIS
   - For each competitor in [COMPETITOR_LIST], what constitutes their competitive moat?
   - How defensible is each moat — what structural factors sustain or erode it?
   - Search for: competitive advantage discussions, investor analyses, industry expert commentary
   - Analyze: which moats are deepening vs. narrowing, and what forces drive the change

2. STRATEGIC POSITIONING DYNAMICS
   - How is each competitor positioned, and how is that positioning evolving?
   - Where are competitors converging (feature parity) vs. diverging (differentiation)?
   - Search for: product positioning changes, messaging evolution, target market shifts
   - Analyze: whether stated differentiation has substance or is marketing fiction

3. COMPETITIVE RESPONSE SCENARIOS
   - What are each competitor's likely next 2-3 strategic moves based on their trajectory?
   - Under what conditions would a competitor pivot to directly challenge [SPECIFIC_ASPECT]?
   - Search for: hiring patterns, patent filings, technology investments, partnership signals
   - Analyze: what each competitor's behavior reveals about their strategic intent

4. DIFFERENTIATION DURABILITY
   - Where is genuine, sustainable differentiation vs. temporary advantage?
   - What competitive dynamics (pricing pressure, feature convergence, platform effects) are reshaping the space?
   - Search for: feature launch cadence, pricing movement, customer switching stories
   - Analyze: half-life of each differentiation claim

5. CROSS-DOMAIN COMPETITIVE PATTERNS
   After completing primary analysis:
   - What competitive dynamics from other industries illuminate this competitive landscape?
   - Where has a similar competitive structure led to surprising outcomes?
   - What would need to be true for the current competitive consensus to be wrong?

6. STRATEGIC IMPLICATIONS
   - What opportunities do competitor vulnerabilities create?
   - What threats do competitor strengths pose?
   - What competitive dynamics require immediate response vs. monitoring?

Ground every claim in evidence. Distinguish between web-verified facts, inferred strategic intent, and your analytical reasoning. Flag confidence level on all strategic predictions.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Confirmation bias (are you telling the story you expected?)
- Strategic claims without behavioral evidence
- Missing consideration of competitors' perspective on YOUR position
- Competitive dynamics that don't survive adversarial scrutiny
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting competitive intelligence analysis of [COMPETITOR_LIST] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: feature-level comparison matrices, pricing table compilation, or market share data gathering (another model handles structured cataloging). Focus on strategic analysis and competitive dynamics.

Focus your research and analysis on:

1. MOAT SUSTAINABILITY ANALYSIS
   - For each competitor, what constitutes their moat and how defensible is it?
   - Search for: competitive advantage discussions, investor analyses
   - Analyze: which moats are deepening vs. narrowing

2. COMPETITIVE RESPONSE SCENARIOS
   - What are each competitor's likely next 2-3 strategic moves?
   - Under what conditions would they pivot to challenge [SPECIFIC_ASPECT]?
   - Search for: hiring patterns, technology investments, partnership signals
   - Analyze: what behavior reveals about strategic intent

3. DIFFERENTIATION DURABILITY
   - Where is genuine differentiation vs. temporary advantage?
   - What dynamics are reshaping the competitive space?
   - Search for: feature convergence trends, pricing pressure, platform effects
   - Analyze: half-life of differentiation claims

4. CROSS-DOMAIN SYNTHESIS
   - What competitive dynamics from other industries illuminate this landscape?
   - What would need to be true for the competitive consensus to be wrong?

Ground every claim in evidence. Flag confidence on all strategic predictions.

SELF-REVIEW (mandatory before finalizing):
Review for confirmation bias, unsupported strategic claims, and missing adversarial scrutiny.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive competitive data set for [COMPETITOR_LIST] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. FEATURE COMPARISON MATRIX
   - Create a detailed feature comparison table across [COMPETITOR_LIST]
   - Include: feature availability, quality tier, recent additions, planned features
   - Organize by feature category (core product, integrations, analytics, support, etc.)

2. PRICING COMPARISON
   - Create a pricing comparison table for all competitors
   - Include: pricing model, tiers, per-unit costs, enterprise pricing (where available)
   - Note recent pricing changes and pricing model evolution
   - Flag free tier limitations and trial terms

3. MARKET SHARE AND ADOPTION DATA
   - Compile market share estimates from multiple sources
   - Include: revenue estimates, customer count, growth metrics, geographic distribution
   - Create a market share table with source attribution and dates
   - Note where estimates diverge across sources

4. FUNDING HISTORY AND FINANCIAL HEALTH
   - Document funding history for each competitor
   - Include: round dates, amounts, investors, valuation (where available)
   - Revenue growth trajectory (public or estimated)
   - Create a funding timeline comparison table

5. TEAM AND HIRING SIGNALS
   - Current team size and growth rate
   - Key executive changes in the last 12 months
   - Hiring patterns that signal strategic direction
   - Survey practitioner sentiment from community discussions about each competitor

6. POSITIONING MAP
   - Create a positioning table mapping each competitor across key strategic dimensions
   - Include: target market, primary value proposition, go-to-market approach
   - Note positioning evolution over last 12 months

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all multi-option analyses
- Note where sources conflict on competitor data
- Distinguish between public data and estimates
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive competitive data set for [COMPETITOR_LIST] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. FEATURE COMPARISON MATRIX
   - Create a detailed feature comparison table across [COMPETITOR_LIST]
   - Include: feature availability, quality tier, recent additions

2. PRICING COMPARISON
   - Create a pricing comparison table for all competitors
   - Note recent pricing changes and pricing model evolution

3. MARKET SHARE AND ADOPTION DATA
   - Compile market share estimates from multiple sources
   - Create a market share table with source attribution and dates

4. FUNDING HISTORY AND FINANCIAL HEALTH
   - Document funding history for each competitor
   - Create a funding timeline comparison table

5. TEAM AND HIRING SIGNALS
   - Key executive changes and hiring patterns
   - Survey practitioner sentiment from community discussions

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all analyses
- Note where sources conflict
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent competitive moves for [COMPETITOR_LIST] in [DOMAIN].

Do NOT cover: strategic moat analysis or comprehensive feature cataloging (other models handle those). Focus on recent events and authoritative signal verification.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- [COMPETITOR_1_DOMAIN]
- [COMPETITOR_2_DOMAIN]
- techcrunch.com
- theinformation.com
- g2.com
- gartner.com
- linkedin.com

RESEARCH DIMENSIONS:

1. RECENT STRATEGIC MOVES (last 6 months)
   - What product launches, pivots, or major feature releases have occurred?
   - What to find: product announcements, launch blog posts, feature changelogs
   - What to verify: are announced features actually available?

2. RECENT PRICING CHANGES
   - Have any competitors changed pricing models or price points?
   - What to find: pricing page changes, billing announcements, customer reactions
   - What these signal: margin pressure, segment targeting shifts

3. PARTNERSHIP AND ECOSYSTEM ANNOUNCEMENTS
   - What new partnerships, integrations, or ecosystem moves have been made?
   - What to find: partnership press releases, integration announcements, API launches
   - What these signal: platform strategy, market expansion direction

4. HIRING AND LEADERSHIP SIGNALS
   - Key hires, departures, or organizational changes
   - What to find: executive announcements, job postings, organizational restructuring

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on competitive dynamics for [COMPETITOR_LIST] in [DOMAIN].

Cover:
1. Most notable competitive moves in the last 6 months
2. Current momentum — which competitors are gaining or losing ground?
3. Emerging competitive threats not yet in mainstream analyst coverage
4. Where the competitive landscape today differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed moves and speculation.
```

---

## 6. Market Research

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher analyzing the market for [TOPIC] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Focus your research and analysis on:

1. MARKET STRUCTURE DYNAMICS
   - Is this a winner-take-all, oligopolistic, or fragmented market — and what structural forces determine this?
   - What stage is this market in (emerging, growth, mature, declining)?
   - Search for: market structure analyses, industry reports, academic research on market dynamics
   - Analyze: whether structural forces favor consolidation or fragmentation over time

2. SEGMENT ATTRACTIVENESS ANALYSIS
   - Which market segments are most attractive and why?
   - What drives segment growth — technology adoption, regulatory push, buyer behavior shifts?
   - Search for: segment analyses, growth driver discussions, customer acquisition patterns
   - Analyze: which segments have the best combination of size, growth, accessibility, and competitive dynamics

3. ENTRY BARRIER ASSESSMENT
   - What barriers to entry exist (technical, regulatory, capital, network effects, brand)?
   - How are these barriers evolving — rising or falling?
   - Search for: startup entry stories, market entry case studies, regulatory barrier analyses
   - Analyze: which barriers are structural vs. temporary

4. DEMAND DRIVER REASONING
   - What forces are growing or shrinking demand in this market?
   - Which demand drivers are cyclical vs. secular?
   - Search for: industry trend reports, demand analysis, technology adoption curves
   - Analyze: which demand drivers are strengthening vs. weakening

5. CROSS-DOMAIN MARKET PATTERNS
   After completing primary analysis:
   - What market dynamics from analogous markets illuminate this one?
   - Where have similar market structures led to surprising evolutions?
   - What would need to be true for the consensus market outlook to be wrong?

6. STRATEGIC IMPLICATIONS
   - Given the market structure, what entry strategy optimizes for [PURPOSE]?
   - What timing considerations affect market entry?
   - Which segments should be prioritized and why?

Ground every claim in evidence. Distinguish between web-verified market data and your analytical reasoning. Present ranges rather than point estimates.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Market sizing claims without methodology or source
- Segment boundaries that don't hold under scrutiny
- Demand drivers that are assumed rather than evidenced
- Missing consideration of disruptive scenarios
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher analyzing the market for [TOPIC] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: quantitative market sizing data (TAM/SAM/SOM numbers), growth rate compilations, or geographic distribution data (another model handles data gathering). Focus on structural dynamics, segment attractiveness reasoning, and entry barrier analysis.

Focus your research and analysis on:

1. MARKET STRUCTURE DYNAMICS
   - Is this winner-take-all, oligopolistic, or fragmented — what structural forces determine this?
   - Search for: market structure analyses, industry reports
   - Analyze: consolidation vs. fragmentation forces

2. SEGMENT ATTRACTIVENESS REASONING
   - Which segments are most attractive and why?
   - What drives segment growth?
   - Search for: segment analyses, growth driver discussions
   - Analyze: best combination of size, growth, accessibility

3. ENTRY BARRIER ASSESSMENT
   - What barriers exist and how are they evolving?
   - Search for: market entry case studies, regulatory analyses
   - Analyze: structural vs. temporary barriers

4. CROSS-DOMAIN SYNTHESIS
   - What dynamics from analogous markets illuminate this one?
   - What would need to be true for the consensus outlook to be wrong?

Ground every claim in evidence. Present ranges rather than point estimates.

SELF-REVIEW (mandatory before finalizing):
Review for unsupported sizing, questionable segment boundaries, and assumed demand drivers.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger conducting comprehensive market data collection for [TOPIC] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. MARKET SIZING (TAM/SAM/SOM)
   - Total Addressable Market: estimated size with methodology
   - Serviceable Addressable Market: scoped to [MARKET_SEGMENT]
   - Serviceable Obtainable Market: realistic capture estimate
   - Create a market sizing table with: metric, value (range), methodology, source, date
   - Reconcile estimates from multiple sources where available

2. GROWTH RATES AND PROJECTIONS
   - Historical growth rate (last 3-5 years)
   - Projected growth rate (next 3-5 years)
   - Create a growth trajectory table with: year, market size, growth rate, source
   - Note where growth projections diverge across analyst reports

3. SEGMENT BREAKDOWN
   - Define market segments with clear boundary criteria
   - For each segment, document: size, growth rate, key players, barriers to entry
   - Create a segment comparison table
   - Rank segments by attractiveness

4. GEOGRAPHIC DISTRIBUTION
   - Market size by region/country
   - Regional growth rate differences
   - Create a geographic market distribution table
   - Note regulatory factors affecting geographic expansion

5. FUNDING ACTIVITY AND INVESTMENT SIGNALS
   - Recent funding activity in this market (last 12 months)
   - Investment thesis patterns from VC activity
   - Create a funding activity table: company, round, amount, date, investor
   - Survey practitioner and investor sentiment from community discussions

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all sizing analyses
- Present ranges, not point estimates, for all sizing figures
- Note methodological differences between sources
- Distinguish between primary research data and model estimates
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger conducting comprehensive market data collection for [TOPIC] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. MARKET SIZING (TAM/SAM/SOM)
   - Create a market sizing table with: metric, value (range), methodology, source, date
   - Reconcile estimates from multiple sources

2. GROWTH RATES AND PROJECTIONS
   - Create a growth trajectory table: year, market size, growth rate, source
   - Note where projections diverge across reports

3. SEGMENT BREAKDOWN
   - Define segments with clear boundaries
   - Create a segment comparison table with: size, growth, key players, barriers

4. GEOGRAPHIC DISTRIBUTION
   - Market size by region with regulatory factors
   - Create a geographic distribution table

5. FUNDING ACTIVITY
   - Recent funding in this market (last 12 months)
   - Create a funding activity table
   - Survey investor sentiment

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Present ranges, not point estimates
- Note methodological differences between sources
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Deep Recency Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a deep recency investigator researching recent market developments for [TOPIC] in [DOMAIN].

Do NOT cover: structural market analysis or comprehensive sizing data (other models handle those). Focus on recent funding, segment shifts, and regulatory changes.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- crunchbase.com
- pitchbook.com
- sec.gov
- statista.com
- [DOMAIN-SPECIFIC trade publications]
- [DOMAIN-SPECIFIC analyst report sites]

RESEARCH DIMENSIONS:

1. RECENT FUNDING ROUNDS (last 6 months)
   - What significant funding events have occurred?
   - What to find: round announcements, investor commentary, valuation data
   - What these signal: which segments are attracting capital, investor thesis shifts

2. SEGMENT SHIFTS
   - Have any market segments shown accelerating or decelerating growth?
   - What to find: analyst report updates, market sizing revisions, adoption rate changes
   - Recent changes: segments that are emerging, converging, or declining

3. REGULATORY CHANGES AFFECTING MARKET
   - What regulatory developments have impacted this market?
   - What to find: new regulations, enforcement actions, policy proposals
   - What to verify: implementation timelines and market impact estimates

4. EMERGING MARKET SIGNALS
   - What early-stage signals suggest market evolution?
   - What to find: new market entrants from adjacent spaces, technology enablers, buyer behavior shifts

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on the market for [TOPIC] in [DOMAIN].

Cover:
1. Most notable funding events or exits in the last 6 months
2. Current market momentum — accelerating or decelerating?
3. Emerging market segments or buyer behavior shifts not yet in analyst reports
4. Where the market today differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed data and market speculation.
```

---

## 7. User Research

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting user research for [USERS] of [SOLUTIONS] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Focus your research and analysis on:

1. JOBS-TO-BE-DONE FRAMEWORK
   - What are the primary jobs [USERS] are hiring [SOLUTIONS] to do?
   - Map jobs across three layers: functional (what task), emotional (how they want to feel), social (how they want to be perceived)
   - Search for: user discussions on forums and communities, product reviews explaining "why I use X", switching stories
   - Analyze: the job hierarchy — which jobs are primary drivers vs. secondary considerations

2. UNMET NEEDS HIERARCHY
   - What needs are consistently unmet by current [SOLUTIONS]?
   - Rank needs by: frequency (how many users experience this) x intensity (how painful is it) x solution gap (how poorly served)
   - Search for: feature requests, complaint threads, negative reviews with specific pain points, workaround descriptions
   - Analyze: why these needs remain unmet (technical difficulty, misaligned incentives, market blindness)

3. BEHAVIORAL DRIVER ANALYSIS
   - What drives adoption and switching behavior for [SOLUTIONS]?
   - What triggers the "job search" — when do users start looking for a new solution?
   - Search for: switching stories, "why I left X for Y" posts, adoption decision threads
   - Analyze: the decision journey from awareness to adoption to retention or churn

4. PERSONA SYNTHESIS WITH PSYCHOLOGICAL DEPTH
   - Beyond demographics, what behavioral segments exist among [USERS]?
   - What are each segment's goals, frustrations, current solutions, and decision criteria?
   - Search for: user self-descriptions, community segmentation, usage pattern discussions
   - Analyze: what psychological and situational factors differentiate user segments

5. WORKAROUND ANALYSIS
   - What workarounds have [USERS] built to fill gaps in current [SOLUTIONS]?
   - What do these workarounds reveal about what solutions are missing?
   - Search for: DIY solutions, tool combinations, custom scripts, community-built extensions
   - Analyze: which workarounds signal the highest-value product opportunities

6. CROSS-DOMAIN BEHAVIORAL PATTERNS
   After completing primary analysis:
   - What user behavior patterns from analogous domains apply to [USERS]?
   - Where does the conventional understanding of these users have blind spots?
   - What would need to be true for the consensus user model to be wrong?

Ground every claim in evidence. Distinguish between web-verified user signals and your analytical reasoning. Prioritize direct user voices (reviews, forum posts, community discussions) over secondary sources.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Personas based on demographics rather than behaviors
- Needs asserted without evidence from actual user voices
- Workarounds overlooked that signal unmet needs
- Confirmation bias toward pre-existing user models
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting user research for [USERS] of [SOLUTIONS] in [DOMAIN] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: demographic data compilation, usage pattern surveys, or review score aggregation (another model handles structured data). Focus on JTBD analysis, behavioral drivers, persona synthesis, and unmet needs hierarchy.

Focus your research and analysis on:

1. JOBS-TO-BE-DONE FRAMEWORK
   - What jobs are [USERS] hiring [SOLUTIONS] to do (functional, emotional, social)?
   - Search for: user discussions, switching stories, "why I use X" posts
   - Analyze: job hierarchy and primary drivers

2. UNMET NEEDS HIERARCHY
   - What needs are consistently unmet? Rank by frequency x intensity x gap.
   - Search for: feature requests, complaints, workaround descriptions
   - Analyze: why needs remain unmet

3. BEHAVIORAL DRIVERS AND PERSONA SYNTHESIS
   - What drives adoption, switching, and churn?
   - What behavioral segments exist beyond demographics?
   - Search for: switching stories, adoption decision threads
   - Analyze: psychological and situational differentiators

4. WORKAROUND ANALYSIS AND CROSS-DOMAIN PATTERNS
   - What workarounds signal unmet needs?
   - What user patterns from analogous domains apply?
   - What would need to be true for the consensus user model to be wrong?

Ground every claim in evidence. Prioritize direct user voices.

SELF-REVIEW (mandatory before finalizing):
Review for demographic fixation, unsupported needs, and overlooked workarounds.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive user data set for [USERS] of [SOLUTIONS] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. DEMOGRAPHIC DATA
   - Compile demographic profiles of [USERS] from available research
   - Include: age ranges, roles/titles, company sizes, industries, experience levels
   - Create a demographic summary table with source attribution
   - Note where demographic data varies by source

2. USAGE PATTERN DATA
   - Document how [USERS] currently use [SOLUTIONS]
   - Include: frequency of use, common workflows, feature utilization rates
   - Create a usage pattern table: workflow, frequency, satisfaction level
   - Compile any available survey data on usage patterns

3. REVIEW AND SENTIMENT AGGREGATION
   - Aggregate reviews from G2, Capterra, App Store, ProductHunt, etc.
   - For each major solution, document: overall rating, category ratings, review count, trend
   - Create a sentiment comparison table across solutions
   - Catalog top praised features and top complaints per solution
   - Survey practitioner sentiment from community discussions, Reddit, and forums

4. SATISFACTION SCORES AND NPS DATA
   - Compile customer satisfaction and NPS data where available
   - Include: overall scores, segment-specific scores, trend over time
   - Create a satisfaction comparison table
   - Note sample sizes and methodology

5. COMMUNITY DISCUSSION SYNTHESIS
   - Catalog common discussion themes from relevant communities
   - Include: subreddits, forums, Slack communities, Discord servers
   - Create a theme frequency table: topic, frequency, sentiment (positive/negative/neutral)
   - Note the most active and representative community sources

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all analyses
- Distinguish between quantitative data and qualitative observations
- Note sample sizes where available
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive user data set for [USERS] of [SOLUTIONS] in [DOMAIN] to [PURPOSE].

Provide systematic coverage of:

1. DEMOGRAPHIC DATA
   - Compile demographic profiles with source attribution
   - Create a demographic summary table

2. USAGE PATTERN DATA
   - Document usage patterns with frequency and satisfaction
   - Create a usage pattern table

3. REVIEW AND SENTIMENT AGGREGATION
   - Aggregate reviews from review platforms
   - Create a sentiment comparison table across solutions
   - Survey practitioner sentiment from community discussions

4. SATISFACTION SCORES
   - Compile satisfaction and NPS data where available
   - Create a satisfaction comparison table

5. COMMUNITY DISCUSSION THEMES
   - Catalog common themes from relevant communities
   - Create a theme frequency table

Prioritize 2025-2026 sources. Flag information age on all claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Create comparison tables for all analyses
- Note sample sizes where available
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Deep Recency Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a deep recency investigator researching recent behavioral shifts and emerging needs for [USERS] of [SOLUTIONS] in [DOMAIN].

Do NOT cover: persona synthesis, JTBD framework, or review aggregation (other models handle those). Focus on recent behavioral shifts, emerging pain points, and community sentiment evolution.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- reddit.com/r/[RELEVANT_SUBREDDITS]
- producthunt.com
- g2.com
- capterra.com
- [COMMUNITY_FORUMS]
- twitter.com (X)

RESEARCH DIMENSIONS:

1. RECENT BEHAVIORAL SHIFTS
   - How have [USERS]' behaviors or expectations changed in the last 6 months?
   - What to find: new workflow patterns, tool adoption shifts, changed expectations
   - What to verify: are shifts widespread or limited to early adopters?

2. EMERGING PAIN POINTS
   - What new pain points are [USERS] expressing that weren't prominent 6 months ago?
   - What to find: new complaint threads, feature requests trending upward, frustration patterns
   - Recent changes: pain points that have been resolved vs. growing worse

3. COMMUNITY SENTIMENT EVOLUTION
   - How is community sentiment toward [SOLUTIONS] evolving?
   - What to find: sentiment trend in discussions, recommendation pattern changes
   - What to verify: is sentiment shift driven by product changes or user expectation changes?

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on [USERS] of [SOLUTIONS] in [DOMAIN].

Cover:
1. Most notable shifts in user behavior or expectations in the last 6 months
2. Current sentiment momentum — improving or deteriorating?
3. Emerging needs or pain points not yet addressed by existing solutions
4. Where user expectations today differ from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed behavioral trends and anecdotal reports.
```

---

## 8. Economic Analysis

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting economic analysis of [TOPIC] in [DOMAIN] to [PURPOSE] over [TIMEFRAME].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources for pricing and cost data.

Focus your research and analysis on:

1. FINANCIAL MODELING FRAMEWORK
   - What is the appropriate financial model structure for evaluating [TOPIC]?
   - What are the cost categories (one-time, recurring, variable, hidden)?
   - What are the value drivers (revenue increase, cost reduction, risk mitigation, time savings)?
   - Search for: TCO analyses, ROI case studies, financial model templates for similar decisions
   - Analyze: which cost and value components are well-understood vs. uncertain

2. SENSITIVITY ANALYSIS
   - Which assumptions have the largest impact on financial outcome?
   - What is the breakeven point under different scenarios (base, optimistic, pessimistic)?
   - Search for: sensitivity analyses of similar investments, variable impact studies
   - Analyze: which variables, if wrong by 20%, flip the recommendation

3. HIDDEN COST IDENTIFICATION
   - What costs are consistently underestimated in [TOPIC] implementations?
   - What are the migration, training, integration, and opportunity costs?
   - Search for: "hidden costs of X" analyses, implementation retrospectives with cost breakdowns
   - Analyze: cost categories that are systematically underestimated and why

4. ROI SCENARIO CONSTRUCTION
   - What is the ROI under base, optimistic, and pessimistic scenarios?
   - What is the payback period for each scenario?
   - Search for: ROI case studies, industry benchmark returns, comparable company data
   - Analyze: confidence intervals for each scenario based on evidence quality

5. CROSS-DOMAIN FINANCIAL PATTERNS
   After completing primary analysis:
   - What financial outcomes from analogous investments in other domains inform this analysis?
   - Where have similar cost structures led to surprising financial outcomes?
   - What would need to be true for the consensus financial case to be wrong?

6. DECISION FRAMEWORK
   - Given the analysis, what is the recommended decision and under what conditions?
   - What monitoring triggers should cause re-evaluation?
   - What is the cost of delaying the decision?

Ground every claim in evidence. Present all estimates as ranges with confidence levels. Flag which estimates are well-sourced vs. modeled assumptions.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- False precision (point estimates where ranges are appropriate)
- Hidden costs not accounted for
- Sensitivity variables not tested
- Optimistic bias in value estimates
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher conducting economic analysis of [TOPIC] in [DOMAIN] to [PURPOSE] over [TIMEFRAME].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: pricing data compilation, industry benchmark gathering, or comparable company data aggregation (another model handles data collection). Focus on financial modeling, sensitivity analysis, hidden cost identification, and scenario construction.

Focus your research and analysis on:

1. FINANCIAL MODELING AND SENSITIVITY
   - What is the appropriate model structure for evaluating [TOPIC]?
   - Which assumptions most impact the financial outcome?
   - Search for: TCO analyses, ROI case studies, sensitivity analyses
   - Analyze: which variables flip the recommendation if wrong by 20%

2. HIDDEN COST IDENTIFICATION
   - What costs are consistently underestimated?
   - Search for: "hidden costs" analyses, implementation retrospectives
   - Analyze: systematically underestimated cost categories

3. ROI SCENARIO CONSTRUCTION
   - ROI under base, optimistic, and pessimistic scenarios with payback periods
   - Search for: industry benchmark returns, comparable implementations
   - Analyze: confidence intervals based on evidence quality

4. CROSS-DOMAIN SYNTHESIS
   - What financial patterns from analogous investments inform this analysis?
   - What would need to be true for the consensus financial case to be wrong?

Present all estimates as ranges with confidence levels.

SELF-REVIEW (mandatory before finalizing):
Review for false precision, missing hidden costs, untested sensitivities, and optimistic bias.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger collecting comprehensive financial data for the economic analysis of [TOPIC] in [DOMAIN] to [PURPOSE] over [TIMEFRAME].

Provide systematic coverage of:

1. PRICING DATA COMPILATION
   - Current pricing for [TOPIC] from all relevant vendors/sources
   - Include: pricing model, tiers, per-unit costs, volume discounts, enterprise pricing
   - Create a pricing comparison table with source URLs and dates
   - Note pricing model differences (seat, usage, flat, tiered)

2. BENCHMARK COSTS
   - Industry benchmark costs for similar implementations
   - Include: implementation costs, ongoing costs, scaling costs, labor costs
   - Create a cost benchmark table: cost category, range, median, source
   - Compile per-unit economics where available

3. INDUSTRY FINANCIAL METRICS
   - Relevant financial benchmarks for [DOMAIN]
   - Include: typical ROI ranges, payback periods, cost as % of revenue
   - Create a financial metrics table with industry comparables
   - Note where metrics vary by company size or segment

4. COMPARABLE COMPANY DATA
   - Financial data from companies that have implemented [TOPIC]
   - Include: implementation cost, timeline, reported outcomes, lessons learned
   - Create a comparable implementations table
   - Survey practitioner sentiment on financial outcomes from community discussions

5. TCO COMPONENT CATALOG
   - Comprehensive list of cost components for [TOPIC] TCO
   - For each component: typical range, frequency (one-time/recurring), variability
   - Create a TCO component table
   - Flag commonly overlooked cost categories

Prioritize 2025-2026 sources. Flag information age on all pricing claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Present ranges, not point estimates, for all financial figures
- Create comparison tables for all pricing and cost analyses
- Note where sources conflict on pricing or cost data
- Distinguish between current pricing and historical data
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger collecting financial data for the economic analysis of [TOPIC] in [DOMAIN] to [PURPOSE] over [TIMEFRAME].

Provide systematic coverage of:

1. PRICING DATA
   - Current pricing from all relevant vendors/sources
   - Create a pricing comparison table with source URLs and dates

2. BENCHMARK COSTS
   - Industry benchmark costs for similar implementations
   - Create a cost benchmark table: category, range, median, source

3. INDUSTRY FINANCIAL METRICS
   - Relevant financial benchmarks for [DOMAIN]
   - Create a financial metrics table with industry comparables

4. COMPARABLE IMPLEMENTATIONS
   - Financial data from similar implementations
   - Create a comparable implementations table

5. TCO COMPONENTS
   - Comprehensive cost component list
   - Flag commonly overlooked categories

Prioritize 2025-2026 sources. Flag information age on pricing claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs
- Present ranges, not point estimates
- Note where sources conflict
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent financial data and pricing changes for [TOPIC] in [DOMAIN].

Do NOT cover: financial modeling, sensitivity analysis, or TCO framework construction (other models handle those). Focus on recent pricing changes, cost trends, and updated benchmarks.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- [VENDOR_PRICING_PAGES]
- sec.gov (EDGAR)
- [CLOUD_PROVIDER_PRICING]
- [FINANCIAL_DATABASE_SITES]
- [COST_CALCULATOR_SITES]

RESEARCH DIMENSIONS:

1. RECENT PRICING CHANGES
   - What pricing changes have relevant vendors made in the last 6 months?
   - What to find: pricing page updates, billing model changes, promotional offers
   - What to verify: are published prices current and accurate?

2. COST TREND DATA
   - How are costs trending for key components of [TOPIC]?
   - What to find: historical pricing data, cost trajectory analyses
   - Recent changes: any cost spikes or reductions signaling market shifts

3. UPDATED FINANCIAL BENCHMARKS
   - What recent financial reports or analyses provide updated benchmark data?
   - What to find: recent case studies with financial outcomes, updated industry reports
   - What to verify: methodology and sample size of benchmark data

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on the economics of [TOPIC] in [DOMAIN].

Cover:
1. Most notable pricing changes across relevant vendors in the last 6 months
2. Current cost trajectory — are costs rising, falling, or stable?
3. Emerging cost factors not yet in standard TCO models
4. Where the financial picture today differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between confirmed pricing and estimated costs.
```

---

## 9. Compliance & Requirements

### Claude Opus 4.6 — Primary Researcher

<!-- DUAL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher analyzing compliance and regulatory requirements for [TOPIC] in [JURISDICTIONS] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources, especially for evolving regulatory environments.

Focus your research and analysis on:

1. REGULATORY INTERPRETATION
   - What regulations apply to [TOPIC] in [JURISDICTIONS], and what do they specifically require?
   - Where is the regulatory text clear vs. ambiguous? What is the range of defensible interpretations?
   - Search for: regulatory text, enforcement guidance, regulatory body FAQs, legal commentary
   - Analyze: which requirements are unambiguous vs. requiring legal judgment

2. CROSS-JURISDICTIONAL ANALYSIS
   - How do requirements differ across [JURISDICTIONS]?
   - Where are the conflicts or gaps between jurisdictional requirements?
   - Search for: jurisdiction comparison analyses, cross-border compliance guides, harmonization efforts
   - Analyze: which requirements can be satisfied by a single implementation vs. requiring jurisdiction-specific handling

3. GOVERNANCE FRAMEWORK DESIGN
   - What governance framework would satisfy the identified regulatory requirements?
   - What organizational structures, processes, and controls are needed?
   - Search for: governance framework examples, compliance program designs, industry standards (ISO, NIST)
   - Analyze: minimum viable governance vs. best-in-class governance

4. RISK-IMPACT REASONING
   - What are the consequences of non-compliance for each requirement?
   - Which requirements carry the highest risk (probability x impact)?
   - Search for: enforcement actions, penalty histories, compliance failure case studies
   - Analyze: risk-priority ranking to guide implementation sequencing

5. CONSTRAINT INTERACTION MAPPING
   - How do different regulatory requirements interact or conflict?
   - Where does satisfying one requirement make another harder?
   - Search for: compliance conflict analyses, multi-regulation implementation guides
   - Analyze: which constraints create binding interactions requiring careful design

6. PENDING REGULATORY CHANGES
   - What regulatory changes are pending or proposed that could affect compliance posture?
   - Search for: proposed legislation, regulatory body roadmaps, industry lobbying positions
   - Analyze: probability and timeline of pending changes

Ground every claim in evidence. Distinguish between established regulatory requirements, interpretive guidance, and your analytical reasoning. Flag confidence level on all regulatory interpretations. Items with low interpretation confidence should include "requires legal review" flags.

SELF-REVIEW (mandatory before finalizing):
After completing your analysis, review for:
- Regulatory interpretations stated as certainties when they are ambiguous
- Missing jurisdictional requirements
- Constraint interactions not identified
- Risk assessments without evidence from enforcement history
Revise before producing final output. Note significant revisions.
```

<!-- FULL -->

```
# API Configuration
# model: "claude-opus-4-6"
# thinking: {"type": "adaptive"}
# effort: "max"
# max_tokens: 16000

You are a primary researcher analyzing compliance and regulatory requirements for [TOPIC] in [JURISDICTIONS] to [PURPOSE].

Use your web search capability to ground all analysis in current, verified sources. Prioritize 2025-2026 sources.

Do NOT cover: regulatory text cataloging, compliance checklist creation, or audit requirement matrix compilation (another model handles structured data). Focus on regulatory interpretation, governance design, and constraint interaction analysis.

Focus your research and analysis on:

1. REGULATORY INTERPRETATION
   - Where is the regulatory text clear vs. ambiguous?
   - What is the range of defensible interpretations?
   - Search for: enforcement guidance, legal commentary
   - Analyze: ambiguous vs. clear requirements

2. CROSS-JURISDICTIONAL ANALYSIS AND GOVERNANCE
   - How do requirements differ across [JURISDICTIONS]?
   - What governance framework satisfies the requirements?
   - Search for: jurisdiction comparisons, governance framework examples
   - Analyze: single-implementation vs. jurisdiction-specific needs

3. CONSTRAINT INTERACTION MAPPING
   - How do different regulatory requirements interact or conflict?
   - Search for: compliance conflict analyses, multi-regulation guides
   - Analyze: binding constraint interactions

4. PENDING CHANGES AND RISK ASSESSMENT
   - What pending regulatory changes could affect compliance?
   - Which requirements carry the highest non-compliance risk?
   - What would need to be true for the current compliance approach to be insufficient?

Flag confidence on all regulatory interpretations. Low-confidence items require "requires legal review" flags.

SELF-REVIEW (mandatory before finalizing):
Review for false certainty on ambiguous regulations, missing jurisdictions, and unidentified constraint interactions.
Revise before producing final output. Note significant revisions.
```

### Gemini 3.1 Pro Deep Research — Structured Cataloger

<!-- DUAL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive compliance reference for [TOPIC] in [JURISDICTIONS] to [PURPOSE].

Provide systematic coverage of:

1. REGULATORY TEXT CATALOG
   - Catalog all regulations applicable to [TOPIC] in [JURISDICTIONS]
   - For each regulation, document:
     - Full name and citation
     - Effective date and amendment history
     - Key requirements (summarized)
     - Penalties for non-compliance
     - Enforcement body
   - Create a regulatory requirements table

2. COMPLIANCE CHECKLIST
   - Create a comprehensive compliance checklist organized by regulation
   - For each checklist item:
     - Requirement ID
     - Requirement description
     - Evidence needed
     - Implementation complexity (low/medium/high)
     - Deadline (if applicable)
   - Organize by priority tier (mandatory, recommended, best practice)

3. AUDIT REQUIREMENT MATRICES
   - Document audit requirements for each applicable regulation
   - Include: audit frequency, scope, required documentation, certifications needed
   - Create an audit requirements matrix
   - Note differences by company size or processing volume

4. DEADLINE TRACKING
   - Compile all compliance deadlines and transition periods
   - Include: regulation, requirement, deadline, grace period, penalty for late compliance
   - Create a timeline table of upcoming compliance deadlines
   - Flag urgency level for each deadline

5. JURISDICTION COMPARISON TABLES
   - Create comparison tables showing requirement differences across [JURISDICTIONS]
   - Include: requirement area, jurisdiction A rules, jurisdiction B rules, conflict/gap analysis
   - Survey practitioner sentiment on compliance burden from community discussions

Prioritize 2025-2026 sources. Flag information age on all regulatory claims.

OUTPUT REQUIREMENTS:
- Include sources for all claims with URLs to regulatory text where possible
- Create structured checklists and matrices
- Note where regulatory text is ambiguous (flag for legal review)
- Distinguish between enacted law, regulatory guidance, and industry practice
- Organize with clear section headers for navigability
```

<!-- FULL -->

```
# Gemini Configuration
# agent: "deep-research-pro-preview-12-2025"
# thinking: "High"
# background: true

You are a structured cataloger building a comprehensive compliance reference for [TOPIC] in [JURISDICTIONS] to [PURPOSE].

Provide systematic coverage of:

1. REGULATORY TEXT CATALOG
   - Catalog all applicable regulations with: name, citation, effective date, key requirements, penalties, enforcement body
   - Create a regulatory requirements table

2. COMPLIANCE CHECKLIST
   - Create a comprehensive checklist organized by regulation and priority tier
   - Include: requirement ID, description, evidence needed, complexity, deadline

3. AUDIT REQUIREMENT MATRICES
   - Document audit requirements per regulation
   - Create an audit requirements matrix

4. DEADLINE TRACKING
   - Compile all compliance deadlines and transition periods
   - Create a timeline table with urgency flags

5. JURISDICTION COMPARISON
   - Create comparison tables across [JURISDICTIONS]
   - Survey practitioner sentiment on compliance burden

Prioritize 2025-2026 sources. Flag information age on all regulatory claims.

OUTPUT REQUIREMENTS:
- Include sources with URLs to regulatory text
- Create structured checklists and matrices
- Flag ambiguous regulatory text for legal review
- Organize with clear section headers for navigability
```

### GPT-5.2 Deep Research — Targeted Investigator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Configuration
# thinking_effort: "extended"

You are a targeted investigator researching recent regulatory developments for [TOPIC] in [JURISDICTIONS].

Do NOT cover: regulatory interpretation, governance framework design, or comprehensive compliance catalogs (other models handle those). Focus on recent regulatory changes, enforcement actions, and policy updates.

SITE RESTRICTIONS:
Limit your research to the following authoritative sources:
- [REGULATORY_BODY_SITES] (.gov domains)
- iso.org
- nist.gov
- [COMPLIANCE_PORTALS]
- [INDUSTRY_REGULATOR_SITES]
- [LEGAL_DATABASE_SITES]

RESEARCH DIMENSIONS:

1. RECENT REGULATORY CHANGES (last 6 months)
   - What new regulations, amendments, or guidance documents have been issued?
   - What to find: new regulatory text, guidance updates, FAQ additions
   - What to verify: effective dates and transition period details

2. ENFORCEMENT ACTIONS
   - What enforcement actions related to [TOPIC] have occurred recently?
   - What to find: enforcement announcements, penalty details, settlement terms
   - What these signal: enforcement priorities, compliance bar in practice

3. POLICY UPDATES AND PENDING LEGISLATION
   - What policy proposals or legislative bills could affect [TOPIC] compliance?
   - What to find: proposed rules, comment periods, legislative drafts
   - What to verify: probability of passage and expected timelines

4. STANDARDS BODY UPDATES
   - Have relevant standards (ISO, NIST, industry-specific) been updated?
   - What to find: new standard versions, draft standards, transition guidance
   - What to verify: mandatory vs. voluntary adoption requirements

For each finding:
- Note the specific source domain and page
- Flag the date of the information
- Note confidence level based on source authority

Prioritize precision over breadth.
```

### GPT-5.2 Chat — Recency Validator (FULL only)

<!-- FULL -->

```
# GPT-5.2 Chat Configuration
# mode: instant

Provide a recency validation check on compliance for [TOPIC] in [JURISDICTIONS].

Cover:
1. Most notable regulatory changes or enforcement actions in the last 6 months
2. Current regulatory momentum — increasing or stable enforcement?
3. Emerging compliance requirements not yet widely adopted
4. Where the compliance landscape today differs from 12 months ago

Keep focused and efficient. Flag information age on all claims.
Include sources. Distinguish between enacted regulations and proposals.
```

---

## Appendix A: File Search Preamble (Gemini Only)

Add this preamble to any Gemini template when file_search is recommended per model-profiles.md Section 7.

```
CONTEXT DOCUMENTS:
The following documents have been uploaded as research context. Use them
to ground your analysis in the specific situation being researched.
Cross-reference findings from web sources against these internal documents.
Flag where web-sourced best practices conflict with current implementation.

Uploaded: [DOCUMENT_LIST]
```

**When to include** (by pattern):

| Pattern | Include When | What to Upload |
|---|---|---|
| Best Practices | User has existing codebase or config | Code samples, config files, requirements.txt |
| Comparative Evaluation | User has vendor proposals or RFPs | RFP responses, vendor proposals, existing ADRs |
| Competitive Intelligence | User has competitor teardowns | Feature screenshots, teardown notes, battle cards |
| Implementation Pattern | User has current architecture | Architecture diagrams, ADRs, config files |
| Compliance & Requirements | User has regulatory docs | Requirements docs, policy documents, matrices |
| Economic Analysis | User has financial models | Cost models, vendor quotes, projections |
| Landscape Mapping | User has partial research | Prior outputs, internal assessments |
| User Research | User has qualitative data | Interview transcripts, survey results, tickets |
| Market Research | User has internal data | Internal assessments, segment definitions |

---

## Appendix B: Mid-Session Intervention Protocol (GPT-5.2 Deep Research)

Include in FULL-mode research briefs that use GPT-5.2 Deep Research.

```
MONITORING CHECKLIST (while GPT-5.2 Deep Research runs):
[ ] Drift: Research exploring tangential topics
    -> Intervene: "Refocus on [SPECIFIC DIMENSION]"
[ ] Source quality: Results from low-authority sources
    -> Intervene: "Prioritize [SPECIFIC SITES]"
[ ] Coverage gap: Missing a key dimension
    -> Intervene: "Also investigate [MISSING AREA]"
[ ] Redundancy: Repeating findings already covered
    -> Intervene: "Skip [COVERED AREA], focus on [UNCOVERED]"
[ ] Stale data: Using pre-2025 sources on fast-changing topics
    -> Intervene: "Focus on 2025-2026 sources only"
```

---

## Appendix C: Template Selection Quick Reference

| Pattern | Claude DUAL | Claude FULL | Gemini DUAL | Gemini FULL | GPT-5.2 Deep | GPT-5.2 Chat |
|---|---|---|---|---|---|---|
| Landscape Mapping | Sec 1, DUAL | Sec 1, FULL | Sec 1, DUAL | Sec 1, FULL | Sec 1, FULL | Sec 1, FULL |
| Comparative Evaluation | Sec 2, DUAL | Sec 2, FULL | Sec 2, DUAL | Sec 2, FULL | Sec 2, FULL | Sec 2, FULL |
| Implementation Pattern | Sec 3, DUAL | Sec 3, FULL | Sec 3, DUAL | Sec 3, FULL | Sec 3, FULL | Sec 3, FULL |
| Best Practices | Sec 4, DUAL | Sec 4, FULL | Sec 4, DUAL | Sec 4, FULL | Sec 4, FULL | Sec 4, FULL |
| Competitive Intelligence | Sec 5, DUAL | Sec 5, FULL | Sec 5, DUAL | Sec 5, FULL | Sec 5, FULL | Sec 5, FULL |
| Market Research | Sec 6, DUAL | Sec 6, FULL | Sec 6, DUAL | Sec 6, FULL | Sec 6, FULL | Sec 6, FULL |
| User Research | Sec 7, DUAL | Sec 7, FULL | Sec 7, DUAL | Sec 7, FULL | Sec 7, FULL | Sec 7, FULL |
| Economic Analysis | Sec 8, DUAL | Sec 8, FULL | Sec 8, DUAL | Sec 8, FULL | Sec 8, FULL | Sec 8, FULL |
| Compliance & Requirements | Sec 9, DUAL | Sec 9, FULL | Sec 9, DUAL | Sec 9, FULL | Sec 9, FULL | Sec 9, FULL |

**Total templates**: 9 patterns x 6 variants = 54 templates (18 Claude + 18 Gemini + 9 GPT-5.2 Deep + 9 GPT-5.2 Chat)
