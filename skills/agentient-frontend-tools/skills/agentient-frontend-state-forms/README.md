# agentient-frontend-state-forms

**Comprehensive state management with Zustand 5.0.2+ and form handling with React Hook Form 7.x + Zod 4.1.12+ for Next.js 14+ applications.**

## Overview

This plugin provides specialized agents, commands, and skills for implementing type-safe state management and validated forms in modern Next.js 14+ applications. It enforces the **Type Inference Chain pattern**, ensuring absolute type safety across your entire data layer from schema definition to form submission to global state storage.

## Core Architectural Pattern: The Type Inference Chain

The **Type Inference Chain** is the foundational pattern of this plugin:

```
Zod Schema (single source of truth)
    ↓
z.infer<typeof schema> (generate TypeScript type)
    ↓
useForm<Type>({ resolver: zodResolver(schema) }) (type-safe form)
    ↓
Zustand Store<Type> (type-safe state)
```

This pattern ensures:
- ✅ **Single source of truth** - Zod schema defines both validation rules and TypeScript types
- ✅ **Zero duplication** - No manual type definitions that can drift out of sync
- ✅ **End-to-end type safety** - From validation to forms to global state
- ✅ **Automatic updates** - Change schema → types update automatically
- ✅ **Runtime + compile-time safety** - Zod validates at runtime, TypeScript at compile-time

## Features

### State Management (Zustand 5.0.2+)

- **Lightweight, hook-based state management** - No Redux boilerplate
- **TypeScript-first API** - Fully typed stores with strict mode support
- **Middleware support** - persist (localStorage/sessionStorage), devtools, immer
- **Optimal performance** - Fine-grained selectors with useShallow hook
- **Slice pattern** - Organize large stores into modular, maintainable slices
- **Next.js 14+ integration** - Client components with SSR hydration handling

### Form Handling (React Hook Form 7.x + Zod 4.1.12+)

- **Type-safe forms** - Zod schema validation integrated with React Hook Form
- **Minimal re-renders** - Uncontrolled components for optimal performance
- **Built-in error handling** - User-friendly validation messages from Zod
- **Dynamic field arrays** - useFieldArray for lists, nested forms, repeating sections
- **Async validation** - Server-side validation support
- **Complex form patterns** - Multi-step forms, conditional validation, nested objects

## Components

### Agents (2)

#### **state-architect-agent**
Zustand 5.0.2+ state architecture design and implementation.

**Responsibilities:**
- Store architecture and organization
- Slice pattern implementation
- Middleware configuration (persist, devtools, immer)
- Performance optimization with selectors and useShallow
- State persistence strategies
- Async action patterns

**Activation:**
Keywords: `zustand`, `create store`, `global state`, `state management`

**Model:** Sonnet (balanced performance and capability)

#### **form-builder-agent**
React Hook Form 7.x with Zod 4.1.12+ validation implementation.

**Responsibilities:**
- Form component creation with validation
- Zod schema design and validation rules
- Error handling and display
- Dynamic field arrays (useFieldArray)
- Form-Zustand store synchronization
- Type Inference Chain enforcement

**Activation:**
Keywords: `create form`, `react hook form`, `validation`, `zod`

**Model:** Sonnet (balanced performance and capability)

### Commands (4)

#### `/create-store` - Generate Zustand Store
Creates a fully typed Zustand v5 store with middleware configuration.

**Generates:**
- Store file at `lib/stores/[name]-store.ts`
- TypeScript interface
- Middleware (persist, devtools)
- Optimized selectors
- Usage examples

**Example:**
```bash
/create-store
# Prompts for: store name, state properties, actions, middleware
# Generates: lib/stores/user-store.ts with full typing and middleware
```

#### `/create-form` - Generate Form with Zod Validation
Creates a React Hook Form component with Zod schema validation.

**Generates:**
- Zod schema at `lib/schemas/[name]-schema.ts`
- Form component at `components/forms/[Name]Form.tsx`
- Type inference with `z.infer<typeof schema>`
- zodResolver integration
- Error handling and loading states

**Example:**
```bash
/create-form
# Prompts for: form name, fields, validation rules, submission behavior
# Generates: lib/schemas/signup-schema.ts + components/forms/SignupForm.tsx
```

#### `/add-field` - Add Field to Existing Form
Adds a new validated field to an existing form and schema.

**Updates:**
- Zod schema with new field validation
- Form component with new field UI
- Error display for new field
- Default values (if needed)

