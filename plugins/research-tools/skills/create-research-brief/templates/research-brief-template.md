# Research Brief Template

This template defines the Phase 1 output structure for research brief generation. Use this structure when creating research briefs before research is conducted. The XML tags enable machine-readable parsing and downstream automation.

---

## Template Structure

```xml
<research_brief>
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- HEADER BLOCK                                                            -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <header>
    <research_id>[AUTO-GENERATED: YYYY-MM-DD-XXXXX]</research_id>
    <created>[ISO 8601 timestamp]</created>
    <type>[market | competitive | technology | strategic | user | regulatory]</type>
    <mode>[quick | standard | deep]</mode>
    <parameters>
      <research_domain>[Domain specification]</research_domain>
      <time_horizon>[Time range for research relevance]</time_horizon>
      <geography>[Geographic scope: global | region | country | local]</geography>
      <target_models>
        <model priority="primary">[claude-opus-4.5 | gemini-pro-3 | gpt-5.2-deep]</model>
        <model priority="secondary">[model name]</model>
        <model priority="tertiary">[model name]</model>
      </target_models>
      <hypothesis_mode enabled="[true|false]">[If true, include Section 3]</hypothesis_mode>
      <expert_panel enabled="[true|false]">[If true, include Section 5]</expert_panel>
    </parameters>
  </header>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 1: RESEARCH CLASSIFICATION                                      -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_1_research_classification>
    <objective>
      <statement>[Clear, single-sentence research objective]</statement>
      <decision_context>[What decision will this research inform?]</decision_context>
      <stakeholders>
        <stakeholder role="[primary|secondary]">[Who needs this research]</stakeholder>
      </stakeholders>
    </objective>

    <key_questions>
      <question id="KQ1" priority="critical">
        [Primary research question - must be answered]
      </question>
      <question id="KQ2" priority="important">
        [Secondary research question]
      </question>
      <question id="KQ3" priority="nice_to_have">
        [Tertiary research question]
      </question>
    </key_questions>

    <success_criteria>
      <criterion id="SC1" measurable="true">
        [What constitutes a successful research outcome]
        <measurement>[How to measure this criterion]</measurement>
      </criterion>
      <criterion id="SC2" measurable="true">
        [Another success criterion]
        <measurement>[How to measure]</measurement>
      </criterion>
    </success_criteria>

    <scope>
      <in_scope>
        <item>[What IS included in research]</item>
        <item>[Another included topic]</item>
      </in_scope>
      <out_of_scope>
        <item>[What is explicitly EXCLUDED]</item>
        <item>[Another excluded topic]</item>
      </out_of_scope>
      <boundary_conditions>
        <condition>[Constraints that define scope edges]</condition>
      </boundary_conditions>
    </scope>
  </section_1_research_classification>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 2: MECE QUESTION DECOMPOSITION                                  -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_2_mece_decomposition>
    <decomposition_pattern>[market | competitive | technology | strategic]</decomposition_pattern>

    <categories>
      <category id="C1" name="[Category Name]">
        <description>[What this category covers]</description>
        <model_assignment>[claude-opus-4.5 | gemini-pro-3 | gpt-5.2-deep]</model_assignment>
        <assignment_rationale>[Why this model for this category]</assignment_rationale>

        <questions>
          <question id="C1Q1" researchable="true">
            <text>[Specific, answerable research question]</text>
            <expected_output>[What form the answer should take]</expected_output>
            <min_evidence_score>3</min_evidence_score>
          </question>
          <question id="C1Q2" researchable="true">
            <text>[Second question in this category]</text>
            <expected_output>[Expected output form]</expected_output>
            <min_evidence_score>3</min_evidence_score>
          </question>
          <question id="C1Q3" researchable="true">
            <text>[Third question in this category]</text>
            <expected_output>[Expected output form]</expected_output>
            <min_evidence_score>2</min_evidence_score>
          </question>
        </questions>
      </category>

      <category id="C2" name="[Category Name]">
        <description>[What this category covers]</description>
        <model_assignment>[model]</model_assignment>
        <assignment_rationale>[Why]</assignment_rationale>
        <questions>
          <question id="C2Q1" researchable="true">
            <text>[Question]</text>
            <expected_output>[Output form]</expected_output>
            <min_evidence_score>3</min_evidence_score>
          </question>
          <!-- Additional questions -->
        </questions>
      </category>

      <category id="C3" name="[Category Name]">
        <!-- Structure repeats -->
      </category>

      <category id="C4" name="[Category Name]">
        <!-- Structure repeats -->
      </category>

      <category id="C5" name="[Category Name]">
        <!-- Structure repeats -->
      </category>
    </categories>

    <coverage_matrix>
      <dimension name="[Dimension 1]">
        <coverage_by category="C1">partial</coverage_by>
        <coverage_by category="C2">full</coverage_by>
      </dimension>
      <dimension name="[Dimension 2]">
        <coverage_by category="C3">full</coverage_by>
      </dimension>
      <!-- Additional dimensions -->

      <completeness_check>
        <mece_verified>[true|false]</mece_verified>
        <gaps_identified>
          <gap severity="[critical|significant|minor]">[Description of gap]</gap>
        </gaps_identified>
      </completeness_check>
    </coverage_matrix>
  </section_2_mece_decomposition>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 3: MULTI-HYPOTHESIS FRAMING (CONDITIONAL)                       -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_3_hypothesis_framing enabled="[true|false]">
    <!-- Include this section only if hypothesis_mode is enabled -->

    <core_question>[The prediction/outcome being tested]</core_question>

    <hypotheses>
      <hypothesis id="H1" position="[affirmative]">
        <statement>[Clear hypothesis statement]</statement>
        <prior_probability>[0-100%]</prior_probability>
        <prior_rationale>[Why this prior probability]</prior_rationale>

        <supporting_evidence_needed>
          <evidence id="H1E1">[What would support this hypothesis]</evidence>
          <evidence id="H1E2">[Another supporting evidence type]</evidence>
        </supporting_evidence_needed>

        <refuting_evidence>
          <evidence id="H1R1">[What would refute this hypothesis]</evidence>
          <evidence id="H1R2">[Another refuting evidence type]</evidence>
        </refuting_evidence>
      </hypothesis>

      <hypothesis id="H2" position="[partial]">
        <statement>[Partial/conditional outcome hypothesis]</statement>
        <prior_probability>[0-100%]</prior_probability>
        <prior_rationale>[Why]</prior_rationale>
        <supporting_evidence_needed>
          <evidence id="H2E1">[Supporting evidence]</evidence>
        </supporting_evidence_needed>
        <refuting_evidence>
          <evidence id="H2R1">[Refuting evidence]</evidence>
        </refuting_evidence>
      </hypothesis>

      <hypothesis id="H3" position="[negative]">
        <statement>[Counter-hypothesis]</statement>
        <prior_probability>[0-100%]</prior_probability>
        <prior_rationale>[Why]</prior_rationale>
        <supporting_evidence_needed>
          <evidence id="H3E1">[Supporting evidence]</evidence>
        </supporting_evidence_needed>
        <refuting_evidence>
          <evidence id="H3R1">[Refuting evidence]</evidence>
        </refuting_evidence>
      </hypothesis>
    </hypotheses>

    <hypothesis_verification_note>
      Priors must sum to 100%. Evidence criteria should be specific enough to
      enable objective assessment during research consolidation.
    </hypothesis_verification_note>
  </section_3_hypothesis_framing>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 4: RISK ASSESSMENT                                              -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_4_risk_assessment depth="[quick|standard|comprehensive]">

    <!-- QUICK DEPTH: Basic risk identification -->
    <quick_assessment>
      <top_risks>
        <risk id="R1" category="[execution|information|external]">
          <description>[Brief risk description]</description>
          <likelihood>[high|medium|low]</likelihood>
          <impact>[high|medium|low]</impact>
        </risk>
        <risk id="R2" category="[category]">
          <description>[Risk description]</description>
          <likelihood>[level]</likelihood>
          <impact>[level]</impact>
        </risk>
        <risk id="R3" category="[category]">
          <description>[Risk description]</description>
          <likelihood>[level]</likelihood>
          <impact>[level]</impact>
        </risk>
      </top_risks>
    </quick_assessment>

    <!-- STANDARD DEPTH: Add mitigations and contingencies -->
    <standard_assessment include_if="[standard|comprehensive]">
      <risk_details>
        <risk ref="R1">
          <mitigation>[How to reduce likelihood or impact]</mitigation>
          <contingency>[What to do if risk materializes]</contingency>
          <early_warning>[Signal that risk is materializing]</early_warning>
        </risk>
        <risk ref="R2">
          <mitigation>[Mitigation strategy]</mitigation>
          <contingency>[Contingency plan]</contingency>
          <early_warning>[Warning signal]</early_warning>
        </risk>
        <risk ref="R3">
          <mitigation>[Mitigation]</mitigation>
          <contingency>[Contingency]</contingency>
          <early_warning>[Warning]</early_warning>
        </risk>
      </risk_details>
    </standard_assessment>

    <!-- COMPREHENSIVE DEPTH: Add scenarios and dependencies -->
    <comprehensive_assessment include_if="[comprehensive]">
      <risk_scenarios>
        <scenario id="RS1" name="[Scenario Name]">
          <description>[What happens in this scenario]</description>
          <trigger_conditions>
            <condition>[What triggers this scenario]</condition>
          </trigger_conditions>
          <risks_activated>
            <risk ref="R1"/>
            <risk ref="R2"/>
          </risks_activated>
          <response_plan>[How to respond if scenario occurs]</response_plan>
        </scenario>
      </risk_scenarios>

      <risk_dependencies>
        <dependency>
          <if_risk ref="R1">materializes</if_risk>
          <then_risk ref="R2">likelihood increases to high</then_risk>
        </dependency>
      </risk_dependencies>

      <risk_matrix>
        <!-- Visual risk matrix representation -->
        <high_impact_high_likelihood>
          <risk ref="[risk ids]"/>
        </high_impact_high_likelihood>
        <high_impact_low_likelihood>
          <risk ref="[risk ids]"/>
        </high_impact_low_likelihood>
        <low_impact_high_likelihood>
          <risk ref="[risk ids]"/>
        </low_impact_high_likelihood>
        <low_impact_low_likelihood>
          <risk ref="[risk ids]"/>
        </low_impact_low_likelihood>
      </risk_matrix>
    </comprehensive_assessment>
  </section_4_risk_assessment>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 5: EXPERT PANEL RECOMMENDATIONS (CONDITIONAL)                   -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_5_expert_panel enabled="[true|false]">
    <!-- Include this section only if expert_panel is enabled -->

    <panel_purpose>[What the expert panel will evaluate or advise on]</panel_purpose>

    <recommended_panel size="[3-8]" perspective_balance="[technical_heavy|business_heavy|balanced|challenger_heavy]">
      <expert id="E1">
        <role>[Expert title/role]</role>
        <domain>[Area of expertise]</domain>
        <perspective>[What unique view they bring]</perspective>
        <key_questions>
          <question>[What to ask this expert]</question>
        </key_questions>
      </expert>

      <expert id="E2">
        <role>[Role]</role>
        <domain>[Domain]</domain>
        <perspective>[Perspective]</perspective>
        <key_questions>
          <question>[Questions for this expert]</question>
        </key_questions>
      </expert>

      <expert id="E3">
        <role>[Role]</role>
        <domain>[Domain]</domain>
        <perspective>[Perspective]</perspective>
        <key_questions>
          <question>[Questions]</question>
        </key_questions>
      </expert>

      <!-- Additional experts as needed -->

      <challenger role="true">
        <expert ref="E[N]"/>
        <challenge_focus>[What assumptions to challenge]</challenge_focus>
      </challenger>
    </recommended_panel>

    <deliberation_format>
      <structure>[round_robin | debate | delphi | structured_analytic]</structure>
      <rounds>[Number of deliberation rounds]</rounds>
      <consensus_requirement>[unanimous | majority | none]</consensus_requirement>
    </deliberation_format>
  </section_5_expert_panel>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 6: MODEL ROLE ASSIGNMENTS                                       -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_6_model_roles>
    <assignment_strategy>[parallel | sequential | convergent]</assignment_strategy>

    <model_assignments>
      <model name="claude-opus-4.5">
        <role>synthesis_and_strategy</role>
        <assigned_categories>
          <category ref="C[N]"/>
          <category ref="C[N]"/>
        </assigned_categories>
        <strengths_leveraged>
          <strength>Extended reasoning for complex synthesis</strength>
          <strength>Nuanced analysis of conflicting information</strength>
          <strength>Strategic implication assessment</strength>
        </strengths_leveraged>
        <execution_order>[1|2|3 or "parallel"]</execution_order>
      </model>

      <model name="gemini-pro-3">
        <role>breadth_and_grounding</role>
        <assigned_categories>
          <category ref="C[N]"/>
          <category ref="C[N]"/>
        </assigned_categories>
        <strengths_leveraged>
          <strength>Web grounding for current information</strength>
          <strength>Comprehensive source coverage</strength>
          <strength>Citation and attribution</strength>
        </strengths_leveraged>
        <execution_order>[1|2|3 or "parallel"]</execution_order>
      </model>

      <model name="gpt-5.2-deep">
        <role>depth_and_detail</role>
        <assigned_categories>
          <category ref="C[N]"/>
        </assigned_categories>
        <strengths_leveraged>
          <strength>Exhaustive investigation of narrow topics</strength>
          <strength>Technical depth and precision</strength>
          <strength>Detailed competitive analysis</strength>
        </strengths_leveraged>
        <execution_order>[1|2|3 or "parallel"]</execution_order>
      </model>
    </model_assignments>

    <handoff_protocol>
      <handoff from="[model]" to="[model]">
        <trigger>[When to hand off]</trigger>
        <deliverable>[What to pass]</deliverable>
      </handoff>
    </handoff_protocol>
  </section_6_model_roles>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 7: READY-TO-EXECUTE PROMPTS                                     -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_7_prompts>

    <prompt model="claude-opus-4.5" id="PROMPT-CLAUDE">
      <purpose>[What this prompt will uncover]</purpose>
      <categories_addressed>
        <category ref="C[N]"/>
      </categories_addressed>

      <prompt_text><![CDATA[
<context>
[Research context and background]
[Scope definition and constraints]
[Key stakeholders and decision context]
</context>

<task>
[Specific research task for Claude]
[Clear deliverable expectations]
</task>

<output_requirements>
Format: [Required output structure]
Include:
- [Required element 1]
- [Required element 2]
- [Required element 3]

Confidence: Provide confidence level (High/Medium/Low) for each finding with rationale.

Evidence: Cite sources with evidence strength scores (1-5 scale).
</output_requirements>

<constraints>
- [Constraint 1]
- [Constraint 2]
</constraints>
      ]]></prompt_text>

      <expected_tokens>[Estimated input + output tokens]</expected_tokens>
    </prompt>

    <prompt model="gemini-pro-3" id="PROMPT-GEMINI">
      <purpose>[What this prompt will uncover]</purpose>
      <categories_addressed>
        <category ref="C[N]"/>
      </categories_addressed>

      <prompt_text><![CDATA[
Research Task: [Clear task statement]

Requirements:
1. [Requirement with citation request]
2. [Requirement with recency emphasis]
3. [Requirement with breadth expectation]

Output Format:
- [Specified format]
- [Structure requirements]

Note: Prioritize recent sources (2024-2025) and include citations with URLs where available.

Scope: [Geographic/temporal/domain boundaries]
      ]]></prompt_text>

      <expected_tokens>[Estimated tokens]</expected_tokens>
    </prompt>

    <prompt model="gpt-5.2-deep" id="PROMPT-GPT">
      <purpose>[What this prompt will uncover]</purpose>
      <categories_addressed>
        <category ref="C[N]"/>
      </categories_addressed>

      <prompt_text><![CDATA[
Deep Research Request: [Specific topic for exhaustive investigation]

Objective: [Clear objective statement]

Investigation Areas:
1. [Specific area 1 - go deep]
2. [Specific area 2 - go deep]
3. [Specific area 3 - go deep]

Required Depth:
- Examine all available evidence
- Identify edge cases and exceptions
- Surface contradictions and debates
- Assess methodology of sources

Output Requirements:
- Structured findings with evidence hierarchy
- Explicit uncertainty quantification
- Alternative interpretations considered

Boundaries: [What to exclude to maintain focus]
      ]]></prompt_text>

      <expected_tokens>[Estimated tokens]</expected_tokens>
    </prompt>
  </section_7_prompts>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 8: CONSOLIDATION STRATEGY                                       -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_8_consolidation>
    <consolidation_approach>[triangulation | weighted_synthesis | hierarchical | dialectical]</consolidation_approach>

    <synthesis_rules>
      <rule id="SR1" condition="models_agree">
        <action>Report as high-confidence finding</action>
        <confidence_adjustment>+20%</confidence_adjustment>
      </rule>

      <rule id="SR2" condition="models_conflict">
        <action>Apply conflict resolution protocol</action>
        <protocol>
          <step>Identify methodology differences</step>
          <step>Assess source quality for each position</step>
          <step>Report both positions with evidence scores</step>
          <step>Recommend resolution or state "unresolved"</step>
        </protocol>
      </rule>

      <rule id="SR3" condition="single_model_finding">
        <action>Flag for verification, reduce confidence</action>
        <confidence_adjustment>-15%</confidence_adjustment>
      </rule>

      <rule id="SR4" condition="evidence_gap">
        <action>Document as epistemic uncertainty</action>
        <flag>research_gap</flag>
      </rule>
    </synthesis_rules>

    <evidence_weighting>
      <source_type weight="1.0">Primary sources (Score 5)</source_type>
      <source_type weight="0.85">Authoritative secondary (Score 4)</source_type>
      <source_type weight="0.70">Credible secondary (Score 3)</source_type>
      <source_type weight="0.40">Weak secondary (Score 2)</source_type>
      <source_type weight="0.10">Speculative (Score 1)</source_type>
    </evidence_weighting>

    <output_tiers>
      <tier level="1" threshold="75">High confidence findings</tier>
      <tier level="2" threshold="50">Medium confidence findings</tier>
      <tier level="3" threshold="0">Low confidence / contested findings</tier>
    </output_tiers>
  </section_8_consolidation>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 9: VERIFICATION PRIORITIES                                      -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_9_verification>
    <verification_order>
      <priority level="1" category="critical_claims">
        <description>Findings that directly answer key questions</description>
        <verification_method>Cross-reference with primary sources</verification_method>
        <min_sources>3</min_sources>
      </priority>

      <priority level="2" category="decision_drivers">
        <description>Findings that would change the decision</description>
        <verification_method>Seek contradicting evidence</verification_method>
        <min_sources>2</min_sources>
      </priority>

      <priority level="3" category="assumptions">
        <description>Implicit assumptions in the research</description>
        <verification_method>Explicit assumption testing</verification_method>
        <min_sources>1</min_sources>
      </priority>
    </verification_order>

    <red_flags>
      <flag trigger="single_source">
        Findings supported by only one source require additional verification
      </flag>
      <flag trigger="outdated_data">
        Data older than [time threshold] requires currency check
      </flag>
      <flag trigger="circular_citation">
        Sources citing each other without primary evidence
      </flag>
      <flag trigger="conflict_of_interest">
        Source has financial or reputational stake in finding
      </flag>
    </red_flags>
  </section_9_verification>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- SECTION 10: EFFORT ESTIMATES                                            -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <section_10_effort>
    <mode_estimates>
      <quick>
        <prompt_execution>15-30 minutes</prompt_execution>
        <consolidation>15 minutes</consolidation>
        <verification>Minimal (spot check)</verification>
        <total>30-60 minutes</total>
      </quick>

      <standard>
        <prompt_execution>1-2 hours</prompt_execution>
        <consolidation>30-60 minutes</consolidation>
        <verification>Key findings verified</verification>
        <total>2-4 hours</total>
      </standard>

      <deep>
        <prompt_execution>2-4 hours (may require iteration)</prompt_execution>
        <consolidation>1-2 hours</consolidation>
        <verification>Comprehensive verification</verification>
        <total>4-8 hours</total>
      </deep>
    </mode_estimates>

    <resource_requirements>
      <tokens_estimated>
        <model name="claude-opus-4.5">[Estimated tokens]</model>
        <model name="gemini-pro-3">[Estimated tokens]</model>
        <model name="gpt-5.2-deep">[Estimated tokens]</model>
        <total>[Total estimated tokens]</total>
      </tokens_estimated>

      <cost_estimate currency="USD">
        <low>[Minimum expected cost]</low>
        <high>[Maximum expected cost]</high>
      </cost_estimate>
    </resource_requirements>

    <dependencies>
      <dependency type="data_access">
        [Any data sources that must be accessible]
      </dependency>
      <dependency type="expertise">
        [Any human expertise needed for verification]
      </dependency>
      <dependency type="timing">
        [Any timing dependencies or constraints]
      </dependency>
    </dependencies>
  </section_10_effort>

</research_brief>
```

