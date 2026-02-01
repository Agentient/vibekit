# Problem Statement Output Template

CONTRACT-01 compliant template for structured problem definition artifacts.

---

## Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<problem_statement contract="CONTRACT-01" version="1.0">

  <metadata>
    <artifact_id>PS-[YYYY-MM-DD]-[5-char-hash]</artifact_id>
    <contract_type>PROBLEM-STATEMENT</contract_type>
    <created_at>[ISO 8601 timestamp]</created_at>
    <created_by>research-interviewer</created_by>
    <confidence>[0.0-1.0]</confidence>
    <provenance>
      <source>interview</source>
      <interview_goal>[Goal from Phase 1]</interview_goal>
      <interviewee_role>[Role/title of primary interviewee]</interviewee_role>
      <interview_date>[ISO 8601 date]</interview_date>
      <interview_turns>[Total conversation turns]</interview_turns>
      <questions_asked>[N]</questions_asked>
      <dimensions_covered>[N]</dimensions_covered>
      <validation_mode>[empathetic|balanced|rigorous]</validation_mode>
    </provenance>
  </metadata>

  <statement>[Clear, actionable problem statement - 1-2 sentences]</statement>

  <solution_contamination>
    <detected>[true|false]</detected>
    <flagged_phrases>
      <phrase original="[solution-oriented phrase]" issue="[why problematic]"/>
      <!-- Additional flagged phrases if detected -->
    </flagged_phrases>
    <cleaned_statement>[Problem-only version if contamination detected]</cleaned_statement>
  </solution_contamination>

  <jtbd_format>
    <situation>[When/context - specific trigger or circumstance]</situation>
    <motivation>[What the user wants to do - the job]</motivation>
    <outcome>[Desired result/benefit - expected value]</outcome>
  </jtbd_format>

  <context>
    <domain>[product|architecture|research|requirements|custom|none]</domain>
    <stakeholders>
      <stakeholder role="[role]" impact="[high|medium|low]">[Name/description]</stakeholder>
      <!-- Add more stakeholders as identified -->
    </stakeholders>
    <constraints>
      <constraint type="[technical|business|regulatory|temporal]" negotiable="[true|false]">
        [Constraint description]
      </constraint>
      <!-- Add more constraints -->
    </constraints>
    <assumptions>
      <assumption id="A1" type="[explicit|implicit|structural]"
                  validated="[true|false]" confidence="[0.0-1.0]">
        <statement>[Assumption text]</statement>
        <implications>[What depends on this being true]</implications>
      </assumption>
      <!-- Add more assumptions -->
    </assumptions>
  </context>

  <knowledge_map>
    <known>
      <ref finding_id="[ID]">[Direct statements from interview]</ref>
      <!-- Additional known facts -->
    </known>
    <believed>
      <ref finding_id="[ID]">[Strong inferences from multiple statements]</ref>
      <!-- Additional believed items -->
    </believed>
    <assumed>
      <ref finding_id="[ID]">[Interviewer interpretations]</ref>
      <!-- Additional assumed items -->
    </assumed>
    <unknown>
      <gap dimension="[MECE dimension]">[What we don't know]</gap>
      <!-- Additional unknown gaps -->
    </unknown>
  </knowledge_map>

  <epistemic_registry>
    <claim id="C1" label="[FACT|LIKELY|PLAUSIBLE|ASSUMPTION|UNCERTAIN]"
           confidence="[0.0-1.0]">
      <statement>[Claim text]</statement>
      <evidence_basis>[Source of evidence]</evidence_basis>
    </claim>
    <!-- Additional claims -->
  </epistemic_registry>

  <success_criteria>
    <criterion id="SC1" measurable="[true|false]"
               priority="[must_have|should_have|nice_to_have]">
      <description>[What success looks like]</description>
      <metric>[How to measure - quantitative if possible]</metric>
      <target>[Target value or threshold]</target>
    </criterion>
    <!-- Add more criteria -->
  </success_criteria>

  <epistemic_status>
    <overall_confidence>[0.0-1.0]</overall_confidence>
    <uncertainty_breakdown>
      <epistemic_gaps>
        <gap severity="[critical|significant|minor]">
          <description>[Knowledge gap description]</description>
          <resolution_approach>[How to close this gap]</resolution_approach>
        </gap>
      </epistemic_gaps>
      <aleatory_factors>
        <factor>[Inherent uncertainty that cannot be reduced]</factor>
      </aleatory_factors>
      <model_dependencies>
        <dependency>[Framework or model assumption]</dependency>
      </model_dependencies>
    </uncertainty_breakdown>
  </epistemic_status>

  <downstream_guidance>
    <recommended_next_skill>[create-research-brief|requirements|architecture]</recommended_next_skill>
    <research_questions>
      <question priority="[high|medium|low]">[Question to investigate]</question>
      <!-- Additional research questions -->
    </research_questions>
    <validation_needed>
      <item ref="[assumption_id or claim_id]">[What needs validation]</item>
      <!-- Additional validation items -->
    </validation_needed>
  </downstream_guidance>

</problem_statement>
```

---

## Field Guidance

### metadata
| Field | Description | Example |
|-------|-------------|---------|
| `artifact_id` | Unique identifier | PS-2025-01-15-a3f2b |
| `confidence` | Overall artifact confidence | 0.82 |
| `interviewee_role` | Primary interviewee's role | Product Manager |
| `interview_date` | Date of interview | 2025-01-15 |
| `interview_turns` | Total conversation turns | 42 |
| `questions_asked` | Total questions in interview | 24 |
| `dimensions_covered` | MECE dimensions addressed | 5 |

### statement
- Single sentence preferred, max 2
- Must be actionable (implies what to do)
- Avoid jargon unless domain-specific

### jtbd_format
Job-To-Be-Done structure:
- **situation**: "When I am [context/trigger]..."
- **motivation**: "I want to [action/capability]..."
- **outcome**: "So that [benefit/result]..."

### constraints
| Type | Examples |
|------|----------|
| technical | "Must integrate with legacy API" |
| business | "Budget capped at $50K" |
| regulatory | "GDPR compliance required" |
| temporal | "Must launch before Q3" |

### solution_contamination
Detects when problem statement includes solution language:
- **detected**: Set `true` if solution-oriented phrases found
- **flagged_phrases**: Each phrase that embeds a solution (e.g., "need an API", "requires a dashboard")
- **cleaned_statement**: Problem-only version with solutions removed

### knowledge_map
Categorizes findings by epistemic certainty (see epistemic-labeling-guide.md):
| Category | Content | Confidence Range |
|----------|---------|------------------|
| `known` | Direct statements from interview | FACT (95-100%) |
| `believed` | Strong inferences from multiple statements | LIKELY (80-94%) |
| `assumed` | Interviewer interpretations | PLAUSIBLE/ASSUMPTION (40-79%) |
| `unknown` | MECE gaps requiring investigation | UNCERTAIN (0-39%) |

### epistemic_registry
Individual claims with confidence labels:
- **id**: Unique claim identifier (C1, C2, etc.)
- **label**: One of FACT, LIKELY, PLAUSIBLE, ASSUMPTION, UNCERTAIN
- **confidence**: Numeric confidence (0.0-1.0)
- **evidence_basis**: Source of evidence supporting the claim

### epistemic_status
Reflects Phase 4 confidence tracking:
- **epistemic_gaps**: Knowledge we could obtain but haven't
- **aleatory_factors**: Inherent randomness/variability
- **model_dependencies**: Conclusions dependent on chosen framework

### downstream_guidance
Recommendations for next steps:
- **recommended_next_skill**: Suggested skill to invoke next (create-research-brief, requirements, architecture)
- **research_questions**: Priority-ranked questions for further investigation
- **validation_needed**: Items requiring validation before proceeding

---

## Validation Rules (CONTRACT-01 Compliance)

### Required Elements
- `artifact_id` must match pattern: `PS-YYYY-MM-DD-[5-char-hash]`
- `contract_type` must be `PROBLEM-STATEMENT`
- `confidence` must be in range 0.0-1.0
- `statement` must be non-empty
- `jtbd_format` must have all three components (situation, motivation, outcome)

### Structural Rules
- All `assumption` elements must have `id`, `type`, `validated`, `confidence` attributes
- All `claim` elements in epistemic_registry must have `id`, `label`, `confidence` attributes
- `label` values must be one of: FACT, LIKELY, PLAUSIBLE, ASSUMPTION, UNCERTAIN
- `priority` values must be one of: must_have, should_have, nice_to_have

### Semantic Rules
- If `solution_contamination.detected` is `true`, `cleaned_statement` must be non-empty
- Each `knowledge_map` category should have at least one entry or explicit comment
- `downstream_guidance.recommended_next_skill` must reference a valid skill name
- All `ref` elements must have valid `finding_id` or `assumption_id` references

---

## Validation Checklist

Before finalizing:
- [ ] Statement is actionable and clear
- [ ] Solution contamination check performed
- [ ] If contamination detected, cleaned_statement provided
- [ ] JTBD components are specific, not generic
- [ ] All critical stakeholders identified
- [ ] Constraints validated (negotiable flag accurate)
- [ ] Assumptions surfaced and categorized
- [ ] Knowledge map covers all four categories
- [ ] Epistemic registry labels match evidence quality
- [ ] Success criteria are measurable where possible
- [ ] Confidence reflects actual evidence quality
- [ ] Gaps have resolution approaches
- [ ] Downstream guidance includes research questions
- [ ] Validation items linked to assumptions/claims

---

## Example Output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<problem_statement contract="CONTRACT-01" version="1.0">

  <metadata>
    <artifact_id>PS-2025-01-15-a3f2b</artifact_id>
    <contract_type>PROBLEM-STATEMENT</contract_type>
    <created_at>2025-01-15T14:30:00Z</created_at>
    <created_by>research-interviewer</created_by>
    <confidence>0.82</confidence>
    <provenance>
      <source>interview</source>
      <interview_goal>Understand checkout abandonment causes</interview_goal>
      <interviewee_role>Product Manager</interviewee_role>
      <interview_date>2025-01-15</interview_date>
      <interview_turns>42</interview_turns>
      <questions_asked>18</questions_asked>
      <dimensions_covered>5</dimensions_covered>
      <validation_mode>balanced</validation_mode>
    </provenance>
  </metadata>

  <statement>E-commerce checkout abandonment exceeds industry benchmarks due to payment friction and trust concerns, requiring a streamlined payment flow with enhanced security signals.</statement>

  <solution_contamination>
    <detected>true</detected>
    <flagged_phrases>
      <phrase original="requiring a streamlined payment flow" issue="Embeds solution approach"/>
      <phrase original="with enhanced security signals" issue="Prescribes specific implementation"/>
    </flagged_phrases>
    <cleaned_statement>E-commerce checkout abandonment exceeds industry benchmarks due to payment friction and trust concerns.</cleaned_statement>
  </solution_contamination>

  <jtbd_format>
    <situation>When a customer has items in cart and is ready to purchase</situation>
    <motivation>I want to complete payment quickly with confidence my data is secure</motivation>
    <outcome>So that I receive my items without anxiety about fraud or complications</outcome>
  </jtbd_format>

  <context>
    <domain>product</domain>
    <stakeholders>
      <stakeholder role="Product Manager" impact="high">Sarah Chen</stakeholder>
      <stakeholder role="End User" impact="high">First-time buyers, 25-45 demographic</stakeholder>
      <stakeholder role="Engineering Lead" impact="medium">Payment team</stakeholder>
    </stakeholders>
    <constraints>
      <constraint type="technical" negotiable="false">
        Must integrate with existing Stripe infrastructure
      </constraint>
      <constraint type="business" negotiable="true">
        Implementation budget of $30K
      </constraint>
      <constraint type="regulatory" negotiable="false">
        PCI-DSS compliance required
      </constraint>
    </constraints>
    <assumptions>
      <assumption id="A1" type="explicit" validated="true" confidence="0.90">
        <statement>Users abandon primarily at payment step, not earlier</statement>
        <implications>Solution should focus on payment UX, not cart experience</implications>
      </assumption>
      <assumption id="A2" type="implicit" validated="false" confidence="0.65">
        <statement>Trust badges significantly impact conversion</statement>
        <implications>Design should prominently feature security indicators</implications>
      </assumption>
    </assumptions>
  </context>

  <knowledge_map>
    <known>
      <ref finding_id="D1F1">Abandonment rate is 48% at payment step</ref>
      <ref finding_id="D1F2">Users cite "too many steps" as primary complaint</ref>
    </known>
    <believed>
      <ref finding_id="D2F1">Mobile users abandon at higher rates than desktop</ref>
      <ref finding_id="D2F2">Guest checkout would improve conversion</ref>
    </believed>
    <assumed>
      <ref finding_id="D3F1">Trust badges placement affects user confidence</ref>
    </assumed>
    <unknown>
      <gap dimension="Competitive Landscape">Competitor checkout flows not analyzed</gap>
      <gap dimension="Success Metrics">Baseline mobile vs desktop conversion rates</gap>
    </unknown>
  </knowledge_map>

  <epistemic_registry>
    <claim id="C1" label="FACT" confidence="0.95">
      <statement>Current checkout abandonment rate is 48%</statement>
      <evidence_basis>Analytics dashboard data, confirmed by PM</evidence_basis>
    </claim>
    <claim id="C2" label="LIKELY" confidence="0.85">
      <statement>Payment step causes most friction</statement>
      <evidence_basis>Drop-off analysis shows 60% of abandonments at payment</evidence_basis>
    </claim>
    <claim id="C3" label="PLAUSIBLE" confidence="0.70">
      <statement>Guest checkout would reduce abandonment by 15%</statement>
      <evidence_basis>Industry benchmarks suggest this, not validated internally</evidence_basis>
    </claim>
    <claim id="C4" label="ASSUMPTION" confidence="0.50">
      <statement>Trust badges significantly impact conversion</statement>
      <evidence_basis>PM belief based on competitor analysis</evidence_basis>
    </claim>
  </epistemic_registry>

  <success_criteria>
    <criterion id="SC1" measurable="true" priority="must_have">
      <description>Reduce checkout abandonment rate</description>
      <metric>Abandonment percentage at payment step</metric>
      <target>Below 35% (currently 48%)</target>
    </criterion>
    <criterion id="SC2" measurable="true" priority="should_have">
      <description>Improve checkout completion time</description>
      <metric>Average seconds from cart to confirmation</metric>
      <target>Under 90 seconds</target>
    </criterion>
  </success_criteria>

  <epistemic_status>
    <overall_confidence>0.82</overall_confidence>
    <uncertainty_breakdown>
      <epistemic_gaps>
        <gap severity="significant">
          <description>No A/B test data on trust badge effectiveness</description>
          <resolution_approach>Run 2-week A/B test before full implementation</resolution_approach>
        </gap>
      </epistemic_gaps>
      <aleatory_factors>
        <factor>Seasonal variation in buyer behavior</factor>
      </aleatory_factors>
      <model_dependencies>
        <dependency>Industry benchmark comparison assumes similar customer demographics</dependency>
      </model_dependencies>
    </uncertainty_breakdown>
  </epistemic_status>

  <downstream_guidance>
    <recommended_next_skill>create-research-brief</recommended_next_skill>
    <research_questions>
      <question priority="high">What is the actual impact of trust badges on conversion?</question>
      <question priority="high">How do competitor checkout flows compare to ours?</question>
      <question priority="medium">What is the mobile vs desktop conversion breakdown?</question>
    </research_questions>
    <validation_needed>
      <item ref="A2">Trust badges impact needs A/B testing</item>
      <item ref="C3">Guest checkout benefit estimate needs validation</item>
    </validation_needed>
  </downstream_guidance>

</problem_statement>
```

---

## Integration Notes

### For create-research-brief Consumption

The create-research-brief skill reads PROBLEM-STATEMENT artifacts to:
1. Extract `statement` and `jtbd_format` as research context
2. Use `knowledge_map.unknown` to identify research gaps
3. Use `epistemic_registry` claims labeled ASSUMPTION/UNCERTAIN to prioritize investigation
4. Use `downstream_guidance.research_questions` as starting points for research design

### Handoff Protocol

1. Save artifact to `artifacts/` directory using `artifact_id` as filename (e.g., `PS-2025-01-15-a3f2b.xml`)
2. Reference in research brief metadata via `source_artifact` field
3. Carry forward unvalidated assumptions (`validated="false"`) for tracking through research phase
4. Use `validation_needed` items to structure research objectives

### Artifact Chaining

```
research-interviewer → PROBLEM-STATEMENT
                            ↓
create-research-brief → RESEARCH-BRIEF
                            ↓
         [research execution] → RESEARCH-FINDINGS
                            ↓
research-interviewer → REQUIREMENTS (if applicable)
```
