# API Contract Design Command

You are designing a type-safe API contract for a Next.js 14+ application, including TypeScript interfaces, Zod validation schemas, and implementation patterns.

## Task Overview

Create a comprehensive API contract that defines:
1. Request and response TypeScript types
2. Zod validation schemas
3. Error response formats
4. Implementation approach (Server Action vs API Route)
5. Backend synchronization notes

## Prerequisites

Ask the user:
1. **Endpoint purpose**: What does this API do?
2. **Data requirements**: What data is sent/received?
3. **Backend model**: Does a Python/Pydantic model exist? (path to file)
4. **Authentication**: Required/optional/public?
5. **External access**: Will external clients call this?

## Execution Instructions

### Step 1: Choose Implementation Approach

**Decision Tree**:
- **Is this a data mutation (create, update, delete)?** → Prefer **Server Action**
- **Do external clients need to call this?** → Use **API Route**
- **Is this called only from your own frontend?** → Prefer **Server Action**
- **Do you need custom HTTP logic (headers, streaming)?** → Use **API Route**

### Step 2: Read Backend Model (If Exists)

If user provides a Python/Pydantic model path, read it first:

```bash
# Example: read backend/src/models/project.py
```

Map Python types to TypeScript:
- `str` → `string`
- `int` → `number`
- `UUID4` → `string` (with UUID validation)
- `datetime` → `string` (ISO 8601)
- `list[T]` → `T[]`
- `T | None` → `T | null`

### Step 3: Create Type Definitions File

Create `src/types/api/[resource].ts`:

```typescript
// src/types/api/project.ts

/**
 * Project API Types
 * Synchronized with backend: backend/src/models/project.py
 */

// ===== Request Types =====

export interface CreateProjectRequest {
  name: string;
  description: string | null;
  settings?: ProjectSettings;
}

export interface UpdateProjectRequest {
  name?: string;
  description?: string | null;
  settings?: ProjectSettings;
}

export interface ProjectSettings {
  isPublic: boolean;
  allowComments: boolean;
}

// ===== Response Types =====

export interface Project {
  id: string; // UUID
  name: string;
  description: string | null;
  ownerId: string; // UUID
  createdAt: string; // ISO 8601
  updatedAt: string; // ISO 8601
  settings: ProjectSettings;
}

// ===== Standard API Response Wrapper =====

export type ApiResponse<T> =
  | { success: true; data: T }
  | { success: false; error: ApiError };

export interface ApiError {
  code: string;
  message: string;
  details?: Record<string, string[]>;
}

// ===== Error Codes =====

export const ProjectErrorCodes = {
  VALIDATION_ERROR: 'VALIDATION_ERROR',
  PROJECT_NOT_FOUND: 'PROJECT_NOT_FOUND',
  UNAUTHORIZED: 'UNAUTHORIZED',
  FORBIDDEN: 'FORBIDDEN',
} as const;
```

### Step 4: Create Zod Validation Schemas

Create `src/lib/validations/[resource].ts`:

```typescript
// src/lib/validations/project.ts

import { z } from 'zod';

/**
 * Zod schemas for runtime validation
 * Must match backend Pydantic models
 */

const projectSettingsSchema = z.object({
  isPublic: z.boolean(),
  allowComments: z.boolean(),
});

export const createProjectSchema = z.object({
  name: z.string().min(1, 'Name is required').max(100, 'Name too long'),
  description: z.string().nullable(),
  settings: projectSettingsSchema.optional(),
});

export const updateProjectSchema = z.object({
  name: z.string().min(1).max(100).optional(),
  description: z.string().nullable().optional(),
  settings: projectSettingsSchema.optional(),
});

// Infer TypeScript types from Zod schemas
export type CreateProjectInput = z.infer<typeof createProjectSchema>;
export type UpdateProjectInput = z.infer<typeof updateProjectSchema>;
```

### Step 5A: Implement Server Action (Recommended for Mutations)

Create `src/app/actions/[resource].ts`:

```typescript
// src/app/actions/projects.ts
'use server';

import { z } from 'zod';
import { revalidatePath } from 'next/cache';
import { createProjectSchema } from '@/lib/validations/project';
import type { ApiResponse, Project } from '@/types/api/project';

export async function createProject(
  input: unknown
): Promise<ApiResponse<Project>> {
  try {
    // 1. Validate input
    const validated = createProjectSchema.parse(input);

    // 2. Check authentication
    const user = await getCurrentUser();
    if (!user) {
      return {
        success: false,
        error: {
          code: 'UNAUTHORIZED',
          message: 'You must be logged in to create a project',
        },
      };
    }

    // 3. Call backend API or database
    const response = await fetch('https://api.example.com/projects', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${user.token}`,
      },
      body: JSON.stringify({
        // Convert camelCase to snake_case if needed
        name: validated.name,
        description: validated.description,
        owner_id: user.id,
        settings: validated.settings ? {
          is_public: validated.settings.isPublic,
          allow_comments: validated.settings.allowComments,
        } : undefined,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to create project');
    }

    const data = await response.json();

    // 4. Revalidate cache
    revalidatePath('/dashboard');

    // 5. Return success
    return {
      success: true,
      data: {
        // Convert snake_case to camelCase
        id: data.id,
        name: data.name,
        description: data.description,
        ownerId: data.owner_id,
        createdAt: data.created_at,
        updatedAt: data.updated_at,
        settings: {
          isPublic: data.settings.is_public,
          allowComments: data.settings.allow_comments,
        },
      },
    };

  } catch (error) {
    // Handle Zod validation errors
    if (error instanceof z.ZodError) {
      return {
        success: false,
        error: {
          code: 'VALIDATION_ERROR',
          message: 'Invalid input',
          details: error.flatten().fieldErrors as Record<string, string[]>,
        },
      };
    }

    // Log unexpected errors
    console.error('Create project error:', error);

    return {
      success: false,
      error: {
        code: 'INTERNAL_ERROR',
        message: 'Failed to create project. Please try again.',
      },
    };
  }
}
```

### Step 5B: Implement API Route (For External Access)

Create `src/app/api/[resource]/route.ts`:

```typescript
// src/app/api/projects/route.ts

