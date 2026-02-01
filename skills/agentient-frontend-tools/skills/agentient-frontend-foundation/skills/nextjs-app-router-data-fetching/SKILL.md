---
name: nextjs-app-router-data-fetching
description: |
  Data fetching patterns for Next.js 14+ App Router. Async Server Components, Server Actions,
  caching, revalidation. Use when fetching data, calling APIs, using Server Actions. Keywords:
  "fetch data", "api call", "database", "server action", "revalidate", "cache".
---

# Next.js App Router Data Fetching

## Pattern 1: Async Server Components (Recommended)

```tsx
// app/posts/page.tsx (Server Component)
export default async function PostsPage() {
  // Fetch directly in Server Component
  const posts = await fetch('https://api.example.com/posts', {
    next: { revalidate: 60 } // Revalidate every 60 seconds
  }).then(res => res.json());

  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>{post.title}</article>
      ))}
    </div>
  );
}
```

**Benefits**:
- No loading spinners (rendered on server)
- No client-server waterfalls
- Can access database directly (no API layer needed)
- Automatic request deduplication

## Pattern 2: Server Actions (For Mutations)

```tsx
// app/actions/posts.ts
'use server'

import { revalidatePath } from 'next/cache';

export async function createPost(formData: FormData) {
  const title = formData.get('title');

  await db.post.create({ data: { title } });

  revalidatePath('/posts'); // Invalidate cache

  return { success: true };
}

// app/posts/new/page.tsx
import { createPost } from '@/app/actions/posts';

export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}
```

## Caching Strategies

```tsx
// No caching (always fresh)
fetch('...', { cache: 'no-store' })

// Cache forever (static)
fetch('...', { cache: 'force-cache' })

// Time-based revalidation (ISR)
fetch('...', { next: { revalidate: 3600 } }) // 1 hour

// On-demand revalidation (with tags)
fetch('...', { next: { tags: ['posts'] } })
// Later: revalidateTag('posts')
```

## Anti-Pattern: useEffect for Data Fetching

```tsx
// ❌ DON'T: Client-side fetching with useEffect
'use client'
function Posts() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('/api/posts').then(r => r.json()).then(setPosts);
  }, []);

  return // ... causes client-server waterfall, loading spinner needed
}

// ✅ DO: Server Component
async function Posts() {
  const posts = await fetch('...').then(r => r.json());
  return // ... pre-rendered, no loading state
}
```

## Parallel Data Fetching

```tsx
export default async function Page() {
  // Fetch in parallel
  const [user, posts, comments] = await Promise.all([
    fetchUser(),
    fetchPosts(),
    fetchComments(),
  ]);

  return // ...
}
```

For database integration and advanced caching, see `resources/database-patterns.md`.
