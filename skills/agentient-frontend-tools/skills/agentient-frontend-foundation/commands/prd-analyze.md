# PRD Analysis Command

You are analyzing a Product Requirements Document (PRD) to extract technical requirements and create actionable development artifacts. Your goal is to bridge product vision and technical implementation.

## Task Overview

Extract and organize the following information from the PRD:

1. Technical Requirements
2. User Stories with Acceptance Criteria
3. Data Models
4. API Endpoints
5. UI Components
6. Dependencies & Integrations
7. Gaps and Clarifications Needed

## Execution Instructions

### Step 1: Locate and Read the PRD

First, ask the user for the PRD location:
- File path (e.g., `docs/prd/user-dashboard.md`)
- Or ask them to paste it directly

Read the complete document before proceeding.

### Step 2: Extract Technical Requirements

Create a section that captures:

```markdown
## Technical Requirements Extracted from PRD

### Stack & Infrastructure
- **Frontend**: Next.js 14+ with App Router, React 18+, TypeScript (strict mode)
- **Styling**: [Extract from PRD - e.g., Tailwind CSS, shadcn/ui]
- **Backend**: [Extract from PRD or note if not specified]
- **Database**: [Extract from PRD or note if not specified]
- **Third-Party Services**: [List any mentioned - e.g., Auth0, Stripe, SendGrid]
- **Hosting/Deployment**: [Extract from PRD or note if not specified]

### Performance Requirements
- **Page Load Time**: [Extract target or note **[CLARIFICATION NEEDED]**]
- **Core Web Vitals**: [Extract targets or note **[CLARIFICATION NEEDED]**]
- **Concurrent Users**: [Extract expected load or note **[CLARIFICATION NEEDED]**]

### Security Requirements
- **Authentication**: [Extract method - e.g., OAuth, Email/Password, SSO]
- **Authorization**: [Extract RBAC details or note **[CLARIFICATION NEEDED]**]
- **Data Protection**: [Extract compliance needs - e.g., GDPR, HIPAA]
- **Session Management**: [Extract timeout/security requirements]

### Scalability Requirements
- **Expected Users**: [Extract or note **[CLARIFICATION NEEDED]**]
- **Expected Traffic**: [Extract or note **[CLARIFICATION NEEDED]**]
- **Data Volume**: [Extract or note **[CLARIFICATION NEEDED]**]
```

### Step 3: Create User Stories

For each feature mentioned in the PRD, create user stories using this format:

```markdown
## User Stories

### Epic: [Feature Name from PRD]

#### Story 1: [Concise Title]

**Priority**: [P0/P1/P2 - extract from PRD or infer]

**User Story**:
As a [user persona from PRD]
I want to [capability/action]
So that [benefit/value]

**Acceptance Criteria**:
- [ ] **Given** [precondition], **When** [action], **Then** [expected result]
- [ ] **Given** [precondition], **When** [action], **Then** [expected result]
- [ ] **Given** [error condition], **When** [action], **Then** [error handling behavior]
- [ ] [Edge cases and validation rules from PRD]

**Technical Notes**:
- Server Component or Client Component: [Recommend based on interactivity needs]
- Data models needed: [List entities]
- API endpoints needed: [List endpoints]

**Dependencies**:
- Depends on: [Other stories this requires]
- Blocks: [Other stories that need this first]

**Clarifications Needed**:
- **[CLARIFICATION NEEDED]**: [Specific question about this story]
```

Create 3-7 user stories per epic, covering:
- Happy path scenarios
- Error handling scenarios
- Edge cases mentioned in PRD
- Performance/scalability requirements

### Step 4: Identify Data Models

Based on the features, extract or infer data models:

```markdown
## Data Models (Preliminary)

### Entity: [Name]

**Purpose**: [What this entity represents]

**Fields**:
- `id`: string (UUID) - Primary key
- `[fieldName]`: [type] - [description, extracted or inferred from PRD]
- `[fieldName]`: [type] | null - [optional field]
- `createdAt`: string (ISO 8601) - Timestamp
- `updatedAt`: string (ISO 8601) - Timestamp

**Relationships**:
- Belongs to: [Other entity]
- Has many: [Other entity]
- Many-to-many with: [Other entity]

**Validation Rules** (from PRD):
- [Field] must be [constraint]
- [Field] is required when [condition]

**Indexes** (recommended):
- [Field] for efficient queries

**Questions**:
- **[CLARIFICATION NEEDED]**: [What's the max length of field X?]
- **[CLARIFICATION NEEDED]**: [Is field Y optional or required?]
```

