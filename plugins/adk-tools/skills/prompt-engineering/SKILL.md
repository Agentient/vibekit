---
name: prompt-engineering
version: "1.0"
description: >
  Best practices for engineering high-quality system prompts for AI agents with emphasis on XML structure, clarity, few-shot examples, and token efficiency.
  PROACTIVELY activate for: (1) system prompt creation and optimization, (2) instruction clarity improvement and few-shot example design, (3) XML tag structure implementation and prompt templates.
  Triggers: "system prompt", "optimize prompt", "prompt engineering"
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

# Prompt Engineering: Structured System Prompts for Production Agents

## Core Principles

Effective system prompts are the foundation of reliable AI agents. Well-engineered prompts provide clear role definition, structured instructions, and concrete examples, while maintaining token efficiency and clarity.

**Mandatory Standard**: All Vibekit agents MUST use XML tags to section system prompts for improved model comprehension.

## XML Tag Structure (Required Pattern)

### Standard XML Sections

```xml
<role>
You are a senior software architect specializing in Python development.
Your expertise includes system design, API architecture, and database modeling.
</role>

<instructions>
When analyzing a technical requirement:
1. Read the complete specification
2. Identify core components and their relationships
3. Propose a modular architecture
4. Document key decisions with rationale
5. Highlight potential risks and mitigations
</instructions>

<tools>
You have access to the following tools:
- file_reader: Read source code files
- code_analyzer: Analyze code quality and patterns
- diagram_generator: Create architecture diagrams

Use tools when:
- You need to examine existing code
- Analysis requires data you don't have
- Visual representation would clarify the design
</tools>

<output_format>
Provide your response in this format:

**Analysis Summary**
[Brief overview of the system]

**Architecture Proposal**
[Detailed architecture description]

**Key Decisions**
1. [Decision]: [Rationale]

**Risks & Mitigations**
[Identified risks with mitigation strategies]
</output_format>

<examples>
Example 1: API Design Request
User: "Design a REST API for user management"
Assistant: [Shows complete structured response]

Example 2: Database Schema Design
User: "Create a schema for an e-commerce platform"
Assistant: [Shows complete structured response]
</examples>

<constraints>
- ALWAYS validate input before processing
- NEVER expose sensitive information in responses
- MUST follow the established architectural patterns
- DO NOT make assumptions about undocumented requirements
</constraints>
```

### Why XML Tags?

**Benefits**:
1. **Model Comprehension**: Large language models parse XML structure effectively, understanding section boundaries
2. **Maintainability**: Sections can be updated independently without affecting others
3. **Clarity**: Clear visual separation of different prompt components
4. **Composability**: Sections can be conditionally included or reused across prompts

**Anthropic Research**: Claude models specifically benefit from XML-tagged prompts, showing improved adherence to instructions within tagged sections.

## Role Definition (Opening Section)

### Effective Role Patterns

```xml
<role>
You are [SPECIFIC TITLE] with [X] years of experience in [DOMAIN].

Your core competencies:
- [Competency 1]: [Brief description]
- [Competency 2]: [Brief description]
- [Competency 3]: [Brief description]

Your working style:
- You ask clarifying questions before making assumptions
- You provide step-by-step reasoning for complex decisions
- You cite sources and acknowledge uncertainty when appropriate
</role>
```

**Best Practices**:
- Be specific (not "helpful assistant" but "senior DevOps engineer")
- Include relevant experience areas
- Define behavioral expectations (how agent should work)
- Establish communication style

**Anti-Pattern**:
```xml
<!-- BAD: Vague and generic -->
<role>
You are a helpful AI assistant that answers questions.
</role>

<!-- GOOD: Specific and detailed -->
<role>
You are a principal software engineer specializing in distributed systems
and microservices architecture. You have 10+ years designing large-scale
systems at companies like Google and Netflix.

Your strengths:
- Trade-off analysis for architectural decisions
- Performance optimization and scalability planning
- Clear communication of complex technical concepts
</role>
```

## Instruction Structure (Core Logic)

### Hierarchical Instructions

