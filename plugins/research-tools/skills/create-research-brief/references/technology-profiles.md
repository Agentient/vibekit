# Technology Family Profiles

Pre-built scope templates and dimension weighting for common technology families. Load this reference during research design when the research type is **Best Practices** to accelerate topic scoping.

## How to Use

1. Identify which technology family the user's topic belongs to
2. Use the family profile as a starting point for scope boundaries and dimension weights
3. Adapt to the specific technology — profiles are templates, not rigid prescriptions
4. If the technology doesn't fit any family, scope from scratch using the 8 dimensions

---

## Serverless Functions
**Examples**: Firebase Functions, AWS Lambda, Azure Functions, Cloudflare Workers, Vercel Edge Functions

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | Medium | Runtime matters but setup is usually straightforward |
| Idiomatic Patterns | **High** | Cold start, connection pooling, global scope patterns are critical |
| Anti-Patterns | **High** | Stateless execution model is widely misunderstood |
| Testing & Validation | Medium | Emulator fidelity varies significantly by platform |
| Dependencies & Versions | Medium | Bundle size matters; dependency bloat causes cold starts |
| Operational Awareness | **High** | Cost, concurrency, timeouts, cold starts — the core operational concerns |
| Decision Trees | **High** | Function types, trigger types, when-to-use-functions-at-all decisions |
| Escape Hatches | Medium | Platform limitations are well-documented but workarounds are scattered |
| **Gemini File Search Value** | **Medium** | Upload function configs, deployment manifests for project-specific guidance |

**Scope Template**:
```yaml
in_scope:
  - Function types (HTTP, triggered, scheduled, callable)
  - Deployment and configuration
  - Cold start optimization
  - Connection and resource management
  - Error handling and retry semantics
  - Integration with platform services (auth, database, storage, queues)
  - Cost optimization patterns
out_of_scope:
  - Alternative serverless platforms (unless for decision context)
  - Container-based alternatives (unless for eject-decision context)
  - Frontend/client-side code
```

**Key Questions to Prioritize**:
- How to minimize cold starts without overprovisioning
- When to use each function type (HTTP vs. callable vs. event-triggered)
- Global scope patterns for connection reuse
- Idempotency requirements for triggered functions

---

## Databases & Data Stores
**Examples**: Firestore, DynamoDB, MongoDB Atlas, Supabase, PlanetScale, Redis, Elasticsearch

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | Medium | Connection setup and SDK configuration matters |
| Idiomatic Patterns | **High** | Data modeling patterns define application quality |
| Anti-Patterns | **High** | Schema design mistakes are expensive to fix |
| Testing & Validation | Medium | Local emulators vary in fidelity |
| Dependencies & Versions | **High** | SDK version compatibility is a common pain point |
| Operational Awareness | **High** | Cost is directly tied to read/write patterns |
| Decision Trees | **High** | When to denormalize, shard, index, use subcollections |
| Escape Hatches | Medium | Platform limitations shape data model decisions |
| **Gemini File Search Value** | **High** | Upload schema files, migration scripts, security rules for project-specific guidance |

**Scope Template**:
```yaml
in_scope:
  - Data modeling patterns for the specific database type
  - Query optimization and indexing strategies
  - Transaction and consistency patterns
  - Security rules and access control
  - Offline/caching strategies (if applicable)
  - Migration and schema evolution patterns
  - Cost model tied to access patterns
out_of_scope:
  - Alternative databases (unless for decision context)
  - Data warehouse or analytics use cases
  - Full ETL pipeline design
```

---

## Frontend Frameworks
**Examples**: Next.js, React, Vue, Svelte, Astro, Remix, Angular

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | **High** | Build tooling, rendering modes, deployment targets vary significantly |
| Idiomatic Patterns | **High** | Component architecture, state management, data fetching patterns |
| Anti-Patterns | Medium | Most are well-documented; focus on framework-specific traps |
| Testing & Validation | **High** | Component testing, E2E testing, visual regression are all relevant |
| Dependencies & Versions | Medium | Ecosystem is large but mature |
| Operational Awareness | Medium | Performance budgets, bundle analysis, caching strategies |
| Decision Trees | **High** | Rendering strategy (SSR/SSG/ISR/CSR), state management, routing |
| Escape Hatches | Low | Mature ecosystem with many alternatives |
| **Gemini File Search Value** | **Medium** | Upload component examples, build configs for project-specific guidance |

