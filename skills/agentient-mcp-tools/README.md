# agentient-mcp-tools

Model Context Protocol (MCP) server integration plugin providing schema-first tool development with Pydantic V2, Python 3.13 asyncio patterns, and JSON-RPC 2.0 compliance.

## Overview

This plugin enables developers to build production-grade MCP servers that integrate with Claude Desktop, exposing custom tools and resources through a standardized protocol.

**Confidence Level**: 99%
**Category**: Backend
**Version**: 1.0.0

## Core Architecture

### Schema-First Development Pattern

```
┌─────────────────────────────────────────┐
│     Pydantic V2 Models (Source of      │
│             Truth)                      │
├─────────────────────────────────────────┤
│ - Strict mode validation                │
│ - Auto-generated JSON Schema            │
│ - Type-safe input/output                │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│      MCP Server Implementation          │
├─────────────────────────────────────────┤
│ - Python 3.13 asyncio.TaskGroup         │
│ - JSON-RPC 2.0 protocol                 │
│ - Tools + Resources                     │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│      Claude Desktop Integration         │
├─────────────────────────────────────────┤
│ - Automatic tool discovery              │
│ - Type-safe invocation                  │
│ - Context provisioning via resources    │
└─────────────────────────────────────────┘
```

**Token Efficiency**: Pydantic handles schema generation, eliminating manual JSON schema writing.

## Components

### 🤖 Agent

#### mcp-developer-agent
**Role**: MCP server development with schema-first patterns, asyncio implementation, and protocol compliance

**Activation**: Keywords like `mcp`, `model context protocol`, `json-rpc`, `pydantic tool`, `mcp server`

**Responsibilities**:
- Schema-first tool development with Pydantic V2 strict mode
- Python 3.13 asyncio patterns (TaskGroup, async context managers)
- JSON-RPC 2.0 protocol compliance
- URI-based resource exposure
- Protocol compliance testing

**Example Use**:
```
User: "Create an MCP server that exposes a code search tool"

Agent: [Plan Mode]
1. Define SearchInput Pydantic model with strict mode
2. Implement async search handler
3. Set up JSON-RPC 2.0 server scaffolding
4. Add protocol compliance tests
5. Generate Claude Desktop integration config
```

### 📝 Commands

#### `/create-mcp-server`
Generate complete MCP server with asyncio scaffolding, tool registry, and testing suite.

```
/create-mcp-server my-code-search
```

**Output**:
- Server scaffolding with Python 3.13 asyncio
- Pydantic V2 tool schemas with strict mode
- Resource exposure patterns
- pytest-asyncio test suite
- Claude Desktop config template

#### `/add-tool`
Add new tool to existing MCP server with schema-first development.

```
/add-tool search_files
```

**Output**:
- Pydantic input/output models (strict mode)
- Async tool handler
- Updated tool registry
- Unit + integration tests

#### `/add-resource`
Add URI-based resource for context provisioning.

```
/add-resource project-docs
```

