# agentient-frontend-foundation

**Core Next.js 14+ App Router architecture, project structure, TypeScript patterns, and architectural decision-making for vibekit marketplace.**

## Overview

This plugin provides the foundational knowledge and tooling for building Next.js 14+ applications with best practices enforced. It emphasizes:

- **React Server Components (RSC)** as the default rendering strategy
- **TypeScript strict mode** for end-to-end type safety
- **PRD-driven development** workflows
- **Plan Mode** as the default for architectural tasks
- **Architecture Decision Records (ADRs)** for documenting technical decisions

## Installation

```bash
# Install the plugin (adjust path as needed)
cd plugins
git clone <vibekit-marketplace-url>
# Or use /plugin install command in Claude Code
```

## Components

### Agents (3)

The plugin includes three specialized subagents that automatically activate based on your task:

#### 1. **architect-agent**
- **When**: System architecture design, technical decisions, ADR creation
- **Capabilities**: Design scalable architectures, evaluate technology trade-offs, create ADRs
- **Default Mode**: Plan Mode (mandatory for architectural work)
- **Tools**: Read, Write, Glob, Grep

#### 2. **product-owner-agent**
- **When**: PRD analysis, user story creation, requirements decomposition
- **Capabilities**: Extract technical requirements, create user stories with acceptance criteria
- **Default Mode**: Plan Mode
- **Tools**: Read, Grep, Glob, Write

#### 3. **api-designer-agent**
- **When**: API contract design, endpoint specification, type modeling
- **Capabilities**: Design type-safe APIs, sync with backend models, create Zod schemas
- **Default Mode**: Plan Mode
- **Tools**: Read, Write, Edit, Grep, Glob

### Commands (5)

Execute these commands with `/command-name`:

| Command | Purpose |
|---------|---------|
| `/prd-analyze` | Analyze Product Requirements Document and extract technical requirements, user stories, data models, API endpoints |
| `/setup-project` | Scaffold a new Next.js 14+ project with opinionated structure, TypeScript strict mode, and baseline dependencies |
| `/create-page` | Generate a new App Router page with layout, loading, error states following RSC-first patterns |
| `/generate-adr` | Create an Architecture Decision Record to document significant technical decisions |
| `/api-contract` | Design a type-safe API contract with TypeScript interfaces, Zod schemas, and implementation guidance |

### Skills (6)

These skills are automatically loaded on-demand when relevant to your task:

1. **nextjs-project-scaffolding** - Opinionated project structure, tsconfig.json setup, folder organization
2. **rsc-composition-patterns** - Server vs Client Component patterns, composition strategies, 'use client' boundaries
3. **nextjs-app-router-data-fetching** - Async Server Components, Server Actions, caching, revalidation
4. **nextjs-app-router-file-conventions** - Special files (page, layout, loading, error, route), dynamic routing
5. **typescript-type-safe-api-contracts** - Strict typing, Zod integration, generic patterns, utility types
6. **architectural-decision-records** - ADR templates, best practices, lifecycle management

### Hooks & Scripts

**Hooks** (automated workflow enhancements):
- **SessionStart**: Display Plan Mode reminder
- **UserPromptSubmit**: PRD-driven development reminder
- **PreToolUse** (Write/Edit): Validate project structure before file operations

**Script**:
- **structure_validator.sh**: Validates Next.js 14+ project structure, blocks legacy patterns (Exit Code 2 on violation)

## Quick Start

### 1. Start a New Project

```bash
/setup-project
```

Follow the prompts to scaffold a production-ready Next.js 14+ project with all configurations.

### 2. Analyze a PRD

```bash
/prd-analyze
```

Provide the path to your PRD or paste the content. The command will extract user stories, data models, API endpoints, and flag ambiguities.

### 3. Create Your First Page

```bash
/create-page
```

Specify the route (e.g., `/dashboard` or `/blog/[slug]`) and the command will generate page.tsx, loading.tsx, error.tsx with proper Server Component patterns.

### 4. Design an API

```bash
/api-contract
```

Provide the API requirements and the command will generate TypeScript types, Zod schemas, and implementation code (Server Action or API Route).

### 5. Document Decisions

```bash
/generate-adr
```

Create an ADR whenever you make a significant architectural decision (e.g., "Adopt Zustand for state management").

## Configuration

The plugin enforces these quality constraints (defined in `.claude-plugin/plugin.json`):

```json
{
  "QUALITY_THRESHOLD": "97",
  "PLAN_MODE_DEFAULT": "true",
  "RSC_DEFAULT": "true",
  "CLIENT_DIRECTIVE_MINIMAL": "true",
  "TYPESCRIPT_STRICT": "true",
  "EXPLICIT_RETURN_TYPES": "true"
}
```

