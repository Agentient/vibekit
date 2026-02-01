# Optimize System Prompt

Analyze and improve an AI agent's system prompt for clarity, structure, and effectiveness using XML tagging and prompt engineering best practices.

## Task

You are tasked with optimizing an existing system prompt to improve agent behavior and reliability.

### Analysis Criteria

The prompt will be evaluated against these dimensions:

```
STRUCTURE:
☐ Uses XML tags for sections (<role>, <instructions>, etc.)
☐ Hierarchical organization (headings, numbered lists)
☐ Logical flow (role → instructions → tools → examples → constraints)
☐ Clear visual separation of components

CLARITY:
☐ Role definition is specific (not vague like "helpful assistant")
☐ Instructions are actionable and testable
☐ No contradicting requirements
☐ Technical terms are defined
☐ Ambiguous phrasing removed

COMPLETENESS:
☐ Tool usage criteria provided
☐ Output format specified
☐ 2-5 diverse examples included
☐ Constraints explicitly stated (must do / must never do)
☐ Edge cases addressed

TOKEN EFFICIENCY:
☐ No redundancy or repetition
☐ Concise phrasing without losing meaning
☐ References used for lengthy content
☐ Conditional sections for multi-mode agents

EFFECTIVENESS:
☐ Examples demonstrate exact expected behavior
☐ Instructions use concrete steps (not abstract principles)
☐ Tool selection logic is clear
☐ Agent knows when to ask clarifying questions
```

### Optimization Process

1. **Invoke prompt-engineer-agent**:
   - Agent analyzes current prompt against criteria
   - Identifies issues (vague role, missing structure, unclear tool guidance)
   - Applies XML tag structure if missing
   - Refines instructions for specificity
   - Adds missing examples
   - Optimizes token usage

2. **Comparison Report**:
   - Original vs optimized versions side-by-side
   - Specific improvements explained
   - Token count comparison
   - Expected behavior improvements
   - Test cases to validate improvements

3. **Validation**:
   - Verify XML structure is complete
   - Ensure no contradictions introduced
   - Confirm token efficiency maintained
   - Check examples are diverse and representative

### Common Issues Fixed

**Issue 1: Vague Role**
```xml
<!-- ❌ BEFORE -->
<role>You are a helpful AI assistant.</role>

<!-- ✅ AFTER -->
<role>
You are a senior Python architect with 10+ years experience in distributed
systems and microservices. You specialize in trade-off analysis,
performance optimization, and clear technical communication.
</role>
```

**Issue 2: Unstructured Instructions**
```xml
<!-- ❌ BEFORE -->
<instructions>
Analyze code, find bugs, suggest improvements, check style, and make sure
tests are good.
</instructions>

<!-- ✅ AFTER -->
<instructions>
## Code Review Process

### Phase 1: Analysis
1. Read complete code file
2. Identify purpose and scope
3. Note immediate syntax/logic errors

### Phase 2: Quality Check
1. **Style**: PEP 8 compliance, naming conventions
2. **Logic**: Execution paths, edge cases
3. **Testing**: Coverage verification (80%+ required)

### Phase 3: Recommendations
Provide prioritized list:
- Critical issues (must fix immediately)
- Important improvements (should fix soon)
- Optional enhancements (nice to have)
</instructions>
```

**Issue 3: Missing Tool Guidance**
```xml
<!-- ❌ BEFORE -->
<tools>
You have file_reader and web_search tools.
</tools>

<!-- ✅ AFTER -->
<tools>
**file_reader(path: str) -> str**
- Use when: User mentions specific files, need to verify code
- Don't use when: General concepts, hypothetical scenarios
- Example: "Read src/auth.py to check login implementation"

**web_search(query: str) -> list[dict]**
- Use when: Need current info, latest docs, recent changes
- Don't use when: Info in training data, coding tasks
- Example: "Search for 'Vertex AI 2025 new features'"

## Tool Selection Logic
1. Is info in your training data? → No tools needed
2. User explicitly requests file? → Use file_reader
3. Time-sensitive query? → Use web_search
</tools>
```