### Step 5: List Required API Endpoints

Based on user stories and data models:

```markdown
## API Endpoints Required

### [HTTP Method] /api/[resource]/[action]

**Purpose**: [What this endpoint does]

**Request**:
```typescript
interface [RequestName] {
  [field]: [type];
}
```

**Response**:
```typescript
interface [ResponseName] {
  success: boolean;
  data: [Type];
  error?: { code: string; message: string };
}
```

**Authentication**: [Required/Optional/Public]

**Recommendation**: [ ] Server Action  [ ] API Route  [ ] Both

**Used by Stories**: [List story IDs]

**Questions**:
- **[CLARIFICATION NEEDED]**: [What should happen if...?]
```

### Step 6: Identify UI Components

Extract or infer major UI components from PRD:

```markdown
## UI Components Needed

### [ComponentName]

**Purpose**: [What it displays/enables]

**Type**: [ ] Server Component  [ ] Client Component

**Key Features** (from PRD):
- [Feature 1]
- [Feature 2]

**Props** (preliminary):
```typescript
interface [ComponentName]Props {
  [prop]: [type];
}
```

**User Interactions**:
- [What users can do with this component]

**Responsive Behavior**:
- **Mobile**: [How it adapts]
- **Tablet**: [How it adapts]
- **Desktop**: [How it displays]

**Dependencies**:
- Requires: [Other components or data]

**Questions**:
- **[CLARIFICATION NEEDED]**: [Layout/behavior question]
```

### Step 7: List Dependencies and Integrations

```markdown
## External Dependencies

### Third-Party Services
- **[Service Name]** (e.g., Stripe for payments)
  - Purpose: [Why we need it]
  - Integration points: [Where it's used]
  - **[CLARIFICATION NEEDED]**: [Do we have an account? API keys?]

### Libraries/Packages (in addition to Next.js/React core)
- **[Package name]**: [Purpose]
  - Recommended version: [Version]
  - Use case: [Where/why used]

### Infrastructure Requirements
- [Hosting needs]
- [Database needs]
- [CDN needs]
- **[CLARIFICATION NEEDED]**: [Budget? Preferred vendor?]
```

### Step 8: Compile All Gaps and Clarifications

```markdown
## Summary of Clarifications Needed

**HIGH PRIORITY** (blockers for starting development):
1. **[CLARIFICATION NEEDED]**: [Question]
2. **[CLARIFICATION NEEDED]**: [Question]

**MEDIUM PRIORITY** (needed before implementation):
1. **[CLARIFICATION NEEDED]**: [Question]

**LOW PRIORITY** (can be decided during development):
1. **[CLARIFICATION NEEDED]**: [Question]

## Recommended Next Steps

1. **Review this analysis** with product stakeholders
2. **Get answers** to HIGH PRIORITY clarifications
3. **Create Architecture Decision Records** (ADRs) for major technical choices
   - Use `/generate-adr` command for each significant decision
4. **Design API contracts** with `/api-contract` command
5. **Set up project** with `/setup-project` command
6. **Begin implementation** starting with data layer, then API layer, then UI layer
```

## Output Format

Provide a **single, comprehensive Markdown document** with all sections above.

## Important Guidelines

1. **Be Thorough**: Extract every feature, requirement, and constraint mentioned
2. **Be Specific**: Use concrete examples and detailed descriptions
3. **Flag Ambiguities**: Use **[CLARIFICATION NEEDED]** liberally - don't guess
4. **Map Everything**: Cross-reference stories to data models to APIs to components
5. **Think Technically**: Consider Next.js 14+ constraints (Server vs Client Components, data fetching patterns)
6. **Be Realistic**: Flag technical challenges or potential architecture decisions needed

## Activation

This command automatically activates the **product-owner-agent** subagent, which has specialized knowledge in:
- PRD analysis and requirements extraction
- User story creation with acceptance criteria
- Bridging product and engineering perspectives

The subagent will use **Plan Mode** to ensure thorough, systematic analysis.

---

**Ready to analyze? Please provide the PRD document (file path or paste the content).**