**Example:**
```bash
/add-field
# Prompts for: which form, field name, type, validation, label
# Updates both schema and form component
```

#### `/setup-persistence` - Configure State Persistence
Adds persist middleware to a Zustand store for localStorage/sessionStorage.

**Configures:**
- Persist middleware with storage type
- Selective field persistence (partialize)
- Version and migration strategy
- SSR hydration handling for Next.js 14+

**Example:**
```bash
/setup-persistence
# Prompts for: store name, storage type, which fields to persist
# Configures persist middleware with Next.js 14+ hydration handling
```

### Skills (6)

Skills are organized using a **3-tier progressive disclosure model** for optimal token efficiency:

- **Tier 1 (YAML frontmatter)** - Always loaded (~100 tokens) - Metadata and activation criteria
- **Tier 2 (Instructions)** - Loaded on activation (~2000-2800 tokens) - Patterns and examples
- **Tier 3 (Resources)** - On-demand only - Complex examples and deep-dive docs

#### **zod-schema-type-inference-chain** (~2500 tokens)
The foundational skill - establishes the Type Inference Chain pattern.

**Provides:**
- Zod v4 schema definition patterns
- Type inference with `z.infer<typeof schema>`
- Schema composition (.extend, .merge, .pick, .omit)
- Safe error handling with .safeParse()
- Cross-field validation with .refine()

**Activation:**
Keywords: `zod`, `schema`, `validation`, `z.infer`, `type inference`

#### **zustand-v5-typed-store-creation** (~2200 tokens)
Zustand v5-specific store creation patterns.

**Provides:**
- v5 curried function syntax: `create<Type>()()`
- TypeScript store typing
- Middleware integration (persist, devtools, immer)
- Async action patterns
- Performance optimization with useShallow

**Activation:**
Keywords: `zustand`, `create store`, `global state`, `state management`

**Dependencies:** None (foundational)

#### **zustand-slices-pattern-for-scalability** (~1800 tokens)
Organize large Zustand stores into modular slices.

**Provides:**
- Slice pattern for large stores
- Store composition with spread syntax
- TypeScript type composition
- Selective slice persistence

**Activation:**
Keywords: `zustand slice`, `large store`, `organize store`, `modular state`

**Dependencies:** `zustand-v5-typed-store-creation`

#### **rhf-zod-schema-integration** (~2800 tokens)
React Hook Form v7 with Zod integration.

**Provides:**
- zodResolver setup and configuration
- Type-safe form creation with `useForm<Type>`
- v7 field registration (spread syntax)
- Error handling and display patterns
- Form state management (isSubmitting, isDirty, isValid)

**Activation:**
Keywords: `react hook form`, `rhf`, `form validation`, `zod resolver`

**Dependencies:** `zod-schema-type-inference-chain`

#### **rhf-dynamic-field-arrays** (~2400 tokens)
Dynamic form lists with useFieldArray.

**Provides:**
- useFieldArray hook usage
- Dynamic list management (add, remove, insert, move)
- Array validation with Zod
- Proper key usage with field.id

**Activation:**
Keywords: `field array`, `dynamic form`, `useFieldArray`, `add remove fields`

**Dependencies:** `rhf-zod-schema-integration`

#### **zustand-rhf-state-synchronization** (~2000 tokens)
Integrating forms with Zustand stores.

**Provides:**
- Form-to-store data flow patterns
- Submission handler integration
- Pre-populating forms from store (edit mode)
- Type consistency between forms and stores

**Activation:**
Keywords: `form state sync`, `save form data`, `submit to store`

**Dependencies:** `zustand-v5-typed-store-creation`, `rhf-zod-schema-integration`

## Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Zustand** | 5.0.2+ | Global state management |
| **React Hook Form** | 7.x+ | Form state and validation integration |
| **Zod** | 4.1.12+ | Schema validation and type inference |
| **TypeScript** | 5.x+ | Static type checking (strict mode) |
| **Next.js** | 14+ | App Router framework |
| **React** | 18.2+ | UI library |

## Plugin Dependencies

- **agentient-frontend-foundation** - TypeScript patterns, React patterns, App Router conventions

## Installation

This plugin is part of the vibekit marketplace and is installed via Claude Code plugin system:

```bash
/plugin install agentient-frontend-state-forms@vibekit
```

## Usage Examples

### Example 1: Creating a Type-Safe Store

```bash
/create-store
```

