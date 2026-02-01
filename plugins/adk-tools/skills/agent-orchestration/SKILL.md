---
name: agent-orchestration
version: "1.0"
description: >
  Multi-agent orchestration patterns including coordinator agents, LlmAgent vs WorkflowAgent selection, agent-as-tool pattern, and inter-agent communication via session state.
  PROACTIVELY activate for: (1) multi-agent systems and agent coordination, (2) sub-agent delegation and agent-as-tool implementation, (3) workflow orchestration with LlmAgent and WorkflowAgent.
  Triggers: "multi-agent", "orchestration", "agent team"
core-integration:
  techniques:
    primary: ["structured_decomposition"]
    secondary: []
  contracts:
    input: "none"
    output: "none"
  patterns: "none"
  rubrics: "none"
---

# Agent Orchestration: Multi-Agent System Patterns

## Core Principles

Complex problems often require multiple specialized agents working together. ADK provides robust patterns for orchestrating agent teams, enabling modular, maintainable, and scalable agentic systems.

**Key Insight**: Single monolithic agents with overly complex prompts are harder to maintain and debug than teams of focused specialists coordinated by a simple orchestrator.

## Agent Types: LlmAgent vs WorkflowAgent

### LlmAgent (Dynamic Reasoning)

**Purpose**: For tasks where the next action depends on runtime reasoning and context.

**Characteristics**:
- LLM decides which tool to call and when
- Flexible, adaptive behavior
- Suitable for open-ended problems
- Can handle unexpected inputs

**Use Cases**:
- Conversational assistants
- Complex problem-solving requiring judgment
- Tasks with unpredictable user requests
- Research and analysis workflows

**Example**:
```python
from google import genai
from google.genai import types

async def create_research_agent() -> types.Agent:
    """
    Create LlmAgent for research tasks.

    The agent dynamically decides whether to search, read, or summarize
    based on user questions and intermediate findings.
    """
    client = genai.Client(vertexai=True)

    # Define tools
    search_tool = types.Tool(function_declarations=[...])
    read_tool = types.Tool(function_declarations=[...])
    summarize_tool = types.Tool(function_declarations=[...])

    # LlmAgent with dynamic tool selection
    agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        You are a research assistant. For each user query:
        1. Use search_tool to find relevant sources
        2. Use read_tool to examine source content
        3. Use summarize_tool to synthesize findings

        Adapt your approach based on the query complexity.
        """,
        tools=[search_tool, read_tool, summarize_tool]
    )

    return agent
```

### WorkflowAgent (Deterministic Flow)

**Purpose**: For tasks with predictable, repeatable processes where the execution flow is known in advance.

**Characteristics**:
- Hardcoded execution sequence
- Predictable, reliable behavior
- No LLM reasoning overhead for flow control
- Ideal for automation pipelines

**Types**:
- **SequentialAgent**: Execute agents one after another
- **ParallelAgent**: Execute agents concurrently
- **LoopAgent**: Repeat agent execution with conditions

**Use Cases**:
- Data processing pipelines
- Validation workflows
- Multi-stage transformations
- Scheduled automation tasks

**Example - SequentialAgent**:
```python
from google.genai import types

async def create_document_processor() -> types.SequentialAgent:
    """
    Sequential workflow for document processing.

    Flow: Upload -> Parse -> Validate -> Store (deterministic sequence)
    """
    # Define sub-agents for each stage
    upload_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Validate and upload documents to storage.",
        tools=[upload_tool]
    )

    parse_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Extract structured data from documents.",
        tools=[parse_tool]
    )

    validate_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Validate extracted data against schema.",
        tools=[validate_tool]
    )

    store_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Store validated data in database.",
        tools=[store_tool]
    )

    # Sequential workflow
    workflow = types.SequentialAgent(
        agents=[upload_agent, parse_agent, validate_agent, store_agent]
    )

    return workflow
```

**Example - ParallelAgent**:
```python
async def create_parallel_analyzer() -> types.ParallelAgent:
    """
    Parallel analysis workflow.

    Run sentiment analysis, entity extraction, and summarization
    simultaneously for speed.
    """
    sentiment_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Analyze sentiment of the text.",
        tools=[sentiment_tool]
    )

    entity_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Extract named entities from text.",
        tools=[entity_tool]
    )

    summary_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="Generate concise summary of text.",
        tools=[summary_tool]
    )

    # Parallel execution (faster)
    parallel_workflow = types.ParallelAgent(
        agents=[sentiment_agent, entity_agent, summary_agent]
    )

    return parallel_workflow
```