---

## Usage Instructions

### 1. Generating a Research Brief

1. **Identify research type** → Select appropriate MECE pattern from `mece-decomposition-guide.md`
2. **Set parameters** → Complete header block with scope, mode, and model selections
3. **Decompose questions** → Apply MECE pattern to generate categories and sub-questions
4. **Assign models** → Map categories to models based on capability profiles
5. **Generate prompts** → Create model-specific prompts using the templates
6. **Define consolidation** → Specify how outputs will be synthesized

### 2. Conditional Sections

| Section | Condition | Default |
|---------|-----------|---------|
| Section 3: Hypothesis Framing | `hypothesis_mode="true"` | Excluded |
| Section 5: Expert Panel | `expert_panel="true"` | Excluded |
| Section 4 depth levels | `depth` parameter | Varies by mode |

### 3. Mode Defaults

| Mode | Risk Depth | Verification | Expert Panel |
|------|------------|--------------|--------------|
| Quick | quick | Spot check | Off |
| Standard | standard | Key findings | Optional |
| Deep | comprehensive | Comprehensive | Recommended |

### 4. XML Parsing Notes

- All IDs are unique within their scope (e.g., `C1Q1` = Category 1, Question 1)
- Cross-references use `ref` attribute (e.g., `<category ref="C1"/>`)
- CDATA sections preserve prompt formatting
- Boolean attributes use lowercase `true`/`false`

