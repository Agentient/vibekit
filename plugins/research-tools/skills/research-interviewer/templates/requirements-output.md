# Requirements Output Template

CONTRACT-01 compliant template for structured requirements artifacts including job stories, acceptance criteria, and functional/non-functional requirements.

---

## Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<requirements contract="CONTRACT-01" version="1.0">

  <metadata>
    <artifact_id>REQ-[YYYY-MM-DD]-[5-char-hash]</artifact_id>
    <contract_type>REQUIREMENTS</contract_type>
    <created_at>[ISO 8601 timestamp]</created_at>
    <created_by>research-interviewer</created_by>
    <confidence>[0.0-1.0]</confidence>
    <provenance>
      <source>interview</source>
      <source_artifact>[PS-YYYY-MM-DD-hash or KB-YYYY-MM-DD-hash]</source_artifact>
      <interview_goal>[Goal from Phase 1]</interview_goal>
      <interviewee_role>[Role/title of primary interviewee]</interviewee_role>
      <interview_date>[ISO 8601 date]</interview_date>
      <interview_turns>[Total conversation turns]</interview_turns>
      <validation_mode>[empathetic|balanced|rigorous]</validation_mode>
    </provenance>
  </metadata>

  <stakeholder_context>
    <stakeholder id="SH1" type="primary">
      <role>[Role/title]</role>
      <name>[Name if available]</name>
      <goals>
        <goal priority="[high|medium|low]">[Stakeholder goal]</goal>
        <!-- Additional goals -->
      </goals>
      <pain_points>
        <pain_point severity="[critical|significant|minor]">[Pain point description]</pain_point>
        <!-- Additional pain points -->
      </pain_points>
      <success_definition>[What success looks like for this stakeholder]</success_definition>
    </stakeholder>
    <stakeholder id="SH2" type="secondary">
      <!-- Same structure -->
    </stakeholder>
    <!-- Additional stakeholders -->
  </stakeholder_context>

  <job_stories>
    <job_story id="JS1" priority="[must_have|should_have|could_have|wont_have]"
               stakeholder_ref="[SH1]" confidence="[0.0-1.0]">
      <situation>[When/context - specific trigger or circumstance]</situation>
      <motivation>[What the user wants to do - the job]</motivation>
      <outcome>[Desired result/benefit - expected value]</outcome>
      <acceptance_criteria>
        <criterion id="AC1" format="gherkin">
          <given>[Initial context/state]</given>
          <when>[Action or trigger]</when>
          <then>[Expected outcome]</then>
        </criterion>
        <criterion id="AC2" format="gherkin">
          <!-- Additional criteria -->
        </criterion>
      </acceptance_criteria>
      <edge_cases>
        <edge_case id="EC1" likelihood="[common|occasional|rare]">
          <scenario>[Edge case description]</scenario>
          <expected_behavior>[How system should handle it]</expected_behavior>
        </edge_case>
        <!-- Additional edge cases -->
      </edge_cases>
    </job_story>
    <!-- Additional job stories -->
  </job_stories>

  <functional_requirements>
    <requirement id="FR1" priority="[must_have|should_have|could_have|wont_have]"
                 job_story_ref="[JS1]" confidence="[0.0-1.0]">
      <description>[What the system must do]</description>
      <rationale>[Why this requirement exists]</rationale>
      <acceptance_criteria>
        <criterion id="FR1-AC1" format="gherkin">
          <given>[Initial context/state]</given>
          <when>[Action or trigger]</when>
          <then>[Expected outcome]</then>
        </criterion>
      </acceptance_criteria>
      <dependencies>
        <dependency type="[requires|extends|conflicts]" ref="[FR2]">[Relationship description]</dependency>
      </dependencies>
    </requirement>
    <!-- Additional functional requirements -->
  </functional_requirements>

  <non_functional_requirements>
    <category name="Performance">
      <requirement id="NFR-P1" priority="[must_have|should_have|could_have|wont_have]"
                   confidence="[0.0-1.0]">
        <description>[Performance requirement]</description>
        <metric>[Measurable metric]</metric>
        <target>[Target value]</target>
        <measurement_method>[How to measure]</measurement_method>
      </requirement>
      <!-- Additional performance requirements -->
    </category>
    <category name="Security">
      <requirement id="NFR-S1" priority="[must_have|should_have|could_have|wont_have]"
                   confidence="[0.0-1.0]">
        <description>[Security requirement]</description>
        <compliance>[Compliance standards if applicable]</compliance>
        <verification_method>[How to verify]</verification_method>
      </requirement>
      <!-- Additional security requirements -->
    </category>
    <category name="Usability">
      <requirement id="NFR-U1" priority="[must_have|should_have|could_have|wont_have]"
                   confidence="[0.0-1.0]">
        <description>[Usability requirement]</description>
        <user_segment>[Target user segment]</user_segment>
        <success_criteria>[How to measure success]</success_criteria>
      </requirement>
      <!-- Additional usability requirements -->
    </category>
    <category name="Reliability">
      <requirement id="NFR-R1" priority="[must_have|should_have|could_have|wont_have]"
                   confidence="[0.0-1.0]">
        <description>[Reliability requirement]</description>
        <metric>[Measurable metric]</metric>
        <target>[Target value]</target>
      </requirement>
      <!-- Additional reliability requirements -->
    </category>
    <category name="Scalability">
      <requirement id="NFR-SC1" priority="[must_have|should_have|could_have|wont_have]"
                   confidence="[0.0-1.0]">
        <description>[Scalability requirement]</description>
        <current_baseline>[Current capacity]</current_baseline>
        <target_capacity>[Target capacity]</target_capacity>
        <growth_assumption>[Expected growth rate]</growth_assumption>
      </requirement>
      <!-- Additional scalability requirements -->
    </category>
    <category name="Maintainability">
      <requirement id="NFR-M1" priority="[must_have|should_have|could_have|wont_have]"
                   confidence="[0.0-1.0]">
        <description>[Maintainability requirement]</description>
        <rationale>[Why this matters]</rationale>
      </requirement>
      <!-- Additional maintainability requirements -->
    </category>
    <!-- Additional NFR categories as needed -->
  </non_functional_requirements>

  <constraints>
    <constraint id="CON1" type="[technical|business|regulatory|resource|temporal]"
                negotiable="[true|false]">
      <description>[Constraint description]</description>
      <impact>[What this constrains]</impact>
      <source>[Who/what imposed this constraint]</source>
    </constraint>
    <!-- Additional constraints -->
  </constraints>

  <dependencies>
    <dependency id="DEP1" type="[internal|external|data|system]">
      <description>[Dependency description]</description>
      <owner>[Who owns the dependency]</owner>
      <status>[available|planned|at_risk|blocked]</status>
      <requirements_affected>
        <ref>[FR1]</ref>
        <ref>[NFR-P1]</ref>
      </requirements_affected>
      <mitigation>[Risk mitigation if status is at_risk or blocked]</mitigation>
    </dependency>
    <!-- Additional dependencies -->
  </dependencies>

  <assumptions>
    <assumption id="A1" type="[explicit|implicit|structural]"
                validated="[true|false]" confidence="[0.0-1.0]"
                impact="[high|medium|low]">
      <statement>[Assumption text]</statement>
      <implications>[What depends on this being true]</implications>
      <validation_approach>[How to validate]</validation_approach>
      <requirements_affected>
        <ref>[FR1]</ref>
        <ref>[JS2]</ref>
      </requirements_affected>
    </assumption>
    <!-- Additional assumptions -->
  </assumptions>

  <traceability>
    <trace_matrix>
      <trace job_story="JS1" functional_requirements="FR1,FR2" nfr="NFR-P1,NFR-S1"
             acceptance_criteria="AC1,AC2,FR1-AC1" constraints="CON1"/>
      <trace job_story="JS2" functional_requirements="FR3" nfr="NFR-U1"
             acceptance_criteria="AC3,FR3-AC1" constraints="CON2"/>
      <!-- Additional traces -->
    </trace_matrix>
    <orphan_check>
      <orphaned_requirements>
        <!-- List any requirements not traced to job stories -->
      </orphaned_requirements>
      <unmet_job_stories>
        <!-- List any job stories without implementing requirements -->
      </unmet_job_stories>
    </orphan_check>
  </traceability>

  <coverage_assessment>
    <mece_coverage>
      <dimension name="[MECE Dimension 1]" coverage="[complete|partial|minimal]"
                 confidence="[0.0-1.0]">
        <requirements_count>[N]</requirements_count>
        <gap_notes>[Any coverage gaps]</gap_notes>
      </dimension>
      <!-- Additional dimensions -->
    </mece_coverage>
    <priority_distribution>
      <must_have count="[N]" percentage="[%]"/>
      <should_have count="[N]" percentage="[%]"/>
      <could_have count="[N]" percentage="[%]"/>
      <wont_have count="[N]" percentage="[%]"/>
    </priority_distribution>
    <confidence_summary>
      <average_confidence>[0.0-1.0]</average_confidence>
      <low_confidence_items>
        <item ref="[FR3]" confidence="[0.0-1.0]" reason="[Why low confidence]"/>
        <!-- Additional low confidence items -->
      </low_confidence_items>
    </confidence_summary>
    <validation_needed>
      <item ref="[A1]" priority="[high|medium|low]">[What needs validation]</item>
      <!-- Additional validation items -->
    </validation_needed>
  </coverage_assessment>