### Decision Matrix: Which Agent Type?

| Scenario | Agent Type | Rationale |
|----------|------------|-----------|
| Answering unpredictable user questions | LlmAgent | Requires dynamic reasoning |
| Processing uploaded files through fixed steps | SequentialAgent | Deterministic pipeline |
| Running multiple independent analyses | ParallelAgent | No dependencies, gain speed |
| Customer support with varying needs | LlmAgent | Adaptive to user situation |
| Daily report generation | LoopAgent | Repeatable schedule |
| Code review (lint -> test -> analyze) | SequentialAgent | Fixed validation sequence |

## Coordinator Pattern (Recommended Architecture)

### Root Coordinator with Specialist Sub-Agents

**Architecture**: Single coordinator agent dispatches tasks to specialized agents based on request type.

**Benefits**:
- Clear separation of concerns
- Easy to add new specialists
- Simple routing logic
- Improved debuggability

**Implementation**:
```python
from google import genai
from google.genai import types
from pydantic import BaseModel, ConfigDict, Field

# Specialist agents
async def create_code_specialist() -> types.LlmAgent:
    """Agent specialized in code generation and review."""
    return types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        You are a senior software engineer specializing in Python.

        Your responsibilities:
        - Generate production-ready code with type hints
        - Review code for bugs and improvements
        - Suggest optimal algorithms and data structures

        Always follow PEP 8 and include comprehensive docstrings.
        """,
        tools=[code_analyzer_tool, code_formatter_tool]
    )

async def create_architecture_specialist() -> types.LlmAgent:
    """Agent specialized in system architecture."""
    return types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        You are a principal architect with 15+ years experience.

        Your responsibilities:
        - Design scalable system architectures
        - Evaluate trade-offs between approaches
        - Create architecture decision records (ADRs)

        Focus on maintainability, scalability, and security.
        """,
        tools=[diagram_tool, adr_tool]
    )

async def create_test_specialist() -> types.LlmAgent:
    """Agent specialized in testing."""
    return types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        You are a test automation engineer.

        Your responsibilities:
        - Generate comprehensive test suites
        - Design test strategies (unit, integration, e2e)
        - Achieve 80%+ code coverage

        Use pytest patterns and AAA structure.
        """,
        tools=[test_generator_tool, coverage_tool]
    )

# Coordinator agent
async def create_coordinator() -> types.LlmAgent:
    """
    Root coordinator that delegates to specialists.

    Analyzes user requests and routes to appropriate specialist.
    """
    # Create specialist agents
    code_agent = await create_code_specialist()
    arch_agent = await create_architecture_specialist()
    test_agent = await create_test_specialist()

    # Wrap specialists as tools (agent-as-tool pattern)
    code_tool = types.AgentTool(
        agent=code_agent,
        name="code_specialist",
        description="For code generation, review, and optimization tasks"
    )

    arch_tool = types.AgentTool(
        agent=arch_agent,
        name="architecture_specialist",
        description="For system design, architecture decisions, and scalability analysis"
    )

    test_tool = types.AgentTool(
        agent=test_agent,
        name="test_specialist",
        description="For test generation, test strategy, and coverage analysis"
    )

    # Coordinator with specialist tools
    coordinator = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        You are a project coordinator managing specialist engineers.

        Your role:
        1. Analyze user requests
        2. Determine which specialist(s) to consult
        3. Delegate tasks using appropriate specialist tools
        4. Synthesize results into cohesive response

        Available specialists:
        - code_specialist: For implementation and code review
        - architecture_specialist: For system design
        - test_specialist: For testing and quality assurance

        Routing rules:
        - "Create/implement/write code" -> code_specialist
        - "Design/architect/plan system" -> architecture_specialist
        - "Test/coverage/quality" -> test_specialist
        - Complex tasks may require multiple specialists
        """,
        tools=[code_tool, arch_tool, test_tool]
    )

    return coordinator
```

### Using the Coordinator

```python
async def main() -> None:
    """Example usage of coordinator pattern."""
    coordinator = await create_coordinator()
    client = genai.Client(vertexai=True)

    # User request
    user_query = "Design and implement a user authentication system"

    # Coordinator analyzes and delegates
    # 1. Calls architecture_specialist to design system
    # 2. Calls code_specialist to implement
    # 3. Calls test_specialist to generate tests
    # 4. Synthesizes results into complete response

    response = await client.aio.chats.create(
        agent=coordinator
    ).send_message(user_query)

    print(response.text)
```

