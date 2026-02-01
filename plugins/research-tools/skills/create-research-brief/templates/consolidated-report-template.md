# Consolidated Research Report Template

This template defines the Phase 2 output structure for consolidated research reports. Use this structure when synthesizing multi-model research outputs into a final deliverable. Critical Constraints are placed at the END for optimal context retention during generation.

---

## Template Structure

```xml
<consolidated_report>
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- HEADER BLOCK                                                            -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <header>
    <report_id>[AUTO-GENERATED: YYYY-MM-DD-XXXXX-RPT]</report_id>
    <research_brief_ref>[Original research brief ID]</research_brief_ref>
    <generated>[ISO 8601 timestamp]</generated>
    <research_type>[market | competitive | technology | strategic | user | regulatory]</research_type>
    <research_mode>[quick | standard | deep]</research_mode>

    <models_used>
      <model name="[model name]" contribution="[primary|supporting]">
        <categories_researched>
          <category ref="C[N]"/>
        </categories_researched>
        <tokens_consumed>[Actual tokens used]</tokens_consumed>
      </model>
      <!-- Repeat for each model -->
    </models_used>

    <quality_summary>
      <overall_confidence>[HIGH | MEDIUM | LOW | INSUFFICIENT]</overall_confidence>
      <evidence_profile>
        <score_5_count>[N]</score_5_count>
        <score_4_count>[N]</score_4_count>
        <score_3_count>[N]</score_3_count>
        <score_2_count>[N]</score_2_count>
        <score_1_count>[N]</score_1_count>
      </evidence_profile>
      <mece_coverage>[X/Y categories covered at ≥Score 3]</mece_coverage>
    </quality_summary>
  </header>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 1: EXECUTIVE SUMMARY                                               -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_1_executive_summary>
    <bottom_line>
      [1-2 sentence answer to the primary research question]
    </bottom_line>

    <numbered_findings>
      <finding number="1" confidence="[HIGH|MEDIUM|LOW]">
        [Key finding statement]
        <implication>[What this means for the decision]</implication>
      </finding>

      <finding number="2" confidence="[confidence]">
        [Key finding statement]
        <implication>[Implication]</implication>
      </finding>

      <finding number="3" confidence="[confidence]">
        [Key finding statement]
        <implication>[Implication]</implication>
      </finding>

      <finding number="4" confidence="[confidence]">
        [Key finding statement]
        <implication>[Implication]</implication>
      </finding>

      <finding number="5" confidence="[confidence]">
        [Key finding statement]
        <implication>[Implication]</implication>
      </finding>
    </numbered_findings>

    <critical_caveats>
      <caveat severity="[high|medium]">
        [Important limitation or uncertainty affecting conclusions]
      </caveat>
      <caveat severity="[severity]">
        [Another caveat]
      </caveat>
    </critical_caveats>

    <recommendation>
      [Clear recommendation based on findings, or explicit statement of why
       recommendation cannot be made with current evidence]
    </recommendation>
  </part_1_executive_summary>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 2: TIERED FINDINGS                                                 -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_2_tiered_findings>

    <!-- TIER 1: High Confidence (>75%) -->
    <tier level="1" confidence_threshold="75">
      <tier_description>
        Findings with strong evidence support from multiple sources and/or
        model agreement. Safe to base decisions on.
      </tier_description>

      <findings>
        <finding id="T1F1">
          <statement>[Finding statement]</statement>
          <confidence_score>[76-100]%</confidence_score>
          <evidence_basis>
            <source score="[1-5]" model="[model]">[Source citation]</source>
            <source score="[1-5]" model="[model]">[Source citation]</source>
          </evidence_basis>
          <model_agreement>[agreed | partial | single_source]</model_agreement>
          <key_question_addressed ref="KQ[N]"/>
        </finding>

        <finding id="T1F2">
          <statement>[Finding]</statement>
          <confidence_score>[%]</confidence_score>
          <evidence_basis>
            <source score="[score]" model="[model]">[Citation]</source>
          </evidence_basis>
          <model_agreement>[status]</model_agreement>
        </finding>
        <!-- Additional Tier 1 findings -->
      </findings>
    </tier>

    <!-- TIER 2: Medium Confidence (50-75%) -->
    <tier level="2" confidence_threshold="50">
      <tier_description>
        Findings with reasonable evidence support but some uncertainty.
        Consider with appropriate hedging.
      </tier_description>

      <findings>
        <finding id="T2F1">
          <statement>[Finding statement]</statement>
          <confidence_score>[50-75]%</confidence_score>
          <evidence_basis>
            <source score="[score]" model="[model]">[Citation]</source>
          </evidence_basis>
          <model_agreement>[status]</model_agreement>
          <uncertainty_factors>
            <factor type="[epistemic|aleatory|model]">[Description]</factor>
          </uncertainty_factors>
        </finding>
        <!-- Additional Tier 2 findings -->
      </findings>
    </tier>

    <!-- TIER 3: Low Confidence (<50%) -->
    <tier level="3" confidence_threshold="0">
      <tier_description>
        Findings with weak evidence, contested claims, or high uncertainty.
        Treat as hypotheses requiring further investigation.
      </tier_description>

      <findings>
        <finding id="T3F1">
          <statement>[Finding statement]</statement>
          <confidence_score>[0-49]%</confidence_score>
          <evidence_basis>
            <source score="[score]" model="[model]">[Citation]</source>
          </evidence_basis>
          <why_low_confidence>
            [Explanation of evidence weakness or conflict]
          </why_low_confidence>
          <recommended_action>
            [What would increase confidence]
          </recommended_action>
        </finding>
        <!-- Additional Tier 3 findings -->
      </findings>
    </tier>
  </part_2_tiered_findings>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 3: EVIDENCE QUALITY ASSESSMENT                                     -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_3_evidence_quality>
    <score_distribution>
      <score level="5" name="Primary Source">
        <count>[N]</count>
        <examples>
          <example>[Source name/type]</example>
        </examples>
      </score>

      <score level="4" name="Authoritative Secondary">
        <count>[N]</count>
        <examples>
          <example>[Source name/type]</example>
        </examples>
      </score>

      <score level="3" name="Credible Secondary">
        <count>[N]</count>
        <examples>
          <example>[Source name/type]</example>
        </examples>
      </score>

      <score level="2" name="Weak Secondary">
        <count>[N]</count>
        <examples>
          <example>[Source name/type]</example>
        </examples>
      </score>

      <score level="1" name="Speculative">
        <count>[N]</count>
        <examples>
          <example>[Source name/type]</example>
        </examples>
      </score>
    </score_distribution>

    <source_type_distribution>
      <source_type name="[Type]" count="[N]" avg_score="[X.X]"/>
      <source_type name="[Type]" count="[N]" avg_score="[X.X]"/>
      <!-- e.g., analyst_reports, press_releases, financial_filings, etc. -->
    </source_type_distribution>

    <evidence_gaps>
      <gap category="C[N]" severity="[critical|significant|minor]">
        <description>[What evidence is missing]</description>
        <impact>[How this affects conclusions]</impact>
      </gap>
    </evidence_gaps>

    <weighted_confidence_calculation>
      <formula>Σ(Finding Score × Finding Weight) / Σ(Weights)</formula>
      <components>
        <component finding_ref="T1F1" score="[X]" weight="[Y]"/>
        <component finding_ref="T1F2" score="[X]" weight="[Y]"/>
        <!-- Additional components -->
      </components>
      <weighted_score>[Calculated score]</weighted_score>
      <resulting_tier>[HIGH | MEDIUM | LOW | INSUFFICIENT]</resulting_tier>
    </weighted_confidence_calculation>
  </part_3_evidence_quality>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 4: CONTESTED CLAIMS & CONFLICT RESOLUTION                          -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_4_contested_claims>

    <!-- Resolved Conflicts -->
    <resolved_conflicts>
      <conflict id="RC1">
        <claim>[The contested claim]</claim>
        <positions>
          <position holder="[Source/Model]" value="[Their position]">
            <evidence score="[1-5]">[Supporting evidence]</evidence>
          </position>
          <position holder="[Source/Model]" value="[Their position]">
            <evidence score="[1-5]">[Supporting evidence]</evidence>
          </position>
        </positions>
        <resolution>
          <chosen_position>[Which position was selected]</chosen_position>
          <rationale>[Why this position was selected]</rationale>
          <confidence_impact>[How resolution affected confidence]</confidence_impact>
        </resolution>
      </conflict>
    </resolved_conflicts>

    <!-- Unresolved Conflicts with WWHTBT -->
    <unresolved_conflicts>
      <conflict id="UC1">
        <claim>[The contested claim that remains unresolved]</claim>
        <positions>
          <position holder="[Source/Model]" value="[Position A]">
            <evidence score="[1-5]">[Evidence]</evidence>
          </position>
          <position holder="[Source/Model]" value="[Position B]">
            <evidence score="[1-5]">[Evidence]</evidence>
          </position>
        </positions>

        <!-- What Would Have To Be True (WWHTBT) -->
        <wwhtbt>
          <for_position_a>
            <condition>[What would have to be true for Position A to be correct]</condition>
            <condition>[Another necessary condition]</condition>
            <testability>[How could we test these conditions]</testability>
          </for_position_a>

          <for_position_b>
            <condition>[What would have to be true for Position B to be correct]</condition>
            <condition>[Another necessary condition]</condition>
            <testability>[How could we test these conditions]</testability>
          </for_position_b>
        </wwhtbt>

        <recommendation>
          [How to proceed given unresolved conflict — e.g., scenario planning,
           waiting for more data, decision under uncertainty]
        </recommendation>
      </conflict>
    </unresolved_conflicts>

    <conflict_summary>
      <total_conflicts>[N]</total_conflicts>
      <resolved>[N]</resolved>
      <unresolved>[N]</unresolved>
      <resolution_rate>[X%]</resolution_rate>
    </conflict_summary>
  </part_4_contested_claims>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 5: UNCERTAINTY ANALYSIS                                            -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_5_uncertainty_analysis>

    <!-- Epistemic Uncertainty (Can be reduced with more research) -->
    <epistemic_gaps>
      <gap id="EG1">
        <description>[What we don't know but could find out]</description>
        <research_question_affected ref="KQ[N]"/>
        <potential_sources>
          <source>[Where this information might be found]</source>
        </potential_sources>
        <impact_if_resolved>[How knowing would change conclusions]</impact_if_resolved>
        <research_recommendation>
          <action>[Specific research action]</action>
          <estimated_effort>[Time/resource estimate]</estimated_effort>
          <priority>[high|medium|low]</priority>
        </research_recommendation>
      </gap>
      <!-- Additional epistemic gaps -->
    </epistemic_gaps>

    <!-- Aleatory Uncertainty (Cannot be reduced — inherent randomness) -->
    <aleatory_factors>
      <factor id="AF1">
        <description>[Inherently unpredictable element]</description>
        <finding_affected ref="T[X]F[Y]"/>
        <range>
          <low>[Lower bound of plausible range]</low>
          <high>[Upper bound of plausible range]</high>
          <most_likely>[Most likely value if applicable]</most_likely>
        </range>
        <scenarios>
          <scenario probability="[X%]">[Scenario description]</scenario>
          <scenario probability="[X%]">[Scenario description]</scenario>
        </scenarios>
        <monitoring>
          <early_warning>[Signal to watch for]</early_warning>
          <trigger_event>[What would clarify the uncertainty]</trigger_event>
        </monitoring>
      </factor>
      <!-- Additional aleatory factors -->
    </aleatory_factors>

    <!-- Model Uncertainty (Depends on framework/definition choices) -->
    <model_dependencies>
      <dependency id="MD1">
        <finding_affected ref="T[X]F[Y]"/>
        <assumption>[The assumption or framework choice]</assumption>
        <alternatives>
          <alternative name="[Alternative framework]">
            <result>[What result this would give]</result>
            <who_uses>[Who uses this framework]</who_uses>
          </alternative>
        </alternatives>
        <sensitivity>
          [How much conclusions change with different assumptions]
        </sensitivity>
        <chosen_framework>
          <name>[Framework we used]</name>
          <rationale>[Why we chose it]</rationale>
        </chosen_framework>
      </dependency>
      <!-- Additional model dependencies -->
    </model_dependencies>

    <uncertainty_summary>
      <epistemic_count>[N] gaps identified</epistemic_count>
      <aleatory_count>[N] factors identified</aleatory_count>
      <model_count>[N] dependencies identified</model_count>
      <overall_uncertainty_level>[HIGH | MEDIUM | LOW]</overall_uncertainty_level>
    </uncertainty_summary>
  </part_5_uncertainty_analysis>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 6: GAP ANALYSIS                                                    -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_6_gap_analysis>

    <!-- MECE Coverage Audit -->
    <mece_coverage_audit>
      <coverage_matrix>
        <category ref="C1" name="[Category Name]">
          <coverage_status>[complete | partial | missing]</coverage_status>
          <best_evidence_score>[1-5]</best_evidence_score>
          <questions_answered>[X/Y]</questions_answered>
          <gap_details condition_if="[partial|missing]">
            <missing_element>[What's missing]</missing_element>
            <severity>[critical|significant|minor]</severity>
          </gap_details>
        </category>

        <category ref="C2" name="[Category Name]">
          <coverage_status>[status]</coverage_status>
          <best_evidence_score>[score]</best_evidence_score>
          <questions_answered>[X/Y]</questions_answered>
        </category>
        <!-- Repeat for all categories -->
      </coverage_matrix>

      <coverage_score>
        <categories_complete>[N]</categories_complete>
        <categories_partial>[N]</categories_partial>
        <categories_missing>[N]</categories_missing>
        <overall>[X/Y at Score ≥3]</overall>
      </coverage_score>
    </mece_coverage_audit>

    <!-- Unknown Unknowns Identified -->
    <unknown_unknowns_identified>
      <unknown id="UU1" discovered_via="[probe name]">
        <description>[Factor that wasn't in original MECE structure]</description>
        <relevance>[Why this matters to the research question]</relevance>
        <impact>[Potential impact on conclusions]</impact>
        <action_taken>[How it was addressed, or "flagged for future"]</action_taken>
      </unknown>

      <unknown id="UU2" discovered_via="[probe name]">
        <description>[Another discovered factor]</description>
        <relevance>[Why it matters]</relevance>
        <impact>[Potential impact]</impact>
        <action_taken>[Action]</action_taken>
      </unknown>
    </unknown_unknowns_identified>

    <probes_executed>
      <probe name="adjacent_domain" executed="[true|false]">
        <findings_count>[N]</findings_count>
      </probe>
      <probe name="stakeholder_blind_spot" executed="[true|false]">
        <findings_count>[N]</findings_count>
      </probe>
      <probe name="time_horizon" executed="[true|false]">
        <findings_count>[N]</findings_count>
      </probe>
      <probe name="failure_mode" executed="[true|false]">
        <findings_count>[N]</findings_count>
      </probe>
      <probe name="second_order_effects" executed="[true|false]">
        <findings_count>[N]</findings_count>
      </probe>
    </probes_executed>
  </part_6_gap_analysis>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 7: MODEL CONTRIBUTION ANALYSIS                                     -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_7_model_contributions>
    <model_summary>
      <model name="claude-opus-4.5">
        <categories_researched>
          <category ref="C[N]"/>
        </categories_researched>
        <findings_contributed>[N] findings</findings_contributed>
        <tier_distribution>
          <tier_1>[N]</tier_1>
          <tier_2>[N]</tier_2>
          <tier_3>[N]</tier_3>
        </tier_distribution>
        <unique_contributions>
          [What this model provided that others didn't]
        </unique_contributions>
        <limitations_observed>
          [Any notable limitations or gaps in this model's output]
        </limitations_observed>
      </model>

      <model name="gemini-pro-3">
        <categories_researched>
          <category ref="C[N]"/>
        </categories_researched>
        <findings_contributed>[N] findings</findings_contributed>
        <tier_distribution>
          <tier_1>[N]</tier_1>
          <tier_2>[N]</tier_2>
          <tier_3>[N]</tier_3>
        </tier_distribution>
        <unique_contributions>
          [Unique contributions — typically citations, recency]
        </unique_contributions>
        <limitations_observed>
          [Limitations]
        </limitations_observed>
      </model>

      <model name="gpt-5.2-deep">
        <categories_researched>
          <category ref="C[N]"/>
        </categories_researched>
        <findings_contributed>[N] findings</findings_contributed>
        <tier_distribution>
          <tier_1>[N]</tier_1>
          <tier_2>[N]</tier_2>
          <tier_3>[N]</tier_3>
        </tier_distribution>
        <unique_contributions>
          [Unique contributions — typically depth, edge cases]
        </unique_contributions>
        <limitations_observed>
          [Limitations]
        </limitations_observed>
      </model>
    </model_summary>

    <model_agreement_analysis>
      <agreement_rate>[X%] of findings had model agreement</agreement_rate>
      <disagreement_areas>
        <area>[Topic where models disagreed]</area>
      </disagreement_areas>
      <complementarity>
        [Assessment of how well model strengths complemented each other]
      </complementarity>
    </model_agreement_analysis>
  </part_7_model_contributions>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 8: DECISION SUPPORT                                                -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_8_decision_support>

    <decision_tree>
      <node id="D1" type="decision">
        <question>[Primary decision question]</question>

        <branch condition="IF [condition based on findings]">
          <recommendation>[Recommended action]</recommendation>
          <confidence>[Confidence in this path]</confidence>
          <supporting_findings>
            <finding ref="T[X]F[Y]"/>
          </supporting_findings>
        </branch>

        <branch condition="IF [alternative condition]">
          <recommendation>[Alternative recommended action]</recommendation>
          <confidence>[Confidence]</confidence>
          <supporting_findings>
            <finding ref="T[X]F[Y]"/>
          </supporting_findings>
        </branch>

        <branch condition="IF [another condition]">
          <node id="D1.1" type="decision">
            <question>[Sub-decision question]</question>
            <branch condition="IF [sub-condition]">
              <recommendation>[Recommendation]</recommendation>
            </branch>
            <branch condition="IF [sub-condition]">
              <recommendation>[Recommendation]</recommendation>
            </branch>
          </node>
        </branch>

        <branch condition="ELSE (insufficient evidence)">
          <recommendation>Defer decision pending [specific additional research]</recommendation>
          <required_evidence>
            <evidence>[What evidence would enable decision]</evidence>
          </required_evidence>
        </branch>
      </node>
    </decision_tree>

    <scenario_recommendations>
      <scenario name="[Scenario Name]" probability="[X%]">
        <description>[Scenario description]</description>
        <recommended_action>[What to do in this scenario]</recommended_action>
        <trigger_indicators>
          <indicator>[How to know this scenario is emerging]</indicator>
        </trigger_indicators>
      </scenario>
    </scenario_recommendations>

    <next_steps>
      <immediate>
        <action priority="1">[First action to take]</action>
        <action priority="2">[Second action]</action>
      </immediate>
      <near_term>
        <action>[Actions for next 30-90 days]</action>
      </near_term>
      <contingent>
        <action trigger="[What triggers this]">[Contingent action]</action>
      </contingent>
    </next_steps>
  </part_8_decision_support>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 9: KILL CRITERIA                                                   -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_9_kill_criteria>
    <purpose>
      Conditions that would invalidate this research and require re-investigation
    </purpose>

    <kill_criteria>
      <criterion id="KC1" type="[data_staleness | assumption_failure | market_shift | regulatory_change]">
        <condition>
          [Specific condition that would invalidate research]
        </condition>
        <monitoring>
          <check_frequency>[How often to check]</check_frequency>
          <check_method>[How to verify]</check_method>
        </monitoring>
        <trigger_action>
          [What to do if criterion triggers]
        </trigger_action>
      </criterion>

      <criterion id="KC2" type="[type]">
        <condition>[Invalidation condition]</condition>
        <monitoring>
          <check_frequency>[Frequency]</check_frequency>
          <check_method>[Method]</check_method>
        </monitoring>
        <trigger_action>[Action]</trigger_action>
      </criterion>
    </kill_criteria>

    <validity_window>
      <valid_from>[Date research becomes valid]</valid_from>
      <valid_until>[Date research should be refreshed]</valid_until>
      <rationale>[Why this validity window]</rationale>
    </validity_window>
  </part_9_kill_criteria>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 10: METHODOLOGY TRANSPARENCY                                       -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_10_methodology>
    <research_approach>
      <description>[Overall methodology description]</description>
      <decomposition_pattern>[market | competitive | technology | strategic]</decomposition_pattern>
      <execution_mode>[parallel | sequential | convergent]</execution_mode>
    </research_approach>

    <models_and_prompts>
      <model name="[model]">
        <prompt_summary>[Brief description of what was asked]</prompt_summary>
        <prompt_id ref="PROMPT-[ID]"/>
        <execution_date>[When prompt was run]</execution_date>
        <tokens_used>[Input + output tokens]</tokens_used>
      </model>
    </models_and_prompts>

    <consolidation_method>
      <approach>[triangulation | weighted_synthesis | hierarchical | dialectical]</approach>
      <conflict_resolution>[How conflicts were resolved]</conflict_resolution>
      <confidence_calculation>[How confidence scores were determined]</confidence_calculation>
    </consolidation_method>

    <verification_performed>
      <verification type="[cross_reference | primary_source | expert_review]">
        <scope>[What was verified]</scope>
        <result>[Outcome of verification]</result>
      </verification>
    </verification_performed>

    <limitations>
      <limitation type="[scope | data | methodology | time]">
        [Description of limitation and how it affects conclusions]
      </limitation>
    </limitations>

    <reproducibility>
      <can_reproduce>[true | false | partial]</can_reproduce>
      <reproduction_requirements>
        [What would be needed to reproduce this research]
      </reproduction_requirements>
    </reproducibility>
  </part_10_methodology>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- PART 11: APPENDICES                                                     -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <part_11_appendices>

    <appendix_a_raw_findings>
      <model_output model="claude-opus-4.5">
        <!-- Full model output or reference to stored output -->
        <output_ref>[Link or file reference to full output]</output_ref>
        <summary>[Brief summary of what model produced]</summary>
      </model_output>

      <model_output model="gemini-pro-3">
        <output_ref>[Reference]</output_ref>
        <summary>[Summary]</summary>
      </model_output>

      <model_output model="gpt-5.2-deep">
        <output_ref>[Reference]</output_ref>
        <summary>[Summary]</summary>
      </model_output>
    </appendix_a_raw_findings>

    <appendix_b_source_list>
      <sources>
        <source id="S[N]" score="[1-5]">
          <citation>[Full citation]</citation>
          <url>[URL if applicable]</url>
          <access_date>[When accessed]</access_date>
          <used_in_findings>
            <finding ref="T[X]F[Y]"/>
          </used_in_findings>
        </source>
        <!-- Additional sources -->
      </sources>
    </appendix_b_source_list>

    <appendix_c_prompts_used>
      <prompt id="PROMPT-CLAUDE">
        <full_text><![CDATA[
          [Complete prompt text used]
        ]]></full_text>
      </prompt>

      <prompt id="PROMPT-GEMINI">
        <full_text><![CDATA[
          [Complete prompt text used]
        ]]></full_text>
      </prompt>

      <prompt id="PROMPT-GPT">
        <full_text><![CDATA[
          [Complete prompt text used]
        ]]></full_text>
      </prompt>
    </appendix_c_prompts_used>

    <appendix_d_data_tables>
      <!-- Any structured data tables referenced in findings -->
      <table id="T[N]" name="[Table Name]">
        <description>[What this table shows]</description>
        <data_ref>[Reference to data or inline data]</data_ref>
      </table>
    </appendix_d_data_tables>

    <appendix_e_hypothesis_analysis include_if="hypothesis_mode">
      <!-- Detailed hypothesis probability updates -->
      <hypothesis ref="H1">
        <prior>[X%]</prior>
        <posterior>[Y%]</posterior>
        <evidence_impact>
          <supporting_evidence_found>[N items]</supporting_evidence_found>
          <refuting_evidence_found>[N items]</refuting_evidence_found>
        </evidence_impact>
        <conclusion>[Assessment of hypothesis]</conclusion>
      </hypothesis>
    </appendix_e_hypothesis_analysis>
  </part_11_appendices>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- CRITICAL CONSTRAINTS (PLACED AT END FOR CONTEXT RETENTION)              -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->

  <critical_constraints>
    <!--
    IMPORTANT: These constraints are placed at the end of the document to ensure
    they remain in active context when generating or reviewing the report.

    LLMs tend to compress/summarize earlier content while retaining recent content
    in full. Placing critical constraints here ensures they are "loaded" when
    making final assessments.
    -->

    <constraint id="CC1" severity="absolute">
      <rule>Never state conclusions with more confidence than evidence supports</rule>
      <application>
        - Tier 1 findings only if evidence score ≥ 4 AND model agreement
        - Tier 2 for score 3-4 with caveats
        - Tier 3 for score ≤ 2 or significant disagreement
      </application>
    </constraint>

    <constraint id="CC2" severity="absolute">
      <rule>All contested claims must be surfaced, not buried</rule>
      <application>
        - Conflicts in Part 4, not hidden in appendices
        - WWHTBT required for unresolved conflicts
        - Executive summary must reference major disagreements
      </application>
    </constraint>

    <constraint id="CC3" severity="absolute">
      <rule>Distinguish uncertainty types explicitly</rule>
      <application>
        - Epistemic: "We don't know but could find out"
        - Aleatory: "Cannot be known — inherently uncertain"
        - Model: "Depends on framework/definition choice"
        - Part 5 must classify all significant uncertainties
      </application>
    </constraint>

    <constraint id="CC4" severity="absolute">
      <rule>Evidence scores must use the 5-point rubric consistently</rule>
      <application>
        - Score 5: Primary source only
        - Score 4: Major analyst with citations
        - Score 3: Credible secondary
        - Score 2: Weak secondary, outdated, or anonymous
        - Score 1: Speculative, no verifiable basis
        - Apply time decay for outdated sources
      </application>
    </constraint>

    <constraint id="CC5" severity="absolute">
      <rule>Gap analysis must be complete</rule>
      <application>
        - MECE coverage audit in Part 6
        - All 5 unknown unknowns probes executed (or explicitly skipped with rationale)
        - Critical gaps flagged in executive summary caveats
      </application>
    </constraint>

    <constraint id="CC6" severity="absolute">
      <rule>Decision support must be actionable</rule>
      <application>
        - Decision tree with concrete if-then branches
        - Kill criteria with monitoring plans
        - Clear next steps with priorities
      </application>
    </constraint>

    <constraint id="CC7" severity="strong">
      <rule>Methodology must be reproducible</rule>
      <application>
        - Full prompts in Appendix C
        - Source list with access dates
        - Consolidation method documented
      </application>
    </constraint>

    <verification_checklist>
      <check>[ ] Confidence tiers match evidence quality</check>
      <check>[ ] All conflicts surfaced and addressed</check>
      <check>[ ] Uncertainty types correctly classified</check>
      <check>[ ] Evidence scores applied consistently</check>
      <check>[ ] Gap analysis complete</check>
      <check>[ ] Decision support is actionable</check>
      <check>[ ] Methodology documented for reproducibility</check>
      <check>[ ] Kill criteria defined with monitoring</check>
      <check>[ ] Executive summary accurately reflects body</check>
      <check>[ ] All key questions from brief addressed</check>
    </verification_checklist>
  </critical_constraints>

</consolidated_report>
```

