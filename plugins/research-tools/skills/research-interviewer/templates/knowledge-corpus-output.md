# Knowledge Corpus Output Template

RAG-optimized template for structured knowledge capture with semantic chunking and cross-reference support.

---

## Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<knowledge_corpus version="1.0">

  <!-- METADATA -->
  <metadata>
    <artifact_id>KC-[YYYY-MM-DD]-[5-char-hash]</artifact_id>
    <artifact_type>KNOWLEDGE-CORPUS</artifact_type>
    <created_at>[ISO 8601 timestamp]</created_at>
    <created_by>research-interviewer</created_by>
    <confidence>[0.0-1.0]</confidence>
    <topic>[Primary topic]</topic>
    <domain>[product|architecture|research|requirements|custom|none]</domain>
    <provenance>
      <source_type>interview</source_type>
      <interview_turns>[Total conversation turns]</interview_turns>
      <interviewee_role>[Role/title]</interviewee_role>
      <interview_date>[ISO 8601 date]</interview_date>
      <validation_mode>[empathetic|balanced|rigorous]</validation_mode>
    </provenance>
  </metadata>

  <!-- EXECUTIVE SUMMARY -->
  <executive_summary>
    <key_points>
      <point confidence="[HIGH|MEDIUM|LOW]">[Key point 1]</point>
      <point confidence="[confidence]">[Key point 2]</point>
      <point confidence="[confidence]">[Key point 3]</point>
      <!-- 3-5 key points recommended -->
    </key_points>
    <scope_coverage>[What this corpus covers - topic boundaries]</scope_coverage>
    <known_gaps>[What it doesn't cover - explicit limitations]</known_gaps>
  </executive_summary>

  <!-- KNOWLEDGE DIMENSIONS (MECE) -->
  <knowledge_dimensions>
    <dimension id="D1" name="[Dimension Name]">
      <description>[What this dimension covers]</description>
      <coverage_status>[complete|partial|sparse]</coverage_status>
      <confidence>[0.0-1.0]</confidence>

      <facts>
        <fact id="D1F1" label="[FACT|LIKELY|PLAUSIBLE|ASSUMPTION|UNCERTAIN]"
              confidence="[0.0-1.0]">
          <statement>[Factual statement]</statement>
          <source_turn>[Interview turn number]</source_turn>
          <verbatim_quote>[Direct quote if available]</verbatim_quote>
        </fact>
        <!-- Additional facts -->
      </facts>

      <relationships>
        <relationship type="[causes|enables|blocks|depends_on|contradicts]">
          <from ref="D[N]F[M]"/>
          <to ref="D[N]F[M]"/>
          <strength>[strong|moderate|weak]</strength>
          <notes>[Optional explanation]</notes>
        </relationship>
        <!-- Additional relationships -->
      </relationships>
    </dimension>

    <!-- Additional dimensions (typically 4-6 for MECE coverage) -->
  </knowledge_dimensions>

  <!-- ENTITY REGISTRY -->
  <entity_registry>
    <entity id="E1" type="[person|organization|system|concept|process|artifact]">
      <name>[Entity name]</name>
      <description>[Brief description]</description>
      <aliases>
        <alias>[Alternative name or abbreviation]</alias>
      </aliases>
      <mentioned_in>
        <dimension ref="D[N]"/>
        <fact ref="D[N]F[M]"/>
      </mentioned_in>
      <relationships>
        <related_to entity_ref="E[N]" type="[owns|uses|manages|depends_on|part_of]"/>
      </relationships>
    </entity>
    <!-- Additional entities -->
  </entity_registry>

  <!-- ASSUMPTION INVENTORY -->
  <assumption_inventory>
    <assumption id="A1" type="[explicit|implicit|structural]"
                impact="[high|medium|low]" validated="[true|false]">
      <statement>[Assumption statement]</statement>
      <evidence>[How this was identified - turn reference or inference]</evidence>
      <alternative>[What if this assumption is wrong]</alternative>
      <affects_dimensions>
        <dimension ref="D[N]"/>
      </affects_dimensions>
      <affects_facts>
        <fact ref="D[N]F[M]"/>
      </affects_facts>
    </assumption>
    <!-- Additional assumptions -->
  </assumption_inventory>

  <!-- CONSISTENCY MATRIX -->
  <consistency_matrix>
    <verification id="V1">
      <claims_compared>
        <claim ref="D[N]F[M]"/>
        <claim ref="D[N]F[M]"/>
      </claims_compared>
      <status>[consistent|tension|contradiction]</status>
      <resolution>[How contradiction was resolved, if applicable]</resolution>
      <notes>[Explanation of status]</notes>
    </verification>
    <!-- Additional verifications -->
  </consistency_matrix>

  <!-- GAPS AND UNKNOWNS -->
  <gaps>
    <gap id="G1" severity="[critical|significant|minor]">
      <description>[What's missing]</description>
      <dimension_affected ref="D[N]"/>
      <impact>[Why this matters - what decisions it affects]</impact>
      <resolution_path>[How to fill this gap - research, interview, etc.]</resolution_path>
      <priority>[high|medium|low]</priority>
    </gap>
    <!-- Additional gaps -->
  </gaps>

  <!-- RAG OPTIMIZATION -->
  <rag_metadata>
    <chunk_boundaries>
      <chunk id="CH1" start_fact="D1F1" end_fact="D1F5"
             topic="[Chunk topic for retrieval]"
             token_estimate="[Approximate tokens]"/>
      <!-- Suggested chunking for RAG ingestion -->
    </chunk_boundaries>
    <search_keywords>
      <keyword weight="[1-10]" category="[primary|secondary|contextual]">[Keyword]</keyword>
      <!-- Keywords for semantic search optimization -->
    </search_keywords>
    <semantic_clusters>
      <cluster id="SC1" name="[Cluster name]" coherence="[high|medium|low]">
        <fact ref="D[N]F[M]"/>
        <fact ref="D[N]F[M]"/>
        <!-- Facts that belong together semantically -->
      </cluster>
    </semantic_clusters>
    <cross_references>
      <xref from="D[N]F[M]" to="D[N]F[M]" type="[supports|extends|qualifies]"/>
      <!-- Important cross-references to preserve during chunking -->
    </cross_references>
  </rag_metadata>

</knowledge_corpus>
```

---

## Field Documentation

### metadata

| Field | Description | Example |
|-------|-------------|---------|
| `artifact_id` | Unique identifier | KC-2025-01-15-b7c3d |
| `artifact_type` | Always KNOWLEDGE-CORPUS | KNOWLEDGE-CORPUS |
| `confidence` | Overall corpus confidence | 0.78 |
| `topic` | Primary subject matter | E-commerce checkout optimization |
| `domain` | Domain classification | product |
| `interview_turns` | Total conversation exchanges | 42 |
| `interviewee_role` | Primary source role | Product Manager |
| `validation_mode` | Interview rigor level | balanced |

### executive_summary

| Element | Description |
|---------|-------------|
| `key_points` | 3-5 most important findings with confidence levels |
| `point/@confidence` | HIGH (80%+), MEDIUM (60-79%), LOW (<60%) |
| `scope_coverage` | What topics/areas are covered |
| `known_gaps` | Explicit statement of what's NOT covered |

### knowledge_dimensions

Organize knowledge into MECE (Mutually Exclusive, Collectively Exhaustive) dimensions.

| Element | Description |
|---------|-------------|
| `dimension/@id` | Unique ID (D1, D2, etc.) |
| `dimension/@name` | Human-readable dimension name |
| `coverage_status` | complete (90%+), partial (50-89%), sparse (<50%) |
| `fact/@id` | Unique within corpus (D1F1, D1F2, etc.) |
| `fact/@label` | Epistemic label: FACT, LIKELY, PLAUSIBLE, ASSUMPTION, UNCERTAIN |
| `fact/@confidence` | Numeric confidence 0.0-1.0 |
| `source_turn` | Interview turn number for traceability |
| `verbatim_quote` | Direct quote when available (aids credibility) |

**Relationship Types:**
| Type | Meaning |
|------|---------|
| `causes` | A leads to B |
| `enables` | A makes B possible |
| `blocks` | A prevents B |
| `depends_on` | A requires B |
| `contradicts` | A conflicts with B |

### entity_registry

Track all significant entities mentioned in the corpus.

| Entity Type | Examples |
|-------------|----------|
| `person` | Stakeholder, user persona, team member |
| `organization` | Company, department, vendor |
| `system` | Software, platform, tool |
| `concept` | Business term, metric, principle |
| `process` | Workflow, procedure, method |
| `artifact` | Document, spec, code, deliverable |

**Entity Relationship Types:**
| Type | Meaning |
|------|---------|
| `owns` | Entity A is responsible for B |
| `uses` | Entity A utilizes B |
| `manages` | Entity A controls/oversees B |
| `depends_on` | Entity A requires B |
| `part_of` | Entity A is component of B |

### assumption_inventory

| Field | Description |
|-------|-------------|
| `type` | explicit (stated), implicit (inferred), structural (framework) |
| `impact` | high (invalidates conclusions), medium (weakens), low (minor effect) |
| `validated` | Whether assumption has been verified |
| `alternative` | What changes if assumption is false |
| `affects_dimensions` | Which MECE dimensions depend on this |

### consistency_matrix

| Status | Meaning | Action |
|--------|---------|--------|
| `consistent` | Claims align and support each other | None needed |
| `tension` | Claims partially conflict but coexist | Document nuance |
| `contradiction` | Claims directly conflict | Must resolve or flag |

### gaps

| Severity | Definition | Response |
|----------|------------|----------|
| `critical` | Missing info blocks key decisions | Must fill before use |
| `significant` | Weakens conclusions substantially | Should address |
| `minor` | Nice to have, not essential | Document for future |

### rag_metadata

| Element | Purpose |
|---------|---------|
| `chunk_boundaries` | Suggested semantic breaks for RAG ingestion |
| `search_keywords` | Terms optimized for retrieval |
| `semantic_clusters` | Facts that should retrieve together |
| `cross_references` | Links to preserve across chunks |

---

## RAG Optimization Guidance

### Chunking Strategy

**Principle:** Chunk by semantic coherence, not character count.

1. **Respect dimension boundaries** - Each dimension is a natural chunk unit
2. **Keep relationships intact** - Don't split related facts across chunks
3. **Include context** - Each chunk should be self-contained enough to be useful alone
4. **Preserve metadata** - Include dimension name and topic in each chunk

**Recommended chunk structure:**
```
[Dimension: {name}]
[Topic: {description}]
[Coverage: {status}] [Confidence: {confidence}]

Facts:
- {fact statement} [{label}, {confidence}]
  Source: Turn {N}, "{verbatim_quote}"

Relationships:
- {from} {type} {to}
```

### Keyword Selection

**Weight Guidelines:**
| Weight | Usage |
|--------|-------|
| 9-10 | Core topic identifiers, unique terms |
| 7-8 | Important concepts, frequent terms |
| 5-6 | Supporting concepts, related terms |
| 3-4 | Contextual terms, domain jargon |
| 1-2 | Broad category terms |

**Category Guidelines:**
- `primary`: Terms that should trigger retrieval of this corpus
- `secondary`: Terms that might be relevant
- `contextual`: Background terms that add context

### Semantic Clustering

Group facts that:
1. Answer the same question
2. Describe the same entity or process
3. Support the same conclusion
4. Contradict each other (retrieve together for balanced view)

**Coherence levels:**
- `high`: Facts directly support each other
- `medium`: Facts are related but independent
- `low`: Facts share topic but diverge

### Cross-Reference Preservation

Critical cross-references to maintain:
1. **Causal chains** - If A causes B causes C, retrieving A should surface B and C
2. **Contradictions** - Always retrieve opposing views together
3. **Evidence-conclusion** - Keep evidence with its conclusions
4. **Assumption-dependent** - Facts depending on assumptions should link to those assumptions

---

## Chunking Recommendations by RAG System

### OpenAI / GPT-based Systems

| Parameter | Recommendation |
|-----------|----------------|
| Chunk size | 500-800 tokens |
| Overlap | 50-100 tokens |
| Embedding model | text-embedding-3-large |
| Metadata | Include dimension, confidence, entity names |

**Chunking approach:**
```
Chunk = Dimension header + facts + relationships
If chunk > 800 tokens: Split at semantic cluster boundaries
Always include: artifact_id, dimension_id, topic in metadata
```

### Anthropic / Claude-based Systems

| Parameter | Recommendation |
|-----------|----------------|
| Chunk size | 1000-1500 tokens (larger context window) |
| Overlap | 100-200 tokens |
| Format | Preserve XML structure when possible |
| Metadata | Full provenance chain recommended |

**Chunking approach:**
```
Prefer larger chunks that maintain XML structure
Include assumption inventory with dependent facts
Preserve verbatim quotes for attribution
```

### Local/Custom RAG (LangChain, LlamaIndex)

| Parameter | Recommendation |
|-----------|----------------|
| Chunk size | 400-600 tokens (tune to your embedding model) |
| Overlap | 10-15% of chunk size |
| Splitter | Use semantic splitting, not character |
| Metadata | Store all attributes for filtering |

**Metadata schema for vector DB:**
```json
{
  "artifact_id": "KC-2025-01-15-b7c3d",
  "dimension_id": "D1",
  "dimension_name": "User Needs",
  "fact_ids": ["D1F1", "D1F2", "D1F3"],
  "confidence": 0.85,
  "coverage_status": "complete",
  "entities": ["E1", "E3"],
  "keywords": ["checkout", "abandonment", "friction"],
  "has_contradictions": false,
  "interview_date": "2025-01-15"
}
```

### Hybrid Search Optimization

For systems combining semantic + keyword search:

1. **Extract explicit keywords** from `search_keywords` for BM25/keyword index
2. **Use dimension descriptions** for semantic embeddings
3. **Index entity names and aliases** separately for exact match
4. **Store confidence scores** for result ranking

---

## Example Output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<knowledge_corpus version="1.0">

  <metadata>
    <artifact_id>KC-2025-01-15-b7c3d</artifact_id>
    <artifact_type>KNOWLEDGE-CORPUS</artifact_type>
    <created_at>2025-01-15T16:45:00Z</created_at>
    <created_by>research-interviewer</created_by>
    <confidence>0.78</confidence>
    <topic>E-commerce checkout optimization</topic>
    <domain>product</domain>
    <provenance>
      <source_type>interview</source_type>
      <interview_turns>42</interview_turns>
      <interviewee_role>Product Manager</interviewee_role>
      <interview_date>2025-01-15</interview_date>
      <validation_mode>balanced</validation_mode>
    </provenance>
  </metadata>

  <executive_summary>
    <key_points>
      <point confidence="HIGH">Checkout abandonment rate is 48%, exceeding 35% industry benchmark</point>
      <point confidence="HIGH">Payment step accounts for 60% of all abandonments</point>
      <point confidence="MEDIUM">Mobile users experience higher friction than desktop users</point>
      <point confidence="MEDIUM">Guest checkout option is expected to improve conversion</point>
      <point confidence="LOW">Trust badges may influence purchase decisions</point>
    </key_points>
    <scope_coverage>User checkout experience, payment friction points, mobile vs desktop behavior, trust factors</scope_coverage>
    <known_gaps>Competitor checkout analysis not included; no direct user research data; A/B test results pending</known_gaps>
  </executive_summary>

  <knowledge_dimensions>
    <dimension id="D1" name="User Needs">
      <description>What users want from the checkout experience</description>
      <coverage_status>complete</coverage_status>
      <confidence>0.85</confidence>

      <facts>
        <fact id="D1F1" label="FACT" confidence="0.95">
          <statement>Users cite "too many steps" as the primary complaint about checkout</statement>
          <source_turn>12</source_turn>
          <verbatim_quote>"Every customer survey for the past 6 months has 'too many steps' in the top 3 complaints"</verbatim_quote>
        </fact>
        <fact id="D1F2" label="LIKELY" confidence="0.85">
          <statement>Users expect checkout to complete in under 2 minutes</statement>
          <source_turn>15</source_turn>
          <verbatim_quote>"Based on our session recordings, users who take longer than 2 minutes almost always abandon"</verbatim_quote>
        </fact>
        <fact id="D1F3" label="LIKELY" confidence="0.80">
          <statement>First-time buyers have higher trust concerns than returning customers</statement>
          <source_turn>18</source_turn>
          <verbatim_quote></verbatim_quote>
        </fact>
      </facts>

      <relationships>
        <relationship type="causes">
          <from ref="D1F1"/>
          <to ref="D2F1"/>
          <strength>strong</strength>
          <notes>Too many steps directly causes abandonment</notes>
        </relationship>
      </relationships>
    </dimension>

    <dimension id="D2" name="Current Solution">
      <description>How the existing checkout system performs</description>
      <coverage_status>complete</coverage_status>
      <confidence>0.90</confidence>

      <facts>
        <fact id="D2F1" label="FACT" confidence="0.95">
          <statement>Current checkout abandonment rate is 48%</statement>
          <source_turn>5</source_turn>
          <verbatim_quote>"We're at 48% abandonment, which is about 13 points above the industry benchmark of 35%"</verbatim_quote>
        </fact>
        <fact id="D2F2" label="FACT" confidence="0.92">
          <statement>60% of abandonments occur at the payment step</statement>
          <source_turn>8</source_turn>
          <verbatim_quote>"Our funnel analysis shows payment is where we lose most people—about 60% of all drops"</verbatim_quote>
        </fact>
        <fact id="D2F3" label="LIKELY" confidence="0.80">
          <statement>Current checkout requires 5 distinct pages/steps</statement>
          <source_turn>10</source_turn>
          <verbatim_quote></verbatim_quote>
        </fact>
      </facts>

      <relationships>
        <relationship type="causes">
          <from ref="D2F3"/>
          <to ref="D2F1"/>
          <strength>moderate</strength>
          <notes>Multiple steps contribute to high abandonment</notes>
        </relationship>
      </relationships>
    </dimension>

    <dimension id="D3" name="Competitive Landscape">
      <description>How competitors handle checkout</description>
      <coverage_status>sparse</coverage_status>
      <confidence>0.50</confidence>

      <facts>
        <fact id="D3F1" label="ASSUMPTION" confidence="0.50">
          <statement>Competitors likely use one-page checkout</statement>
          <source_turn>22</source_turn>
          <verbatim_quote>"I assume Amazon and others have optimized this heavily, but we haven't done a formal analysis"</verbatim_quote>
        </fact>
      </facts>

      <relationships/>
    </dimension>

    <dimension id="D4" name="Success Metrics">
      <description>How success will be measured</description>
      <coverage_status>partial</coverage_status>
      <confidence>0.75</confidence>

      <facts>
        <fact id="D4F1" label="LIKELY" confidence="0.85">
          <statement>Target abandonment rate is below 35%</statement>
          <source_turn>28</source_turn>
          <verbatim_quote>"We need to get to at least the industry benchmark of 35%"</verbatim_quote>
        </fact>
        <fact id="D4F2" label="PLAUSIBLE" confidence="0.70">
          <statement>Target checkout time is under 90 seconds</statement>
          <source_turn>30</source_turn>
          <verbatim_quote></verbatim_quote>
        </fact>
      </facts>

      <relationships>
        <relationship type="depends_on">
          <from ref="D4F1"/>
          <to ref="D2F2"/>
          <strength>strong</strength>
          <notes>Reducing payment friction is key to hitting target</notes>
        </relationship>
      </relationships>
    </dimension>

    <dimension id="D5" name="Constraints">
      <description>Technical and business limitations</description>
      <coverage_status>complete</coverage_status>
      <confidence>0.90</confidence>

      <facts>
        <fact id="D5F1" label="FACT" confidence="0.95">
          <statement>Must integrate with existing Stripe infrastructure</statement>
          <source_turn>35</source_turn>
          <verbatim_quote>"Stripe is non-negotiable—we have a 3-year contract"</verbatim_quote>
        </fact>
        <fact id="D5F2" label="FACT" confidence="0.90">
          <statement>PCI-DSS compliance is required</statement>
          <source_turn>36</source_turn>
          <verbatim_quote></verbatim_quote>
        </fact>
        <fact id="D5F3" label="LIKELY" confidence="0.80">
          <statement>Budget is capped at $30K</statement>
          <source_turn>38</source_turn>
          <verbatim_quote>"We've got about 30K approved, maybe a bit more if we show good ROI projections"</verbatim_quote>
        </fact>
      </facts>

      <relationships>
        <relationship type="blocks">
          <from ref="D5F1"/>
          <to ref="D3F1"/>
          <strength>moderate</strength>
          <notes>Stripe integration may limit checkout redesign options</notes>
        </relationship>
      </relationships>
    </dimension>
  </knowledge_dimensions>

  <entity_registry>
    <entity id="E1" type="system">
      <name>Stripe</name>
      <description>Payment processing platform</description>
      <aliases>
        <alias>Stripe API</alias>
      </aliases>
      <mentioned_in>
        <dimension ref="D5"/>
        <fact ref="D5F1"/>
      </mentioned_in>
      <relationships>
        <related_to entity_ref="E2" type="part_of"/>
      </relationships>
    </entity>
    <entity id="E2" type="system">
      <name>Checkout System</name>
      <description>Current e-commerce checkout flow</description>
      <aliases>
        <alias>checkout</alias>
        <alias>cart checkout</alias>
      </aliases>
      <mentioned_in>
        <dimension ref="D2"/>
        <fact ref="D2F1"/>
        <fact ref="D2F3"/>
      </mentioned_in>
      <relationships/>
    </entity>
    <entity id="E3" type="person">
      <name>Sarah Chen</name>
      <description>Product Manager, primary stakeholder</description>
      <aliases/>
      <mentioned_in>
        <dimension ref="D1"/>
      </mentioned_in>
      <relationships>
        <related_to entity_ref="E2" type="manages"/>
      </relationships>
    </entity>
    <entity id="E4" type="concept">
      <name>Guest Checkout</name>
      <description>Checkout without account creation</description>
      <aliases>
        <alias>anonymous checkout</alias>
      </aliases>
      <mentioned_in>
        <dimension ref="D1"/>
      </mentioned_in>
      <relationships>
        <related_to entity_ref="E2" type="part_of"/>
      </relationships>
    </entity>
  </entity_registry>

  <assumption_inventory>
    <assumption id="A1" type="explicit" impact="medium" validated="false">
      <statement>Trust badges significantly impact conversion</statement>
      <evidence>PM stated belief based on competitor observation, turn 25</evidence>
      <alternative>If wrong, trust badge implementation may waste development effort</alternative>
      <affects_dimensions>
        <dimension ref="D1"/>
      </affects_dimensions>
      <affects_facts>
        <fact ref="D1F3"/>
      </affects_facts>
    </assumption>
    <assumption id="A2" type="implicit" impact="high" validated="false">
      <statement>Guest checkout will reduce abandonment by 10-15%</statement>
      <evidence>Inferred from industry benchmarks cited, turn 20</evidence>
      <alternative>If wrong, core strategy needs revision</alternative>
      <affects_dimensions>
        <dimension ref="D4"/>
      </affects_dimensions>
      <affects_facts>
        <fact ref="D4F1"/>
      </affects_facts>
    </assumption>
    <assumption id="A3" type="structural" impact="medium" validated="true">
      <statement>Abandonment rate is the right metric to optimize</statement>
      <evidence>Implicit in all discussion framing; confirmed explicitly turn 40</evidence>
      <alternative>Could optimize for revenue per visitor or customer lifetime value instead</alternative>
      <affects_dimensions>
        <dimension ref="D2"/>
        <dimension ref="D4"/>
      </affects_dimensions>
      <affects_facts/>
    </assumption>
  </assumption_inventory>

  <consistency_matrix>
    <verification id="V1">
      <claims_compared>
        <claim ref="D2F1"/>
        <claim ref="D4F1"/>
      </claims_compared>
      <status>consistent</status>
      <resolution/>
      <notes>Current 48% vs target 35% is internally consistent gap analysis</notes>
    </verification>
    <verification id="V2">
      <claims_compared>
        <claim ref="D1F2"/>
        <claim ref="D4F2"/>
      </claims_compared>
      <status>tension</status>
      <resolution/>
      <notes>2-minute abandonment threshold vs 90-second target creates aggressive goal</notes>
    </verification>
  </consistency_matrix>

  <gaps>
    <gap id="G1" severity="significant">
      <description>No competitive checkout analysis</description>
      <dimension_affected ref="D3"/>
      <impact>Cannot benchmark against best practices or identify differentiation opportunities</impact>
      <resolution_path>Conduct UX teardown of top 5 competitor checkout flows</resolution_path>
      <priority>high</priority>
    </gap>
    <gap id="G2" severity="significant">
      <description>No A/B test data on trust badges</description>
      <dimension_affected ref="D1"/>
      <impact>Trust badge investment may be misallocated</impact>
      <resolution_path>Run 2-week A/B test before full implementation</resolution_path>
      <priority>medium</priority>
    </gap>
    <gap id="G3" severity="minor">
      <description>Mobile vs desktop breakdown not quantified</description>
      <dimension_affected ref="D2"/>
      <impact>May miss mobile-specific optimization opportunities</impact>
      <resolution_path>Pull segmented analytics from existing tools</resolution_path>
      <priority>medium</priority>
    </gap>
  </gaps>

  <rag_metadata>
    <chunk_boundaries>
      <chunk id="CH1" start_fact="D1F1" end_fact="D1F3"
             topic="User needs and expectations for checkout"
             token_estimate="350"/>
      <chunk id="CH2" start_fact="D2F1" end_fact="D2F3"
             topic="Current checkout performance metrics"
             token_estimate="400"/>
      <chunk id="CH3" start_fact="D3F1" end_fact="D3F1"
             topic="Competitive landscape assumptions"
             token_estimate="150"/>
      <chunk id="CH4" start_fact="D4F1" end_fact="D4F2"
             topic="Success metrics and targets"
             token_estimate="250"/>
      <chunk id="CH5" start_fact="D5F1" end_fact="D5F3"
             topic="Technical and business constraints"
             token_estimate="350"/>
    </chunk_boundaries>
    <search_keywords>
      <keyword weight="10" category="primary">checkout abandonment</keyword>
      <keyword weight="10" category="primary">payment friction</keyword>
      <keyword weight="9" category="primary">e-commerce conversion</keyword>
      <keyword weight="8" category="secondary">guest checkout</keyword>
      <keyword weight="8" category="secondary">cart abandonment</keyword>
      <keyword weight="7" category="secondary">Stripe integration</keyword>
      <keyword weight="6" category="secondary">trust badges</keyword>
      <keyword weight="5" category="contextual">PCI compliance</keyword>
      <keyword weight="4" category="contextual">mobile checkout</keyword>
      <keyword weight="3" category="contextual">one-page checkout</keyword>
    </search_keywords>
    <semantic_clusters>
      <cluster id="SC1" name="Abandonment Problem" coherence="high">
        <fact ref="D1F1"/>
        <fact ref="D2F1"/>
        <fact ref="D2F2"/>
      </cluster>
      <cluster id="SC2" name="Target State" coherence="high">
        <fact ref="D4F1"/>
        <fact ref="D4F2"/>
      </cluster>
      <cluster id="SC3" name="Technical Constraints" coherence="high">
        <fact ref="D5F1"/>
        <fact ref="D5F2"/>
        <fact ref="D5F3"/>
      </cluster>
    </semantic_clusters>
    <cross_references>
      <xref from="D1F1" to="D2F1" type="supports"/>
      <xref from="D2F2" to="D4F1" type="qualifies"/>
      <xref from="D5F1" to="D2F3" type="qualifies"/>
    </cross_references>
  </rag_metadata>

</knowledge_corpus>
```

---

## Validation Checklist

Before finalizing:

### Structure
- [ ] All MECE dimensions have unique IDs (D1, D2, etc.)
- [ ] All facts have unique IDs within corpus (D1F1, D1F2, etc.)
- [ ] All entities have unique IDs (E1, E2, etc.)
- [ ] All assumptions have unique IDs (A1, A2, etc.)
- [ ] All gaps have unique IDs (G1, G2, etc.)

### Epistemic Quality
- [ ] Each fact has appropriate epistemic label (FACT/LIKELY/PLAUSIBLE/ASSUMPTION/UNCERTAIN)
- [ ] Confidence scores align with labels
- [ ] Verbatim quotes included where available
- [ ] Source turns documented for traceability

### Coverage
- [ ] Executive summary captures 3-5 key points
- [ ] Known gaps explicitly documented
- [ ] Each dimension has coverage_status assessment
- [ ] Assumptions inventory includes all three types

### Consistency
- [ ] Consistency matrix checks performed on related claims
- [ ] Contradictions flagged and resolved or documented
- [ ] Cross-references capture important relationships

### RAG Optimization
- [ ] Chunk boundaries respect semantic coherence
- [ ] Keyword weights reflect retrieval importance
- [ ] Semantic clusters group related facts
- [ ] Cross-references identify links to preserve
- [ ] Token estimates provided for each chunk