## Inter-Agent Communication via Session State

### Sharing Data Between Agents

**Pattern**: Use session state to pass context and results between agents in a workflow.

**Example**:
```python
from google.genai import types

async def data_extraction_agent(context: types.ToolContext) -> dict:
    """
    Extract data from document and save to session state.

    Args:
        context: Tool execution context with session state

    Returns:
        Extracted data dictionary
    """
    # Extract data (implement your logic)
    extracted_data = {
        "entities": ["Alice", "Bob", "TechCorp"],
        "dates": ["2025-01-15"],
        "amounts": [150000]
    }

    # Save to session state for next agent
    context.state["extracted_data"] = extracted_data

    return extracted_data

async def data_validation_agent(context: types.ToolContext) -> dict:
    """
    Validate data extracted by previous agent.

    Args:
        context: Tool execution context with session state

    Returns:
        Validation results
    """
    # Retrieve data from session state
    extracted_data = context.state.get("extracted_data", {})

    # Validate data
    validation_results = {
        "valid": True,
        "errors": [],
        "warnings": ["Amount exceeds typical range"]
    }

    # Update session state
    context.state["validation_results"] = validation_results

    return validation_results

async def data_storage_agent(context: types.ToolContext) -> dict:
    """
    Store validated data in database.

    Args:
        context: Tool execution context with session state

    Returns:
        Storage confirmation
    """
    # Retrieve from session state
    extracted_data = context.state.get("extracted_data")
    validation_results = context.state.get("validation_results")

    # Only store if validation passed
    if validation_results.get("valid"):
        # Store data (implement your logic)
        return {"stored": True, "record_id": "12345"}
    else:
        return {"stored": False, "reason": "Validation failed"}
```

**Best Practices**:
- Use session state for lightweight data (< 10KB)
- Clear state after workflow completion
- Document state schema in agent instructions
- Validate state exists before accessing

## Agent-as-Tool Pattern (AgentTool)

### Wrapping Agents as Tools

**Purpose**: Make entire agents callable by other agents, enabling hierarchical delegation.

**Pattern**:
```python
from google.genai import types

# Create specialist agent
specialist_agent = types.LlmAgent(
    model="gemini-2.0-flash-exp",
    system_instruction="You are a database optimization specialist...",
    tools=[query_analyzer_tool, index_advisor_tool]
)

# Wrap as tool
db_specialist_tool = types.AgentTool(
    agent=specialist_agent,
    name="database_optimizer",
    description="Optimize database queries and schema design. Use for slow queries, indexing strategy, or schema refactoring."
)

# Coordinator can now call the specialist
coordinator = types.LlmAgent(
    model="gemini-2.0-flash-exp",
    system_instruction="You coordinate technical specialists...",
    tools=[db_specialist_tool, other_tools...]
)
```

**Benefits**:
- Specialists maintain their own context and tools
- Coordinator stays simple (routing logic only)
- Easy to test specialists in isolation
- Specialists can be reused across coordinators

**When to Use**:
- Complex domain requiring specialized expertise
- Agent has multiple related tools
- Task requires extended reasoning in specific domain
- Want to isolate and test sub-functionality

## Advanced Orchestration Patterns

### Dynamic Agent Selection

```python
async def create_dynamic_coordinator() -> types.LlmAgent:
    """
    Coordinator that dynamically selects agents based on query analysis.
    """
    # Create diverse specialists
    specialists = {
        "python": await create_python_specialist(),
        "typescript": await create_typescript_specialist(),
        "rust": await create_rust_specialist(),
        "devops": await create_devops_specialist(),
        "security": await create_security_specialist()
    }

    # Wrap all as tools
    specialist_tools = [
        types.AgentTool(
            agent=agent,
            name=name,
            description=f"{name.title()} specialist for {name}-related tasks"
        )
        for name, agent in specialists.items()
    ]

    coordinator = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        Analyze user queries and select appropriate specialist(s):

        Query indicators:
        - "Python"/"Django"/"Flask" -> python specialist
        - "TypeScript"/"React"/"Node" -> typescript specialist
        - "Rust"/"performance"/"systems" -> rust specialist
        - "CI/CD"/"deployment"/"Docker" -> devops specialist
        - "security"/"auth"/"encryption" -> security specialist

        For cross-cutting concerns, consult multiple specialists.
        """,
        tools=specialist_tools
    )

    return coordinator
```

