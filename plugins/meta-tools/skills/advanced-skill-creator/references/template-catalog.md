# Template Catalog Reference

Quick reference for available templates in the advanced-skill-creator.

## Evaluation Templates

### expert-panel
**Purpose:** Generate domain-appropriate expert panels
**Parameters:**
- `domain` (required): Domain for expert specialization
- `evaluation_goal` (required): What the panel evaluates
- `panel_size` (default: 5): Number of experts (3-8)
- `perspective_balance`: technical_heavy | business_heavy | balanced | challenger_heavy
- `include_challenger` (default: true): Include devil's advocate

**Expert Archetypes Available:**
- Technical Authority
- Quality Guardian
- User Advocate
- Risk Specialist
- Efficiency Expert
- Domain Specialist
- Challenger/Devil's Advocate
- Compliance Officer

### tournament-ranking
**Purpose:** Pairwise comparison with statistical ranking
**Parameters:**
- `items` (required): List of items to rank (3-20)
- `evaluation_criteria` (required): Dimensions for comparison
- `scoring_algorithm`: BRADLEY-TERRY | ELO | WEIGHTED-SUM
- `position_swap` (default: true): Reduce order bias
- `iterations` (default: 2): Tournament rounds

### adversarial-validation
**Purpose:** Red/blue team stress testing
**Parameters:**
- `proposition` (required): Claim to stress-test
- `attack_vectors`: Specific angles to attack
- `intensity`: light | standard | aggressive
- `rounds` (default: 2): Attack-defend cycles
- `output_focus`: risks_only | mitigations | revised_proposition

## Research Templates

### research-brief
**Purpose:** Multi-LLM research prompt generation
**Parameters:**
- `research_domain` (required): market | industry | competitive | user | technology | regulatory
- `research_question` (required): Core question to answer
- `target_models`: claude_opus_4_5 | gemini_pro_3 | gpt_5_2_lite | gpt_5_2_deep
- `depth`: quick | standard | deep
- `output_format`: prompts_only | prompts_with_consolidation | full_workflow

### research-consolidation
**Purpose:** Synthesize multi-source research
**Parameters:**
- `sources` (required): Research outputs to consolidate
- `reconciliation_mode`: agreement_focused | tension_focused | comprehensive
- `confidence_methodology`: corroboration_count | source_weighted | evidence_quality

## Requirements Templates

### feature-extraction
**Purpose:** Identify features from content
**Parameters:**
- `context_type` (required): prd | conversation | competitor_analysis | user_feedback | specification
- `granularity`: epic | feature | capability
- `include_metadata` (default: true): Priority, effort estimates

### job-story-generation
**Purpose:** Generate JTBD-format stories
**Parameters:**
- `input_type` (required): feature_list | user_feedback | interview_transcript | problem_statement
- `persona`: Target user persona object
- `format`: classic_jtbd | situation_motivation_outcome | user_story
- `include_acceptance_criteria` (default: true)

### user-flow-mapping
**Purpose:** Document user flows and journeys
**Parameters:**
- `process` (required): Process to map
- `flow_type`: task_flow | user_journey | service_blueprint
- `include_emotions` (default: true)
- `output_format`: narrative | structured | mermaid_diagram

## Documentation Templates

### diataxis-documentation
**Purpose:** Generate Diátaxis-aligned docs
**Parameters:**
- `doc_type` (required): tutorial | how_to | explanation | reference
- `topic` (required): What to document
- `audience`: expertise_level, persona, prior_knowledge
- `reading_level`: grade_8 | grade_12 | professional

## Validation Templates

### gap-audit
**Purpose:** Identify gaps against standards
**Parameters:**
- `document` (required): Content to audit
- `standards`: framework name or explicit checklist
- `audit_depth`: surface | thorough | exhaustive
- `include_recommendations` (default: true)
