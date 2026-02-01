# agentient-adk-agents

**Production-Grade ADK Agent Development Plugin for Vibekit Marketplace**

Version: 1.0.0
Author: Agentient Labs

---

## Overview

The `agentient-adk-agents` plugin provides comprehensive patterns and tools for building production-grade AI agents using Google's Agent Development Kit (ADK) and Vertex AI. It establishes the foundational standards for ADK development across the Vibekit ecosystem, covering agent architecture, tool composition, prompt engineering, multi-agent orchestration, and RAG integration.

This plugin is **the standard-setter** for ADK agent development in the Vibekit marketplace. All ADK-based agents inherit its patterns and quality requirements.

## Key Features

✅ **ADK Agent Scaffolding**: Complete patterns for creating LlmAgent and WorkflowAgent types
✅ **Pydantic V2 Tool Schemas**: Strict mode validation for reliable function calling
✅ **Vertex AI Integration**: Gemini model configuration, safety settings, streaming responses
✅ **Prompt Engineering**: XML-structured prompts with few-shot examples
✅ **Multi-Agent Orchestration**: Coordinator patterns and agent-as-tool delegation
✅ **RAG Integration**: Vertex AI RAG Engine with mandatory citation extraction
✅ **3 Specialized Agents**: Architecture, prompt optimization, RAG integration
✅ **5 Knowledge Skills**: Progressive disclosure for efficient context management
✅ **4 Slash Commands**: Agent creation, prompt optimization, RAG setup, tool generation

## Plugin Components

### Agents (3)

#### 1. adk-architect-agent

**Specialization**: ADK agent architecture and tool composition

**Use Cases**:
- Designing ADK agent systems (LlmAgent vs WorkflowAgent selection)
- Creating Pydantic V2 tool schemas with strict mode
- Building multi-agent orchestration patterns
- Configuring Vertex AI models and safety settings
- Implementing async tool functions with error handling

**Invocation**:
```bash
# Automatically invoked for ADK architecture tasks
"Design an ADK agent for customer support with RAG knowledge base"
```

**Quality Mandate**: Enforces Pydantic strict mode, async-first patterns, XML prompt structure, and comprehensive error handling.

#### 2. prompt-engineer-agent

**Specialization**: System prompt optimization and clarity

**Use Cases**:
- Analyzing existing prompts for issues
- Applying XML tag structure to prompts
- Creating effective few-shot examples
- Improving instruction clarity and specificity
- Optimizing prompts for token efficiency

**Invocation**:
```bash
# Use /optimize-prompt command or direct request
/optimize-prompt

# Or direct invocation
"Optimize this agent's system prompt for better tool usage"
```

**Quality Mandate**: Ensures all prompts use XML structure, include tool guidance, provide examples, and define clear constraints.

#### 3. rag-integration-agent

**Specialization**: Vertex AI RAG Engine integration

**Use Cases**:
- Creating RAG corpora and managing documents
- Uploading documents to GCS and importing to corpus
- Configuring retrieval parameters (top-k, thresholds)
- Implementing citation extraction from grounding metadata
- Optimizing chunk strategies and retrieval quality

**Invocation**:
```bash
# Use /add-rag command or direct request
/add-rag

# Or direct invocation
"Add RAG to this agent using our company policy documents"
```

**Quality Mandate**: Ensures citation extraction, corpus documentation, anti-hallucination constraints, and source attribution.

### Skills (5)

All skills follow a 3-tier progressive disclosure model for token efficiency:
- **Tier 1**: Metadata (activation criteria) - ~100 tokens
- **Tier 2**: Instructions (core patterns and examples) - 1500-3000 tokens
- **Tier 3**: Resources (on-demand deep reference) - links only

#### 1. adk-fundamentals

**Purpose**: Core ADK agent scaffolding and environment setup

**Covers**:
- Python uv environment setup with ADK installation
- Vertex AI environment configuration (.env templates)
- Basic agent structure (LlmAgent patterns)
- Tool registration and session state
- Project directory organization

**Token Budget**: ~1500 tokens (Tier 2)

**Activation**: Keywords like "create adk agent", "new agent", "setup adk", "AdkApp"

#### 2. vertex-ai-sdk