### Multi-Stage Pipeline with Error Handling

```python
async def create_robust_pipeline() -> types.SequentialAgent:
    """
    Pipeline with error handling and rollback capabilities.
    """
    # Stage 1: Input validation
    validation_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        Validate input data. Save validation results to session state.
        If validation fails, set state["pipeline_stop"] = True.
        """,
        tools=[validation_tool]
    )

    # Stage 2: Data transformation
    transform_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        Check state["pipeline_stop"]. If True, skip transformation.
        Otherwise, transform data and save to state.
        """,
        tools=[transform_tool]
    )

    # Stage 3: Storage
    storage_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        Check state["pipeline_stop"]. If True, skip storage.
        Otherwise, store data and record transaction ID.
        If storage fails, set state["rollback_needed"] = True.
        """,
        tools=[storage_tool]
    )

    # Stage 4: Cleanup/Rollback
    cleanup_agent = types.LlmAgent(
        model="gemini-2.0-flash-exp",
        system_instruction="""
        If state["rollback_needed"], revert changes.
        Clean up temporary resources.
        Report final status.
        """,
        tools=[rollback_tool, cleanup_tool]
    )

    pipeline = types.SequentialAgent(
        agents=[
            validation_agent,
            transform_agent,
            storage_agent,
            cleanup_agent
        ]
    )

    return pipeline
```

## Anti-Patterns to Avoid

### Monolithic Agent
```python
# BAD: Single agent trying to do everything
giant_agent = types.LlmAgent(
    model="gemini-2.0-flash-exp",
    system_instruction="""
    You are an expert in Python, TypeScript, Rust, DevOps, security,
    databases, networking, machine learning, data science, mobile dev,
    game dev, blockchain... [10 more domains]

    [3000 line prompt trying to cover everything]
    """,
    tools=[100_different_tools]  # Too many!
)
```

**Problem**: Impossible to maintain, debug, or improve. Model gets confused.

**Solution**: Use coordinator pattern with focused specialists.

### Circular Agent Dependencies
```python
# BAD: Agent A calls Agent B which calls Agent A
agent_a = types.LlmAgent(
    tools=[types.AgentTool(agent=agent_b)]  # Calls B
)

agent_b = types.LlmAgent(
    tools=[types.AgentTool(agent=agent_a)]  # Calls A - CIRCULAR!
)
```

**Problem**: Infinite loops, stack overflow.

**Solution**: Design clear hierarchies (coordinator -> specialists, no loops).

### Using WorkflowAgent for Dynamic Tasks
```python
# BAD: Fixed sequence for unpredictable task
workflow = types.SequentialAgent([
    search_agent,  # What if user doesn't need search?
    analyze_agent,
    summarize_agent  # What if there's nothing to summarize?
])
```

**Problem**: Wastes resources on unnecessary steps.

**Solution**: Use LlmAgent for dynamic tasks, WorkflowAgent only for predictable flows.

### Overstuffing Session State
```python
# BAD: Storing large data in session state
context.state["entire_dataset"] = load_1gb_file()  # Too big!
context.state["all_search_results"] = [...]  # Thousands of items
```

**Problem**: Performance degradation, memory issues.

**Solution**: Store references (IDs, paths) in session state, not full data.

## When to Use This Skill

Activate this skill when:
- Designing multi-agent systems
- Choosing between LlmAgent and WorkflowAgent
- Implementing coordinator/dispatcher patterns
- Creating hierarchical agent teams
- Optimizing agent communication
- Debugging multi-agent workflows

## Integration Points

This skill **depends on**:
- `adk-fundamentals`: Single-agent basics
- `agentient-python-core/async-patterns`: Async coordination

This skill **enables**:
- Complex production agent systems
- Modular, maintainable agent architectures

## Related Resources

For deeper understanding:
- **Google ADK Multi-Agent Blog**: https://cloud.google.com/blog/products/ai-machine-learning/build-multi-agentic-systems-using-google-adk
- **Agent Patterns Guide**: https://medium.com/google-cloud/agent-patterns-with-adk-1-agent-5-ways-58bff801c2d6
- **ADK Agents Documentation**: https://google.github.io/adk-docs/agents/
- **Agent-as-Tool Pattern**: https://medium.com/@shins777/how-to-use-adk-tools-part-1-function-tools-and-built-in-tools-6e6100f9dfaa