**Scope Template**:
```yaml
in_scope:
  - Rendering strategies and when to use each
  - Component architecture patterns
  - State management approaches
  - Data fetching and caching patterns
  - Performance optimization (bundle size, rendering, hydration)
  - Testing strategies by component type
  - Deployment and hosting patterns
out_of_scope:
  - CSS framework comparison (unless specifically asked)
  - Backend API design
  - Alternative frontend frameworks
```

---

## Infrastructure-as-Code
**Examples**: Terraform, Pulumi, CDK, CloudFormation, Bicep

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | **High** | State management, provider configuration, workspace/stack setup |
| Idiomatic Patterns | Medium | Module structure, naming, composition patterns |
| Anti-Patterns | **High** | State corruption, circular dependencies, drift management |
| Testing & Validation | Medium | Testing IaC is notoriously difficult |
| Dependencies & Versions | Medium | Provider version pinning matters |
| Operational Awareness | Medium | State management, plan/apply workflows |
| Decision Trees | **High** | Module vs. inline, workspace strategy, import vs. recreate |
| Escape Hatches | **High** | Provider bugs and workarounds are frequent |
| **Gemini File Search Value** | **High** | Upload current terraform/CDK files, state configs for project-specific guidance |

**Scope Template**:
```yaml
in_scope:
  - Module design and composition patterns
  - State management and backend configuration
  - Variable and output patterns
  - Resource lifecycle management
  - Drift detection and remediation
  - CI/CD integration for IaC
  - Multi-environment patterns
out_of_scope:
  - Cloud provider service details (focus on IaC patterns)
  - Alternative IaC tools (unless for decision context)
  - Application deployment (distinct from infrastructure)
```

---

## API Development
**Examples**: Express, FastAPI, NestJS, Flask, Spring Boot, Hono, tRPC

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | Medium | Framework setup is usually straightforward |
| Idiomatic Patterns | **High** | Middleware, routing, validation, error handling patterns |
| Anti-Patterns | **High** | Security vulnerabilities, N+1 queries, error swallowing |
| Testing & Validation | **High** | API testing is well-established but patterns vary by framework |
| Dependencies & Versions | Medium | Auth, validation, ORM packages matter |
| Operational Awareness | Medium | Rate limiting, caching, connection management |
| Decision Trees | Medium | REST vs. GraphQL, auth strategy, validation layer placement |
| Escape Hatches | Low | Mature ecosystem |
| **Gemini File Search Value** | **Low** | Well-documented publicly; project files add limited value |

---

## CI/CD & DevOps Tools
**Examples**: GitHub Actions, GitLab CI, CircleCI, ArgoCD, Flux

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | **High** | Runner configuration, secrets, caching setup |
| Idiomatic Patterns | Medium | Workflow composition, reusable actions/jobs |
| Anti-Patterns | **High** | Security (secret exposure), performance (unnecessary runs), reliability |
| Testing & Validation | Medium | Testing CI pipelines is difficult; focus on debugging patterns |
| Dependencies & Versions | Medium | Action/orb versioning, runner image versions |
| Operational Awareness | **High** | Cost (build minutes), caching, parallelism, artifact management |
| Decision Trees | Medium | When to run, what to cache, monorepo strategies |
| Escape Hatches | Medium | Platform-specific limitations and workarounds |
| **Gemini File Search Value** | **Medium** | Upload pipeline configs, workflow definitions for project-specific guidance |

---

## AI/ML SDKs & Platforms
**Examples**: LangChain, LlamaIndex, Anthropic SDK, OpenAI SDK, Vertex AI, ADK, MCP

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | Medium | SDK setup and authentication |
| Idiomatic Patterns | **High** | Prompt patterns, chain/graph composition, memory management |
| Anti-Patterns | **High** | Token waste, prompt injection, context window mismanagement |
| Testing & Validation | **High** | Eval-driven development, non-deterministic output testing |
| Dependencies & Versions | **High** | Rapidly evolving APIs, breaking changes are frequent |
| Operational Awareness | **High** | Token costs, rate limits, latency, fallback strategies |
| Decision Trees | **High** | Model selection, RAG vs. fine-tuning, agent vs. chain, tool selection |
| Escape Hatches | **High** | APIs change frequently; workarounds have short shelf lives |
| **Gemini File Search Value** | **High** | Upload current agent configs, prompt files, tool definitions for project-specific guidance |

