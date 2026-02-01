# Output Templates

Complete XML templates for the three output formats produced by the research-interviewer skill.

---

## 1. PROBLEM-STATEMENT Template

Aligns with CONTRACT-01 from the artifact contracts catalog.

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
      <interview_goal>[Goal]</interview_goal>
      <questions_asked>[N]</questions_asked>
      <dimensions_covered>[N]</dimensions_covered>
      <validation_mode>[empathetic|balanced|rigorous]</validation_mode>
    </provenance>
  </metadata>

  <statement>[Clear, actionable problem statement]</statement>

  <jtbd_format>
    <situation>[When/context]</situation>
    <motivation>[What the user wants to do]</motivation>
    <outcome>[Desired result/benefit]</outcome>
  </jtbd_format>

  <context>
    <domain>[product|architecture|strategy|research|security|operations]</domain>
    <stakeholders>
      <stakeholder role="[role]" impact="[high|medium|low]">[Who]</stakeholder>
    </stakeholders>
    <constraints>
      <constraint type="[technical|business|regulatory]" negotiable="[true|false]">
        [Constraint description]
      </constraint>
    </constraints>
    <assumptions>
      <assumption id="A1" type="[explicit|implicit|structural]"
                  validated="[true|false]" confidence="[0.0-1.0]">
        <statement>[Assumption text]</statement>
        <implications>[What depends on this]</implications>
      </assumption>
    </assumptions>
  </context>

  <success_criteria>
    <criterion id="SC1" measurable="[true|false]"
               priority="[must_have|should_have|nice_to_have]">
      <description>[What success looks like]</description>
      <metric>[How to measure]</metric>
      <target>[Target value]</target>
    </criterion>
  </success_criteria>

  <epistemic_status>
    <overall_confidence>[0.0-1.0]</overall_confidence>
    <uncertainty_breakdown>
      <epistemic_gaps>
        <gap severity="[critical|significant|minor]">
          <description>[Knowledge gap]</description>
          <resolution_approach>[How to close]</resolution_approach>
        </gap>
      </epistemic_gaps>
      <aleatory_factors>
        <factor>[Inherent uncertainty]</factor>
      </aleatory_factors>
      <model_dependencies>
        <dependency>[Framework-dependent answer]</dependency>
      </model_dependencies>
    </uncertainty_breakdown>
  </epistemic_status>

</problem_statement>
```

---

## 2. KNOWLEDGE-CORPUS Template

Optimized for RAG systems and context injection.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<knowledge_corpus version="1.0">

  <metadata>
    <corpus_id>KC-[YYYY-MM-DD]-[5-char-hash]</corpus_id>
    <topic>[Interview topic]</topic>
    <created_at>[ISO 8601]</created_at>
    <created_by>research-interviewer</created_by>
    <overall_confidence>[0.0-1.0]</overall_confidence>
    <stats>
      <dimensions_count>[N]</dimensions_count>
      <findings_count>[N]</findings_count>
      <relationships_count>[N]</relationships_count>
    </stats>
  </metadata>

  <coverage_map>
    <dimension id="D1" name="[Name]" confidence="[0.0-1.0]"
               priority="[critical|important|nice_to_have]">
      <finding id="D1F1" confidence="[0.0-1.0]"
               uncertainty_type="[EPISTEMIC|ALEATORY|MODEL]">
        <statement>[What was learned]</statement>
        <evidence>[How we know this]</evidence>
        <source_question type="[question_type]">[Question asked]</source_question>
      </finding>
    </dimension>
  </coverage_map>

  <relationships>
    <relationship id="R1" from="[finding_id]" to="[finding_id]"
                  type="[depends_on|supports|contradicts|refines]">
      <description>[How they relate]</description>
      <strength>[strong|moderate|weak]</strength>
    </relationship>
  </relationships>

  <assumption_inventory>
    <assumption id="A1" type="[explicit|implicit|structural]"
                validated="[true|false]" confidence="[0.0-1.0]">
      <statement>[Assumption]</statement>
      <implications>[What depends on this]</implications>
    </assumption>
  </assumption_inventory>

  <gaps_registry>
    <gap id="G1" dimension="[dimension_id]" severity="[critical|significant|minor]">
      <description>[What's missing]</description>
      <suggested_resolution>[How to close]</suggested_resolution>
    </gap>
  </gaps_registry>

  <confidence_report>
    <overall_confidence>[0.0-1.0]</overall_confidence>
    <by_dimension>
      <dimension ref="D1" confidence="[0.0-1.0]"/>
    </by_dimension>
    <by_uncertainty_type>
      <epistemic count="[N]"/>
      <aleatory count="[N]"/>
      <model count="[N]"/>
    </by_uncertainty_type>
  </confidence_report>

</knowledge_corpus>
```

---

## 3. REQUIREMENTS Template

Job stories with acceptance criteria and traceability.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<requirements version="1.0">

  <metadata>
    <requirements_id>REQ-[YYYY-MM-DD]-[5-char-hash]</requirements_id>
    <topic>[Interview topic]</topic>
    <created_at>[ISO 8601]</created_at>
    <created_by>research-interviewer</created_by>
    <overall_confidence>[0.0-1.0]</overall_confidence>
  </metadata>

  <job_stories>
    <job_story id="JS1" priority="[must_have|should_have|nice_to_have]"
               confidence="[0.0-1.0]">
      <situation>When [context/trigger]</situation>
      <motivation>I want to [action/capability]</motivation>
      <outcome>So that [benefit/result]</outcome>
      <acceptance_criteria>
        <criterion id="JS1AC1" testable="[true|false]">
          Given [precondition], When [action], Then [result]
        </criterion>
      </acceptance_criteria>
      <assumptions>
        <ref assumption_id="A1"/>
      </assumptions>
    </job_story>
  </job_stories>

  <constraints>
    <constraint id="C1" type="[technical|business|regulatory]"
                non_negotiable="[true|false]">
      <description>[Constraint]</description>
      <rationale>[Why it exists]</rationale>
    </constraint>
  </constraints>

  <non_functional_requirements>
    <nfr id="NFR1" category="[performance|security|scalability|reliability]"
         priority="[must_have|should_have|nice_to_have]">
      <description>[NFR description]</description>
      <measurement>[How to verify]</measurement>
      <target>[Target value]</target>
    </nfr>
  </non_functional_requirements>

  <traceability>
    <finding_to_requirement from="[finding_id]" to="[requirement_id]">
      <rationale>[How finding led to requirement]</rationale>
    </finding_to_requirement>
  </traceability>

  <confidence_report>
    <overall_confidence>[0.0-1.0]</overall_confidence>
    <by_priority>
      <must_have count="[N]" avg_confidence="[0.0-1.0]"/>
      <should_have count="[N]" avg_confidence="[0.0-1.0]"/>
      <nice_to_have count="[N]" avg_confidence="[0.0-1.0]"/>
    </by_priority>
  </confidence_report>

</requirements>
```

---

## Template Selection Guide

| Output Format | Best For | Downstream Use |
|---------------|----------|----------------|
| **PROBLEM-STATEMENT** | Research briefs, ideation, problem analysis | create-research-brief, generate-ideas |
| **KNOWLEDGE-CORPUS** | Documentation, RAG, context | Context injection, documentation skills |
| **REQUIREMENTS** | Development, specifications | Specification skills, development workflows |
