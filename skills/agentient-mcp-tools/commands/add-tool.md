# Add MCP Tool

Add a new tool to an existing MCP server with schema-first Pydantic V2 model definition and async implementation.

## Instructions

Add a new tool to the MCP server by:

1. **Define Pydantic Input Model**: Create strict mode model for tool parameters
2. **Implement Async Handler**: Add async tool execution logic
3. **Register with Server**: Update tool registry and list_tools handler
4. **Add Tests**: Unit tests for Pydantic validation + integration tests for tool execution

**CRITICAL REQUIREMENTS**:
- Tool input MUST be a Pydantic V2 model with `model_config = ConfigDict(strict=True)`
- Tool handler MUST be async (no blocking operations)
- MUST validate JSON-RPC 2.0 message structure
- MUST include both happy path and error case tests

**Pattern**:

```python
# tools/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class NewToolInput(BaseModel):
    """Input schema for new_tool."""
    model_config = ConfigDict(strict=True)

    param1: str = Field(..., description="Parameter description")
    param2: int = Field(default=10, ge=1, le=100, description="Bounded integer")
    option: Literal["opt1", "opt2"] = "opt1"

class NewToolOutput(BaseModel):
    """Output schema for new_tool."""
    model_config = ConfigDict(strict=True)

    result: str
    metadata: dict[str, Any] | None = None

# server.py
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "new_tool":
        # Pydantic validates input automatically
        input_data = NewToolInput(**arguments)

        # Async implementation
        result = await execute_new_tool(input_data)

        # Return Pydantic model (serializes to JSON)
        return NewToolOutput(
            result=result,
            metadata={"timestamp": datetime.utcnow()}
        ).model_dump()

@server.list_tools()
async def list_tools():
    return [
        {
            "name": "new_tool",
            "description": "Tool description",
            "inputSchema": NewToolInput.model_json_schema()
        }
    ]
```

**Anti-Patterns to Avoid**:
- ❌ Manual JSON schema writing (use Pydantic model_json_schema())
- ❌ Synchronous blocking operations in async handlers
- ❌ Missing input validation (strict mode prevents silent coercion)
- ❌ No error handling for invalid tool calls

**Example Workflow**:

User: "Add a tool that searches files by regex pattern"

Generate:
1. `SearchFilesInput` Pydantic model with pattern, file_glob, max_results
2. Async `search_files()` handler using aiofiles
3. Updated tool registry in list_tools()
4. Tests for valid/invalid patterns, edge cases

Activate the **mcp-developer-agent** for implementation.