</requirements>
```

---

## Field Documentation

### metadata

| Field | Description | Example |
|-------|-------------|---------|
| `artifact_id` | Unique identifier | REQ-2025-01-15-b7c3d |
| `contract_type` | Must be `REQUIREMENTS` | REQUIREMENTS |
| `confidence` | Overall artifact confidence | 0.78 |
| `source_artifact` | Reference to source artifact | PS-2025-01-14-a3f2b |
| `interviewee_role` | Primary interviewee's role | Product Owner |
| `validation_mode` | Interview validation intensity | empathetic |

### stakeholder_context

| Field | Description | Values |
|-------|-------------|--------|
| `type` | Stakeholder classification | primary, secondary, tertiary |
| `goals.priority` | Goal importance | high, medium, low |
| `pain_points.severity` | Pain point impact | critical, significant, minor |
| `success_definition` | What success looks like | Free-form text |

### job_stories

Jobs-To-Be-Done format capturing user needs in context.

| Field | Description | Notes |
|-------|-------------|-------|
| `situation` | When/context | Specific trigger or circumstance |
| `motivation` | What user wants | The job to be done |
| `outcome` | Desired result | Expected value/benefit |
| `stakeholder_ref` | Links to stakeholder | SH1, SH2, etc. |
| `priority` | MoSCoW classification | See Priority Classification |

### acceptance_criteria

Gherkin-format criteria for testability.

| Field | Description | Example |
|-------|-------------|---------|
| `given` | Initial context/state | "Given a logged-in user with items in cart" |
| `when` | Action or trigger | "When the user clicks checkout" |
| `then` | Expected outcome | "Then the payment form is displayed" |

### functional_requirements

| Field | Description | Notes |
|-------|-------------|-------|
| `description` | What system must do | Specific, testable |
| `rationale` | Why this exists | Business justification |
| `job_story_ref` | Traces to job story | JS1, JS2, etc. |
| `dependencies.type` | Relationship type | requires, extends, conflicts |

### non_functional_requirements

| Category | Typical Metrics | Examples |
|----------|-----------------|----------|
| **Performance** | Response time, throughput | "Page load < 2 seconds" |
| **Security** | Compliance, encryption | "PCI-DSS Level 1 compliance" |
| **Usability** | Task completion, error rate | "95% task success rate" |
| **Reliability** | Uptime, MTBF | "99.9% availability" |
| **Scalability** | Concurrent users, data volume | "Support 10,000 concurrent users" |
| **Maintainability** | Code coverage, documentation | "80% test coverage" |

### constraints

| Type | Description | Examples |
|------|-------------|----------|
| `technical` | Technology limitations | "Must use existing Stripe integration" |
| `business` | Business rules/limits | "Budget capped at $50K" |
| `regulatory` | Compliance requirements | "GDPR data residency" |
| `resource` | Team/capacity limits | "2 developers available" |
| `temporal` | Time constraints | "Must launch before Q3" |

### dependencies

| Type | Description | Risk Level |
|------|-------------|------------|
| `internal` | Within organization | Usually lower risk |
| `external` | Third-party systems | Higher risk, less control |
| `data` | Data availability | Validate early |
| `system` | System integrations | Interface contracts needed |

| Status | Meaning | Action |
|--------|---------|--------|
| `available` | Ready to use | Proceed |
| `planned` | Scheduled but not ready | Track timeline |
| `at_risk` | May not be available | Develop mitigation |
| `blocked` | Currently unavailable | Escalate or redesign |

### assumptions

| Field | Description | Notes |
|-------|-------------|-------|
| `type` | Assumption category | explicit, implicit, structural |
| `validated` | Has been verified | true, false |
| `impact` | Consequence if wrong | high, medium, low |
| `validation_approach` | How to verify | Specific method |

### traceability

| Element | Purpose | Content |
|---------|---------|---------|
| `trace_matrix` | Links artifacts | Job stories → Requirements → Criteria |
| `orphan_check` | Finds gaps | Unlinked requirements or stories |

### coverage_assessment

| Field | Purpose | Values |
|-------|---------|--------|
| `mece_coverage` | Dimension completeness | complete, partial, minimal |
| `priority_distribution` | MoSCoW balance | Count and percentage |
| `confidence_summary` | Quality indicator | Average and low-confidence items |

---

## Gherkin Format Guidance

### Structure

Acceptance criteria use Given/When/Then format for clarity and testability:

```gherkin
Given [initial context or state]
When [action or trigger event]
Then [expected outcome or result]
```

### Writing Effective Criteria

**Good Criteria Are:**
- **Specific**: Describe exact conditions and outcomes
- **Testable**: Can be verified programmatically
- **Independent**: Don't rely on other criteria
- **Complete**: Cover the full scenario

**Examples:**

```gherkin
# ✅ GOOD - Specific and testable
Given a customer with 3 items totaling $75 in cart
When the customer applies coupon code "SAVE10"
Then the cart total is reduced by $7.50
And the coupon code appears in the order summary