---

## Example: Completed Research Brief Header

```xml
<research_brief>
  <header>
    <research_id>2025-01-31-MKT01</research_id>
    <created>2025-01-31T14:30:00Z</created>
    <type>market</type>
    <mode>standard</mode>
    <parameters>
      <research_domain>AI-powered legal research tools</research_domain>
      <time_horizon>2024-2028</time_horizon>
      <geography>North America</geography>
      <target_models>
        <model priority="primary">gemini-pro-3</model>
        <model priority="secondary">claude-opus-4.5</model>
        <model priority="tertiary">gpt-5.2-deep</model>
      </target_models>
      <hypothesis_mode enabled="false"/>
      <expert_panel enabled="false"/>
    </parameters>
  </header>
  <!-- Remaining sections... -->
</research_brief>
```

---

## Validation Checklist

Before executing research brief:

```
[ ] Header block complete with valid type and mode
[ ] All key questions have priority assigned
[ ] Success criteria are measurable
[ ] Scope boundaries clearly defined
[ ] MECE decomposition passes quality checklist (see mece-decomposition-guide.md)
[ ] All categories have model assignments
[ ] Coverage matrix shows no critical gaps
[ ] Risk assessment appropriate for mode
[ ] Prompts are executable without modification
[ ] Consolidation rules handle all expected scenarios
[ ] Verification priorities align with key questions
[ ] Effort estimates are realistic
```
