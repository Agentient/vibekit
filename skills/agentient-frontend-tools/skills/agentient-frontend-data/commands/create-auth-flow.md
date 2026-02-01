---
name: create-auth-flow
description: Implement complete authentication flow with sign-in, sign-up, session management, and protected routes for Next.js 14+
---

# /create-auth-flow Command

**Purpose**: Generate production-ready authentication flow with Firebase Authentication, including UI components, session management, protected routes, and optional RBAC with custom claims.

## Usage

```bash
/create-auth-flow
```

Or specify authentication providers upfront:

```bash
/create-auth-flow --providers email,google,github --rbac admin,user
```

## What This Command Generates

1. **Authentication Helper Functions** (`src/lib/firebase/auth.ts`)
2. **Auth UI Components** (sign-in, sign-up, sign-out forms)
3. **Session Management** (middleware for protected routes)
4. **Auth Context Provider** (React Context for client-side auth state)
5. **Protected Route HOC/Wrapper**
6. **Custom Claims API** (for RBAC, if requested)
7. **User Profile Schema** (extends with role/permissions if RBAC enabled)

## Output Structure

```
src/
├── lib/firebase/
│   ├── auth.ts                    # Auth helper functions
│   └── schemas/user.schema.ts     # User profile schema
├── components/auth/
│   ├── SignInForm.tsx             # Sign-in UI
│   ├── SignUpForm.tsx             # Sign-up UI
│   ├── SignOutButton.tsx          # Sign-out UI
│   └── AuthProvider.tsx           # Auth context provider
├── app/
│   ├── api/admin/
│   │   └── set-role/route.ts      # Custom claims API (RBAC)
│   ├── (auth)/
│   │   ├── login/page.tsx         # Login page
│   │   └── signup/page.tsx        # Signup page
│   └── (protected)/               # Protected routes group
│       └── layout.tsx             # Protected layout with auth check
└── middleware.ts                   # Route protection middleware
```

## Interactive Prompts

The command will ask:

1. **Authentication Providers**:
   - [ ] Email/Password
   - [ ] Google
   - [ ] GitHub
   - [ ] Facebook
   - [ ] Anonymous
2. **RBAC (Role-Based Access Control)**:
   - Enable custom roles? (y/n)
   - Roles: (e.g., admin, user, moderator)
3. **User Profile Fields**:
   - Additional fields beyond email? (name, avatar, bio, etc.)
4. **Password Requirements**:
   - Minimum length, complexity rules
5. **Redirect Behavior**:
   - After sign-in: (e.g., /dashboard)
   - After sign-out: (e.g., /login)

## Example Session

```
User: /create-auth-flow

Agent: I'll help you set up Firebase Authentication for your Next.js app.

Authentication Providers:
  ✓ Email/Password
  ✓ Google
  ✗ GitHub
  ✗ Facebook

Enable Role-Based Access Control (RBAC)? y
  Define roles (comma-separated): admin, user, moderator

User Profile Fields:
  ✓ name (required)
  ✓ avatar URL (optional)
  ✗ bio

Password Requirements:
  Minimum length: 8
  Require uppercase: y
  Require number: y
  Require special character: n

Redirect After Sign-In: /dashboard
Redirect After Sign-Out: /login

Protected Routes:
  Which routes require authentication? /dashboard/*, /profile/*

Generating files...
✓ src/lib/firebase/auth.ts
✓ src/lib/firebase/schemas/user.schema.ts
✓ src/components/auth/SignInForm.tsx
✓ src/components/auth/SignUpForm.tsx
✓ src/components/auth/SignOutButton.tsx
✓ src/components/auth/AuthProvider.tsx
✓ src/app/(auth)/login/page.tsx
✓ src/app/(auth)/signup/page.tsx
✓ src/app/api/admin/set-role/route.ts
✓ middleware.ts

Next steps:
1. Enable authentication providers in Firebase Console
2. Add OAuth app credentials (Google, etc.)
3. Wrap your app with <AuthProvider> in app/layout.tsx
4. Test sign-up at http://localhost:3000/signup
```

## Generated Auth Helper Functions

