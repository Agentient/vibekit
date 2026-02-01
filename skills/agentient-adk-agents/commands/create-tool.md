# Create ADK Tool

Generate a complete ADK tool with Pydantic V2 strict schema and async implementation for reliable function calling.

## Task

You are tasked with creating a new ADK tool that can be used by agents for specific functionality.

### Tool Components

A complete ADK tool includes:

```
Tool Structure:
├── Pydantic Schema (Input Validation)
│   ├── BaseModel with ConfigDict(strict=True, frozen=True)
│   ├── Field descriptions for all parameters
│   └── Custom validators using @field_validator
├── Async Function (Business Logic)
│   ├── async def implementation
│   ├── Comprehensive error handling
│   ├── Timeout configuration
│   └── Type annotations
└── Vertex AI Integration
    ├── FunctionDeclaration with detailed description
    ├── Parameters from model_json_schema()
    └── Tool wrapper
```

### Quality Standards (MANDATORY)

All tools MUST meet these standards:

1. **Pydantic V2 Strict Mode**:
   - Schema uses `model_config = ConfigDict(strict=True, frozen=True)`
   - NO type coercion (strict validation)
   - ALL fields have `Field(description="...")`
   - Use `@field_validator` for custom validation (NOT V1 `@validator`)
   - Use `model_json_schema()` to generate FunctionDeclaration parameters

2. **Async Implementation**:
   - Tool function is `async def` (if any I/O operations)
   - Comprehensive try/except error handling
   - Specific exception types (NOT bare `except`)
   - Timeouts on all external calls (`asyncio.wait_for()`)
   - Async context managers for resources (`async with`)

3. **Type Safety**:
   - Complete type annotations on all parameters and return values
   - Use Python 3.13 built-in generics: `list[str]`, `dict[str, int]`
   - Use union operator: `str | None` (not `Optional[str]`)
   - Pass `mypy --strict` with zero errors

4. **Function Calling Optimization**:
   - FunctionDeclaration `description` is detailed and specific
   - Field descriptions explain purpose and format
   - Examples included in descriptions when helpful
   - Parameter names are clear and unambiguous

5. **Documentation**:
   - Comprehensive docstring with Args, Returns, Raises sections
   - Usage examples in docstring
   - Error cases documented

### Implementation Steps

1. **Invoke adk-architect-agent**:
   - Agent analyzes tool requirements
   - Designs Pydantic schema with strict validation
   - Implements async function with error handling
   - Creates FunctionDeclaration with detailed descriptions
   - Wraps in Tool object
   - Provides usage example

2. **Generate Files**:
   - Create `{tool_name}_schema.py` with Pydantic model
   - Create `{tool_name}_function.py` with async implementation
   - Create `{tool_name}_tool.py` with FunctionDeclaration and Tool
   - Create `test_{tool_name}.py` with unit tests

3. **Quality Checks**:
   - Verify Pydantic model uses `strict=True`
   - Verify function is async with error handling
   - Verify all fields have descriptions
   - Run `mypy --strict` on generated code
   - Run tests to verify functionality

### Pydantic Schema Template

```python
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Literal

class WeatherRequest(BaseModel):
    """
    Request schema for weather tool.

    This schema defines the input parameters for retrieving current weather
    information for a specific location.
    """
    model_config = ConfigDict(
        strict=True,  # MANDATORY: No type coercion
        frozen=True   # MANDATORY: Immutable after creation
    )

    location: str = Field(
        description="City name or location string (e.g., 'San Francisco, CA' or 'London, UK'). Can include city, state/region, and country for disambiguation."
    )

    units: Literal["celsius", "fahrenheit"] = Field(
        default="celsius",
        description="Temperature units for the response. Choose 'celsius' for Celsius (°C) or 'fahrenheit' for Fahrenheit (°F)."
    )

    include_forecast: bool = Field(
        default=False,
        description="Whether to include a 3-day forecast in addition to current conditions. Set to true for forecast, false for current conditions only."
    )

    @field_validator('location')
    @classmethod
    def validate_location(cls, v: str) -> str:
        """Validate location is not empty and normalize."""
        if not v or not v.strip():
            raise ValueError("Location cannot be empty")
        return v.strip()
```

### Async Function Template

```python
import asyncio
import aiohttp
from typing import Any

async def get_weather(request: WeatherRequest) -> dict[str, Any]:
    """
    Retrieve current weather information for a location.

    This function makes an async HTTP request to a weather API and returns
    current conditions, temperature, and optionally a forecast.

    Args:
        request: Weather request with location and configuration

    Returns:
        Dictionary containing:
        - location (str): Resolved location name
        - temperature (float): Current temperature in requested units
        - conditions (str): Current weather conditions (e.g., "sunny", "cloudy")
        - humidity (int): Humidity percentage
        - forecast (list[dict], optional): 3-day forecast if requested

    Raises:
        TimeoutError: If weather API doesn't respond within 10 seconds
        ConnectionError: If weather API is unreachable
        ValueError: If location is not found

    Example:
        >>> request = WeatherRequest(location="San Francisco", units="celsius")
        >>> result = await get_weather(request)
        >>> print(result["temperature"])
        18.5
    """
    try:
        # Apply timeout to entire operation
        async with asyncio.timeout(10.0):
            # Use async context manager for HTTP session
            async with aiohttp.ClientSession() as session:
                # Build API request
                url = "https://api.weather.com/v1/current"
                params = {
                    "location": request.location,
                    "units": request.units,
                    "forecast": str(request.include_forecast).lower()
                }

                # Make async HTTP request
                async with session.get(url, params=params) as response:
                    if response.status == 404:
                        raise ValueError(f"Location not found: {request.location}")

                    if response.status != 200:
                        raise ConnectionError(f"Weather API error: {response.status}")

                    data = await response.json()

                    # Build response
                    result: dict[str, Any] = {
                        "location": data["location"],
                        "temperature": data["temp"],
                        "conditions": data["conditions"],
                        "humidity": data["humidity"]
                    }

                    if request.include_forecast and "forecast" in data:
                        result["forecast"] = data["forecast"]

                    return result

    except asyncio.TimeoutError:
        raise TimeoutError(
            f"Weather API timed out for location: {request.location}"
        )
    except aiohttp.ClientError as e:
        raise ConnectionError(f"Failed to connect to weather API: {e}")
```

