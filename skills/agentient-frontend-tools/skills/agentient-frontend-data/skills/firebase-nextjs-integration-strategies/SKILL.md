---
name: firebase-nextjs-integration-strategies
description: |
  Next.js 14+ App Router integration with Firebase, including server/client SDK separation, data fetching
  in Server Components, real-time listeners, middleware patterns, and optimistic updates with caching.
  Keywords: "nextjs", "app router", "server component", "client component", "middleware", "integration"
---

# Firebase Next.js Integration Strategies

## Overview

Next.js 14+ App Router has a clear server/client boundary. This skill provides patterns for integrating Firebase's dual SDK model (Client SDK + Admin SDK) with Next.js execution environments.

## Dual SDK Architecture

### Client SDK (Client Components, Browser)

**Use For**:
- Client-side authentication (sign-in, sign-up, sign-out)
- Real-time listeners (`onSnapshot`)
- Client-side mutations with optimistic updates
- File uploads to Storage

**Location**: `src/lib/firebase/client.ts`

```typescript
import { initializeApp, getApps } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0];

export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
```

### Admin SDK (Server Components, API Routes, Server Actions)

**Use For**:
- Privileged data access in Server Components
- Token verification in middleware
- Server-side mutations
- Bypassing security rules

**Location**: `src/lib/firebase/admin.ts`

```typescript
import 'server-only'; // CRITICAL: Prevents client bundling

import { initializeApp, getApps, cert } from 'firebase-admin/app';
import { getAuth } from 'firebase-admin/auth';
import { getFirestore } from 'firebase-admin/firestore';

const adminConfig = {
  projectId: process.env.FIREBASE_ADMIN_PROJECT_ID,
  credential: cert({
    projectId: process.env.FIREBASE_ADMIN_PROJECT_ID,
    clientEmail: process.env.FIREBASE_ADMIN_CLIENT_EMAIL,
    privateKey: process.env.FIREBASE_ADMIN_PRIVATE_KEY?.replace(/\\n/g, '\n'),
  }),
};

const adminApp = getApps().length === 0 ? initializeApp(adminConfig, 'admin') : getApps()[0];

export const adminAuth = getAuth(adminApp);
export const adminDb = getFirestore(adminApp);
```

## Data Fetching Patterns

### Pattern 1: Server Component (Recommended for Initial Load)

**Advantages**:
- Fast (no client-side fetch)
- SEO-friendly (pre-rendered)
- Secure (uses Admin SDK)
- Cached by Next.js

```typescript
// app/posts/page.tsx
import { adminDb } from '@/lib/firebase/admin';
import { postAdminConverter, type Post } from '@/lib/firebase/schemas/post.schema';

export default async function PostsPage() {
  // Fetch data server-side with Admin SDK
  const postsSnapshot = await adminDb
    .collection('posts')
    .withConverter(postAdminConverter)
    .where('status', '==', 'published')
    .orderBy('createdAt', 'desc')
    .limit(10)
    .get();

  const posts: Post[] = postsSnapshot.docs.map(doc => doc.data());

  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </article>
      ))}
    </div>
  );
}
```

**Next.js Caching**:
```typescript
// Revalidate every 60 seconds
export const revalidate = 60;

// Or use on-demand revalidation
import { revalidatePath } from 'next/cache';
revalidatePath('/posts');
```

### Pattern 2: Client Component with Real-Time Listener

**Use When**:
- Need real-time updates
- User-specific data (respects security rules)
- Interactive UI

```typescript
// components/CommentsList.tsx
'use client';

import { useEffect, useState } from 'react';
import { collection, query, where, onSnapshot, orderBy } from 'firebase/firestore';
import { db } from '@/lib/firebase/client';
import { commentConverter, type Comment } from '@/lib/firebase/schemas/comment.schema';

export function CommentsList({ postId }: { postId: string }) {
  const [comments, setComments] = useState<Comment[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Real-time listener with withConverter
    const q = query(
      collection(db, 'comments'),
      where('postId', '==', postId),
      orderBy('createdAt', 'desc')
    ).withConverter(commentConverter);

    const unsubscribe = onSnapshot(q, (snapshot) => {
      const commentsData = snapshot.docs.map(doc => doc.data());
      setComments(commentsData);
      setLoading(false);
    });

    return unsubscribe; // Cleanup on unmount
  }, [postId]);

  if (loading) return <div>Loading comments...</div>;

  return (
    <div>
      {comments.map(comment => (
        <div key={comment.id}>{comment.content}</div>
      ))}
    </div>
  );
}
```

### Pattern 3: Server Action (Mutations)

**Use For**:
- Form submissions
- User-initiated mutations
- Progressive enhancement

```typescript
// app/actions/createPost.ts
'use server';

import { adminDb } from '@/lib/firebase/admin';
import { PostSchema, postAdminConverter } from '@/lib/firebase/schemas/post.schema';
import { revalidatePath } from 'next/cache';
import { z } from 'zod';

const CreatePostInput = PostSchema.pick({
  title: true,
  content: true,
}).extend({
  authorId: z.string(),
});

export async function createPost(input: z.infer<typeof CreatePostInput>) {
  // Validate input
  const validated = CreatePostInput.parse(input);

  // Create post with Admin SDK
  const postRef = adminDb.collection('posts').doc();
  await postRef.withConverter(postAdminConverter).set({
    ...validated,
    status: 'draft',
    viewCount: 0,
    createdAt: new Date(),
    updatedAt: new Date(),
  });

  // Revalidate posts page cache
  revalidatePath('/posts');

  return { success: true, postId: postRef.id };
}
```

