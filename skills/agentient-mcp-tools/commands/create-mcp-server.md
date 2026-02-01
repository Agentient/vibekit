# Create MCP Server

Generate a complete Model Context Protocol server with Python 3.13 asyncio patterns, Pydantic V2 schema-first tool definitions, and JSON-RPC 2.0 compliance.

## Instructions

Create a new MCP server implementation with:

1. **Server Scaffolding**: Python 3.13 asyncio.TaskGroup, async context managers
2. **Tool Registry**: Schema-first Pydantic V2 models with strict mode
3. **Resource Exposure**: URI-based resource patterns
4. **Protocol Compliance**: JSON-RPC 2.0 message validation
5. **Testing Suite**: pytest-asyncio tests with protocol compliance validation

**CRITICAL REQUIREMENTS**:
- Use Pydantic V2 strict mode (`model_config = ConfigDict(strict=True)`)
- Use Python 3.13 `asyncio.TaskGroup()` (not `asyncio.gather()`)
- Validate all JSON-RPC 2.0 messages with Pydantic
- Include protocol compliance tests

**Server Structure**:
```
mcp_servers/
├── <server_name>/
│   ├── server.py           # Main server implementation
│   ├── tools/
│   │   ├── __init__.py
│   │   └── schemas.py      # Pydantic tool input/output models
│   ├── resources/
│   │   ├── __init__.py
│   │   └── handlers.py     # Resource read/list handlers
│   ├── tests/
│   │   ├── test_tools.py
│   │   ├── test_resources.py
│   │   └── test_protocol.py
│   └── pyproject.toml      # Dependencies (mcp, pydantic>=2.0)
```

**Example Output**:

When user requests: "Create an MCP server for code search"

Generate:
1. `mcp_servers/code_search/server.py` with async server implementation
2. `mcp_servers/code_search/tools/schemas.py` with SearchInput Pydantic model
3. `mcp_servers/code_search/tests/test_protocol.py` with JSON-RPC validation
4. Complete README with integration instructions

Activate the **mcp-developer-agent** for implementation.