```xml
<instructions>
## Primary Objective
[One-sentence goal statement]

## When you receive a request:

### Phase 1: Analysis
1. Read all provided context and requirements
2. Identify ambiguities and ask clarifying questions
3. List assumptions you're making
4. Note any missing information needed

### Phase 2: Planning
1. Break down the problem into logical components
2. Identify dependencies between components
3. Propose a high-level approach
4. Present the plan for user approval

### Phase 3: Execution (only after approval)
1. Implement the solution step-by-step
2. Document each decision with rationale
3. Run validation checks
4. Summarize what was accomplished

## Decision-Making Framework
When choosing between options:
- Evaluate technical feasibility
- Consider maintainability and scalability
- Assess security and performance implications
- Document trade-offs clearly
</instructions>
```

**Best Practices**:
- Use hierarchical headings (##, ###) for organization
- Number sequential steps
- Define decision criteria explicitly
- Separate analysis from execution
- Include validation checkpoints

**Anti-Pattern**:
```xml
<!-- BAD: Unstructured wall of text -->
<instructions>
You should analyze the code and find bugs and suggest fixes and make sure
the code is good and follows best practices and has tests and...
</instructions>

<!-- GOOD: Clear, structured steps -->
<instructions>
## Code Review Process

1. **Syntax & Style**
   - Check for linting errors
   - Verify formatting compliance
   - Review naming conventions

2. **Logic & Correctness**
   - Trace execution paths
   - Identify edge cases
   - Check error handling

3. **Testing**
   - Verify test coverage (minimum 80%)
   - Review test quality
   - Suggest missing test cases
</instructions>
```

## Few-Shot Examples (Critical for Reliability)

### Effective Few-Shot Pattern

```xml
<examples>
## Example 1: Simple Query
<user_input>
What's the best way to handle authentication in a REST API?
</user_input>

<assistant_response>
**Analysis**
You're asking about authentication strategies for REST APIs. This is a
foundational security decision that affects the entire system.

**Recommended Approach: JWT with Refresh Tokens**

Rationale:
- Stateless authentication (no server-side session storage)
- Scalable across multiple servers
- Includes expiration for security
- Refresh token pattern prevents constant re-login

**Implementation Pattern**
1. User login returns access token (short-lived, 15 min) + refresh token (long-lived, 7 days)
2. Access token sent in Authorization header: `Bearer <token>`
3. When access token expires, use refresh token to get new access token
4. Refresh tokens stored securely (HTTP-only cookies or secure storage)

**Security Considerations**
- Use HTTPS only
- Implement token rotation
- Add rate limiting on auth endpoints
- Consider multi-factor authentication

**Code Example**
[Provides actual code implementation]
</assistant_response>

## Example 2: Complex Design Task
<user_input>
Design a data pipeline for processing 1M events per second.
</user_input>

<assistant_response>
**Clarifying Questions (Always Ask First)**
1. What's the event payload size?
2. What processing is required (filtering, enrichment, aggregation)?
3. What's the acceptable latency?
4. What's the retention period for raw data?
5. What's the budget constraint?

[Assuming answers provided...]

**Architecture Proposal**
[Shows complete structured response with diagrams]
</assistant_response>

## Example 3: Error Handling
<user_input>
How should I handle errors in async Python code?
</user_input>

<assistant_response>
[Shows structured response with code examples and anti-patterns]
</assistant_response>
</examples>
```

**Why Few-Shot Works**:
- Demonstrates expected response format
- Shows reasoning process
- Establishes quality bar
- Reduces ambiguity

**Guidelines**:
- Include 3-5 diverse examples
- Show edge cases (not just happy path)
- Demonstrate clarifying questions
- Include one example of uncertainty handling

## Output Format Specification

### Structured Output Template

```xml
<output_format>
**Structure your response as follows:**

1. **Summary** (2-3 sentences)
   [High-level overview of the solution]

2. **Detailed Analysis**
   [In-depth explanation with subsections]

3. **Implementation Steps**
   [Numbered, actionable steps]
   Each step should include:
   - What to do
   - Why it's necessary
   - Expected outcome

4. **Code Examples**
   [Well-commented code snippets]
   ```python
   # Example pattern
   ```

5. **Validation & Testing**
   [How to verify the solution works]

6. **Next Steps**
   [What the user should do next]

**Formatting Rules:**
- Use **bold** for section headers
- Use `code blocks` for all code
- Use bullet points for lists
- Use numbered lists for sequences
- Include line breaks between sections
</output_format>
```

**Benefits**:
- Consistent responses
- Easy to parse programmatically
- User knows what to expect
- Improves agent reliability

## Tool Usage Guidance

### Clear Tool Instructions

```xml
<tools>
You have access to these tools:

**file_reader(path: str) -> str**
- Purpose: Read file contents
- When to use: User asks about specific files, you need to verify existing code
- When NOT to use: For general knowledge questions, hypothetical scenarios
- Example: "Read the authentication module to check current implementation"

**code_executor(code: str, language: str) -> dict**
- Purpose: Execute code and return results
- When to use: User wants to test code, verify behavior, run examples
- When NOT to use: For explaining concepts (explain instead), security-sensitive operations
- Example: "Test this sorting algorithm with sample data"

**web_search(query: str) -> list[dict]**
- Purpose: Find current information, documentation, or solutions
- When to use: Need latest framework docs, current best practices, recent changes
- When NOT to use: For knowledge in your training data, coding tasks, architecture design
- Example: "Find the latest Vertex AI SDK release notes"

## Tool Selection Criteria
1. Is the information in your training data? -> Don't use tools
2. Does the user explicitly request a file/search? -> Use tool
3. Would verification improve accuracy? -> Use tool
4. Is it a time-sensitive query? -> Use web_search

## Tool Error Handling
If a tool fails:
1. Acknowledge the failure to the user
2. Explain what went wrong
3. Suggest an alternative approach
4. Never claim success if tool failed
</tools>
```

## Constraints and Guardrails

### Explicit Constraint Definition

```xml
<constraints>
## Must Do
- ALWAYS ask clarifying questions for ambiguous requests
- ALWAYS explain your reasoning for significant decisions
- ALWAYS cite sources when referencing external information
- ALWAYS validate assumptions before proceeding

## Must Never Do
- NEVER make up information (acknowledge uncertainty instead)
- NEVER expose sensitive data (API keys, passwords, PII)
- NEVER execute code that could be harmful or malicious
- NEVER make irreversible changes without explicit user confirmation

## Quality Standards
- Code MUST include type hints and docstrings
- Responses MUST be concise but complete
- Examples MUST be runnable and tested
- Explanations MUST be technically accurate

## When Uncertain
If you're unsure about:
- The user's intent -> Ask clarifying questions
- Technical details -> State assumptions and limitations
- Best approach -> Present options with trade-offs
- Current information -> Use web_search tool or acknowledge gap
</constraints>
```

## Token Efficiency Strategies

### 1. Prompt Compression Techniques

```xml
<!-- BAD: Verbose and repetitive -->
<instructions>
You should analyze the code. When analyzing the code, make sure to check
for bugs. After checking for bugs, you should also check for code quality
issues. Code quality issues include things like...
</instructions>

<!-- GOOD: Concise and clear -->
<instructions>
Analyze code for:
1. Bugs and logic errors
2. Code quality (style, naming, structure)
3. Security vulnerabilities
4. Performance issues
</instructions>
```

### 2. Reference Pattern (for long documents)

```xml
<instructions>
Refer to the coding standards in the adjacent file: `CODING_STANDARDS.md`

For architecture decisions, consult: `docs/architecture/ADR-001-principles.md`

Do not duplicate these documents in your responses. Reference them by name.
</instructions>
```

### 3. Conditional Sections

For multi-purpose agents, define clear mode switching:

```xml
<mode_definitions>
## Mode: Analysis
When user says "analyze" or "review":
- Focus on critique and improvement
- Identify issues and risks
- Suggest alternatives

## Mode: Implementation
When user says "create" or "implement":
- Focus on writing working code
- Include error handling
- Add comprehensive tests

## Mode: Explanation
When user says "explain" or "teach":
- Focus on concepts and reasoning
- Use analogies and examples
- Build from fundamentals
</mode_definitions>
```

## Advanced Patterns

### Chain-of-Thought Prompting

```xml
<reasoning_instructions>
For complex problems, show your thinking process:

**Step 1: Problem Decomposition**
Break the problem into smaller sub-problems.

**Step 2: Information Gathering**
List what you know and what you need to find out.

**Step 3: Solution Exploration**
Consider multiple approaches with pros/cons.

**Step 4: Selection & Justification**
Choose the best approach and explain why.

**Step 5: Implementation Plan**
Provide concrete steps to execute the solution.

Always show this reasoning before your final answer.
</reasoning_instructions>
```

### Self-Critique Pattern

```xml
<self_critique>
After providing a solution:

1. **Assumptions Made**
   List any assumptions in your solution

2. **Potential Issues**
   Identify limitations or edge cases

3. **Alternative Approaches**
   Briefly mention other valid approaches

4. **Confidence Level**
   Rate your confidence: High / Medium / Low
   Explain what factors affect your confidence
</self_critique>
```

## Anti-Patterns to Avoid

### Over-Prompting
```xml
<!-- BAD: Trying to control every detail -->
<instructions>
Always say "Hello" at the start. Then introduce yourself. Then ask if the
user needs help. Then wait for response. Then when they respond, categorize
their request. If it's type A, do X. If it's type B, do Y. If it's type C...
[continues for 500 more lines]
</instructions>

<!-- GOOD: Trust the model's capabilities -->
<instructions>
Greet the user professionally and ask how you can help.
Based on their request, provide relevant assistance.
</instructions>
```

### Conflicting Instructions
```xml
<!-- BAD: Contradictory requirements -->
<instructions>
Be extremely concise. Provide comprehensive explanations with examples.
</instructions>

<!-- GOOD: Clear priority -->
<instructions>
Default to concise responses. Provide detailed explanations when user asks
for clarification or says "explain in detail".
</instructions>
```

### Embedding Examples as Instructions
```xml
<!-- BAD: Examples mixed with instructions -->
<instructions>
Format your response like this: **Title** then content, for example you might
say **Summary** and then write a summary, and also include **Details** and
then add details...
</instructions>

<!-- GOOD: Separate examples section -->
<instructions>
Structure responses with Title, Summary, Details sections.
</instructions>

<examples>
**Title**
User Authentication System

**Summary**
JWT-based authentication with refresh tokens.

**Details**
[Full explanation]
</examples>
```

## Prompt Testing & Iteration

### Testing Checklist

- [ ] Does the prompt produce consistent outputs for the same input?
- [ ] Does it handle edge cases (empty input, unclear requests)?
- [ ] Does it refuse harmful requests appropriately?
- [ ] Are the outputs in the expected format?
- [ ] Does it ask clarifying questions when needed?
- [ ] Is the tone appropriate for the use case?
- [ ] Does it stay within scope (not hallucinating capabilities)?

### Iteration Process

1. **Baseline**: Start with minimal prompt
2. **Test**: Run representative queries
3. **Identify Gaps**: Where does it fail?
4. **Refine**: Add specific instructions for failure cases
5. **Re-test**: Verify improvement without regression
6. **Optimize**: Remove redundant instructions

## When to Use This Skill

Activate this skill when:
- Creating new agent system prompts
- Optimizing existing prompts for clarity
- Debugging agent behavior issues
- Implementing structured output formats
- Designing few-shot examples
- Improving prompt token efficiency

## Integration Points

This skill is **critical for**:
- All agent definitions in Vibekit marketplace
- `adk-fundamentals`: Agent system prompts
- `agent-orchestration`: Multi-agent communication prompts

## Related Resources

For deeper understanding:
- **Anthropic Prompt Engineering**: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Prompt Engineering Guide**: https://www.promptingguide.ai/
- **OpenAI Best Practices**: https://platform.openai.com/docs/guides/prompt-engineering
- **XML Prompt Structure Research**: See Anthropic blog on structured prompts
