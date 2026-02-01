# agentient-frontend-data

**Firebase integration, Firestore data modeling, type-safe data access with Zod, authentication patterns, and security rules for Next.js 14+ applications.**

## Overview

This plugin provides comprehensive Firebase integration for Next.js 14+ App Router applications, with a focus on:

- **Type-Safe Data Access**: Zod schema validation with Firestore `withConverter` API
- **Dual SDK Architecture**: Proper separation of client-side and server-side Firebase SDKs
- **Authentication Flows**: Complete auth implementation with session management and RBAC
- **Security Rules**: Automated generation of granular Firestore and Storage security rules
- **Data Modeling**: Best practices for Firestore schema design and query optimization

## Installation

```bash
# Install the plugin (adjust path as needed)
cd plugins
git clone <vibekit-marketplace-url>
# Or use /plugin install command in Claude Code
```

## Components

### Agents (2)

#### 1. **data-modeler-agent**
- **When**: Firestore schema design, Zod validation, data relationships, query optimization
- **Capabilities**: Design optimal collection structure, create type-safe schemas, plan indexes
- **Default Mode**: Plan Mode (mandatory for data modeling)
- **Tools**: Read, Write, Glob, Grep

#### 2. **firebase-integration-agent**
- **When**: Firebase setup, authentication flows, security rules, SDK configuration
- **Capabilities**: Initialize Firebase SDKs, implement auth, generate security rules, deploy configurations
- **Default Mode**: Plan Mode
- **Tools**: Read, Write, Bash, Glob, Grep

### Commands (4)

| Command | Purpose |
|---------|---------|
| `/model-collection` | Generate type-safe Firestore collection with Zod schema, TypeScript types, and converters |
| `/setup-firebase` | Initialize Firebase project with dual SDK setup (client + server Admin SDK) |
| `/create-auth-flow` | Implement complete authentication flow with sign-in, sign-up, protected routes, and RBAC |
| `/generate-security-rules` | Generate Firestore and Storage security rules based on data models and access patterns |

### Skills (6)

1. **firestore-data-modeling-patterns** - Subcollections vs root collections, relationships, document structure, query optimization
2. **zod-firestore-type-safety** - Runtime validation with Zod, withConverter pattern, type inference, schema evolution
3. **firebase-authentication-patterns** - Sign-in/sign-up flows, OAuth providers, session management, password reset
4. **firebase-admin-sdk-server-integration** - Server-only SDK initialization, custom claims, token verification, privileged operations
5. **firestore-security-rules-generation** - User-scoped rules, RBAC, multi-tenant patterns, field validation
6. **firebase-nextjs-integration-strategies** - Server/client SDK separation, data fetching patterns, middleware, caching

### Hooks & Scripts

**Hooks** (automated workflow enhancements):
- **SessionStart**: Display available Firebase commands
- **PreToolUse** (Bash): Validate Firebase CLI commands to prevent destructive operations
- **PostToolUse** (Write/Edit): Remind to run type-check after TypeScript file modifications

**Script**:
- **firebase_command_validator.sh**: Blocks dangerous Firebase CLI commands (project deletion, bulk data deletion, etc.)

## Quick Start

### 1. Initialize Firebase

```bash
/setup-firebase
```

This will:
- Create client SDK initialization (`src/lib/firebase/client.ts`)
- Create server Admin SDK initialization (`src/lib/firebase/admin.ts` with `server-only` protection)
- Generate Zod converter utilities (`src/lib/firebase/zodConverter.ts`)
- Create environment variable template (`.env.local.example`)
- Configure Firebase project files (`firebase.json`, `.firebaserc`)

### 2. Create Your First Type-Safe Collection

```bash
/model-collection
```

This will generate:
- Zod schema with runtime validation
- TypeScript type inferred from schema
- Client and server `withConverter` objects
- Baseline security rules
- Composite indexes (if needed)

**Example Output**:
```typescript
// src/lib/firebase/schemas/post.schema.ts
export const PostSchema = z.object({
  id: z.string(),
  title: z.string().min(1).max(200),
  content: z.string(),
  authorId: z.string(),
  status: z.enum(['draft', 'published', 'archived']),
  createdAt: z.instanceof(Timestamp),
});

export type Post = z.infer<typeof PostSchema>;

export const postConverter = zodConverter(PostSchema);
export const postAdminConverter = zodAdminConverter(PostSchema);
```

### 3. Implement Authentication

```bash
/create-auth-flow
```

This will generate:
- Auth helper functions (sign-in, sign-up, sign-out)
- Auth UI components (forms, buttons)
- Session management (middleware for protected routes)
- Auth context provider (React Context)
- Custom claims API (for RBAC, if requested)

### 4. Generate Security Rules

```bash
/generate-security-rules
```

This will create:
- Firestore security rules (`firestore.rules`) with user-scoped access, RBAC, field validation
- Storage security rules (`storage.rules`)
- Test suite (`firestore.rules.spec.ts`)
- Security documentation

## Configuration

The plugin enforces these quality constraints (defined in `.claude-plugin/plugin.json`):

```json
{
  "QUALITY_THRESHOLD": "97",
  "PLAN_MODE_DEFAULT": "true",
  "FIREBASE_ADMIN_SERVER_ONLY": "true",
  "ZOD_CONVERTER_REQUIRED": "true",
  "ERROR_HANDLING_MANDATORY": "true",
  "SECURITY_RULES_REQUIRED": "true"
}
```

## Architectural Principles

### 1. Dual SDK Architecture

**Client SDK** (Browser, Client Components):
- Used for client-side authentication (sign-in, sign-up)
- Real-time listeners (`onSnapshot`)
- Respects Firestore security rules

**Admin SDK** (Server Components, API Routes, Server Actions):
- Used for privileged server-side operations
- Bypasses security rules
- **MUST** be protected with `'server-only'` package

