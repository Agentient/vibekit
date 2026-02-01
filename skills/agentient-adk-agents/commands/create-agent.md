# Create ADK Agent

Generate a complete ADK (Agent Development Kit) agent with Vertex AI integration, Pydantic tool schemas, and structured system prompt.

## Task

You are tasked with creating a new ADK agent with the following requirements:

### Agent Structure

Create a production-grade ADK agent with:

```
<agent_name>/
├── agent.py           # Main agent definition
├── tools/
│   ├── __init__.py
│   ├── schemas.py     # Pydantic V2 tool schemas
│   └── functions.py   # Async tool implementations
├── config.py          # Vertex AI configuration
├── .env.example       # Environment template
└── README.md          # Usage documentation
```

### Quality Standards (MANDATORY)

All generated code MUST meet these standards:

1. **ADK Requirements**:
   - Agent uses either `LlmAgent` (dynamic reasoning) or `WorkflowAgent` (deterministic flow)
   - All tools registered in agent's `tools` list
   - System prompt uses XML tag structure (`<role>`, `<instructions>`, `<tools>`, etc.)
   - Vertex AI client initialized once and reused

2. **Pydantic V2 Strict Mode**:
   - All tool schemas use `model_config = ConfigDict(strict=True, frozen=True)`
   - Use `model_json_schema()` to generate FunctionDeclaration parameters
   - Field descriptions provided for all model fields (improves function calling)
   - Use `@field_validator` for validation (not V1 `@validator`)

3. **Async Implementation**:
   - All tool functions with I/O are `async def`
   - Comprehensive error handling with try/except blocks
   - Timeouts on all external calls (`asyncio.wait_for()`)
   - Async context managers for resource cleanup

4. **Type Safety**:
   - All functions have complete type annotations
   - Use Python 3.13 built-in generics: `list[T]`, `dict[K, V]`
   - Use union operator: `str | None` (not `Optional[str]`)
   - Pass `mypy --strict` with zero errors

5. **Prompt Engineering**:
   - System prompt uses mandatory XML tag structure
   - Tool usage criteria clearly defined
   - Output format specified
   - Few-shot examples included (2-3)
   - Anti-patterns and constraints documented

### Implementation Steps

1. **Invoke adk-architect-agent**:
   - The architect will analyze requirements
   - Design agent type selection (LlmAgent vs WorkflowAgent)
   - Create Pydantic tool schemas with strict mode
   - Implement async tool functions with error handling
   - Design structured system prompt with XML tags
   - Configure Vertex AI model and safety settings

2. **Generate Files**:
   - Create `agent.py` with complete agent definition
   - Create `tools/schemas.py` with Pydantic BaseModel definitions
   - Create `tools/functions.py` with async tool implementations
   - Create `config.py` with Vertex AI configuration
   - Create `.env.example` with required environment variables
   - Create `README.md` with usage instructions

3. **Quality Checks**:
   - Verify Pydantic models use `strict=True`
   - Verify all tool functions are async
   - Verify system prompt uses XML structure
   - Run `mypy --strict` on generated code
   - Test agent with sample queries

### Example Usage

```bash
# User invokes the command
/create-agent weather_assistant

# Result: Creates weather_assistant/ with:
# - agent.py: LlmAgent with get_weather tool
# - tools/schemas.py: WeatherRequest (Pydantic V2 strict)
# - tools/functions.py: async def get_weather(...)
# - config.py: Vertex AI client initialization
# - .env.example: GOOGLE_CLOUD_PROJECT, etc.
# - README.md: Setup and usage guide
```

### Agent Types Decision Matrix

**Use LlmAgent when:**
- User requests vary unpredictably
- Need dynamic tool selection based on context
- Conversational, adaptive behavior required
- Examples: customer support, research assistant, general Q&A

**Use WorkflowAgent when:**
- Task has predictable, repeatable steps
- Deterministic flow (A → B → C always)
- Automation pipeline or scheduled job
- Examples: document processing, data validation, report generation

### Tool Schema Template

```python
from pydantic import BaseModel, ConfigDict, Field, field_validator

class ToolInputSchema(BaseModel):
    """Tool input schema with strict validation."""
    model_config = ConfigDict(strict=True, frozen=True)

    param1: str = Field(
        description="Clear, specific description for function calling"
    )
    param2: int = Field(
        gt=0,
        description="Positive integer parameter"
    )

    @field_validator('param1')
    @classmethod
    def validate_param1(cls, v: str) -> str:
        if len(v) < 1:
            raise ValueError("param1 cannot be empty")
        return v.lower()
```

### System Prompt Template

```xml
<role>
You are [SPECIFIC ROLE] with expertise in [DOMAIN].
Your communication style is [STYLE].
</role>

<instructions>
## Primary Objective
[One-sentence goal]

## When you receive a request:

### Phase 1: Analysis
1. [Specific step]
2. [Specific step]

### Phase 2: Execution
1. Use [tool_name] to [action]
2. [Next step]
</instructions>

<tools>
**tool_name(param: type) -> return_type**
- Use when: [Specific criteria]
- Don't use when: [Anti-criteria]
- Example: "[Example usage]"
</tools>

<output_format>
Structure your response:
1. **Section 1**
   [Description]
</output_format>

<examples>
## Example 1: [Scenario]
<user_input>[Query]</user_input>
<assistant_response>[Complete response]</assistant_response>
</examples>

<constraints>
## Must Do
- ALWAYS [specific behavior]

## Must Never Do
- NEVER [specific behavior]
</constraints>
```

### Validation Checklist

After generation, the agent MUST:
- ✅ Use LlmAgent or WorkflowAgent appropriately
- ✅ All tool schemas use `ConfigDict(strict=True)`
- ✅ All tool functions are `async def` with error handling
- ✅ System prompt uses complete XML structure
- ✅ FunctionDeclaration descriptions are detailed
- ✅ Safety settings explicitly configured
- ✅ Pass `mypy --strict <agent_name>` with zero errors
- ✅ Include `.env.example` with all required variables

## Prompt

I need to create an ADK agent for **{agent_purpose}** that can **{capabilities}**.

Requirements:
- Domain: {domain}
- Tools needed: {tool_list}
- Agent type preference: {llm_or_workflow}
- Special considerations: {any_constraints}

Please use the adk-architect-agent to design and implement a complete, production-ready ADK agent following all Vibekit quality standards.
