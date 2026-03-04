# Best Practices: 8-Dimension Framework & Prompt Fragments

Load this reference when research type is **Best Practices**. Contains the dimension definitions, per-dimension prompt fragments for Claude and Gemini, and assembly instructions.

## The 8 Dimensions

| # | Dimension | Research Focus |
|---|-----------|---------------|
| 1 | **Environmental Context** | Runtime versions, deployment targets, project structure, IAM/auth, secrets management |
| 2 | **Idiomatic Patterns** | How experienced practitioners write it vs. how it merely works; performance optimization |
| 3 | **Anti-Patterns & Guardrails** | What fails at scale, common mistakes with root cause explanations |
| 4 | **Testing & Validation** | Emulator/mock patterns, integration test approaches, pre-deploy validation |
| 5 | **Dependencies & Versions** | Recommended packages, packages to avoid, compatibility matrices, pinning strategy |
| 6 | **Operational Awareness** | Logging conventions, cost model implications, scaling behavior, cold start mitigation |
| 7 | **Decision Trees** | When to use which variant/approach; architectural boundary decisions |
| 8 | **Escape Hatches** | Known bugs contradicting docs, workarounds with expiration context, when to eject |

Not all dimensions apply equally to every technology. Weight by technology family using [references/technology-profiles.md](technology-profiles.md).

---

## Dimension Prompt Fragments

When generating research prompts, select relevant dimensions, weight by technology family, and assemble into unified Claude and Gemini prompts. Include the Claude fragment in the Claude prompt and the Gemini fragment in the Gemini prompt.

Adapt placeholders `[TECHNOLOGY]`, `[VERSION]`, `[RUNTIME]` to the specific topic.

---

### Dimension 1: Environmental Context & Setup

#### Claude Prompt Fragment
```
ENVIRONMENTAL CONTEXT for [TECHNOLOGY]:
Research the current recommended environment setup, including:
- Supported runtime versions and which version to target for new projects
- Recommended project directory structure and file organization conventions
- Configuration best practices (what to set, what to leave as defaults, what to override)
- IAM and authentication patterns specific to this platform
- Secrets and environment variable management approaches
- Any setup steps that documentation glosses over but practitioners consider essential

Focus on the GAP between "getting started" tutorials and production-ready setup.
Identify setup decisions that have downstream consequences developers don't anticipate.
```

#### Gemini Prompt Fragment
```
ENVIRONMENTAL CONTEXT for [TECHNOLOGY]:
Document the current state of environment setup:
- Official runtime version support matrix with EOL dates
- Project scaffolding tools and their current status (maintained, deprecated, recommended)
- Configuration reference: all configurable parameters with defaults and recommended values
- Authentication/authorization setup steps from official documentation
- Known setup issues from GitHub issues, Stack Overflow (last 12 months)
- Migration guides between versions if version transition is current

Create a comparison table of setup approaches if multiple exist.
Include links to authoritative sources.
```

---

### Dimension 2: Idiomatic Patterns

#### Claude Prompt Fragment
```
IDIOMATIC PATTERNS for [TECHNOLOGY]:
Research how experienced practitioners write [TECHNOLOGY] code vs. how beginners approach it:
- What patterns distinguish production-quality code from "it works" code?
- What performance optimization patterns are considered standard practice?
- What initialization, connection pooling, or resource management patterns are idiomatic?
- What code organization patterns emerge in mature codebases?
- Are there patterns that the official docs recommend but the community has moved beyond?

For each pattern:
- Explain WHY it's done this way (the underlying mechanism, not just convention)
- Quantify the impact where possible (cold start reduction, latency improvement, cost savings)
- Note if the pattern is specific to a version or generation

Identify cross-domain patterns: are there idioms borrowed from other technology domains
that are particularly effective here?
```