### 2. Type Safety End-to-End

- **Zod schemas** for runtime validation
- **TypeScript types** inferred from Zod (`z.infer<typeof Schema>`)
- **withConverter API** to bind schemas to Firestore operations
- **No `any` type** - use `unknown` with type guards

### 3. Security First

- All Admin SDK files **MUST** import `'server-only'`
- Service account credentials stored in server-side environment variables
- Every collection requires baseline security rules
- Token verification in middleware for protected routes

### 4. Data Modeling Best Practices

- **Root collections** preferred over subcollections (flexibility, simpler deletion)
- **Subcollections** only for tightly-coupled, hierarchical data
- **Composite indexes** for multi-field queries
- **Batched writes** default (use transactions only when reads required)

## Anti-Patterns (Blocked by Validation)

❌ Using Admin SDK in client components (leaks credentials)
❌ Skipping Zod validation with `withConverter`
❌ Storing tokens in localStorage (use `HttpOnly` cookies)
❌ Hardcoding Firebase credentials
❌ Embedding large arrays in documents (exceeds 1MB limit)
❌ Using subcollections without cleanup strategy
❌ Skipping security rules generation

## Dependencies

**Required**: `agentient-frontend-foundation` (for Next.js 14+ project structure)

**Optional Cross-Plugin Integration**:
- **agentient-frontend-state-forms**: For Zod schema integration with React Hook Form and Zustand
- **agentient-frontend-bff**: For serverless function patterns using Firebase Functions
- **agentient-security**: For OWASP-compliant security patterns

## Examples

### Example 1: Complete Feature Flow

```bash
# 1. Initialize Firebase
/setup-firebase
> Project ID: my-app-prod

# 2. Create a collection
/model-collection
> Collection: post
> Fields: title:string, content:string, authorId:string, status:enum(draft|published)

# 3. Set up authentication
/create-auth-flow
> Providers: Email/Password, Google
> RBAC: admin, user

# 4. Generate security rules
/generate-security-rules
> Collections: posts
> Pattern: User-scoped (author only)
```

### Example 2: Server Component Data Fetching

```typescript
// app/posts/page.tsx
import { adminDb } from '@/lib/firebase/admin';
import { postAdminConverter, type Post } from '@/lib/firebase/schemas/post.schema';

export default async function PostsPage() {
  // Fetch with Admin SDK in Server Component
  const postsSnapshot = await adminDb
    .collection('posts')
    .withConverter(postAdminConverter)
    .where('status', '==', 'published')
    .get();

  const posts: Post[] = postsSnapshot.docs.map(doc => doc.data());

  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
        </article>
      ))}
    </div>
  );
}
```

### Example 3: Real-Time Listener (Client Component)

```typescript
'use client';

import { useEffect, useState } from 'react';
import { collection, query, onSnapshot } from 'firebase/firestore';
import { db } from '@/lib/firebase/client';
import { commentConverter, type Comment } from '@/lib/firebase/schemas/comment.schema';

export function CommentsList({ postId }: { postId: string }) {
  const [comments, setComments] = useState<Comment[]>([]);

  useEffect(() => {
    const q = query(
      collection(db, 'comments'),
      where('postId', '==', postId)
    ).withConverter(commentConverter);

    const unsubscribe = onSnapshot(q, (snapshot) => {
      setComments(snapshot.docs.map(doc => doc.data()));
    });

    return unsubscribe; // Cleanup
  }, [postId]);

  return <div>{/* Render comments */}</div>;
}
```

### Example 4: Server Action (Mutation)

```typescript
'use server';

import { adminDb } from '@/lib/firebase/admin';
import { PostSchema } from '@/lib/firebase/schemas/post.schema';
import { revalidatePath } from 'next/cache';

export async function createPost(input: z.infer<typeof PostSchema>) {
  const validated = PostSchema.parse(input);

  const postRef = adminDb.collection('posts').doc();
  await postRef.set(validated);

  revalidatePath('/posts'); // Invalidate Next.js cache

  return { success: true, postId: postRef.id };
}
```

## Troubleshooting

### Issue: "server-only module included in client bundle"

**Solution**: Ensure all Admin SDK files have `import 'server-only'` as the first import:

```typescript
import 'server-only'; // FIRST import!
import { initializeApp } from 'firebase-admin/app';
```

### Issue: "Zod validation error on existing documents"

**Solution**: Mark new fields as optional when evolving schemas:

```typescript
export const UserSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  newField: z.string().optional(), // Won't break old docs
});
```

### Issue: "Permission denied" in Firestore

**Solution**:
1. Check security rules match your access pattern
2. Ensure user is authenticated (`request.auth != null`)
3. Verify custom claims are set correctly (for RBAC)

### Issue: "Firebase CLI command blocked"

**Solution**: The PreToolUse hook blocks dangerous commands. To proceed:
1. Use Firebase Console for destructive operations
2. Or manually run the command in your terminal after review

## Contributing

When extending this plugin:
1. Follow 3-tier progressive disclosure model for skills
2. Ensure agents include Plan Mode enforcement boilerplate
3. Add validation rules to `firebase_command_validator.sh`
4. Test with real Firebase projects
5. Document security implications

## License

Part of the vibekit marketplace. See marketplace LICENSE for details.

## Support

- **Documentation**: See individual skills and commands for detailed guidance
- **Issues**: Report plugin issues to vibekit marketplace repository
- **Questions**: Use `/help` command or consult the data-modeler-agent or firebase-integration-agent

---

**Version**: 1.0.0
**Confidence Level**: 97%
**Target Stack**: Firebase v10+, Next.js 14+, TypeScript 5.3+, Zod 3.x
**Maintained by**: Agentient Labs