import { NextRequest, NextResponse } from 'next/server';
import { createProjectSchema } from '@/lib/validations/project';
import type { ApiResponse, Project } from '@/types/api/project';

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    // 1. Parse and validate body
    const body = await request.json();
    const validated = createProjectSchema.parse(body);

    // 2. Check authentication
    const authHeader = request.headers.get('authorization');
    if (!authHeader) {
      return NextResponse.json(
        {
          success: false,
          error: {
            code: 'UNAUTHORIZED',
            message: 'Authorization header required',
          },
        } satisfies ApiResponse<never>,
        { status: 401 }
      );
    }

    // 3. Create project (call backend or database)
    const project = await createProjectInBackend(validated, authHeader);

    // 4. Return success
    return NextResponse.json(
      { success: true, data: project } satisfies ApiResponse<Project>,
      { status: 201 }
    );

  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        {
          success: false,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Invalid request body',
            details: error.flatten().fieldErrors,
          },
        } satisfies ApiResponse<never>,
        { status: 400 }
      );
    }

    console.error('API error:', error);
    return NextResponse.json(
      {
        success: false,
        error: {
          code: 'INTERNAL_ERROR',
          message: 'Internal server error',
        },
      } satisfies ApiResponse<never>,
      { status: 500 }
    );
  }
}

export async function GET(request: NextRequest): Promise<NextResponse> {
  // Implement GET for listing projects
}
```

### Step 6: Create API Contract Documentation

Create `docs/api/[resource].md`:

```markdown
# Project API Contract

**Version**: 1.0.0
**Last Updated**: 2025-10-23

## Create Project

### Approach
- [x] Server Action
- [ ] API Route

### Server Action

**Function**: `createProject(input: unknown): Promise<ApiResponse<Project>>`
**Location**: `src/app/actions/projects.ts`

#### Input

```typescript
interface CreateProjectInput {
  name: string;         // 1-100 characters
  description: string | null;
  settings?: {
    isPublic: boolean;
    allowComments: boolean;
  };
}
```

#### Output

Success:
```typescript
{
  success: true,
  data: {
    id: string,
    name: string,
    description: string | null,
    ownerId: string,
    createdAt: string,
    updatedAt: string,
    settings: {
      isPublic: boolean,
      allowComments: boolean,
    }
  }
}
```

Error:
```typescript
{
  success: false,
  error: {
    code: 'VALIDATION_ERROR' | 'UNAUTHORIZED' | 'INTERNAL_ERROR',
    message: string,
    details?: Record<string, string[]>
  }
}
```

#### Validation Rules

- `name`: Required, 1-100 characters
- `description`: Optional, can be null
- `settings`: Optional object
- `settings.isPublic`: Boolean
- `settings.allowComments`: Boolean

#### Backend Synchronization

**Python Model**: `backend/src/models/project.py`

```python
class Project(BaseModel):
    id: UUID4
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
    owner_id: UUID4
    created_at: datetime
    updated_at: datetime
    settings: ProjectSettings
```

**Field Mapping**:
- TypeScript `camelCase` ↔ Python `snake_case`
- `ownerId` ↔ `owner_id`
- `createdAt` ↔ `created_at`
- `isPublic` ↔ `is_public`

#### Usage Example

```typescript
'use client';

import { createProject } from '@/app/actions/projects';

async function handleSubmit(formData: FormData) {
  const result = await createProject({
    name: formData.get('name') as string,
    description: formData.get('description') as string | null,
    settings: {
      isPublic: formData.get('isPublic') === 'true',
      allowComments: true,
    },
  });

  if (result.success) {
    console.log('Project created:', result.data.id);
  } else {
    console.error('Error:', result.error.message);
  }
}
```
```

## Deliverables Checklist

- [ ] TypeScript types defined in `src/types/api/[resource].ts`
- [ ] Zod schemas created in `src/lib/validations/[resource].ts`
- [ ] Server Action OR API Route implemented
- [ ] Error handling includes all status codes
- [ ] Backend model synchronized (if exists)
- [ ] API contract documented in `docs/api/[resource].md`
- [ ] Usage examples provided

---

**API contract ready! Test with your frontend forms or API clients.**
