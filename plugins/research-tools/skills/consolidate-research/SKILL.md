---
name: consolidate-research
description: >
  Synthesize multi-model research outputs into unified findings with conflict resolution.
  PROACTIVELY activate for: (1) combining research from multiple sources, (2) reconciling
  conflicting findings, (3) research synthesis, (4) evidence aggregation.
  Triggers: "consolidate research", "synthesize findings", "merge research", "combine outputs",
  "reconcile research", "aggregate evidence"
argument-hint: [research outputs or file paths]
disable-model-invocation: true
---

# Consolidate Research

Synthesize multi-source research findings into a unified, evidence-graded report.

## When to Use

Use this skill when you need to:
- Combine research outputs from multiple AI models (Claude, Gemini, GPT)
- Reconcile conflicting findings from different sources
- Create a unified research synthesis with evidence scoring
- Identify gaps and areas of consensus across sources

## Prerequisites

Before using this skill, you should have:
- Research outputs from executing a `/research-brief` across multiple models
- Or multiple research documents/sources to synthesize
- Or findings from different stakeholder interviews

## Workflow

Invoke the `create-research-brief` skill Phase 2 for consolidation.

### Input

$ARGUMENTS

### Consolidation Framework

#### Step 1: Source Inventory
Catalog all input sources with metadata:
- Source type (Claude, Gemini, GPT, human, document)
- Date/recency of information
- Credibility assessment
- Coverage of original MECE categories

#### Step 2: Evidence Scoring
Apply 5-point evidence strength scale:

| Score | Label | Criteria |
|-------|-------|----------|
| 5 | Strong | Multiple independent sources, verified data |
| 4 | Moderate | 2+ sources agree, credible methodology |
| 3 | Mixed | Sources disagree or incomplete evidence |
| 2 | Weak | Single source, unverified claims |
| 1 | Speculative | Inference or hypothesis only |

#### Step 3: Conflict Resolution (WWHTBT Protocol)

When sources disagree:
1. **What** - Identify exact nature of conflict
2. **Why** - Understand root cause of disagreement
3. **How** - Determine resolution approach
4. **Then** - Document resolution and rationale
5. **But** - Note caveats and remaining uncertainty
6. **Therefore** - State final consolidated finding

#### Step 4: Uncertainty Classification

Tag all findings with uncertainty type:
- **Aleatory** - Inherent randomness (can't reduce with more data)
- **Epistemic** - Knowledge gaps (can reduce with more research)
- **Model** - Model limitations or biases
- **Temporal** - Time-sensitive, may change

#### Step 5: MECE Coverage Audit

Verify consolidation covers all original categories:
- [ ] All MECE categories addressed
- [ ] No significant gaps remain
- [ ] Overlaps identified and reconciled

## Output Format

The consolidated research produces:

```xml
<consolidated-report>
  <header>
    <id>[unique identifier]</id>
    <sources>
      <source type="[model|document|human]" name="[source name]">
        [Source metadata]
      </source>
    </sources>
    <consolidation_date>[timestamp]</consolidation_date>
  </header>

  <executive-summary>
    [2-3 paragraph synthesis of key findings]
  </executive-summary>

  <findings-by-category>
    <category name="[MECE Category 1]">
      <finding evidence_score="[1-5]" uncertainty="[type]">
        <claim>[Consolidated finding]</claim>
        <sources>[Which sources support this]</sources>
        <conflicts>[Any disagreements and resolution]</conflicts>
      </finding>
    </category>
    <!-- ... more categories ... -->
  </findings-by-category>

  <conflicts-resolved>
    <conflict>
      <description>[Nature of conflict]</description>
      <resolution>[How it was resolved]</resolution>
      <confidence>[Confidence in resolution]</confidence>
    </conflict>
  </conflicts-resolved>

  <gaps-remaining>
    <gap priority="[high|medium|low]" type="[epistemic|data|scope]">
      [Information still needed]
    </gap>
  </gaps-remaining>

  <recommendations>
    <recommendation priority="[1-n]">
      [Actionable recommendation based on findings]
    </recommendation>
  </recommendations>

  <next-steps>
    1. [Recommended follow-up]
    2. [Additional research if needed]
  </next-steps>
</consolidated-report>
```

## Quality Gates

- [ ] All input sources properly inventoried
- [ ] Evidence scores assigned to all findings
- [ ] Conflicts explicitly identified and resolved
- [ ] Uncertainty types classified
- [ ] MECE coverage verified
- [ ] Recommendations are actionable and specific
- [ ] Executive summary captures key insights

## Workflow Integration

This skill is the final step in the research pipeline:

```
/research-interview → /research-brief → /consolidate-research
     (elicit)            (design)           (synthesize)
```

After consolidation, consider:
- Run `/compare-options` to evaluate recommendations
- Run `/run-expert-panel` for strategic decision validation
- Create documentation with `/write-reference` or `/write-howto`