#### Gemini Prompt Fragment
```
IDIOMATIC PATTERNS for [TECHNOLOGY]:
Document established coding patterns from:
- Official best practices documentation and style guides
- Popular open-source projects using [TECHNOLOGY] (identify 3-5 well-regarded examples)
- Conference talks and blog posts from core team members (last 18 months)
- Benchmark comparisons between pattern approaches (with data)

For each pattern, provide:
- Code example (minimal, illustrative)
- Source/attribution
- Version applicability

Create a pattern catalog table: Pattern Name | Use Case | Complexity | Performance Impact.
```

---

### Dimension 3: Anti-Patterns & Guardrails

#### Claude Prompt Fragment
```
ANTI-PATTERNS AND GUARDRAILS for [TECHNOLOGY]:
Research what goes wrong and why:
- What are the most common mistakes developers make with [TECHNOLOGY]?
- For each anti-pattern: what is the ROOT CAUSE of failure? At what scale does it break?
  (Not just "don't do X" — explain the mechanism: "X causes Y because Z, which manifests
  when traffic exceeds N requests/second or data exceeds M records")
- What anti-patterns are TAUGHT by outdated tutorials but are now known to be harmful?
- What patterns work in development/testing but fail in production?
- Are there anti-patterns specific to migrating from [TECHNOLOGY] v1 to v2 (or equivalent)?

Categorize by severity:
- CRITICAL: Will cause outages, data loss, or security vulnerabilities
- MAJOR: Will cause performance degradation, cost overruns, or maintenance burden
- MINOR: Will cause code quality issues or developer friction

For each, provide the detection signal (how to spot it in existing code).
```

#### Gemini Prompt Fragment
```
ANTI-PATTERNS AND GUARDRAILS for [TECHNOLOGY]:
Catalog known anti-patterns from:
- Official "common mistakes" or "troubleshooting" documentation
- GitHub issues tagged as "bug" or "won't fix" that stem from misuse
- Stack Overflow questions with 50+ votes related to [TECHNOLOGY] problems
- Post-mortem blog posts mentioning [TECHNOLOGY] failures
- Linting rules and static analysis checks specific to [TECHNOLOGY]

For each anti-pattern, document:
- The mistake (with code example if applicable)
- The recommended alternative (with code example)
- Source/attribution
- How recently this was validated

Create a table: Anti-Pattern | Severity | Detection Method | Fix.
```

---

### Dimension 4: Testing & Validation

#### Claude Prompt Fragment
```
TESTING AND VALIDATION for [TECHNOLOGY]:
Research the current testing landscape:
- What is the recommended unit testing approach? What mocking/stubbing patterns work well?
- What emulator, simulator, or local development tools exist? How faithful are they?
- What integration testing patterns are practical? What requires a live environment?
- What pre-deployment validation checks should be automated?
- What are the GAPS in testability? What can't be tested locally and how do teams handle it?
- Are there testing patterns that look correct but give false confidence?

Assess the maturity of the testing ecosystem:
- Is the testing story well-supported or a known pain point?
- What recent improvements have been made to testing tooling?
- What testing capabilities are on the roadmap?
```

#### Gemini Prompt Fragment
```
TESTING AND VALIDATION for [TECHNOLOGY]:
Document the testing ecosystem:
- Official testing documentation and recommended frameworks
- Emulator/simulator setup guides and known limitations
- Community testing libraries and their maintenance status
- CI/CD integration patterns for [TECHNOLOGY] testing
- Test coverage tools and their compatibility

Create a testing matrix:
Test Type | Tool/Approach | Fidelity | Setup Complexity | CI-Friendly?

Include links to example test suites in well-maintained open-source projects.
```

---

### Dimension 5: Dependencies & Version Management

#### Claude Prompt Fragment
```
DEPENDENCIES AND VERSION MANAGEMENT for [TECHNOLOGY]:
Research the dependency landscape:
- What are the essential packages/libraries? Which versions are currently compatible?
- Are there packages that are commonly used but should be avoided? Why?
- What is the recommended approach to version pinning?
- What version compatibility constraints exist between the core SDK and common dependencies?
- Are there known dependency conflicts that waste developer time?
- What does the upgrade path look like for major version transitions?

Identify FRAGILITY points: where do version mismatches cause silent failures
(vs. loud errors)?
```

