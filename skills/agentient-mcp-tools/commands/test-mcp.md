# Test MCP Server

Comprehensive testing suite for MCP server protocol compliance, tool validation, and async operation correctness.

## Instructions

Generate a complete testing suite covering:

1. **Protocol Compliance**: JSON-RPC 2.0 message structure validation
2. **Pydantic Validation**: Input/output schema enforcement
3. **Async Operations**: Proper coroutine execution and TaskGroup usage
4. **Error Handling**: Invalid tool calls, malformed requests, edge cases
5. **Integration Tests**: Full request/response cycle

**CRITICAL REQUIREMENTS**:
- Use pytest-asyncio for async test execution
- Test both valid and invalid inputs (Pydantic strict mode)
- Validate JSON-RPC 2.0 response structure
- Test concurrent tool execution with asyncio.TaskGroup
- Coverage target: 90%+ (protocol code requires 100%)

**Test Structure**:

```
tests/
├── conftest.py              # Shared fixtures
├── test_protocol.py         # JSON-RPC 2.0 compliance
├── test_tools.py            # Tool execution and validation
├── test_resources.py        # Resource read/list operations
├── test_schemas.py          # Pydantic model validation
└── test_integration.py      # Full request/response cycle
```

**Example Test Patterns**:

### 1. Protocol Compliance Tests

```python
import pytest
from pydantic import ValidationError
from server.protocol import JsonRpcRequest, JsonRpcResponse

@pytest.mark.asyncio
async def test_valid_json_rpc_request():
    """Valid JSON-RPC 2.0 request passes validation."""
    request = JsonRpcRequest(
        jsonrpc="2.0",
        method="tools/call",
        params={"name": "search", "arguments": {"query": "test"}},
        id=1
    )
    assert request.jsonrpc == "2.0"
    assert request.method == "tools/call"

@pytest.mark.asyncio
async def test_invalid_jsonrpc_version():
    """Invalid jsonrpc version raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        JsonRpcRequest(
            jsonrpc="1.0",  # Invalid version
            method="tools/call",
            id=1
        )
    assert "jsonrpc" in str(exc_info.value)
```

### 2. Pydantic Schema Validation Tests

```python
from server.tools.schemas import SearchInput

@pytest.mark.asyncio
async def test_search_input_valid():
    """Valid SearchInput passes strict mode validation."""
    input_data = SearchInput(
        query="test",
        limit=10,
        filter_type="code"
    )
    assert input_data.query == "test"
    assert input_data.limit == 10

@pytest.mark.asyncio
async def test_search_input_type_coercion_blocked():
    """Strict mode prevents silent type coercion."""
    with pytest.raises(ValidationError) as exc_info:
        SearchInput(
            query="test",
            limit="10"  # String instead of int - strict mode fails
        )
    assert "int" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_search_input_boundary_validation():
    """Field constraints are enforced (ge=1, le=100)."""
    with pytest.raises(ValidationError):
        SearchInput(query="test", limit=0)  # Below minimum

    with pytest.raises(ValidationError):
        SearchInput(query="test", limit=101)  # Above maximum
```

### 3. Async Tool Execution Tests

```python
import asyncio
import pytest

@pytest.mark.asyncio
async def test_tool_async_execution(mcp_server):
    """Tools execute asynchronously without blocking."""
    start = asyncio.get_event_loop().time()

    # Execute multiple tools concurrently using TaskGroup
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(mcp_server.call_tool("search", {"query": "test1"}))
        t2 = tg.create_task(mcp_server.call_tool("search", {"query": "test2"}))

    duration = asyncio.get_event_loop().time() - start

    # Concurrent execution should be faster than sequential
    assert duration < 2.0  # Adjust based on expected tool latency
    assert t1.result() is not None
    assert t2.result() is not None

@pytest.mark.asyncio
async def test_tool_error_handling(mcp_server):
    """Invalid tool calls return proper JSON-RPC error responses."""
    response = await mcp_server.call_tool("nonexistent_tool", {})

    assert response["error"] is not None
    assert response["error"]["code"] == -32601  # Method not found
    assert "nonexistent_tool" in response["error"]["message"]
```

### 4. Resource Tests

```python
@pytest.mark.asyncio
async def test_list_resources(mcp_server):
    """list_resources returns valid resource descriptors."""
    resources = await mcp_server.list_resources()

    assert len(resources) > 0
    for resource in resources:
        assert "uri" in resource
        assert "name" in resource
        assert "mimeType" in resource
        assert resource["uri"].startswith(("file://", "db://", "api://"))

@pytest.mark.asyncio
async def test_read_resource_valid_uri(mcp_server):
    """read_resource returns content for valid URI."""
    result = await mcp_server.read_resource("file:///project/README.md")

    assert "contents" in result
    assert len(result["contents"]) == 1
    assert result["contents"][0]["uri"] == "file:///project/README.md"
    assert "text" in result["contents"][0]

@pytest.mark.asyncio
async def test_read_resource_invalid_uri(mcp_server):
    """read_resource raises error for invalid URI."""
    with pytest.raises(ValueError) as exc_info:
        await mcp_server.read_resource("file:///../etc/passwd")  # Path traversal
    assert "traversal" in str(exc_info.value).lower()
```

### 5. Integration Tests

```python
@pytest.mark.asyncio
async def test_full_request_response_cycle(mcp_server):
    """Complete JSON-RPC 2.0 request/response cycle."""
    # Construct JSON-RPC request
    request = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "search",
            "arguments": {"query": "test", "limit": 5}
        },
        "id": 123
    }

    # Process request
    response = await mcp_server.handle_request(request)

    # Validate response structure
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 123
    assert "result" in response or "error" in response

    if "result" in response:
        # Tool succeeded - validate output
        assert isinstance(response["result"], dict)
```

**Fixtures (conftest.py)**:

```python
import pytest
from server import create_mcp_server

@pytest.fixture
async def mcp_server():
    """Fixture providing initialized MCP server."""
    server = await create_mcp_server("test-server")
    yield server
    await server.cleanup()

@pytest.fixture
def sample_tool_input():
    """Fixture providing valid tool input."""
    return {
        "query": "test query",
        "limit": 10,
        "filter_type": "code"
    }
```

**Running Tests**:

```bash
# Run all tests with coverage
pytest --cov=server --cov-report=html --cov-report=term

# Run only protocol compliance tests
pytest tests/test_protocol.py -v

# Run async tests with detailed output
pytest -v -s --asyncio-mode=auto
```

**Coverage Requirements**:
- Protocol compliance code: 100%
- Tool implementations: 90%+
- Resource handlers: 90%+
- Overall: 90%+

Activate the **mcp-developer-agent** for implementation.
