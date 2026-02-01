# Create New Page Command

You are creating a new page in a Next.js 14+ App Router application following best practices for React Server Components, proper file organization, and complete route segment patterns.

## Task Overview

Generate a new route with all special files:
- `page.tsx` (Server Component by default)
- `layout.tsx` (if needed)
- `loading.tsx` (streaming UI fallback)
- `error.tsx` (error boundary)
- Client Components only where necessary

## Prerequisites

- Project must be initialized with `/setup-project` or equivalent
- `src/app/` directory must exist
- Route path must be decided

## Execution Instructions

### Step 1: Determine Route Structure

Ask the user for:
1. **Route path** (e.g., `/dashboard`, `/blog/[slug]`, `/settings/profile`)
2. **Page purpose** (what it displays, main features)
3. **Data requirements** (what data needs to be fetched?)
4. **Interactivity** (forms, buttons, client-side state?)

### Step 2: Create Directory Structure

For route path `/dashboard/[id]`:

```bash
mkdir -p src/app/dashboard/[id]
```

### Step 3: Generate page.tsx (Server Component Default)

**If page only displays data** (no interactivity):

```typescript
// src/app/dashboard/[id]/page.tsx
import { Suspense } from 'react';
import { notFound } from 'next/navigation';
import { DashboardContent } from './DashboardContent';
import { DashboardSkeleton } from './DashboardSkeleton';

// Metadata for SEO
export async function generateMetadata({ params }: Props) {
  const { id } = await params;
  // Fetch data for metadata if needed
  return {
    title: `Dashboard ${id}`,
    description: 'User dashboard page',
  };
}

interface Props {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}

export default async function DashboardPage({ params }: Props) {
  const { id } = await params;

  // Fetch data server-side
  const data = await fetchDashboardData(id);

  if (!data) {
    notFound(); // Renders not-found.tsx
  }

  return (
    <div>
      <h1>Dashboard {id}</h1>
      <Suspense fallback={<DashboardSkeleton />}>
        <DashboardContent data={data} />
      </Suspense>
    </div>
  );
}

// Optional: Static params for static generation
export async function generateStaticParams() {
  // Return array of { id: string } for static paths
  return [];
}
```

**If page needs interactivity** (hybrid approach):

```typescript
// src/app/dashboard/[id]/page.tsx (Server Component)
import { DashboardClient } from './DashboardClient';

export default async function DashboardPage({ params }: Props) {
  const { id } = await params;
  const data = await fetchDashboardData(id);

  // Pass data as props to Client Component
  return <DashboardClient initialData={data} />;
}

// src/app/dashboard/[id]/DashboardClient.tsx (Client Component)
'use client';

import { useState } from 'react';

interface Props {
  initialData: DashboardData;
}

export function DashboardClient({ initialData }: Props) {
  const [data, setData] = useState(initialData);

  const handleUpdate = async () => {
    // Client-side logic
  };

  return (
    <div>
      {/* Interactive UI */}
      <button onClick={handleUpdate}>Update</button>
    </div>
  );
}
```

### Step 4: Generate loading.tsx

```typescript
// src/app/dashboard/[id]/loading.tsx
export default function Loading() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-gray-900" />
      <p className="ml-4">Loading dashboard...</p>
    </div>
  );
}
```

### Step 5: Generate error.tsx

```typescript
// src/app/dashboard/[id]/error.tsx
'use client'; // Error boundaries must be Client Components

import { useEffect } from 'react';

interface Props {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function Error({ error, reset }: Props) {
  useEffect(() => {
    // Log error to error reporting service
    console.error('Dashboard error:', error);
  }, [error]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Something went wrong!</h2>
      <p className="text-gray-600 mb-4">{error.message}</p>
      <button
        onClick={reset}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Try again
      </button>
    </div>
  );
}
```

### Step 6: Generate layout.tsx (Optional, if route needs specific layout)

```typescript
// src/app/dashboard/layout.tsx
import { DashboardNav } from '@/components/layouts/DashboardNav';

interface Props {
  children: React.ReactNode;
}

export default function DashboardLayout({ children }: Props) {
  return (
    <div className="flex min-h-screen">
      <DashboardNav />
      <main className="flex-1 p-8">{children}</main>
    </div>
  );
}
```

### Step 7: Generate not-found.tsx (Optional, for custom 404)

```typescript
// src/app/dashboard/[id]/not-found.tsx
import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Dashboard Not Found</h2>
      <p className="text-gray-600 mb-4">Could not find the requested dashboard.</p>
      <Link href="/dashboard" className="text-blue-600 hover:underline">
        Return to dashboards
      </Link>
    </div>
  );
}
```

## Anti-Patterns to Avoid

❌ **Don't** use `'use client'` on page.tsx unless absolutely necessary
❌ **Don't** fetch data with `useEffect` - use async Server Components
❌ **Don't** omit loading.tsx and error.tsx
❌ **Don't** create one giant Client Component - compose Server + small Client Components

## Checklist

After creating the page, verify:
- [ ] page.tsx is a Server Component (no 'use client' unless needed)
- [ ] Data fetching is server-side (async/await in component)
- [ ] loading.tsx provides immediate feedback
- [ ] error.tsx handles errors gracefully
- [ ] TypeScript types are defined for all props
- [ ] Metadata is exported (title, description)
- [ ] Page is responsive (mobile, tablet, desktop)

---

**Page created! Test with `npm run dev` and navigate to the new route.**
