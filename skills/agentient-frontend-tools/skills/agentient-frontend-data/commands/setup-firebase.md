---
name: setup-firebase
description: Initialize Firebase project with dual SDK setup (client JS SDK + server Admin SDK) for Next.js 14+ App Router
---

# /setup-firebase Command

**Purpose**: Automate Firebase project initialization with secure, environment-aware SDK setup for both client and server contexts in Next.js 14+ applications.

## Usage

```bash
/setup-firebase
```

The command will guide you through Firebase project setup or you can provide project details:

```bash
/setup-firebase --project-id my-app-prod --region us-central1
```

## What This Command Generates

1. **Client SDK Initialization** (`src/lib/firebase/client.ts`)
2. **Server Admin SDK Initialization** (`src/lib/firebase/admin.ts`) with `server-only` protection
3. **Zod Converter Utilities** (`src/lib/firebase/zodConverter.ts`)
4. **Environment Variable Template** (`.env.local.example`)
5. **Firebase Configuration Files** (`firebase.json`, `.firebaserc`)
6. **Type Definitions** (`src/types/firebase.d.ts`)

## Output Structure

```
src/lib/firebase/
├── client.ts              # Client SDK (auth, db, storage)
├── admin.ts               # Server Admin SDK (server-only)
├── zodConverter.ts        # Generic Zod converter utilities
└── types.ts               # Shared Firebase types

.env.local.example         # Environment variable template
firebase.json              # Firebase project configuration
.firebaserc                # Firebase project aliases
```

## Interactive Prompts

The command will ask:

1. **Firebase Project ID**: Your Firebase project identifier
2. **Firebase Region**: Default region for Functions/Firestore (e.g., `us-central1`)
3. **Services to Enable**:
   - [ ] Authentication
   - [ ] Firestore
   - [ ] Cloud Storage
   - [ ] Cloud Functions (optional)
4. **Admin SDK Credentials**: How to provide service account key
   - Option A: Service account JSON file path
   - Option B: Individual environment variables
5. **Development vs Production**: Separate project IDs or same?

## Example Session

```
User: /setup-firebase

Agent: I'll help you set up Firebase for your Next.js project.

Firebase Project ID: my-app-prod

Firebase Region: us-central1

Enable Firebase services:
  ✓ Authentication
  ✓ Firestore
  ✓ Cloud Storage
  ✗ Cloud Functions

Admin SDK Credentials:
  How would you like to provide service account credentials?
  1. Upload service account JSON file
  2. Set individual environment variables

  Choice: 2

Environment:
  Use separate dev/prod Firebase projects? (recommended): y
  Development Project ID: my-app-dev

Generating files...
✓ src/lib/firebase/client.ts
✓ src/lib/firebase/admin.ts (with server-only protection)
✓ src/lib/firebase/zodConverter.ts
✓ .env.local.example
✓ firebase.json
✓ .firebaserc

Next steps:
1. Copy .env.local.example to .env.local
2. Fill in Firebase credentials (see Firebase Console > Project Settings)
3. Download service account key (Settings > Service Accounts > Generate New Private Key)
4. Run: npm install firebase firebase-admin server-only zod
5. Test with: /model-collection to create your first collection
```

## Generated Client SDK

```typescript
// src/lib/firebase/client.ts
import { initializeApp, getApps, type FirebaseApp } from 'firebase/app';
import { getAuth, type Auth } from 'firebase/auth';
import { getFirestore, type Firestore } from 'firebase/firestore';
import { getStorage, type FirebaseStorage } from 'firebase/storage';

/**
 * Firebase Client SDK Configuration
 * Safe to use in client-side components
 */
const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Initialize Firebase (singleton pattern)
let app: FirebaseApp;
if (getApps().length === 0) {
  app = initializeApp(firebaseConfig);
} else {
  app = getApps()[0];
}

/**
 * Firebase Authentication
 * Use in client components for sign-in, sign-up, sign-out
 */
export const auth: Auth = getAuth(app);

/**
 * Firestore Database
 * Use in client components for real-time listeners and client-side queries
 */
export const db: Firestore = getFirestore(app);

/**
 * Firebase Storage
 * Use in client components for file uploads
 */
export const storage: FirebaseStorage = getStorage(app);

export { app };
```

## Generated Server Admin SDK

```typescript
// src/lib/firebase/admin.ts
import 'server-only'; // CRITICAL: Prevents client-side bundling

import { initializeApp, getApps, cert, type App } from 'firebase-admin/app';
import { getAuth, type Auth } from 'firebase-admin/auth';
import { getFirestore, type Firestore } from 'firebase-admin/firestore';
import { getStorage, type Storage } from 'firebase-admin/storage';

/**
 * Firebase Admin SDK Configuration
 * ONLY use in Server Components, API Routes, or Server Actions
 *
 * The 'server-only' import ensures this code is never bundled for the client
 */
const adminConfig = {
  projectId: process.env.FIREBASE_ADMIN_PROJECT_ID,
  credential: cert({
    projectId: process.env.FIREBASE_ADMIN_PROJECT_ID,
    clientEmail: process.env.FIREBASE_ADMIN_CLIENT_EMAIL,
    // Replace escaped newlines in private key
    privateKey: process.env.FIREBASE_ADMIN_PRIVATE_KEY?.replace(/\\n/g, '\n'),
  }),
};

// Validate required environment variables
if (
  !process.env.FIREBASE_ADMIN_PROJECT_ID ||
  !process.env.FIREBASE_ADMIN_CLIENT_EMAIL ||
  !process.env.FIREBASE_ADMIN_PRIVATE_KEY
) {
  throw new Error(
    'Missing Firebase Admin SDK environment variables. See .env.local.example'
  );
}

// Initialize Admin SDK (singleton pattern)
let adminApp: App;
if (getApps().length === 0) {
  adminApp = initializeApp(adminConfig, 'admin');
} else {
  adminApp = getApps()[0];
}

/**
 * Firebase Admin Authentication
 * Use for:
 * - Verifying ID tokens in middleware
 * - Setting custom claims
 * - Creating users server-side
 */
export const adminAuth: Auth = getAuth(adminApp);

/**
 * Firestore Admin Database
 * Use for:
 * - Privileged data access in Server Components
 * - Bypassing security rules (use responsibly)
 * - Server-side queries and mutations
 */
export const adminDb: Firestore = getFirestore(adminApp);

/**
 * Firebase Admin Storage
 * Use for:
 * - Generating signed URLs
 * - Server-side file operations
 */
export const adminStorage: Storage = getStorage(adminApp);

export { adminApp };
```