**Output**:
- URI pattern definition (file://, db://, etc.)
- list_resources handler
- read_resource handler with validation
- Security validation (path traversal prevention)

#### `/test-mcp`
Comprehensive protocol compliance and validation testing.

```
/test-mcp
```

**Output**:
- JSON-RPC 2.0 message validation tests
- Pydantic schema validation tests
- Async execution tests (TaskGroup)
- Integration tests (full request/response cycle)

### 🎓 Skills (6 Total)

All skills follow 3-tier progressive disclosure:

| Skill | Tier 2 Tokens | Purpose |
|-------|---------------|---------|
| mcp-protocol-fundamentals | ~1,900 | JSON-RPC 2.0, tools vs resources, transport layer |
| mcp-server-scaffolding-asyncio | ~2,100 | Python 3.13 asyncio, TaskGroup, server setup |
| mcp-pydantic-tool-definition | ~2,400 | Schema-first patterns, strict mode, validation |
| mcp-resource-exposure-patterns | ~2,300 | URI patterns, list/read handlers, security |
| mcp-advanced-tool-patterns | ~2,500 | Streaming, orchestration, cancellation, batching |
| mcp-protocol-compliance-testing | ~2,400 | pytest-asyncio, protocol tests, coverage |

**Token Budget**:
- Metadata: ~700 tokens (constant)
- Typical MCP server creation: ~5,500 tokens
- Complex multi-tool server: ~9,800 tokens
- Peak (all skills): ~14,300 tokens

## Installation

### Prerequisites

1. **Claude Code 2.0** installed
2. **Python 3.13** or later
3. **MCP SDK**:
   ```bash
   pip install mcp pydantic>=2.0.0 aiofiles
   ```

### Setup

1. Link plugin to Claude Code:
```bash
ln -s /path/to/vibekit/plugins/agentient-mcp-tools ~/.claude/plugins/
```

2. Verify installation:
```
/help
```

You should see: `/create-mcp-server`, `/add-tool`, `/add-resource`, `/test-mcp`

### Configuration

No additional configuration required. Plugin activates on MCP-related keywords.

## Usage Examples

### Example 1: Create MCP Server

```
User: Create an MCP server for code search with regex support

Agent: [Creates server structure]

Generated:
- mcp_servers/code_search/
  - server.py (asyncio.TaskGroup server)
  - tools/schemas.py (SearchInput with strict mode)
  - resources/providers.py (expose project docs)
  - tests/test_protocol.py (JSON-RPC 2.0 tests)
  - pyproject.toml (dependencies)

# server.py snippet
from pydantic import BaseModel, Field, ConfigDict
from mcp.server import Server
import asyncio

class SearchInput(BaseModel):
    model_config = ConfigDict(strict=True)

    pattern: str = Field(..., description="Regex search pattern")
    file_glob: str = Field("**/*.py", description="File pattern")
    max_results: int = Field(100, ge=1, le=1000)

server = Server("code-search")

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "search_code":
        input_data = SearchInput(**arguments)  # Pydantic validates
        return await execute_search(input_data)

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write)
```

### Example 2: Add Resource

```
User: Expose database schemas as MCP resources

Agent: [Adds resource handlers]

# resources/providers.py
@server.list_resources()
async def list_resources():
    schemas = await get_db_schemas()
    return [
        {
            "uri": f"db:///schemas/{schema.name}",
            "name": f"{schema.name} Schema",
            "mimeType": "application/json",
            "description": f"Database schema for {schema.name}"
        }
        for schema in schemas
    ]

@server.read_resource()
async def read_resource(uri: str):
    if uri.startswith("db:///schemas/"):
        table_name = uri.removeprefix("db:///schemas/")
        schema = await fetch_table_schema(table_name)
        return {
            "contents": [{
                "uri": uri,
                "text": json.dumps(schema, indent=2),
                "mimeType": "application/json"
            }]
        }
```

### Example 3: Protocol Compliance Testing

```
User: Add comprehensive tests for the MCP server

Agent: [Generates test suite]

# tests/test_protocol.py
import pytest
from pydantic import ValidationError

@pytest.mark.asyncio
async def test_strict_mode_prevents_coercion():
    """Strict mode blocks type coercion."""
    with pytest.raises(ValidationError):
        SearchInput(
            pattern="test",
            max_results="10"  # String instead of int - FAILS
        )

@pytest.mark.asyncio
async def test_concurrent_tool_execution(mcp_server):
    """Multiple tools execute concurrently."""
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(mcp_server.call_tool("search", {"pattern": "test1"}))
        t2 = tg.create_task(mcp_server.call_tool("search", {"pattern": "test2"}))

    assert t1.result() is not None
    assert t2.result() is not None

@pytest.mark.asyncio
async def test_json_rpc_response_structure(mcp_server):
    """Response follows JSON-RPC 2.0 spec."""
    response = await mcp_server.handle_request({
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": "search", "arguments": {"pattern": "test"}},
        "id": 1
    })

    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 1
    assert "result" in response or "error" in response
```

## Technology Stack

### Core
- **MCP SDK**: JSON-RPC 2.0 protocol implementation
- **Pydantic V2**: Schema-first validation with strict mode
- **Python 3.13**: Modern asyncio (TaskGroup, async context managers)
- **aiofiles**: Async file I/O for resource reading

### Testing
- **pytest**: Test framework
- **pytest-asyncio**: Async test support
- **pytest-cov**: Coverage reporting

### Quality
- **Ruff**: Fast linting + formatting
- **mypy**: Static type checking

## Best Practices

### Schema-First Development
✅ Define Pydantic models first (single source of truth)
✅ Use strict mode to prevent silent coercion
✅ Let Pydantic generate JSON schemas
❌ Never write JSON schemas manually

### Asyncio Patterns
✅ Use `asyncio.TaskGroup()` (Python 3.13)
✅ Use async context managers for cleanup
✅ Use aiofiles/httpx for I/O operations
❌ Never use blocking I/O in async functions
❌ Never use `asyncio.gather()` (outdated)

### Resources vs Tools
✅ Resources for read-only context (docs, schemas, logs)
✅ Tools for actions with side effects (search, create, update)
✅ Validate resource URIs to prevent path traversal
❌ Never use tools for simple read operations

### Testing
✅ Test both valid and invalid inputs (strict mode)
✅ Test JSON-RPC 2.0 message structure
✅ Test concurrent execution with TaskGroup
✅ Coverage target: 90%+ (protocol code: 100%)

## Anti-Patterns

### Schema Definition
❌ Manual JSON schema writing
❌ Missing `model_config = ConfigDict(strict=True)`
❌ Using `any` type or disabling validation
❌ Not validating field constraints

### Async Implementation
❌ Blocking I/O in async functions (requests, open())
❌ Using `asyncio.gather()` instead of `TaskGroup()`
❌ Missing async context manager cleanup
❌ No timeout on external API calls

### Resource Handling
❌ Using tools for read-only operations
❌ Missing URI validation (security risk)
❌ Hardcoded resource lists (should be dynamic)
❌ No path traversal prevention

### Testing
❌ Not testing strict mode validation
❌ Testing async code without `pytest-asyncio`
❌ Only testing happy paths (missing error cases)
❌ Low coverage on protocol compliance code

## Claude Desktop Integration

### Configuration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

### Verification

1. Restart Claude Desktop
2. Check server appears in MCP servers list
3. Test tool invocation

## Troubleshooting

### Server Not Appearing in Claude Desktop

**Issue**: Server doesn't show up in MCP servers list

**Solution**:
```bash
# Verify server runs standalone
python server.py

# Check Claude Desktop logs
tail -f ~/Library/Logs/Claude/mcp*.log

# Ensure absolute paths in config
```

### Pydantic Validation Errors

**Issue**: `ValidationError` on valid-looking input

**Solution**: Check strict mode is enforcing correct types
```python
# Debug validation
try:
    input_data = SearchInput(**arguments)
except ValidationError as e:
    print(e.errors())  # Detailed error info
```

### Async Tool Hangs

**Issue**: Tool execution never completes

**Solution**: Add timeout and check for blocking I/O
```python
# Add timeout
result = await asyncio.wait_for(
    tool_execution(),
    timeout=30.0
)

# Replace blocking calls
# ❌ result = requests.get(url)
# ✅ async with httpx.AsyncClient() as client:
#       result = await client.get(url)
```

## Dependencies

### Required
- **agentient-python-core**: Pydantic patterns, asyncio best practices, type hints

### Optional
None

## Contributing

This plugin follows vibekit quality standards:
- Quality Threshold: 99%
- Schema-first development mandatory
- Python 3.13 asyncio patterns required
- 3-tier progressive disclosure for skills
- Coverage target: 90%+ (protocol: 100%)

## License

Part of the vibekit Claude Code plugin marketplace.

---

**Generated with Claude Code** | Version 1.0.0 | Confidence 99%