**Client Usage**:
```typescript
'use client';

import { createPost } from '@/app/actions/createPost';

export function CreatePostForm() {
  async function handleSubmit(formData: FormData) {
    const result = await createPost({
      title: formData.get('title') as string,
      content: formData.get('content') as string,
      authorId: 'user123',
    });

    if (result.success) {
      // Handle success
    }
  }

  return (
    <form action={handleSubmit}>
      <input name="title" required />
      <textarea name="content" required />
      <button type="submit">Create Post</button>
    </form>
  );
}
```

### Pattern 4: API Route

**Use For**:
- External API calls
- Webhooks
- Complex server-side logic

```typescript
// app/api/posts/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { adminDb, adminAuth } from '@/lib/firebase/admin';
import { postAdminConverter } from '@/lib/firebase/schemas/post.schema';

export async function GET(request: NextRequest) {
  // Verify authentication
  const token = request.cookies.get('firebase-token')?.value;
  if (!token) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  try {
    await adminAuth.verifyIdToken(token);

    // Fetch posts
    const postsSnapshot = await adminDb
      .collection('posts')
      .withConverter(postAdminConverter)
      .limit(10)
      .get();

    const posts = postsSnapshot.docs.map(doc => doc.data());

    return NextResponse.json({ posts });
  } catch (error) {
    return NextResponse.json({ error: 'Invalid token' }, { status: 401 });
  }
}
```

## Middleware Pattern

### Token Verification

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';
import { adminAuth } from '@/lib/firebase/admin';

export async function middleware(request: NextRequest) {
  const token = request.cookies.get('firebase-token')?.value;

  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  try {
    const decodedToken = await adminAuth.verifyIdToken(token);

    // Add user info to headers for Server Components
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set('x-user-id', decodedToken.uid);
    requestHeaders.set('x-user-email', decodedToken.email || '');
    requestHeaders.set('x-user-role', decodedToken.role || 'user');

    return NextResponse.next({
      request: { headers: requestHeaders },
    });
  } catch (error) {
    const response = NextResponse.redirect(new URL('/login', request.url));
    response.cookies.delete('firebase-token');
    return response;
  }
}

export const config = {
  matcher: ['/dashboard/:path*', '/profile/:path*'],
};
```

### Reading Headers in Server Component

```typescript
// app/dashboard/page.tsx
import { headers } from 'next/headers';

export default async function DashboardPage() {
  const userId = headers().get('x-user-id');
  const userRole = headers().get('x-user-role');

  return <div>Welcome, {userId}</div>;
}
```

## Optimistic Updates Pattern

**Pattern**: Update UI immediately, sync with server in background

```typescript
'use client';

import { useState, useTransition } from 'react';
import { doc, updateDoc } from 'firebase/firestore';
import { db } from '@/lib/firebase/client';

export function LikeButton({ postId, initialLikes }: { postId: string; initialLikes: number }) {
  const [likes, setLikes] = useState(initialLikes);
  const [isPending, startTransition] = useTransition();

  async function handleLike() {
    // Optimistic update
    setLikes(prev => prev + 1);

    // Background sync
    startTransition(async () => {
      try {
        await updateDoc(doc(db, 'posts', postId), {
          likes: likes + 1,
        });
      } catch (error) {
        // Rollback on error
        setLikes(prev => prev - 1);
      }
    });
  }

  return (
    <button onClick={handleLike} disabled={isPending}>
      👍 {likes}
    </button>
  );
}
```

## Caching Strategies

### Next.js Request Memoization

Server Components automatically dedupe requests within the same render:

```typescript
// These will only make ONE request
const posts1 = await getPosts();
const posts2 = await getPosts(); // Deduped!
```

### React Cache

```typescript
import { cache } from 'react';
import { adminDb } from '@/lib/firebase/admin';

export const getPost = cache(async (postId: string) => {
  const postDoc = await adminDb.collection('posts').doc(postId).get();
  return postDoc.data();
});
```

### Time-Based Revalidation

```typescript
// app/posts/page.tsx
export const revalidate = 60; // Revalidate every 60 seconds

export default async function PostsPage() {
  const posts = await getPosts();
  return <div>{/* Render posts */}</div>;
}
```

### On-Demand Revalidation

```typescript
// app/actions/updatePost.ts
'use server';

import { revalidatePath, revalidateTag } from 'next/cache';

export async function updatePost(postId: string, updates: Partial<Post>) {
  await adminDb.collection('posts').doc(postId).update(updates);

  // Revalidate specific path
  revalidatePath('/posts');
  revalidatePath(`/posts/${postId}`);

  // Or use tags for finer control
  revalidateTag('posts');
}
```

## Best Practices

✅ **Do**:
- Use Server Components for initial data load (faster, SEO-friendly)
- Use Client Components for real-time updates
- Use Admin SDK in Server Components/Actions (privileged, bypasses rules)
- Use Client SDK in Client Components (respects security rules)
- Verify tokens in middleware
- Store tokens in `HttpOnly` cookies (not localStorage)
- Use `server-only` package for admin files

❌ **Don't**:
- Import Admin SDK in Client Components
- Use Client SDK in Server Components (wrong execution context)
- Skip token verification
- Fetch data client-side when Server Component would work
- Forget to cleanup real-time listeners (`onSnapshot`)

## Decision Tree

**When to use Server Components**:
- Initial page load
- SEO-critical content
- Privileged data access
- Static or slow-changing data

**When to use Client Components**:
- Real-time updates
- User interactions
- Client-side state
- Animations

**When to use Server Actions**:
- Form submissions
- Mutations
- Progressive enhancement

**When to use API Routes**:
- External webhooks
- Complex server logic
- Non-Next.js clients

---

**Related Skills**: `firebase-admin-sdk-server-integration`, `firestore-data-modeling-patterns`
**Token Estimate**: ~1,400 tokens