### Tool Definition Template

```python
from google.genai import types

# Create FunctionDeclaration
weather_function = types.FunctionDeclaration(
    name="get_weather",
    description=(
        "Retrieve current weather conditions and temperature for any location worldwide. "
        "Returns temperature, conditions (sunny/cloudy/rainy/etc), humidity percentage, "
        "and optionally a 3-day forecast. Use this tool whenever the user asks about "
        "weather, temperature, or current conditions for a specific location."
    ),
    parameters=WeatherRequest.model_json_schema()
)

# Create Tool
weather_tool = types.Tool(
    function_declarations=[weather_function]
)

# Usage in agent
agent = types.LlmAgent(
    model="gemini-2.0-flash-exp",
    system_instruction="""...""",
    tools=[weather_tool]
)
```

### Example Usage

```bash
# User requests new tool
/create-tool get_stock_price

Tool purpose: Retrieve current stock price and basic info for a ticker symbol
Parameters needed:
  - ticker (string): Stock ticker symbol (e.g., "AAPL", "GOOGL")
  - include_stats (boolean): Whether to include trading volume and market cap
Expected behavior: Async API call to stock data service with timeout
Error cases: Invalid ticker, API timeout, market closed

# adk-architect-agent generates complete tool
```

**Result:**
```python
# stock_price_schema.py
class StockPriceRequest(BaseModel):
    model_config = ConfigDict(strict=True, frozen=True)

    ticker: str = Field(
        description="Stock ticker symbol (e.g., 'AAPL' for Apple, 'GOOGL' for Google)"
    )
    include_stats: bool = Field(
        default=False,
        description="Include trading statistics (volume, market cap)"
    )

    @field_validator('ticker')
    @classmethod
    def validate_ticker(cls, v: str) -> str:
        if not v or len(v) > 10:
            raise ValueError("Ticker must be 1-10 characters")
        return v.upper()

# stock_price_function.py
async def get_stock_price(request: StockPriceRequest) -> dict[str, Any]:
    """Retrieve current stock price with comprehensive error handling."""
    try:
        async with asyncio.timeout(5.0):
            # Implementation with proper error handling
            ...
    except asyncio.TimeoutError:
        raise TimeoutError(f"Stock API timed out for {request.ticker}")
    except Exception as e:
        raise ConnectionError(f"Stock API error: {e}")

# stock_price_tool.py
stock_price_function = types.FunctionDeclaration(
    name="get_stock_price",
    description="Get current stock price, change percentage, and optionally trading statistics for any publicly traded stock by ticker symbol.",
    parameters=StockPriceRequest.model_json_schema()
)

stock_price_tool = types.Tool(function_declarations=[stock_price_function])
```

### Tool Categories and Patterns

**Data Retrieval Tools:**
- API calls to external services
- Database queries
- File system reads
- Always async, always with timeouts

**Data Transformation Tools:**
- Text processing
- Format conversion
- Calculations
- Can be sync if no I/O

**Action Tools:**
- Send emails
- Create tickets
- Update records
- Always async, always idempotent if possible

**Agent Tools (Advanced):**
- Wrap another agent as a tool
- Use `types.AgentTool(agent=sub_agent, name="...", description="...")`
- For hierarchical delegation

### Validation Checklist

After generation, verify:
- ✅ Pydantic model uses `ConfigDict(strict=True, frozen=True)`
- ✅ All fields have `Field(description="...")`
- ✅ Custom validators use `@field_validator` (NOT V1 `@validator`)
- ✅ Function is `async def` if any I/O operations
- ✅ Comprehensive try/except with specific exception types
- ✅ Timeouts configured on external calls
- ✅ FunctionDeclaration description is detailed and specific
- ✅ `model_json_schema()` used for parameters
- ✅ Complete type annotations
- ✅ Pass `mypy --strict` with zero errors
- ✅ Unit tests included

### Testing Template

```python
import pytest
from my_tool import MyToolRequest, my_tool_function

@pytest.mark.asyncio
async def test_my_tool_success():
    """Test successful tool execution."""
    request = MyToolRequest(param1="value1", param2=42)
    result = await my_tool_function(request)

    assert result["status"] == "success"
    assert "data" in result

@pytest.mark.asyncio
async def test_my_tool_validation_error():
    """Test Pydantic validation catches invalid input."""
    with pytest.raises(ValueError, match="param1 cannot be empty"):
        MyToolRequest(param1="", param2=42)

@pytest.mark.asyncio
async def test_my_tool_timeout():
    """Test timeout handling."""
    # Mock slow API call
    with pytest.raises(TimeoutError):
        await my_tool_function(request)
```

## Prompt

I need to create an ADK tool for **{tool_purpose}**.

**Requirements:**
- Tool name: {tool_name}
- Input parameters: {parameter_list_with_types}
- Expected behavior: {what_tool_does}
- External dependencies: {api_database_filesystem_etc}
- Error cases: {expected_error_scenarios}

Please use the adk-architect-agent to design and implement a complete ADK tool with Pydantic V2 strict schema, async implementation, and comprehensive error handling following all Vibekit quality standards.