**Prompts:**
- Store name: `user`
- State properties: `user (User | null)`, `isAuthenticated (boolean)`
- Actions: `login`, `logout`, `updateProfile`
- Middleware: `persist (localStorage)`, `devtools`

**Generates:**
```typescript
// lib/stores/user-store.ts
import { create } from 'zustand';
import { persist, devtools, createJSONStorage } from 'zustand/middleware';

interface UserStore {
  user: User | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  updateProfile: (updates: Partial<User>) => void;
}

export const useUserStore = create<UserStore>()(
  devtools(
    persist(
      (set, get) => ({
        user: null,
        isAuthenticated: false,

        login: async (email, password) => {
          const user = await authAPI.login(email, password);
          set({ user, isAuthenticated: true });
        },

        logout: () => set({ user: null, isAuthenticated: false }),

        updateProfile: (updates) => set((state) => ({
          user: state.user ? { ...state.user, ...updates } : null,
        })),
      }),
      {
        name: 'user-storage',
        partialize: (state) => ({ user: state.user, isAuthenticated: state.isAuthenticated }),
      }
    )
  )
);

export const selectUser = (state: UserStore) => state.user;
export const selectIsAuthenticated = (state: UserStore) => state.isAuthenticated;
```

### Example 2: Creating a Validated Form

```bash
/create-form
```

**Prompts:**
- Form name: `Signup`
- Fields: `email (email)`, `password (password, min 8)`, `confirmPassword`
- Validation: Passwords must match
- Submission: POST to `/api/signup`, update auth store

**Generates:**
```typescript
// lib/schemas/signup-schema.ts
import { z } from 'zod';

export const signupSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
  confirmPassword: z.string(),
}).refine((data) => data.password === data.confirmPassword, {
  message: 'Passwords do not match',
  path: ['confirmPassword'],
});

export type SignupFormData = z.infer<typeof signupSchema>;

// components/forms/SignupForm.tsx
'use client'

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { signupSchema, type SignupFormData } from '@/lib/schemas/signup-schema';
import { useUserStore } from '@/lib/stores/user-store';

export function SignupForm() {
  const login = useUserStore((state) => state.login);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm<SignupFormData>({
    resolver: zodResolver(signupSchema),
    defaultValues: {
      email: '',
      password: '',
      confirmPassword: '',
    },
  });

  const onSubmit = async (data: SignupFormData) => {
    try {
      const response = await fetch('/api/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (!response.ok) throw new Error('Signup failed');

      await login(data.email, data.password);
      reset();
    } catch (error) {
      console.error('Signup error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {/* Form fields with validation */}
    </form>
  );
}
```

### Example 3: Complete Type-Safe Data Flow

**Schema (Single Source of Truth):**
```typescript
// lib/schemas/product-schema.ts
import { z } from 'zod';

export const productSchema = z.object({
  name: z.string().min(1, 'Name required'),
  price: z.number().positive('Price must be positive'),
  category: z.enum(['electronics', 'clothing', 'food']),
});

export type ProductData = z.infer<typeof productSchema>;
```

**Store (Uses Same Type):**
```typescript
// lib/stores/product-store.ts
import { create } from 'zustand';
import { type ProductData } from '@/lib/schemas/product-schema';

interface ProductStore {
  products: ProductData[];
  addProduct: (product: ProductData) => void;
}

export const useProductStore = create<ProductStore>()(/* ... */);
```

**Form (Uses Same Type):**
```typescript
// components/forms/ProductForm.tsx
'use client'

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { productSchema, type ProductData } from '@/lib/schemas/product-schema';
import { useProductStore } from '@/lib/stores/product-store';

export function ProductForm() {
  const addProduct = useProductStore((state) => state.addProduct);

  const { register, handleSubmit } = useForm<ProductData>({
    resolver: zodResolver(productSchema),
  });

  const onSubmit = (data: ProductData) => {
    addProduct(data); // All types match!
  };

  return <form onSubmit={handleSubmit(onSubmit)}>{/* ... */}</form>;
}
```

**Result:** `productSchema` → `ProductData` type → `useForm<ProductData>` → `ProductStore.products: ProductData[]`

All components share the same type, derived from the same schema. Change the schema, and everything updates automatically!

## Best Practices

### State Management

1. **Use Zustand for global/shared state** - Authentication, user preferences, shopping cart
2. **Use React state for local component state** - Modal open/closed, form draft state
3. **Organize stores by domain** - userStore, cartStore, settingsStore (not one giant store)
4. **Use selectors for performance** - Select only what you need with useShallow for multiple values
5. **Persist only necessary data** - Use partialize to persist specific fields, not entire state