**Purpose**: Gemini model configuration and Vertex AI SDK usage

**Covers**:
- Model initialization and client reuse
- Generation parameters (temperature, top_p, top_k)
- Safety settings (HarmCategory, HarmBlockThreshold)
- Streaming responses with `generate_content_stream()`
- Function calling patterns
- Endpoint selection (regional vs global)

**Token Budget**: ~2000 tokens (Tier 2)

**Activation**: Keywords like "gemini config", "model parameters", "safety settings", "streaming response"

#### 3. prompt-engineering

**Purpose**: Structured system prompt engineering with XML tags

**Covers**:
- Mandatory XML tag structure (<role>, <instructions>, <tools>, etc.)
- Role definition specificity
- Hierarchical instruction organization
- Few-shot example design (3-5 diverse examples)
- Tool usage guidance patterns
- Output format specification
- Token efficiency strategies

**Token Budget**: ~2800 tokens (Tier 2)

**Critical**: This skill is comprehensive per spec guidance as prompt quality is foundational to agent reliability.

**Activation**: Keywords like "system prompt", "optimize prompt", "xml tags", "few-shot examples"

#### 4. agent-orchestration

**Purpose**: Multi-agent system patterns and coordination

**Covers**:
- LlmAgent vs WorkflowAgent selection criteria
- Coordinator/dispatcher patterns
- Agent-as-tool pattern with AgentTool
- Inter-agent communication via session state
- SequentialAgent, ParallelAgent, LoopAgent patterns
- Dynamic agent selection strategies

**Token Budget**: ~3000 tokens (Tier 2)

**Activation**: Keywords like "multi-agent", "orchestration", "coordinator", "sub-agent", "AgentTool"

#### 5. rag-patterns

**Purpose**: Vertex AI RAG Engine integration and citation extraction

**Covers**:
- RAG pipeline overview (ingest, chunk, embed, index, retrieve, generate)
- Corpus creation and management with Vertex AI SDK
- Document ingestion from GCS with chunking strategies
- RAG tool creation with `Tool.from_retrieval()`
- Grounding metadata extraction (MANDATORY)
- Citation formatting for user display
- Retrieval parameter tuning (top-k, distance threshold)

**Token Budget**: ~2200 tokens (Tier 2)

**Activation**: Keywords like "add rag", "rag pipeline", "corpus", "citations", "grounding_metadata"

### Slash Commands (4)

#### /create-agent

**Purpose**: Generate complete ADK agent with Vertex AI integration

**Usage**:
```bash
/create-agent customer_support
```

**Creates**:
```
customer_support/
├── agent.py           # LlmAgent or WorkflowAgent
├── tools/
│   ├── schemas.py     # Pydantic V2 tool schemas
│   └── functions.py   # Async tool functions
├── config.py          # Vertex AI configuration
├── .env.example       # Environment variables
└── README.md          # Usage guide
```

**Quality Checks**:
- Pydantic models use `strict=True`
- Tool functions are async with error handling
- System prompt uses XML structure
- Safety settings configured

#### /optimize-prompt

**Purpose**: Analyze and improve agent system prompt

**Usage**:
```bash
/optimize-prompt
```

**Provides**:
- Analysis against structure, clarity, completeness criteria
- XML tag structure application
- Hierarchical instruction organization
- Few-shot example generation
- Tool guidance clarification
- Before/after comparison with token counts

**Result**: Optimized prompt with improved consistency and reliability

#### /add-rag

**Purpose**: Integrate Vertex AI RAG Engine into agent

**Usage**:
```bash
/add-rag
```

**Performs**:
- RAG corpus creation with descriptive name
- Document upload to GCS (if needed)
- Document import with chunking strategy
- RAG tool creation with `Tool.from_retrieval()`
- System prompt updates (anti-hallucination constraints)
- Citation extraction implementation
- Test queries with validation

**Result**: RAG-enabled agent with grounded, cited responses

#### /create-tool

**Purpose**: Generate ADK tool with Pydantic schema and async implementation

**Usage**:
```bash
/create-tool get_weather
```

**Creates**:
```
weather_tool/
├── schema.py          # WeatherRequest (Pydantic V2 strict)
├── function.py        # async def get_weather(...)
├── tool.py            # FunctionDeclaration + Tool
└── test_weather.py    # Unit tests
```