**Scope Template**:
```yaml
in_scope:
  - SDK configuration and authentication
  - Prompt engineering patterns for the platform
  - Agent/chain/graph architecture patterns
  - Error handling and retry patterns (rate limits, timeouts)
  - Cost optimization (token management, caching, model routing)
  - Evaluation and testing patterns
  - Tool/function calling patterns
out_of_scope:
  - Model training or fine-tuning
  - Alternative AI platforms (unless for decision context)
  - General prompt engineering theory
```

---

## Mobile Development
**Examples**: React Native, Flutter, SwiftUI, Kotlin Compose, Expo

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | **High** | Build tooling, device targets, platform-specific configuration |
| Idiomatic Patterns | **High** | Navigation, state management, platform-specific patterns |
| Anti-Patterns | **High** | Performance pitfalls, memory leaks, platform guideline violations |
| Testing & Validation | **High** | Device testing, screenshot testing, accessibility testing |
| Dependencies & Versions | **High** | Native module compatibility is a major pain point |
| Operational Awareness | Medium | App size, startup time, battery impact |
| Decision Trees | **High** | Native vs. cross-platform, navigation library, state management |
| Escape Hatches | Medium | Platform-specific workarounds for OS version issues |
| **Gemini File Search Value** | **Low** | Well-documented publicly; project files add limited value |

---

## AI Agent Frameworks
**Examples**: ADK, LangGraph, CrewAI, AutoGen, Semantic Kernel

**Dimension Weighting**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Environmental Context | Medium | SDK setup and model provider configuration are straightforward |
| Idiomatic Patterns | **High** | Agent orchestration, tool composition, memory/state management patterns |
| Anti-Patterns | **High** | Unbounded loops, context window overflow, tool misrouting, prompt injection |
| Testing & Validation | Medium-High | Agent evaluation is emerging but non-deterministic output testing is critical |
| Dependencies & Versions | **High** | Rapidly evolving APIs; framework-to-model compatibility shifts frequently |
| Operational Awareness | **High** | Token costs, latency budgets, rate limits, fallback chains, observability |
| Decision Trees | **High** | Single-agent vs. multi-agent, framework selection, tool vs. retrieval, orchestration patterns |
| Escape Hatches | **High** | Young ecosystem; breaking changes are frequent, workarounds have short shelf lives |
| **Gemini File Search Value** | **High** | Upload orchestration configs, agent definitions, tool schemas for project-specific guidance |

**Scope Template**:
```yaml
in_scope:
  - Agent architecture patterns (single-agent, multi-agent, hierarchical)
  - Tool/function definition and routing strategies
  - Memory and state management across turns and sessions
  - Orchestration patterns (sequential, parallel, conditional branching)
  - Error handling, retry logic, and graceful degradation
  - Cost optimization (token management, model routing, caching)
  - Evaluation and testing patterns for non-deterministic outputs
  - Safety patterns (prompt injection defense, output validation, guardrails)
out_of_scope:
  - Model training or fine-tuning
  - Alternative agent frameworks (unless for decision context)
  - General prompt engineering theory
  - Underlying LLM API details (unless relevant to framework behavior)
```

**Key Questions to Prioritize**:
- When to use single-agent vs. multi-agent architectures
- How to design tool schemas that minimize misrouting
- State management patterns for long-running agent workflows
- Cost-effective model routing strategies (cheap model for planning, capable model for execution)
- How to test and evaluate agent behavior reliably

---

## Unknown Technologies

If the user's technology doesn't fit any of the 8 families above:

1. **Classify by characteristics**:
   - Runtime/execution environment? → Lean toward Serverless profile
   - Data layer? → Lean toward Database profile
   - Development tool? → Lean toward CI/CD profile
   - Framework? → Lean toward Frontend or API profile
   - Rapidly evolving? → Lean toward AI/ML profile (high escape hatch weight)
   - Autonomous/orchestrated AI system? → Lean toward AI Agent Frameworks profile

2. **Default weighting** (when no family matches):
   All dimensions at Medium weight. Elevate to High based on:
   - Technology maturity < 2 years → Escape Hatches to High
   - Technology has a cost model → Operational Awareness to High
   - Technology has multiple modes/variants → Decision Trees to High
   - Technology is frequently misused → Anti-Patterns to High

3. **Always prioritize**: Idiomatic Patterns and Anti-Patterns are almost always High or Medium for any technology. These provide the most value per research token.