# ❌ BAD - Vague and untestable
Given a customer with items
When they use a coupon
Then they get a discount
```

### Multiple Outcomes

Use `And` for additional outcomes:

```gherkin
Given a user on the login page
When the user enters valid credentials
Then the user is redirected to the dashboard
And a success message is displayed
And the session timeout is set to 30 minutes
```

### Negative Scenarios

Include criteria for error conditions:

```gherkin
Given a user on the login page
When the user enters an invalid password
Then an error message "Invalid credentials" is displayed
And the login attempt count is incremented
And the password field is cleared
```

### Edge Cases

Document edge cases with dedicated criteria:

```gherkin
# Edge case: Empty cart checkout attempt
Given a customer with an empty cart
When the customer clicks the checkout button
Then the checkout button is disabled
And a message "Add items to checkout" is displayed
```

### Anti-Patterns to Avoid

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| "User can do X" | Not testable | Specify trigger and outcome |
| Multiple Whens | Unclear causality | One When per criterion |
| Implementation details | Couples to solution | Focus on behavior |
| "System should" | Vague | Specific outcome |
| No Given context | Missing preconditions | Always specify state |

---

## Priority Classification (MoSCoW)

### Must Have

**Definition:** Requirements without which the product has no value. Failure to deliver means project failure.

**Characteristics:**
- Core functionality that defines the product
- Legal or regulatory requirements
- Safety-critical features
- No workaround exists

**Test:** "Would stakeholders accept the product without this?" If no, it's Must Have.

**Target:** 60% or less of total requirements

### Should Have

**Definition:** Important requirements that add significant value but have workarounds.

**Characteristics:**
- High-value features
- Efficiency improvements
- Strong user demand
- Workarounds exist but are painful

**Test:** "Would stakeholders be dissatisfied without this?" If yes, it's Should Have.

**Target:** 20-30% of total requirements

### Could Have

**Definition:** Desirable requirements that enhance the product if time/budget permits.

**Characteristics:**
- Nice-to-have features
- Convenience improvements
- Lower user demand
- Easy workarounds exist

**Test:** "Would this delight users but not disappoint if missing?" If yes, it's Could Have.

**Target:** 10-20% of total requirements

### Won't Have (This Time)

**Definition:** Requirements explicitly out of scope for this release but may be considered later.

**Characteristics:**
- Deferred features
- Future enhancements
- Scope exclusions
- "Phase 2" items

**Purpose:** Prevents scope creep by documenting what was consciously excluded.

### Priority Decision Matrix

| User Impact | Business Impact | Workaround? | Priority |
|-------------|-----------------|-------------|----------|
| High | High | No | Must Have |
| High | High | Yes | Should Have |
| High | Low | Any | Should Have |
| Low | High | No | Should Have |
| Low | High | Yes | Could Have |
| Low | Low | Any | Could Have |
| Any | Any | Deferred | Won't Have |

---

## Traceability Best Practices

### Why Traceability Matters

1. **Impact Analysis**: Understanding change ripple effects
2. **Coverage Verification**: Ensuring all needs are addressed
3. **Gap Detection**: Finding orphaned artifacts
4. **Accountability**: Knowing why requirements exist

### Traceability Chain

```
Stakeholder → Job Story → Functional Req → Acceptance Criteria
                ↓              ↓
            Constraints    NFR → Verification Method
                ↓
            Assumptions → Validation Approach