#### Gemini Prompt Fragment
```
DEPENDENCIES AND VERSION MANAGEMENT for [TECHNOLOGY]:
Create a dependency reference:
- Core SDK packages with current versions and compatibility notes
- Popular community packages with npm/PyPI download counts, last update date, maintenance status
- Known incompatibilities (specific version pairs that conflict)
- Changelog highlights for the last 2-3 releases of core packages

Create a compatibility matrix:
Core SDK Version | Runtime Version | Key Dependencies | Status (Current/Maintenance/EOL)

Document any automated dependency management tools specific to this ecosystem.
```

---

### Dimension 6: Operational Awareness

#### Claude Prompt Fragment
```
OPERATIONAL AWARENESS for [TECHNOLOGY]:
Research what developers need to know for production operations:
- What logging format and conventions does the platform expect? How should structured logging be configured?
- What are the key cost drivers? What design choices have surprising cost implications?
- How does the service scale? What are the concurrency limits, timeout ceilings, memory tiers?
- What cold start characteristics exist? What mitigation strategies are proven effective?
- What monitoring and alerting should be set up? What are the early warning signals for problems?
- What operational surprises do teams encounter in the first 3 months of production use?

Quantify where possible: "Function X with Y MB memory takes Z ms cold start."
Identify the operational knowledge that ONLY comes from running in production.
```

#### Gemini Prompt Fragment
```
OPERATIONAL AWARENESS for [TECHNOLOGY]:
Document operational parameters:
- Official quotas, limits, and pricing documentation (current)
- Monitoring and observability integration guides
- Performance benchmark data from official or reputable third-party sources
- Incident response patterns specific to [TECHNOLOGY] (official runbooks if available)
- Cost calculators and estimation tools

Create tables for:
- Resource Limits: Limit | Default | Maximum | How to Increase
- Pricing Model: Dimension | Unit | Price | Cost Optimization Tip
- Scaling Behavior: Metric | Behavior | Limit | Mitigation
```

---

### Dimension 7: Decision Trees

#### Claude Prompt Fragment
```
DECISION TREES for [TECHNOLOGY]:
Research the key architectural decisions developers face:
- When should a developer choose approach A vs. approach B within [TECHNOLOGY]?
  (e.g., different function types, different deployment modes, different data access patterns)
- When should a developer use [TECHNOLOGY] vs. handle something at a different layer?
  (e.g., business logic in functions vs. in security rules, in the client, in a different service)
- What are the generation/version selection criteria for new projects?
- What are the migration decision points (when to migrate vs. stay)?

For each decision:
- Frame as a clear conditional: "IF [condition] THEN [approach] BECAUSE [reason]"
- Identify the decision criteria that matter most (latency, cost, complexity, team skill)
- Note where the "correct" answer has changed recently and why

These decision trees should encode ARCHITECTURAL JUDGMENT that documentation doesn't cover well.
```

#### Gemini Prompt Fragment
```
DECISION TREES for [TECHNOLOGY]:
Document decision guidance from:
- Official "choosing between X and Y" documentation
- Architecture decision records (ADRs) from notable projects
- Comparison blog posts from recognized practitioners (last 18 months)
- Migration guides that explain when to migrate and when not to

For each decision point, create a comparison table:
Approach | Use When | Advantages | Disadvantages | Typical Scale
```

---

### Dimension 8: Escape Hatches & Known Issues