**Issue 4: No Examples**
```xml
<!-- ❌ BEFORE -->
[No examples section]

<!-- ✅ AFTER -->
<examples>
## Example 1: Clear Request
<user_input>
Write a function to validate email addresses.
</user_input>

<assistant_response>
**Implementation**
```python
import re

def is_valid_email(email: str) -> bool:
    """
    Validate email address format.

    Args:
        email: Email string to validate

    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

**Test Cases**
```python
assert is_valid_email("user@example.com") == True
assert is_valid_email("invalid.email") == False
```
</assistant_response>

## Example 2: Ambiguous Request
<user_input>
Make the code better.
</user_input>

<assistant_response>
**Clarifying Questions**
To improve the code effectively, I need more context:

1. Which code file? (please specify path)
2. What aspect to improve?
   - Performance (speed, memory)?
   - Readability (structure, naming)?
   - Correctness (bugs, edge cases)?
   - Maintainability (modularity, documentation)?
3. Are there specific issues you've noticed?

Please provide these details so I can give targeted recommendations.
</assistant_response>

## Example 3: Limitation Handling
<user_input>
What will the stock price be tomorrow?
</user_input>

<assistant_response>
**Cannot Predict Future Stock Prices**
I cannot predict future stock prices. Stock markets are influenced by
countless unpredictable factors.

**What I Can Help With:**
- Analyze historical stock performance
- Explain technical indicators
- Review company fundamentals
- Discuss investment strategies

Would you like help with any of these instead?
</assistant_response>
</examples>
```

### Example Usage

```bash
# User provides current prompt
/optimize-prompt

Current system prompt:
"You are a helpful assistant that answers questions about code.
Try to be accurate and provide examples when possible."

# prompt-engineer-agent analyzes and optimizes
```

**Result:**
```
ANALYSIS:
- Missing XML structure ❌
- Role too vague ❌
- No tool guidance ❌
- No examples ❌
- No constraints ❌

OPTIMIZED PROMPT:
[Complete XML-structured prompt with all sections]

IMPROVEMENTS:
1. Added XML tags for structure (+300% comprehension)
2. Specified role as "Senior Python Engineer"
3. Added 3 diverse examples
4. Defined output format
5. Added explicit constraints

TOKEN COMPARISON:
- Original: 87 tokens
- Optimized: 456 tokens (+423% more content, +200% better results)

EXPECTED IMPROVEMENTS:
- More consistent responses
- Better tool usage decisions
- Clearer output format
- Handles edge cases appropriately
```

### Validation Checklist

After optimization, verify:
- ✅ All major sections use XML tags
- ✅ Role is specific (domain, expertise, style)
- ✅ Instructions are hierarchical and actionable
- ✅ Tool guidance includes when/when not to use
- ✅ 2-5 diverse examples included
- ✅ Constraints explicitly stated
- ✅ Output format specified
- ✅ No contradictions introduced
- ✅ Token efficiency maintained (concise but complete)

### Testing Recommendations

After deploying optimized prompt:

1. **Consistency Test**: Run same query 5 times, verify consistent responses
2. **Edge Case Test**: Try ambiguous/unclear queries, verify clarifying questions
3. **Tool Usage Test**: Verify correct tool selection for various scenarios
4. **Format Test**: Verify output follows specified format
5. **Constraint Test**: Verify agent follows must/must-never rules

## Prompt

I need to optimize this system prompt:

```
{current_prompt}
```

**Context:**
- Agent purpose: {agent_purpose}
- Current issues: {observed_problems}
- Tools available: {tool_list}
- Desired improvements: {improvement_goals}

Please use the prompt-engineer-agent to analyze and optimize this prompt following all Vibekit prompt engineering standards.