## Architectural Principles

### 1. Server-First Development

**Default**: All components are Server Components unless they require:
- State (`useState`, `useReducer`)
- Effects (`useEffect`)
- Event handlers (`onClick`, `onChange`)
- Browser APIs (`window`, `localStorage`)

### 2. Type Safety End-to-End

- TypeScript **strict mode** is mandatory
- All exported functions **must** have explicit return types
- The `any` type is **forbidden** - use `unknown` with type guards
- Zod schemas for **runtime validation** of all API inputs

### 3. Convention Over Configuration

- Leverage Next.js **file-system routing**
- Use **special files** (page.tsx, layout.tsx, loading.tsx, error.tsx)
- Follow **established folder structure** (`src/app`, `src/components`, `src/lib`)

### 4. Progressive Enhancement

- Core functionality works before JavaScript loads
- Use **`<Suspense>`** for streaming UI
- Implement proper **loading states** and **error boundaries**

### 5. Documentation-Driven Architecture

- Create **ADRs** for all significant decisions
- Document **API contracts** before implementation
- Maintain **PRD traceability** from requirements to code

## Anti-Patterns (Blocked by Validation)

❌ Using the `/pages` directory (legacy Pages Router)
❌ Using `getStaticProps`, `getServerSideProps`, `getInitialProps` (removed in App Router)
❌ Using `'use client'` on high-level page.tsx or layout.tsx files
❌ Using `any` type in TypeScript
❌ Not enabling `strict: true` in tsconfig.json
❌ Client-side data fetching with `useEffect` for initial render

## Dependencies

**None** - This is a foundational plugin.

**Optional Cross-Plugin Integration**:
- **agentient-python-core**: For backend Pydantic model synchronization (API type safety)
- **agentient-frontend-data**: For Firebase-specific data patterns
- **agentient-security**: For authentication and authorization patterns

## Examples

### Example 1: Complete Feature Development Flow

```bash
# 1. Analyze the PRD
/prd-analyze
> Provide path to: docs/prd/user-dashboard.md

# 2. Create ADR for major architectural choice
/generate-adr
> Decision: Use Server Components for dashboard data display

# 3. Design the API contract
/api-contract
> Design: GET /api/dashboard-stats endpoint

# 4. Create the page
/create-page
> Route: /dashboard

# 5. Implement (agents auto-activate based on your prompts)
> "Implement the dashboard page with real-time stats"
```

### Example 2: PRD-Driven User Story Creation

```bash
/prd-analyze

# Input: docs/prd/social-feed.md

# Output:
# - 8 user stories with acceptance criteria
# - 3 data models (Post, Comment, User)
# - 5 API endpoints (create post, list posts, etc.)
# - 12 UI components identified
# - 15 clarification questions flagged
```

### Example 3: Architecture Decision Documentation

```bash
/generate-adr

# Creates: docs/adr/005-adopt-zustand-for-client-state.md

# Includes:
# - Context (why decision is needed)
# - Decision (what we're doing)
# - Consequences (pros/cons/mitigations)
# - Alternatives considered (Redux, Context API)
# - References and related ADRs
```

## Troubleshooting

### Validation Errors

If you see:
```
❌ BLOCKED: Using legacy /pages directory is not allowed.
```

**Solution**: The plugin enforces App Router usage. Move your files from `/pages` to `/app`.

### Plan Mode Prompts

If agents consistently enter Plan Mode:

**This is by design** for architectural tasks. Plan Mode ensures:
- Thorough analysis before implementation
- User approval of approach
- Documentation of decisions

For simple tasks (reading files, quick questions), agents use Direct Mode automatically.

## Contributing

When extending this plugin:
1. Follow the 3-tier progressive disclosure model for skills (Metadata → Instructions → Resources)
2. Ensure all agents include Plan Mode enforcement boilerplate
3. Add validation rules to `structure_validator.sh` for new patterns
4. Document decisions in ADRs
5. Test with real Next.js 14+ projects

## License

Part of the vibekit marketplace. See marketplace LICENSE for details.

## Support

- **Documentation**: See individual skills and commands for detailed guidance
- **Issues**: Report plugin issues to vibekit marketplace repository
- **Questions**: Use `/help` command or consult the architect-agent

---

**Version**: 1.0.0
**Confidence Level**: 97%
**Target Stack**: Next.js 14+, React 18+, TypeScript 5.3+
**Maintained by**: Agentient Labs