#### Claude Prompt Fragment
```
ESCAPE HATCHES AND KNOWN ISSUES for [TECHNOLOGY]:
Research what breaks and how to work around it:
- What platform bugs or behaviors CONTRADICT the official documentation?
- What workarounds exist for known limitations? Do they have expiration dates?
  (e.g., "needed until SDK version X" or "permanent platform limitation")
- When should a developer EJECT from the standard [TECHNOLOGY] pattern entirely?
  What are the signals that the technology isn't the right fit?
- What undocumented behaviors do experienced practitioners know about?
- What recent changes or deprecations have caught developers off guard?

For each issue:
- Classify: Bug | Documented Limitation | Undocumented Behavior | Deprecation
- Provide the workaround with code if applicable
- Note when this was last confirmed active
- Link to tracking issue or discussion if available

This section has the HIGHEST staleness risk. Be explicit about recency of sources.
```

#### Gemini Prompt Fragment
```
ESCAPE HATCHES AND KNOWN ISSUES for [TECHNOLOGY]:
Catalog known issues from:
- GitHub Issues (open, labeled as bug, sorted by reactions/comments)
- GitHub Discussions (many projects have migrated community support to Discussions; search for workarounds and known issues there alongside Issues)
- Official known issues or limitations documentation
- Stack Overflow questions about workarounds (high-vote, recent)
- Release notes mentioning breaking changes (last 3 releases)
- Deprecation notices currently in effect

For each issue, document:
- Issue description and reproduction conditions
- Current status (open/acknowledged/wontfix/planned-fix)
- Workaround if available
- GitHub issue link or tracking reference
- Date last confirmed

Create a table: Issue | Severity | Status | Workaround Available? | Tracking Link
```

---

## Prompt Assembly Instructions

When generating the full Best Practices research prompts:

1. **Identify the technology family** using [references/technology-profiles.md](technology-profiles.md). Get dimension weights.

2. **Select dimensions**: Include all 8, but allocate more prompt space to High-weight dimensions. De-emphasize Low-weight dimensions (1-2 sentences instead of full fragment).

3. **Claude Opus 4.6 prompt**: Combine relevant Claude dimension fragments under a unified research framing. Add:
   - Cross-domain synthesis directive
   - Self-review instruction
   - Web search activation for current sources
   - Effort set to `max`
   - No "Do NOT cover" exclusions in DUAL mode

4. **Gemini 3.1 Pro Deep Research prompt**: Combine relevant Gemini dimension fragments. Add:
   - Set thinking to **High** for Best Practices research
   - Emphasis on structured output (tables, matrices, catalogs)
   - Citation requirements for all claims
   - "Prioritize 2024-2026 sources"
   - Practitioner sentiment from community discussions
   - No "Do NOT cover" exclusions in DUAL mode
   - If the technology family has **High** Gemini File Search Value (see technology-profiles.md), recommend the user upload relevant project files (configs, schemas, orchestration definitions) before executing the Gemini prompt

5. **Adapt to topic**: Technology-specific terminology, relevant version numbers, and any user-provided context about their specific use case.

6. **Technology family emphasis examples**:
   - Serverless functions → Heavy on dimensions 2, 3, 6, 7
   - Database clients → Heavy on dimensions 2, 3, 5, 8
   - Frontend frameworks → Heavy on dimensions 1, 2, 4, 7
   - Infrastructure-as-code → Heavy on dimensions 1, 3, 7, 8
   - AI/ML SDKs → Heavy on dimensions 2, 3, 5, 7, 8

### Downstream Optimization for Claude Code Skills

When the downstream use is **Claude Code skill creation**, additionally:
- Frame anti-patterns as reasoning-based ("X causes Y at Z scale") not rule-based ("don't do X")
- Include code snippets for idiomatic patterns (copy-ready)
- Structure decision trees as conditional logic Claude Code can follow
- Keep version stamps prominent so the skill knows its own freshness
- Include the Quick Reference Card as a potential skill preamble

### Downstream Optimization for Agentient Academy Content

When the downstream use is **Agentient Academy content**, additionally:
- Frame patterns pedagogically (explain the "why" before the "how")
- Include difficulty ratings per pattern (beginner / intermediate / advanced)
- Add "common misconception" callouts that preemptively address what learners typically get wrong
- Structure content for progressive disclosure: overview first, then depth on demand
