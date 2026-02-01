# Add MCP Resource

Add a new resource to an MCP server for context provisioning using URI-based patterns.

## Instructions

Add a new resource to expose contextual data to Claude via:

1. **Define Resource URI Pattern**: Choose appropriate URI scheme (file://, db://, api://, etc.)
2. **Implement list_resources Handler**: Return resource metadata (URI, name, mimeType)
3. **Implement read_resource Handler**: Return resource content based on URI
4. **Add Validation**: URI pattern validation and error handling

**CRITICAL REQUIREMENTS**:
- Resources are **app-controlled** (not model-controlled like tools)
- URI patterns MUST be validated before content retrieval
- MUST handle async I/O operations properly
- MUST return proper mimeType (text/plain, text/markdown, application/json, etc.)

**Resource vs Tool**:
- **Resources**: Read-only context provisioning (logs, docs, database schemas)
- **Tools**: Model-controlled actions with side effects (search, create, update)

**Pattern**:

```python
from pydantic import BaseModel, ConfigDict, validator
from typing import Literal

class ResourceUri(BaseModel):
    """Validated resource URI."""
    model_config = ConfigDict(strict=True)

    scheme: Literal["file", "db", "api"]
    path: str

    @validator("path")
    def validate_path(cls, v, values):
        # Custom validation logic
        if values.get("scheme") == "file" and ".." in v:
            raise ValueError("Path traversal not allowed")
        return v

@server.list_resources()
async def list_resources():
    """List available resources."""
    return [
        {
            "uri": "file:///project/README.md",
            "name": "Project Documentation",
            "mimeType": "text/markdown",
            "description": "Main project README"
        },
        {
            "uri": "db:///schemas/users",
            "name": "User Database Schema",
            "mimeType": "application/json"
        }
    ]

@server.read_resource()
async def read_resource(uri: str):
    """Read resource content by URI."""
    # Validate URI structure
    if not uri.startswith(("file:///", "db:///")):
        raise ValueError(f"Unsupported URI scheme: {uri}")

    # Parse and validate
    parsed = ResourceUri(
        scheme=uri.split("://")[0],
        path=uri.split("://")[1]
    )

    # Async content retrieval
    if parsed.scheme == "file":
        async with aiofiles.open(parsed.path, "r") as f:
            content = await f.read()
    elif parsed.scheme == "db":
        content = await fetch_schema_async(parsed.path)

    return {
        "contents": [
            {
                "uri": uri,
                "text": content,
                "mimeType": get_mime_type(parsed.path)
            }
        ]
    }
```

**URI Pattern Examples**:

```
file:///project/docs/api.md          # Local file
db:///schemas/table_name             # Database schema
api:///endpoints/users               # API documentation
log:///app/2024-01-15                # Application logs
```

**Security Considerations**:
- ✅ Validate URI schemes against allowlist
- ✅ Prevent path traversal attacks (../)
- ✅ Sanitize user input in URI paths
- ❌ NEVER expose sensitive data without authorization

**Anti-Patterns**:
- ❌ Using tools for read-only operations (use resources instead)
- ❌ Missing URI validation (security risk)
- ❌ Synchronous file I/O in async handlers
- ❌ Returning binary data as text (use proper base64 encoding)

**Example Workflow**:

User: "Expose project documentation as MCP resources"

Generate:
1. URI pattern: `file:///project/docs/*.md`
2. list_resources() returning all markdown files
3. read_resource() with async file reading
4. Validation for path traversal prevention
5. Tests for valid/invalid URIs

Activate the **mcp-developer-agent** for implementation.