```

### Forward Traceability

From need to implementation:

| From | To | Purpose |
|------|----|---------|
| Job Story | Functional Requirement | Ensures needs become features |
| Functional Requirement | Acceptance Criteria | Ensures testability |
| Constraint | Affected Requirements | Shows constraint impact |

### Backward Traceability

From implementation to need:

| From | To | Purpose |
|------|----|---------|
| Acceptance Criteria | Functional Requirement | Verifies criteria necessity |
| Functional Requirement | Job Story | Validates business justification |
| NFR | Business Driver | Confirms technical necessity |

### Coverage Validation

**Complete Coverage:** Every job story has implementing requirements.

```xml
<trace job_story="JS1" functional_requirements="FR1,FR2" />
```

**Gap Detection:** Orphan check identifies:
- Requirements without job stories (may be gold-plating)
- Job stories without requirements (unmet needs)

```xml
<orphan_check>
  <orphaned_requirements>
    <ref>FR7</ref> <!-- Needs justification or removal -->
  </orphaned_requirements>
  <unmet_job_stories>
    <ref>JS4</ref> <!-- Needs implementing requirements -->
  </unmet_job_stories>
</orphan_check>
```

### Traceability Matrix Format

Compact format linking all artifact types:

```xml
<trace job_story="JS1"
       functional_requirements="FR1,FR2"
       nfr="NFR-P1,NFR-S1"
       acceptance_criteria="AC1,AC2,FR1-AC1"
       constraints="CON1"
       assumptions="A1"/>
