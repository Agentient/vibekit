# Setup State Persistence

Add localStorage or sessionStorage persistence to an existing Zustand store using the persist middleware.

## Instructions

You will configure the persist middleware for a Zustand store to save state across browser sessions or tabs.

### 1. Identify Requirements

Ask the user for:
- **Which store** needs persistence (store name or file path)
- **Storage type**:
  - `localStorage` - Data persists across browser sessions (survives page refresh, browser restart)
  - `sessionStorage` - Data persists only for current tab session (cleared when tab closes)
- **Persistence strategy**:
  - Persist entire state?
  - Persist only specific fields? (recommended)
- **Version management**: Does the state schema need migrations for breaking changes?

### 2. Check Current Store Structure

Read the existing store file to understand its structure. Look for:
- Current store interface
- Existing middleware (devtools, immer)
- Whether persist is already configured

### 3. Update Store with Persist Middleware

Modify the store to add persist middleware:

```typescript
import { create } from 'zustand';
import { persist, devtools, createJSONStorage } from 'zustand/middleware';

interface [Name]Store {
  // ... existing interface
}

export const use[Name]Store = create<[Name]Store>()(
  devtools(
    // Add persist middleware
    persist(
      (set, get) => ({
        // ... existing store implementation
      }),
      {
        // 1. Storage key (REQUIRED)
        name: '[name]-storage', // localStorage/sessionStorage key

        // 2. Storage type (REQUIRED)
        storage: createJSONStorage(() => localStorage), // or sessionStorage

        // 3. Partial persistence (RECOMMENDED)
        // Only persist specific fields instead of entire state
        partialize: (state) => ({
          [field1]: state.[field1],
          [field2]: state.[field2],
          // Omit fields you don't want to persist (like isLoading, error)
        }),

        // 4. Version for migrations (OPTIONAL)
        version: 1,

        // 5. Migration function (OPTIONAL)
        // Handle state schema changes between versions
        migrate: (persistedState: any, version: number) => {
          if (version === 0) {
            // Migrate from version 0 to 1
            return {
              ...persistedState,
              newField: 'defaultValue',
            };
          }
          return persistedState as [Name]Store;
        },

        // 6. Skip hydration (OPTIONAL)
        // Set to true to manually control hydration timing
        skipHydration: false,

        // 7. OnRehydrateStorage (OPTIONAL)
        // Called when state is loaded from storage
        onRehydrateStorage: (state) => {
          console.log('Hydration started');

          // Return cleanup/completion function
          return (state, error) => {
            if (error) {
              console.error('Hydration error:', error);
            } else {
              console.log('Hydration finished', state);
            }
          };
        },
      }
    ),
    {
      name: '[Name]Store',
      enabled: process.env.NODE_ENV === 'development',
    }
  )
);
```

### 4. Handle SSR/Next.js 14+ Integration (IMPORTANT)

For Next.js 14+ applications, persistence requires special handling to avoid hydration mismatches:

**Option A: Client Component with Hydration Check**
```typescript
'use client'

import { useState, useEffect } from 'react';
import { use[Name]Store } from '@/lib/stores/[name]-store';

export function [Component]() {
  // Prevent hydration mismatch
  const [hydrated, setHydrated] = useState(false);

  const store = use[Name]Store();

  useEffect(() => {
    // Trigger hydration after mount
    setHydrated(true);
  }, []);

  // Show loading or placeholder during hydration
  if (!hydrated) {
    return <div>Loading...</div>; // or null, or skeleton
  }

  // Render component with hydrated store data
  return (
    <div>
      {/* Component using store */}
    </div>
  );
}
```

**Option B: Using persist.hasHydrated()**
```typescript
'use client'

import { use[Name]Store } from '@/lib/stores/[name]-store';

export function [Component]() {
  // Check if store has hydrated
  const hasHydrated = use[Name]Store.persist.hasHydrated();

  if (!hasHydrated) {
    return <div>Loading...</div>;
  }

  const data = use[Name]Store((state) => state.data);

  return <div>{/* Use data */}</div>;
}
```

### 5. Configure Partial Persistence (Recommended)

Specify exactly which fields should be persisted:

```typescript
partialize: (state) => ({
  // ✅ Persist user data
  user: state.user,
  preferences: state.preferences,
  theme: state.theme,

  // ❌ Don't persist temporary/derived state
  // isLoading: state.isLoading,
  // error: state.error,
  // computedValue: state.getComputedValue(),
}),
```

**Best Practices**:
- ✅ Persist: User data, preferences, settings, auth tokens
- ❌ Don't persist: Loading states, errors, derived/computed values, temporary UI state

### 6. Version and Migration Strategy

For stores with evolving schemas, implement versioning:

```typescript
{
  name: 'user-storage',
  storage: createJSONStorage(() => localStorage),
  version: 2, // Current version

  migrate: (persistedState: any, version: number) => {
    // Handle migration from each previous version
    if (version === 1) {
      // v1 -> v2: Renamed 'username' to 'displayName'
      return {
        ...persistedState,
        displayName: persistedState.username,
        username: undefined, // Remove old field
      };
    }

    if (version === 0) {
      // v0 -> v1: Added 'role' field with default
      return {
        ...persistedState,
        role: 'user',
      };
    }

    return persistedState;
  },
}
```

## Critical Requirements

### Zustand v5 Persist (MANDATORY)
- ✅ MUST use `persist` middleware from `zustand/middleware`
- ✅ MUST use `createJSONStorage(() => localStorage)` for storage
- ✅ MUST configure `name` property (localStorage key)
- ✅ Persist middleware MUST wrap the store function (inside devtools if both used)

### SSR Compatibility (MANDATORY for Next.js 14+)
- ✅ Components using persisted stores MUST have `'use client'` directive
- ✅ MUST handle hydration mismatch (use hydrated state check)
- ❌ Server components CANNOT access persisted stores

### Partial Persistence (RECOMMENDED)
- ✅ Use `partialize` to persist only necessary fields
- ✅ Exclude temporary state (isLoading, error, etc.)
- ✅ Exclude derived/computed values

## Quality Checklist

Before completing, verify:

- [ ] Persist middleware added to store
- [ ] `name` configured (storage key)
- [ ] `storage` configured (localStorage or sessionStorage)
- [ ] `partialize` configured to persist only necessary fields
- [ ] SSR hydration handling added to components (if Next.js 14+)
- [ ] Version and migration strategy defined (if schema changes expected)
- [ ] Storage key is unique and descriptive
- [ ] Temporary/derived state excluded from persistence
- [ ] Tested that state persists across page refresh

## Anti-Patterns to Avoid

### ❌ Persisting Everything
```typescript
// WRONG: Persisting entire state including temporary values
persist((set) => ({ ... }), { name: 'storage' })

// CORRECT: Only persist necessary fields
persist((set) => ({ ... }), {
  name: 'storage',
  partialize: (state) => ({
    user: state.user,
    preferences: state.preferences,
  }),
})
```

### ❌ No Hydration Check in Next.js
```typescript
// WRONG: Direct usage without hydration check
export function Component() {
  const data = useStore((state) => state.data); // Hydration mismatch!
  return <div>{data}</div>;
}

// CORRECT: Check hydration status
export function Component() {
  const [hydrated, setHydrated] = useState(false);
  useEffect(() => setHydrated(true), []);
  if (!hydrated) return null;

  const data = useStore((state) => state.data);
  return <div>{data}</div>;
}
```

### ❌ Using String Instead of createJSONStorage
```typescript
// WRONG: v4 syntax
persist((set) => ({ ... }), {
  name: 'storage',
  getStorage: () => localStorage, // v4 syntax
})

// CORRECT: v5 syntax
persist((set) => ({ ... }), {
  name: 'storage',
  storage: createJSONStorage(() => localStorage),
})
```

## Output Format

Provide:
1. Updated store file with persist middleware configured
2. Example component showing hydration handling (for Next.js 14+)
3. Documentation comments explaining:
   - What fields are persisted
   - Storage type (localStorage vs sessionStorage)
   - Hydration requirements
   - Migration strategy (if applicable)

The configured persistence must work correctly in Next.js 14+ with proper SSR hydration handling.
