# agentient-frontend-bff

Backend-for-Frontend implementation patterns for Next.js 14+ with Server Actions, API Route Handlers, and Firebase Functions v2.

**Confidence**: 99% | **Category**: Frontend | **Version**: 1.0.0

## Key Features

- **Three Server-Side Patterns**: Server Actions (form mutations), API Routes (stateless endpoints), Firebase Functions (async processing)
- **Zod Schema Validation**: safeParse for all request/response boundaries
- **Type-Safe Contracts**: z.infer<typeof Schema> as single source of truth
- **Progressive Enhancement**: Server Actions work without JavaScript
- **Security Integration**: Auth validation before business logic

## Pattern Decision Matrix

| Use Case | Pattern | Why |
|----------|---------|-----|
| Form submission | Server Action | Progressive enhancement, cache revalidation |
| External API endpoint | API Route Handler | Stateless, RESTful, public access |
| Background job | Firebase Function | Event-driven, async, Cloud infrastructure |

## Critical Patterns

### 1. Zod Validation (safeParse, Not parse)
```typescript
// ❌ WRONG - throws exception
const data = schema.parse(req.body);

// ✅ CORRECT - returns Result type
const result = schema.safeParse(req.body);
if (!result.success) {
  return { error: result.error.format() };
}
```

### 2. Server Action with Cache Revalidation
```typescript
'use server'

async function createPost(formData: FormData) {
  const result = PostSchema.safeParse({ title: formData.get('title') });
  if (!result.success) return { error: result.error };

  await db.insert(result.data);
  revalidatePath('/posts');  // CRITICAL - invalidate cache
  redirect('/posts');
}
```

### 3. Type Inference from Schema
```typescript
const UserSchema = z.object({
  email: z.string().email(),
  age: z.number().int().positive()
});

// Single source of truth
type User = z.infer<typeof UserSchema>;
```

## Components

- **Agent**: bff-architect-agent
- **Commands**: /create-server-action, /create-api-route, /create-firebase-function, /validate-schema
- **Skills** (7): Zod validation, Server Actions, API Routes, Firebase Functions, security patterns, error handling, type generation

## Dependencies

**Required**: agentient-security, agentient-frontend-foundation

---

**Generated with Claude Code** | Version 1.0.0