```

---

## Validation Rules (CONTRACT-01 Compliance)

### Required Elements

- `artifact_id` must match pattern: `REQ-YYYY-MM-DD-[5-char-hash]`
- `contract_type` must be `REQUIREMENTS`
- `confidence` must be in range 0.0-1.0
- At least one `job_story` must be present
- At least one `functional_requirement` must be present

### Structural Rules

- All `job_story` elements must have `id`, `priority`, `stakeholder_ref`, `confidence` attributes
- All `requirement` elements must have `id`, `priority`, `confidence` attributes
- `priority` values must be one of: must_have, should_have, could_have, wont_have
- All acceptance criteria must have `id` and `format` attributes
- Gherkin criteria must have `given`, `when`, `then` elements

### Semantic Rules

- Every `job_story_ref` must reference a valid job story ID
- Every `stakeholder_ref` must reference a valid stakeholder ID
- Traceability matrix must include all job stories
- No orphaned functional requirements (all must trace to job stories)
- Low confidence items (< 0.6) should appear in `validation_needed`

---

## Example Output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<requirements contract="CONTRACT-01" version="1.0">

  <metadata>
    <artifact_id>REQ-2025-01-16-b7c3d</artifact_id>
    <contract_type>REQUIREMENTS</contract_type>
    <created_at>2025-01-16T10:30:00Z</created_at>
    <created_by>research-interviewer</created_by>
    <confidence>0.82</confidence>
    <provenance>
      <source>interview</source>
      <source_artifact>PS-2025-01-15-a3f2b</source_artifact>
      <interview_goal>Define checkout improvement requirements</interview_goal>
      <interviewee_role>Product Owner</interviewee_role>
      <interview_date>2025-01-16</interview_date>
      <interview_turns>38</interview_turns>
      <validation_mode>empathetic</validation_mode>
    </provenance>
  </metadata>

  <stakeholder_context>
    <stakeholder id="SH1" type="primary">
      <role>End Customer</role>
      <name>First-time buyer segment</name>
      <goals>
        <goal priority="high">Complete purchase quickly and securely</goal>
        <goal priority="medium">Understand total cost before committing</goal>
      </goals>
      <pain_points>
        <pain_point severity="critical">Abandons checkout when payment feels unsafe</pain_point>
        <pain_point severity="significant">Frustrated by too many form fields</pain_point>
      </pain_points>
      <success_definition>Completes checkout in under 2 minutes with confidence</success_definition>
    </stakeholder>
    <stakeholder id="SH2" type="primary">
      <role>Product Manager</role>
      <name>Sarah Chen</name>
      <goals>
        <goal priority="high">Reduce checkout abandonment rate</goal>
        <goal priority="high">Increase conversion rate by 15%</goal>
      </goals>
      <pain_points>
        <pain_point severity="critical">48% abandonment at payment step</pain_point>
      </pain_points>
      <success_definition>Abandonment rate below 35%</success_definition>
    </stakeholder>
    <stakeholder id="SH3" type="secondary">
      <role>Engineering Lead</role>
      <name>Payment team</name>
      <goals>
        <goal priority="high">Maintain PCI compliance</goal>
        <goal priority="medium">Minimize integration complexity</goal>
      </goals>
      <pain_points>
        <pain_point severity="significant">Legacy payment code is brittle</pain_point>
      </pain_points>
      <success_definition>Zero security incidents, clean audit</success_definition>
    </stakeholder>
  </stakeholder_context>

  <job_stories>
    <job_story id="JS1" priority="must_have" stakeholder_ref="SH1" confidence="0.90">
      <situation>When I have items in my cart and am ready to purchase</situation>
      <motivation>I want to complete payment quickly with confidence my data is secure</motivation>
      <outcome>So that I receive my items without anxiety about fraud or complications</outcome>
      <acceptance_criteria>
        <criterion id="JS1-AC1" format="gherkin">
          <given>A customer with items totaling $50+ in cart</given>
          <when>The customer clicks the checkout button</when>
          <then>The checkout flow loads within 2 seconds</then>
        </criterion>
        <criterion id="JS1-AC2" format="gherkin">
          <given>A customer on the payment step</given>
          <when>The customer views the payment form</when>
          <then>Security badges (SSL, PCI) are visible above the fold</then>
        </criterion>
        <criterion id="JS1-AC3" format="gherkin">
          <given>A customer who has entered valid payment details</given>
          <when>The customer submits the payment</when>
          <then>A confirmation message appears within 3 seconds</then>
        </criterion>
      </acceptance_criteria>
      <edge_cases>
        <edge_case id="JS1-EC1" likelihood="occasional">
          <scenario>Payment processor timeout</scenario>
          <expected_behavior>Display friendly error with retry option, preserve cart</expected_behavior>
        </edge_case>
        <edge_case id="JS1-EC2" likelihood="rare">
          <scenario>Session expires mid-checkout</scenario>
          <expected_behavior>Prompt login, restore cart and checkout state</expected_behavior>
        </edge_case>
      </edge_cases>
    </job_story>

    <job_story id="JS2" priority="should_have" stakeholder_ref="SH1" confidence="0.85">
      <situation>When I want to make a quick purchase without creating an account</situation>
      <motivation>I want to checkout as a guest</motivation>
      <outcome>So that I can complete my purchase without the friction of registration</outcome>
      <acceptance_criteria>
        <criterion id="JS2-AC1" format="gherkin">
          <given>A customer on the checkout page</given>
          <when>The customer chooses to checkout</when>
          <then>A "Continue as Guest" option is prominently displayed</then>
        </criterion>
        <criterion id="JS2-AC2" format="gherkin">
          <given>A customer checking out as guest</given>
          <when>The customer completes the purchase</when>
          <then>An option to create an account is offered post-purchase</then>
        </criterion>
      </acceptance_criteria>
      <edge_cases>
        <edge_case id="JS2-EC1" likelihood="common">
          <scenario>Guest tries to view order history</scenario>
          <expected_behavior>Prompt to create account or use order lookup by email</expected_behavior>
        </edge_case>
      </edge_cases>
    </job_story>

    <job_story id="JS3" priority="must_have" stakeholder_ref="SH2" confidence="0.88">
      <situation>When analyzing checkout performance</situation>
      <motivation>I want to see real-time abandonment metrics by checkout step</motivation>
      <outcome>So that I can identify and address friction points quickly</outcome>
      <acceptance_criteria>
        <criterion id="JS3-AC1" format="gherkin">
          <given>A product manager logged into the analytics dashboard</given>
          <when>The PM views the checkout funnel report</when>
          <then>Drop-off rates are shown for each checkout step</then>
        </criterion>
      </acceptance_criteria>
      <edge_cases/>
    </job_story>
  </job_stories>

  <functional_requirements>
    <requirement id="FR1" priority="must_have" job_story_ref="JS1" confidence="0.92">
      <description>The checkout page shall load all elements within 2 seconds on 3G connection</description>
      <rationale>Slow page loads are the #1 cause of checkout abandonment</rationale>
      <acceptance_criteria>
        <criterion id="FR1-AC1" format="gherkin">
          <given>A customer on a 3G mobile connection</given>
          <when>The customer navigates to checkout</when>
          <then>Time to interactive is under 2 seconds</then>
        </criterion>
      </acceptance_criteria>
      <dependencies/>
    </requirement>

    <requirement id="FR2" priority="must_have" job_story_ref="JS1" confidence="0.95">
      <description>The system shall display PCI-DSS compliance badge and SSL indicator on payment form</description>
      <rationale>Trust signals reduce abandonment due to security concerns</rationale>
      <acceptance_criteria>
        <criterion id="FR2-AC1" format="gherkin">
          <given>A customer viewing the payment form</given>
          <when>The page renders</when>
          <then>PCI-DSS and SSL badges are visible without scrolling</then>
        </criterion>
      </acceptance_criteria>
      <dependencies>
        <dependency type="requires" ref="CON3">PCI compliance must be current</dependency>
      </dependencies>
    </requirement>

    <requirement id="FR3" priority="should_have" job_story_ref="JS2" confidence="0.85">
      <description>The system shall provide guest checkout option without mandatory account creation</description>
      <rationale>Guest checkout reduces friction for first-time buyers</rationale>
      <acceptance_criteria>
        <criterion id="FR3-AC1" format="gherkin">
          <given>A customer not logged in</given>
          <when>The customer proceeds to checkout</when>
          <then>A "Continue as Guest" button is displayed equal prominence to "Sign In"</then>
        </criterion>
        <criterion id="FR3-AC2" format="gherkin">
          <given>A guest customer completing purchase</given>
          <when>The order is confirmed</when>
          <then>An optional "Create Account" prompt appears with pre-filled email</then>
        </criterion>
      </acceptance_criteria>
      <dependencies/>
    </requirement>

    <requirement id="FR4" priority="must_have" job_story_ref="JS3" confidence="0.88">
      <description>The system shall track and report checkout funnel metrics by step in real-time</description>
      <rationale>Visibility into abandonment enables rapid optimization</rationale>
      <acceptance_criteria>
        <criterion id="FR4-AC1" format="gherkin">
          <given>A checkout session in progress</given>
          <when>The customer exits at any step</when>
          <then>The exit is logged with step identifier, timestamp, and session data</then>
        </criterion>
      </acceptance_criteria>
      <dependencies>
        <dependency type="requires" ref="DEP1">Analytics integration must be available</dependency>
      </dependencies>
    </requirement>
  </functional_requirements>

  <non_functional_requirements>
    <category name="Performance">
      <requirement id="NFR-P1" priority="must_have" confidence="0.90">
        <description>Checkout page time-to-interactive under 2 seconds on 3G</description>
        <metric>Time to Interactive (TTI)</metric>
        <target>< 2000ms on simulated 3G</target>
        <measurement_method>Lighthouse performance audit</measurement_method>
      </requirement>
      <requirement id="NFR-P2" priority="should_have" confidence="0.85">
        <description>Payment submission response under 3 seconds</description>
        <metric>Server response time</metric>
        <target>P95 < 3000ms</target>
        <measurement_method>APM monitoring (Datadog)</measurement_method>
      </requirement>
    </category>
    <category name="Security">
      <requirement id="NFR-S1" priority="must_have" confidence="0.98">
        <description>Payment processing must maintain PCI-DSS Level 1 compliance</description>
        <compliance>PCI-DSS Level 1</compliance>
        <verification_method>Annual third-party audit</verification_method>
      </requirement>
      <requirement id="NFR-S2" priority="must_have" confidence="0.95">
        <description>All payment data transmitted over TLS 1.3</description>
        <compliance>TLS 1.3</compliance>
        <verification_method>SSL Labs scan score A+</verification_method>
      </requirement>
    </category>
    <category name="Usability">
      <requirement id="NFR-U1" priority="should_have" confidence="0.80">
        <description>First-time users complete checkout without assistance</description>
        <user_segment>First-time buyers, ages 25-45</user_segment>
        <success_criteria>90% task completion rate in usability testing</success_criteria>
      </requirement>
    </category>
    <category name="Reliability">
      <requirement id="NFR-R1" priority="must_have" confidence="0.92">
        <description>Checkout service availability during peak hours</description>
        <metric>Uptime percentage</metric>
        <target>99.9% during 6pm-10pm EST</target>
      </requirement>
    </category>
    <category name="Scalability">
      <requirement id="NFR-SC1" priority="should_have" confidence="0.75">
        <description>Support anticipated Black Friday traffic</description>
        <current_baseline>500 concurrent checkout sessions</current_baseline>
        <target_capacity>2,500 concurrent checkout sessions</target_capacity>
        <growth_assumption>5x peak traffic during sales events</growth_assumption>
      </requirement>
    </category>
  </non_functional_requirements>

  <constraints>
    <constraint id="CON1" type="technical" negotiable="false">
      <description>Must integrate with existing Stripe payment infrastructure</description>
      <impact>Payment processing, refunds, disputes</impact>
      <source>Engineering - existing contracts and integrations</source>
    </constraint>
    <constraint id="CON2" type="business" negotiable="true">
      <description>Implementation budget capped at $30,000</description>
      <impact>Scope of features deliverable</impact>
      <source>Finance - Q1 budget allocation</source>
    </constraint>
    <constraint id="CON3" type="regulatory" negotiable="false">
      <description>PCI-DSS compliance must be maintained throughout implementation</description>
      <impact>All payment-related code changes</impact>
      <source>Legal/Compliance - regulatory requirement</source>
    </constraint>
    <constraint id="CON4" type="temporal" negotiable="true">
      <description>Target launch before Memorial Day sale</description>
      <impact>Feature scope and testing depth</impact>
      <source>Marketing - promotional calendar</source>
    </constraint>
  </constraints>

  <dependencies>
    <dependency id="DEP1" type="internal">
      <description>Analytics team must complete checkout event taxonomy</description>
      <owner>Analytics Team</owner>
      <status>planned</status>
      <requirements_affected>
        <ref>FR4</ref>
      </requirements_affected>
      <mitigation>Use existing events as fallback, enhance post-launch</mitigation>
    </dependency>
    <dependency id="DEP2" type="external">
      <description>Stripe API rate limits for production volume</description>
      <owner>Stripe (external)</owner>
      <status>available</status>
      <requirements_affected>
        <ref>FR1</ref>
        <ref>NFR-SC1</ref>
      </requirements_affected>
      <mitigation>N/A - confirmed adequate limits</mitigation>
    </dependency>
  </dependencies>

  <assumptions>
    <assumption id="A1" type="explicit" validated="true" confidence="0.90" impact="high">
      <statement>Users abandon primarily at payment step, not earlier in funnel</statement>
      <implications>Optimization focus on payment UX will have highest impact</implications>
      <validation_approach>Validated via analytics - 60% of abandonment at payment step</validation_approach>
      <requirements_affected>
        <ref>FR1</ref>
        <ref>FR2</ref>
      </requirements_affected>
    </assumption>
    <assumption id="A2" type="implicit" validated="false" confidence="0.65" impact="medium">
      <statement>Trust badges significantly impact conversion for our demographic</statement>
      <implications>Visual design should prominently feature security indicators</implications>
      <validation_approach>A/B test trust badge placement and design</validation_approach>
      <requirements_affected>
        <ref>FR2</ref>
      </requirements_affected>
    </assumption>
    <assumption id="A3" type="implicit" validated="false" confidence="0.70" impact="high">
      <statement>Guest checkout will improve conversion by 10-15%</statement>
      <implications>Engineering effort for guest flow is justified</implications>
      <validation_approach>Implement and measure conversion delta</validation_approach>
      <requirements_affected>
        <ref>FR3</ref>
        <ref>JS2</ref>
      </requirements_affected>
    </assumption>
  </assumptions>

  <traceability>
    <trace_matrix>
      <trace job_story="JS1"
             functional_requirements="FR1,FR2"
             nfr="NFR-P1,NFR-P2,NFR-S1,NFR-S2,NFR-R1"
             acceptance_criteria="JS1-AC1,JS1-AC2,JS1-AC3,FR1-AC1,FR2-AC1"
             constraints="CON1,CON3"
             assumptions="A1,A2"/>
      <trace job_story="JS2"
             functional_requirements="FR3"
             nfr="NFR-U1"
             acceptance_criteria="JS2-AC1,JS2-AC2,FR3-AC1,FR3-AC2"
             constraints="CON2"
             assumptions="A3"/>
      <trace job_story="JS3"
             functional_requirements="FR4"
             nfr=""
             acceptance_criteria="JS3-AC1,FR4-AC1"
             constraints=""
             assumptions=""/>
    </trace_matrix>
    <orphan_check>
      <orphaned_requirements>
        <!-- All requirements traced -->
      </orphaned_requirements>
      <unmet_job_stories>
        <!-- All job stories have implementing requirements -->
      </unmet_job_stories>
    </orphan_check>
  </traceability>

  <coverage_assessment>
    <mece_coverage>
      <dimension name="User Needs" coverage="complete" confidence="0.88">
        <requirements_count>3</requirements_count>
        <gap_notes>Primary checkout journey covered; edge cases documented</gap_notes>
      </dimension>
      <dimension name="Current Solution" coverage="partial" confidence="0.75">
        <requirements_count>2</requirements_count>
        <gap_notes>Payment flow addressed; cart experience out of scope</gap_notes>
      </dimension>
      <dimension name="Success Metrics" coverage="complete" confidence="0.85">
        <requirements_count>1</requirements_count>
        <gap_notes>Funnel tracking covered; A/B testing infrastructure assumed</gap_notes>
      </dimension>
      <dimension name="Constraints" coverage="complete" confidence="0.95">
        <requirements_count>4</requirements_count>
        <gap_notes>All known constraints documented</gap_notes>
      </dimension>
    </mece_coverage>
    <priority_distribution>
      <must_have count="5" percentage="56%"/>
      <should_have count="4" percentage="44%"/>
      <could_have count="0" percentage="0%"/>
      <wont_have count="0" percentage="0%"/>
    </priority_distribution>
    <confidence_summary>
      <average_confidence>0.86</average_confidence>
      <low_confidence_items>
        <item ref="A2" confidence="0.65" reason="Trust badge impact unvalidated for our demographic"/>
        <item ref="A3" confidence="0.70" reason="Guest checkout conversion lift is estimate from industry benchmarks"/>
        <item ref="NFR-SC1" confidence="0.75" reason="Black Friday traffic projection based on 2023 data"/>
      </low_confidence_items>
    </confidence_summary>
    <validation_needed>
      <item ref="A2" priority="high">A/B test trust badge effectiveness before full rollout</item>
      <item ref="A3" priority="medium">Monitor guest checkout conversion after launch</item>
      <item ref="NFR-SC1" priority="high">Load test at 3x expected peak before sale events</item>
    </validation_needed>
  </coverage_assessment>

</requirements>
```