```typescript
// src/lib/firebase/auth.ts
import { auth } from './client';
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signInWithPopup,
  GoogleAuthProvider,
  signOut as firebaseSignOut,
  onAuthStateChanged,
  type User,
  type UserCredential,
} from 'firebase/auth';

/**
 * Sign in with email and password
 * @throws FirebaseError with specific error codes
 */
export async function signIn(email: string, password: string): Promise<UserCredential> {
  try {
    return await signInWithEmailAndPassword(auth, email, password);
  } catch (error) {
    // Map Firebase error codes to user-friendly messages
    if (error instanceof Error && 'code' in error) {
      const firebaseError = error as { code: string };
      switch (firebaseError.code) {
        case 'auth/user-not-found':
        case 'auth/wrong-password':
          throw new Error('Invalid email or password');
        case 'auth/too-many-requests':
          throw new Error('Too many failed attempts. Try again later.');
        default:
          throw new Error('Sign in failed. Please try again.');
      }
    }
    throw error;
  }
}

/**
 * Sign up with email and password
 * Creates user profile in Firestore after successful registration
 */
export async function signUp(
  email: string,
  password: string,
  displayName: string
): Promise<UserCredential> {
  try {
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);

    // Create user profile in Firestore
    await fetch('/api/users/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        uid: userCredential.user.uid,
        email,
        displayName,
        role: 'user', // Default role
      }),
    });

    return userCredential;
  } catch (error) {
    if (error instanceof Error && 'code' in error) {
      const firebaseError = error as { code: string };
      switch (firebaseError.code) {
        case 'auth/email-already-in-use':
          throw new Error('Email already registered');
        case 'auth/weak-password':
          throw new Error('Password must be at least 8 characters');
        default:
          throw new Error('Sign up failed. Please try again.');
      }
    }
    throw error;
  }
}

/**
 * Sign in with Google OAuth
 */
export async function signInWithGoogle(): Promise<UserCredential> {
  const provider = new GoogleAuthProvider();
  return await signInWithPopup(auth, provider);
}

/**
 * Sign out current user
 */
export async function signOut(): Promise<void> {
  await firebaseSignOut(auth);
}

/**
 * Subscribe to auth state changes
 * Returns unsubscribe function
 */
export function onAuthChange(callback: (user: User | null) => void): () => void {
  return onAuthStateChanged(auth, callback);
}

/**
 * Get current user's ID token
 * Use for authenticated API requests
 */
export async function getIdToken(): Promise<string | null> {
  const user = auth.currentUser;
  if (!user) return null;
  return await user.getIdToken();
}

/**
 * Force refresh ID token (after custom claims are updated)
 */
export async function refreshIdToken(): Promise<string | null> {
  const user = auth.currentUser;
  if (!user) return null;
  return await user.getIdToken(true); // Force refresh
}
```

## Generated Middleware (Protected Routes)

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';
import { adminAuth } from '@/lib/firebase/admin';

/**
 * Middleware to protect routes requiring authentication
 */
export async function middleware(request: NextRequest) {
  const token = request.cookies.get('firebase-token')?.value;

  // No token - redirect to login
  if (!token) {
    const url = new URL('/login', request.url);
    url.searchParams.set('redirect', request.nextUrl.pathname);
    return NextResponse.redirect(url);
  }

  try {
    // Verify token is valid
    const decodedToken = await adminAuth.verifyIdToken(token);

    // Check role-based access (if RBAC enabled)
    const requiredRole = getRequiredRole(request.nextUrl.pathname);
    if (requiredRole && decodedToken.role !== requiredRole) {
      return NextResponse.redirect(new URL('/unauthorized', request.url));
    }

    // Add user info to request headers for Server Components
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set('x-user-id', decodedToken.uid);
    requestHeaders.set('x-user-email', decodedToken.email || '');
    requestHeaders.set('x-user-role', decodedToken.role || 'user');

    return NextResponse.next({
      request: {
        headers: requestHeaders,
      },
    });
  } catch (error) {
    // Invalid token - clear and redirect to login
    const response = NextResponse.redirect(new URL('/login', request.url));
    response.cookies.delete('firebase-token');
    return response;
  }
}