**Quality Checks**:
- Pydantic `ConfigDict(strict=True, frozen=True)`
- Async with comprehensive error handling
- Detailed FunctionDeclaration descriptions
- Complete type annotations

### Quality Gate System

#### Hook Configuration

The plugin includes a PostToolUse hook that validates ADK-specific quality standards.

**Configuration**: `hooks/hooks.json`
```json
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [{"type": "prompt", "prompt": "...validation guidance..."}]
    }
  ]
}
```

#### Quality Checks Performed

After Write/Edit operations on ADK code:
1. **Pydantic Strict Mode**: Verify tool schemas use `ConfigDict(strict=True)`
2. **Async Functions**: Verify I/O tool functions are `async def`
3. **XML Prompt Structure**: Verify system prompts use XML tags
4. **Function Descriptions**: Verify FunctionDeclaration descriptions are detailed

**Behavior**:
- Provides guidance when standards not met
- Does not block (prompt-based, not executable script)
- Educates Claude on ADK quality requirements

## Quality Standards

All code generated using this plugin **MUST** meet these standards:

### ADK-Specific Standards

- ✅ Agent type (LlmAgent vs WorkflowAgent) appropriate for task
- ✅ All tools registered in agent's `tools` list during initialization
- ✅ System prompts use complete XML tag structure
- ✅ Session state used for lightweight inter-tool communication (< 10KB)

### Pydantic V2 Compliance (Tool Schemas)

- ✅ All tool schemas use `model_config = ConfigDict(strict=True, frozen=True)`
- ✅ All fields have `Field(description="...")` for function calling
- ✅ Use `model_json_schema()` to generate FunctionDeclaration parameters
- ✅ Use `@field_validator` for validation (NOT V1 `@validator`)
- ✅ No V1 syntax allowed

### Async/Await Standards

- ✅ All tool functions with I/O are `async def`
- ✅ Comprehensive try/except with specific exception types
- ✅ Timeouts on all external calls (`asyncio.wait_for()`)
- ✅ Async context managers for resources (`async with`)
- ✅ No blocking I/O in async functions

### Vertex AI SDK Standards

- ✅ Client initialized once and reused (no per-request initialization)
- ✅ Safety settings explicitly configured (not relying on defaults)
- ✅ FunctionDeclaration descriptions are detailed and specific
- ✅ Streaming used for interactive UIs (`generate_content_stream()`)

### Prompt Engineering Standards