---

## Validation Checklist

Before finalizing:

### Structure
- [ ] Artifact ID matches pattern REQ-YYYY-MM-DD-[hash]
- [ ] All required sections present (metadata, job_stories, functional_requirements)
- [ ] All IDs are unique within their type (JS1, FR1, NFR-P1, etc.)
- [ ] All references (stakeholder_ref, job_story_ref) point to valid IDs

### Job Stories
- [ ] Every job story has situation, motivation, outcome
- [ ] JTBD components are specific, not generic
- [ ] Acceptance criteria use proper Gherkin format
- [ ] Edge cases documented for complex scenarios

### Requirements Quality
- [ ] Functional requirements are testable and specific
- [ ] NFRs have measurable metrics and targets
- [ ] Rationale explains business justification
- [ ] Priority classification follows MoSCoW definitions

### Traceability
- [ ] Every functional requirement traces to a job story
- [ ] Traceability matrix includes all job stories
- [ ] Orphan check performed and resolved
- [ ] Dependencies documented with status

### Epistemic Integrity
- [ ] Confidence scores reflect evidence quality
- [ ] Assumptions explicitly stated with impact assessment
- [ ] Low confidence items appear in validation_needed
- [ ] Validation approaches are actionable

### Coverage
- [ ] MECE dimensions assessed for completeness
- [ ] Priority distribution is realistic (must_have ≤ 60%)
- [ ] Critical gaps have resolution plans

---

## Integration Notes

### For Downstream Skills

The requirements artifact feeds into:

1. **Architecture skills** - Use constraints and NFRs to inform technical decisions
2. **Development planning** - Use priority and dependencies for sprint planning
3. **Testing skills** - Use acceptance criteria as test case foundation
4. **Documentation skills** - Use job stories for user-facing documentation

### Handoff Protocol

1. Save artifact to `artifacts/` directory using `artifact_id` as filename
2. Reference in downstream artifacts via `source_artifact` field
3. Carry forward unvalidated assumptions for tracking
4. Use acceptance criteria directly for test case generation

### Artifact Chaining

```
research-interviewer → PROBLEM-STATEMENT
                            ↓
research-interviewer → REQUIREMENTS (this artifact)
                            ↓
         [architecture skill] → ARCHITECTURE-DECISION
                            ↓
         [development planning] → SPRINT-PLAN
```
