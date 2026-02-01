# Create Zustand Store Command

Generate a new Zustand 5.0.2+ store with TypeScript types and middleware configuration for Next.js 14+ applications.

## Instructions

You will create a fully typed, production-ready Zustand v5 store following these specifications:

### 1. Gather Requirements

Ask the user for:
- **Store name** (e.g., "user", "cart", "settings")
- **State properties** and their types
- **Actions** needed (what operations modify the state)
- **Middleware requirements**:
  - Persist (localStorage/sessionStorage)?
  - DevTools (for debugging)?
  - Immer (for complex nested updates)?

### 2. Generate Store File Structure

Create the store at `lib/stores/[name]-store.ts` with this structure:

```typescript
import { create } from 'zustand';
import { persist, devtools, createJSONStorage } from 'zustand/middleware';

// 1. Define TypeScript interface (MANDATORY)
interface [Name]Store {
  // State properties
  [property]: [type];

  // Actions
  [actionName]: ([params]) => void | Promise<void>;

  // Computed values (optional)
  [getterName]: () => [returnType];
}

// 2. Create store with v5 curried syntax
export const use[Name]Store = create<[Name]Store>()(
  devtools(
    persist(
      (set, get) => ({
        // 3. Initial state
        [property]: [initialValue],

        // 4. Actions with immutable updates
        [actionName]: ([params]) => set((state) => ({
          // Return new state object - NEVER mutate
          [property]: state.[property] + 1,
        })),

        // 5. Computed values using get()
        [getterName]: () => {
          const state = get();
          return /* computed value */;
        },
      }),
      {
        name: '[name]-storage', // localStorage key
        storage: createJSONStorage(() => localStorage),

        // Optional: Only persist specific fields
        partialize: (state) => ({
          [field]: state.[field],
        }),

        // Optional: Version for migrations
        version: 1,
        migrate: (persistedState, version) => {
          // Handle migrations here
          return persistedState as [Name]Store;
        },
      }
    ),
    {
      name: '[Name]Store', // DevTools name
      enabled: process.env.NODE_ENV === 'development',
    }
  )
);

// 6. Export optimized selectors
export const select[Property] = (state: [Name]Store) => state.[property];
```

### 3. Create Store Index File

If `lib/stores/index.ts` doesn't exist, create it:

```typescript
// lib/stores/index.ts
export * from './[name]-store';
// ... other store exports
```

### 4. Provide Usage Example

Create a usage example showing:

```typescript
'use client'

import { use[Name]Store } from '@/lib/stores/[name]-store';
import { useShallow } from 'zustand/shallow';

export function Example() {
  // Single value selection (optimal)
  const [property] = use[Name]Store((state) => state.[property]);

  // Multiple values with useShallow (prevents unnecessary re-renders)
  const { prop1, prop2 } = use[Name]Store(
    useShallow((state) => ({
      prop1: state.prop1,
      prop2: state.prop2
    }))
  );

  // Get actions
  const [actionName] = use[Name]Store((state) => state.[actionName]);

  return (
    <div>
      <p>Value: {[property]}</p>
      <button onClick={() => [actionName](...)}>
        Update
      </button>
    </div>
  );
}
```

## Critical Requirements

### TypeScript Typing (MANDATORY)
- ✅ MUST define a TypeScript interface for the store
- ✅ MUST pass interface to `create<[Name]Store>()()`
- ✅ MUST use curried function syntax (v5 requirement)
- ❌ NEVER use `any` types
- ❌ NEVER omit the type parameter

### Immutable Updates (MANDATORY)
- ✅ MUST use `set()` function for all state changes
- ✅ MUST return new objects, never mutate existing state
- ❌ NEVER mutate state directly (e.g., `state.items.push()`)

### Selector Performance (MANDATORY)
- ✅ MUST use `useShallow` from `zustand/shallow` when selecting multiple values
- ✅ MUST export reusable selectors for common access patterns
- ❌ NEVER return new objects/arrays from selectors without useShallow

### Persistence Configuration
- If persist middleware is used:
  - ✅ MUST configure `name` (localStorage key)
  - ✅ MUST use `createJSONStorage(() => localStorage)` for storage
  - ✅ Consider `partialize` to only persist specific fields
  - ✅ Consider `version` and `migrate` for schema changes

## Quality Checklist

Before completing, verify:

- [ ] Store has TypeScript interface defined
- [ ] Interface is passed to `create<Interface>()()`
- [ ] Curried function syntax used (two sets of parentheses)
- [ ] All actions use `set()` with immutable updates
- [ ] DevTools middleware configured (enabled in development only)
- [ ] Persistence middleware configured correctly (if needed)
- [ ] Optimized selectors exported
- [ ] Usage example provided
- [ ] File follows naming convention: `[name]-store.ts`
- [ ] Store exported from `lib/stores/index.ts`
- [ ] No `any` types used
- [ ] All action parameters have explicit types

## Anti-Patterns to Avoid

### ❌ Using v4 Syntax
```typescript
// WRONG: v4 syntax without curried function
const useStore = create<StoreType>(persist(...));

// CORRECT: v5 curried syntax
const useStore = create<StoreType>()(persist(...));
```

### ❌ Direct State Mutation
```typescript
// WRONG: Mutating state directly
addItem: (item) => {
  get().items.push(item); // ❌ Mutation!
}

// CORRECT: Immutable update
addItem: (item) => set((state) => ({
  items: [...state.items, item]
}));
```

### ❌ Missing TypeScript Type
```typescript
// WRONG: No type parameter
const useStore = create()((set) => ({ ... }));

// CORRECT: Typed store
interface MyStore { ... }
const useStore = create<MyStore>()((set) => ({ ... }));
```

### ❌ Not Using useShallow for Multiple Values
```typescript
// WRONG: Creates new object on every render
const data = useStore((state) => ({ a: state.a, b: state.b }));

// CORRECT: Use useShallow
const data = useStore(useShallow((state) => ({ a: state.a, b: state.b })));
```

## Output Format

Provide:
1. Complete store file at `lib/stores/[name]-store.ts`
2. Updated `lib/stores/index.ts` (if needed)
3. Usage example component
4. Documentation comments explaining:
   - Store purpose
   - State properties
   - Action descriptions
   - Persistence strategy (if applicable)

The generated store must be production-ready, fully typed, and follow all Zustand v5 best practices.