## Generated Zod Converter Utilities

```typescript
// src/lib/firebase/zodConverter.ts
import type {
  DocumentData,
  FirestoreDataConverter,
  QueryDocumentSnapshot,
  SnapshotOptions,
  WithFieldValue,
} from 'firebase/firestore';
import type { ZodSchema } from 'zod';

/**
 * Generic Zod Firestore Converter (Client SDK)
 *
 * Validates data on both read and write operations
 * Automatically injects document ID and ref
 *
 * @example
 * const postConverter = zodConverter(PostSchema);
 * const postRef = doc(db, 'posts', 'post1').withConverter(postConverter);
 * const post = (await getDoc(postRef)).data(); // Type: Post
 */
export function zodConverter<T extends DocumentData>(
  schema: ZodSchema<T>
): FirestoreDataConverter<T> {
  return {
    toFirestore(data: WithFieldValue<T>): DocumentData {
      // Validate before writing
      const validated = schema.parse(data);
      return validated;
    },
    fromFirestore(
      snapshot: QueryDocumentSnapshot<DocumentData>,
      options?: SnapshotOptions
    ): T {
      const data = snapshot.data(options);
      // Inject document ID and ref for convenience
      const dataWithMeta = {
        ...data,
        id: snapshot.id,
        ref: snapshot.ref,
      };
      // Validate after reading
      return schema.parse(dataWithMeta) as T;
    },
  };
}

/**
 * Generic Zod Firestore Converter (Admin SDK)
 *
 * Validates data on read, optional validation on write
 * Use in server-side code only
 *
 * @example
 * const postConverter = zodAdminConverter(PostSchema);
 * const snapshot = await adminDb.collection('posts').withConverter(postConverter).get();
 * const posts = snapshot.docs.map(doc => doc.data()); // Type: Post[]
 */
export function zodAdminConverter<T extends DocumentData>(
  schema: ZodSchema<T>,
  validateWrites = false
): FirestoreDataConverter<T> {
  return {
    toFirestore(data: WithFieldValue<T>): DocumentData {
      // Optional write validation (server-side code is trusted)
      if (validateWrites) {
        return schema.parse(data);
      }
      return data as DocumentData;
    },
    fromFirestore(snapshot: QueryDocumentSnapshot<DocumentData>): T {
      const data = snapshot.data();
      const dataWithMeta = {
        ...data,
        id: snapshot.id,
        ref: snapshot.ref,
      };
      return schema.parse(dataWithMeta) as T;
    },
  };
}
```

## Generated Environment Template

```bash
# .env.local.example

# ============================================================================
# FIREBASE CLIENT SDK (Public - safe to expose in browser)
# ============================================================================
# Get these from: Firebase Console > Project Settings > General > Your apps
NEXT_PUBLIC_FIREBASE_API_KEY=your_api_key_here
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your_project_id.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
NEXT_PUBLIC_FIREBASE_APP_ID=your_app_id

# ============================================================================
# FIREBASE ADMIN SDK (Private - server-side only, NEVER expose in browser)
# ============================================================================
# Get these from: Firebase Console > Project Settings > Service Accounts >
#                 Generate New Private Key (downloads JSON file)
FIREBASE_ADMIN_PROJECT_ID=your_project_id
FIREBASE_ADMIN_CLIENT_EMAIL=firebase-adminsdk-xxxxx@your_project_id.iam.gserviceaccount.com
FIREBASE_ADMIN_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYourPrivateKeyHere\n-----END PRIVATE KEY-----\n"

# ============================================================================
# DEVELOPMENT ENVIRONMENT (Optional)
# ============================================================================
# Use a separate Firebase project for development
# NODE_ENV=development
# NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id_dev
```

## Integration with Other Commands

- **Follow up with `/model-collection`** to create your first type-safe collection
- **Use `/create-auth-flow`** to implement authentication
- **Reference in `/generate-security-rules`** for security rule deployment

## Best Practices

✅ **Do**:
- Use separate Firebase projects for dev/staging/production
- Store Admin SDK credentials in environment variables (never commit)
- Use the `server-only` package for Admin SDK files
- Validate environment variables on startup

❌ **Don't**:
- Commit `.env.local` to version control
- Use Admin SDK in client components
- Hardcode Firebase credentials
- Share Admin SDK service account keys

## Troubleshooting

**Issue**: "Missing environment variable" error on startup
**Solution**: Ensure `.env.local` exists and matches `.env.local.example`

**Issue**: "server-only module included in client bundle"
**Solution**: Verify `admin.ts` has `import 'server-only'` at the top

**Issue**: "Firebase app already exists"
**Solution**: Use the singleton pattern (check `getApps().length`)

---

**Related Commands**: `/model-collection`, `/create-auth-flow`, `/generate-security-rules`
**Skill Dependencies**: `firebase-nextjs-integration-strategies`, `firebase-admin-sdk-server-integration`