---

## Usage Instructions

### 1. Generating a Consolidated Report

1. **Gather model outputs** from research brief execution
2. **Apply evidence rubric** to score all sources (see `evidence-strength-rubric.md`)
3. **Classify uncertainties** using taxonomy (see `uncertainty-taxonomy.md`)
4. **Run gap analysis** protocol (see `gap-analysis-protocol.md`)
5. **Synthesize findings** into tiered structure
6. **Resolve conflicts** with WWHTBT for unresolved
7. **Build decision tree** based on findings
8. **Define kill criteria** for validity monitoring
9. **Complete appendices** for transparency
10. **Verify against constraints** (end of template)

### 2. Tier Assignment Guidelines

| Tier | Confidence | Evidence Requirement | Model Agreement |
|------|------------|---------------------|-----------------|
| 1 | >75% | Score 4+ average, no critical findings below 3 | Required |
| 2 | 50-75% | Score 3+ average, caveats documented | Partial OK |
| 3 | <50% | Below Score 3 OR significant conflict | Not required |

### 3. Critical Constraints Placement

The Critical Constraints section is **intentionally placed at the end** of the template. This ensures:
- Constraints remain in active LLM context during generation
- Verification checklist is "fresh" when finalizing
- Reduces risk of constraint violations through context compression

**Do not move Critical Constraints earlier in the template.**

---

## Validation Checklist

Before finalizing consolidated report:

```
[ ] Header accurately summarizes quality metrics
[ ] Executive summary has ≤5 numbered findings
[ ] All findings have confidence scores and evidence basis
[ ] Conflicts are in Part 4, not hidden elsewhere
[ ] WWHTBT provided for unresolved conflicts
[ ] All three uncertainty types addressed in Part 5
[ ] MECE coverage audit complete in Part 6
[ ] At least 3 unknown unknowns probes executed
[ ] Decision tree has concrete if-then structure
[ ] Kill criteria have monitoring plans
[ ] Methodology enables reproduction
[ ] Appendices contain full prompts and sources
[ ] Critical constraints verification checklist passed
```