/**
 * Map routes to required roles
 */
function getRequiredRole(pathname: string): string | null {
  if (pathname.startsWith('/admin')) return 'admin';
  if (pathname.startsWith('/moderator')) return 'moderator';
  return null; // Any authenticated user
}

/**
 * Protected route patterns
 */
export const config = {
  matcher: [
    '/dashboard/:path*',
    '/profile/:path*',
    '/admin/:path*',
    '/moderator/:path*',
  ],
};
```

## Generated Auth Context Provider

```typescript
// src/components/auth/AuthProvider.tsx
'use client';

import { createContext, useContext, useEffect, useState } from 'react';
import { User } from 'firebase/auth';
import { onAuthChange } from '@/lib/firebase/auth';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  role: string | null;
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  loading: true,
  role: null,
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [role, setRole] = useState<string | null>(null);

  useEffect(() => {
    const unsubscribe = onAuthChange(async (firebaseUser) => {
      setUser(firebaseUser);

      if (firebaseUser) {
        // Get ID token to access custom claims
        const idTokenResult = await firebaseUser.getIdTokenResult();
        setRole((idTokenResult.claims.role as string) || 'user');

        // Set token in cookie for middleware
        document.cookie = `firebase-token=${idTokenResult.token}; path=/; secure; samesite=strict`;
      } else {
        setRole(null);
        // Clear token cookie
        document.cookie = 'firebase-token=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT';
      }

      setLoading(false);
    });

    return unsubscribe;
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading, role }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
```

## Generated Custom Claims API (RBAC)

```typescript
// src/app/api/admin/set-role/route.ts
import 'server-only';
import { adminAuth } from '@/lib/firebase/admin';
import { NextRequest, NextResponse } from 'next/server';
import { z } from 'zod';

const SetRoleSchema = z.object({
  uid: z.string().min(1),
  role: z.enum(['admin', 'moderator', 'user']),
});

/**
 * Set custom role claim on a user
 * Requires admin role to access
 */
export async function POST(request: NextRequest) {
  try {
    // Verify requester is authenticated and is admin
    const token = request.cookies.get('firebase-token')?.value;
    if (!token) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    const decodedToken = await adminAuth.verifyIdToken(token);
    if (decodedToken.role !== 'admin') {
      return NextResponse.json({ error: 'Forbidden: Admin role required' }, { status: 403 });
    }

    // Validate request body
    const body = await request.json();
    const { uid, role } = SetRoleSchema.parse(body);

    // Set custom claim
    await adminAuth.setCustomUserClaims(uid, { role });

    return NextResponse.json({
      success: true,
      message: `Role '${role}' assigned to user ${uid}`,
    });
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json({ error: 'Invalid request data', details: error.errors }, { status: 400 });
    }

    console.error('Error setting custom claim:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
```

## Integration with Other Commands

- **Requires `/setup-firebase`** to be run first for SDK initialization
- **Integrates with `/model-collection`** for user profile schema
- **Works with `/generate-security-rules`** for user-scoped data access

## Best Practices

✅ **Do**:
- Use `HttpOnly` cookies for storing tokens (not localStorage)
- Force token refresh after setting custom claims
- Validate user input before authentication
- Implement rate limiting for auth endpoints

❌ **Don't**:
- Store sensitive user data in custom claims (1000 byte limit)
- Skip email verification for production apps
- Allow client-side role assignment
- Use weak password requirements

## Troubleshooting

**Issue**: "Token refresh required" after role assignment
**Solution**: Call `refreshIdToken()` after `setCustomUserClaims()`

**Issue**: "Middleware infinite redirect loop"
**Solution**: Exclude `/login` and `/signup` from middleware matcher

**Issue**: "CORS error on OAuth popup"
**Solution**: Add authorized domains in Firebase Console > Authentication > Settings

---

**Related Commands**: `/setup-firebase`, `/generate-security-rules`, `/model-collection`
**Skill Dependencies**: `firebase-authentication-patterns`, `firebase-admin-sdk-server-integration`