### Form Handling

1. **Define Zod schema first** - Schema is the single source of truth
2. **Keep validation in schemas** - NOT in components or register() calls
3. **Use zodResolver for integration** - Seamless Zod + React Hook Form connection
4. **Provide user-friendly error messages** - Write clear messages in Zod schema
5. **Handle loading states** - Disable submit button when isSubmitting, show loading text

### Integration

1. **Forms update stores** - Form validates → submits to API → updates Zustand store
2. **Use store actions for submission** - Don't pass raw set() to forms
3. **Reset forms after success** - Call reset() after successful submission
4. **Pre-populate forms from store** - Use defaultValues from store data for edit mode
5. **Maintain type consistency** - Same Zod-inferred type for form and store

## Common Patterns

### Pattern: Authentication Flow
```typescript
// Schema
const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

// Store
const useAuthStore = create<AuthStore>()((set) => ({
  user: null,
  login: async (data: LoginData) => {
    const user = await authAPI.login(data);
    set({ user });
  },
}));

// Form
function LoginForm() {
  const login = useAuthStore((state) => state.login);
  const { register, handleSubmit } = useForm<LoginData>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginData) => {
    await login(data);
  };

  return <form onSubmit={handleSubmit(onSubmit)}>{/* ... */}</form>;
}
```

### Pattern: Persistent Form Drafts
```typescript
// Store persists draft
const useDraftStore = create(
  persist(
    (set) => ({
      draft: {},
      setDraft: (draft) => set({ draft }),
    }),
    { name: 'form-draft' }
  )
);

// Form saves draft on changes
function PostForm() {
  const { draft, setDraft } = useDraftStore();

  const { register, watch } = useForm({
    defaultValues: draft,
  });

  useEffect(() => {
    const subscription = watch((data) => setDraft(data));
    return () => subscription.unsubscribe();
  }, [watch, setDraft]);

  return <form>{/* ... */}</form>;
}
```

### Pattern: Multi-Step Form with Zustand
```typescript
// Store tracks current step and form data
const useWizardStore = create<WizardStore>()((set) => ({
  step: 1,
  formData: {},
  nextStep: (data) => set((state) => ({
    step: state.step + 1,
    formData: { ...state.formData, ...data },
  })),
}));

// Each step is a separate form
function Step1Form() {
  const nextStep = useWizardStore((state) => state.nextStep);

  const { register, handleSubmit } = useForm<Step1Data>({
    resolver: zodResolver(step1Schema),
  });

  return <form onSubmit={handleSubmit(nextStep)}>{/* ... */}</form>;
}
```

## Token Budget

| Component | Token Cost | When Loaded |
|-----------|------------|-------------|
| **Metadata (All Skills)** | ~600 tokens | Always (6 skills × 100 tokens) |
| **state-architect-agent** | ~4,200 tokens | When state management tasks detected |
| **form-builder-agent** | ~7,900 tokens | When form creation/validation needed |
| **Peak Load (All Skills)** | ~14,300 tokens | Rare (all 6 skills activated simultaneously) |

The 3-tier progressive disclosure model ensures that the vast majority of knowledge remains dormant until explicitly required, maximizing token efficiency.

## Version Notes

### Zustand v5 Breaking Changes
- **Curried function syntax required**: `create<Type>()()`
- **useShallow hook replaces shallow function**: `import { useShallow } from 'zustand/shallow'`
- **Persist middleware signature changed**: Use `createJSONStorage(() => localStorage)`
- **Initial state not auto-persisted**: Explicitly call setState if needed

### React Hook Form v7 Breaking Changes
- **Spread registration required**: `{...register('field')}` instead of `ref={register}`
- **Resolver API**: Use `@hookform/resolvers/zod` for Zod integration
- **Strict typing support**: First-class TypeScript generics

### Zod v4 Breaking Changes
- **Error handling unified**: Single `error` parameter instead of separate `required_error`, `invalid_type_error`
- **Tree-shaking improvements**: Many validation methods promoted to top-level functions

## Contributing

This plugin is part of the vibekit marketplace. For issues, enhancements, or questions:
- GitHub: [agentient-vibekit repository](https://github.com/agentient/vibekit)
- Email: contact@agentient.dev

## License

MIT

---

**Generated with ❤️ by Agentient Labs for the vibekit Claude Code marketplace**