- ✅ All prompts use XML tags: `<role>`, `<instructions>`, `<tools>`, `<output_format>`, `<examples>`, `<constraints>`
- ✅ Instructions hierarchically organized (## Phase 1, ### Step 1)
- ✅ Tool guidance includes "when to use" and "when NOT to use"
- ✅ 2-5 diverse few-shot examples included
- ✅ Output format explicitly specified

### RAG Standards

- ✅ All RAG-enabled agents extract `grounding_metadata`
- ✅ Citations include source URI and text excerpt
- ✅ System prompt includes anti-hallucination constraints
- ✅ Agent instructed to ONLY answer from retrieved documents
- ✅ Agent says "I don't have that information" when not in corpus

## Installation

This plugin is installed as part of the Vibekit plugin system.

**Location**: `plugins/agentient-adk-agents/`

**Dependencies**:
- Python 3.13+
- google-adk (latest)
- google-cloud-aiplatform (latest)
- google-genai (Vertex AI SDK)
- pydantic v2.12+
- aiohttp (for async HTTP)
- **Requires**: `agentient-python-core@vibekit` plugin

**Install dependencies**:
```bash
uv pip install google-adk google-cloud-aiplatform pydantic>=2.12 aiohttp python-dotenv
```

**Environment Setup**:
```bash
# Copy .env.example to .env
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=True

# Optional: Service account authentication
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
```

## Usage Examples

### Example 1: Create Weather Agent with Tools

```bash
# Request agent creation
"Create an ADK agent for weather information with get_weather tool"

# adk-architect-agent activates:
# 1. Analyzes requirements → LlmAgent (dynamic queries)
# 2. Creates WeatherRequest Pydantic schema (strict mode)
# 3. Implements async get_weather() with error handling
# 4. Designs XML-structured system prompt
# 5. Configures Vertex AI with safety settings
# 6. Quality checks pass
```

**Result**: Production-ready weather agent with type-safe tools and structured prompts.

### Example 2: Add RAG to HR Assistant

```bash
/add-rag

Agent: hr_assistant
Documents: gs://my-company-docs/hr-kb/*.pdf
Domain: Employee benefits and policies
Query types: Factual questions about policies

# rag-integration-agent activates:
# 1. Creates "HR Knowledge Base" corpus
# 2. Imports 23 PDF documents (1024 token chunks, 200 overlap)
# 3. Waits for indexing (3 minutes)
# 4. Creates RAG tool with Tool.from_retrieval()
# 5. Updates system prompt with anti-hallucination constraints
# 6. Implements citation extraction
# 7. Tests with "What is the vacation policy?" → 2 citations returned
```

**Result**: RAG-enabled HR assistant with grounded, cited responses.

### Example 3: Optimize Prompt for Better Tool Usage

```bash
/optimize-prompt

Current prompt:
"You are a helpful coding assistant. Answer questions about code."

# prompt-engineer-agent analyzes:
# - Missing XML structure ❌
# - Role too vague ❌
# - No tool guidance ❌
# - No examples ❌

# Generates optimized version with:
# - <role>: "Senior Python engineer with 10+ years..."
# - <instructions>: Hierarchical steps for code review
# - <tools>: Clear when/when-not-to-use criteria
# - <examples>: 3 diverse scenarios (clear, ambiguous, limitation)
# - <constraints>: Must do / Must never do rules

# Token comparison: 87 → 456 tokens (+423% content, +200% reliability)
```

**Result**: Agent with consistent behavior and better tool selection.

### Example 4: Multi-Agent System for Software Development

```bash
"Design a multi-agent system for code generation and testing"

# adk-architect-agent creates:
# 1. code_specialist (LlmAgent): Generates Python code
# 2. test_specialist (LlmAgent): Generates pytest tests
# 3. coordinator (LlmAgent): Routes tasks to specialists

# Uses agent-as-tool pattern:
coordinator_tools = [
    AgentTool(agent=code_specialist, name="code_specialist", ...),
    AgentTool(agent=test_specialist, name="test_specialist", ...)
]

# Coordinator system prompt defines routing logic:
# "Code implementation" → code_specialist
# "Test generation" → test_specialist
```

**Result**: Modular, maintainable multi-agent system with clear separation of concerns.

## Token Efficiency

The Skills architecture dramatically reduces token usage:

**Typical Scenario** (agent creation with tools):
- Metadata (all 5 skills): ~500 tokens
- Active skills (3): ~6000 tokens
- **Total**: ~6500 tokens

**Monolithic Approach** (all content always loaded):
- Total content: ~42,000 tokens

**Efficiency Gain**: ~85% reduction in typical usage

## Integration Points

This plugin serves as a **foundational component** for:

### Depends On (Prerequisites)

**agentient-python-core**:
- **Uses**: Pydantic V2 strict mode patterns, async/await patterns, type hints
- **Skills Needed**: `pydantic-v2-strict`, `async-patterns`, `type-hints-best-practices`
- **Impact**: Tool schemas and async functions inherit quality standards

### Enables (Downstream)

**Custom ADK Agents**:
- Any Vibekit plugin creating ADK agents depends on this plugin's patterns
- Provides reusable skills and agents for ADK development
- Establishes architecture standards for the marketplace

## Architecture Decisions

### Why XML Tags for Prompts?

XML tag structure improves model comprehension by clearly demarcating different sections. Research from Anthropic shows Claude models specifically benefit from XML-tagged prompts, with improved adherence to instructions within tagged sections.

### Why Pydantic Strict Mode Only?

Pydantic's strict mode prevents silent type coercion, which is a common source of bugs in function calling. By enforcing `strict=True` globally for tool schemas, we ensure type contracts are honored exactly, preventing issues like "123" being silently converted to integer 123.

### Why Async-First for Tools?

Modern agents require non-blocking I/O for responsiveness and concurrency. Tools that perform API calls, database queries, or file access must be async to prevent blocking the agent's event loop and enable parallel execution.

### Why Mandatory Citation Extraction?

RAG without citations undermines trustworthiness. Users need to verify information sources. Mandatory citation extraction ensures all RAG responses are grounded and verifiable, preventing hallucination and building user confidence.

### Why LlmAgent vs WorkflowAgent Distinction?

The distinction guides developers to choose the right abstraction:
- **LlmAgent**: Let the model reason (flexible, adaptive)
- **WorkflowAgent**: Hardcode the flow (predictable, efficient)

Using the wrong type leads to either wasted tokens (WorkflowAgent for dynamic tasks) or unreliable behavior (LlmAgent for deterministic processes).

## Troubleshooting

### Agent Not Using Tools Correctly

**Problem**: Agent doesn't call tools when it should, or uses wrong tools.

**Solution**:
1. Check FunctionDeclaration descriptions - are they specific enough?
2. Review system prompt `<tools>` section - is tool guidance clear?
3. Add few-shot examples showing correct tool usage
4. Use `/optimize-prompt` to improve tool guidance

### Pydantic Validation Errors in Function Calling

**Problem**: Agent passes wrong types to tools, causing ValidationError.

**Solution**:
1. Verify tool schema uses `strict=True`
2. Check Field descriptions are clear about expected types
3. Add `@field_validator` for complex validation
4. Improve FunctionDeclaration parameter descriptions

### RAG Not Returning Citations

**Problem**: RAG responses don't include source citations.

**Solution**:
1. Verify grounding_metadata extraction is implemented:
   ```python
   if hasattr(response.candidates[0], 'grounding_metadata'):
       # Extract citations
   ```
2. Check RAG tool was created with `Tool.from_retrieval()`
3. Verify corpus has indexed documents (use `rag.list_files()`)
4. Test with specific factual query to trigger retrieval

### Multi-Agent Coordination Issues

**Problem**: Coordinator agent doesn't properly delegate to specialists.

**Solution**:
1. Verify specialists wrapped with `AgentTool`
2. Check coordinator system prompt clearly defines routing logic
3. Add few-shot examples showing delegation patterns
4. Ensure specialists have distinct, non-overlapping responsibilities

### Async Tool Timeout Errors

**Problem**: Tool functions timing out or hanging.

**Solution**:
1. Verify timeout configured with `asyncio.wait_for()`
2. Check external API/service is responsive
3. Increase timeout value if appropriate
4. Add retry logic with exponential backoff for transient failures

## Contributing

This plugin follows the Vibekit Plugin Specification v2.2.

**Changes must**:
- Maintain backward compatibility with dependent agents
- Pass all quality gates
- Include updated documentation
- Add tests for new features
- Follow ADK best practices

## License

Copyright © 2025 Agentient Labs. All rights reserved.

---

## Quick Reference

### Common Commands
```bash
/create-agent <name>          # Generate ADK agent
/optimize-prompt              # Improve system prompt
/add-rag                      # Integrate RAG Engine
/create-tool <name>           # Generate ADK tool
```

### Quality Tools
```bash
mypy --strict <file>          # Type check
pytest <test_file>            # Run tests
python -m adk.validate        # Validate agent config (if available)
```

### Key Standards
- ADK agent type selection (LlmAgent vs WorkflowAgent)
- Pydantic V2 strict mode for tool schemas
- Async-first for I/O operations
- XML structure for system prompts
- Mandatory citation extraction for RAG

### Agent Type Decision
| Scenario | Agent Type |
|----------|------------|
| Unpredictable user requests | LlmAgent |
| Fixed pipeline steps | WorkflowAgent (Sequential) |
| Independent parallel tasks | WorkflowAgent (Parallel) |
| Conversational support | LlmAgent |

### Retrieval Parameter Tuning
| Use Case | top_k | threshold |
|----------|-------|-----------|
| Precise queries | 5 | 0.2 |
| Balanced (default) | 10 | 0.3 |
| Broad exploration | 20 | 0.5 |

---

**For detailed specifications, see:**
- `.reference/specifications/specification-v2.2.md`
- `.reference/plugin-specs/plugin_spec_agentient-adk-agents.md`
- `.reference/articles/article-1-skills-architecture.md`
- `.reference/articles/article-2-subagent-implementation.md`
