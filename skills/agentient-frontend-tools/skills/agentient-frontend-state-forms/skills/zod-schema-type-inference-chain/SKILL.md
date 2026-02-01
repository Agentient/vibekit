---
name: zod-schema-type-inference-chain
version: 1.0.0
category: validation
activation_criteria:
  keywords: [zod, schema, validation, z.infer, type inference, validate, validator]
  file_patterns: ["**/*schema.ts", "**/*validation.ts", "**/*validator.ts"]
  modes: [typescript_dev, form_builder, data_modeler]
provides:
  - Zod v4 schema definition patterns
  - Type inference with z.infer
  - Schema composition and reusability
  - Safe error handling with safeParse
  - Type Inference Chain pattern (schema → type → form → store)
dependencies: []
token_cost: 2500
---

# Zod Schema Type Inference Chain

## The Type Inference Chain Pattern (CRITICAL)

The **Type Inference Chain** is the foundational pattern for all state and form management in this plugin:

```
Zod Schema (single source of truth)
    ↓
z.infer<typeof schema> (generate TypeScript type)
    ↓
useForm<Type>() (type-safe form)
    ↓
Zustand Store<Type> (type-safe state)
```

This pattern ensures **absolute type safety** across your entire data layer by maintaining **one single source of truth**: the Zod schema.

### Why This Pattern is Critical

**Problem Without Type Inference Chain**:
```typescript
// ❌ BAD: Multiple sources of truth
interface UserData {           // Manual type definition
  email: string;
  age: number;
}

const userSchema = z.object({  // Zod schema
  email: z.string().email(),
  age: z.number().min(18),
});

// These can drift out of sync!
// What if you add a field to the schema but forget the interface?
// What if you change validation rules?
```

**Solution With Type Inference Chain**:
```typescript
// ✅ GOOD: Single source of truth
const userSchema = z.object({
  email: z.string().email('Invalid email'),
  age: z.number().min(18, 'Must be 18+'),
});

// Type is automatically inferred from schema
type UserData = z.infer<typeof userSchema>;

// Now the schema and type are ALWAYS in sync!
// Change schema → type automatically updates!
```

## Schema Definition Patterns

### Basic Object Schema

```typescript
import { z } from 'zod';

// Define schema with validation rules
const userSchema = z.object({
  // String with validations
  username: z.string()
    .min(3, 'Username must be at least 3 characters')
    .max(20, 'Username must be at most 20 characters')
    .regex(/^[a-zA-Z0-9_]+$/, 'Only letters, numbers, and underscores'),

  // Email validation
  email: z.string()
    .email('Invalid email address'),

  // Number with range
  age: z.number()
    .int('Must be a whole number')
    .min(18, 'Must be 18 or older')
    .max(120, 'Invalid age'),

  // Optional field
  middleName: z.string().optional(),

  // Nullable field
  nickname: z.string().nullable(),

  // Enum
  role: z.enum(['user', 'admin', 'moderator']),

  // Boolean
  isActive: z.boolean(),

  // Date
  birthDate: z.date()
    .max(new Date(), 'Birth date cannot be in future'),

  // URL
  website: z.string().url('Invalid URL').optional(),

  // Array of strings
  tags: z.array(z.string())
    .min(1, 'At least one tag required')
    .max(5, 'Maximum 5 tags'),
});

// Infer TypeScript type
type User = z.infer<typeof userSchema>;

// Now User type is:
// {
//   username: string;
//   email: string;
//   age: number;
//   middleName?: string;
//   nickname: string | null;
//   role: 'user' | 'admin' | 'moderator';
//   isActive: boolean;
//   birthDate: Date;
//   website?: string;
//   tags: string[];
// }
```

### Nested Object Schema

```typescript
const addressSchema = z.object({
  street: z.string().min(1, 'Street required'),
  city: z.string().min(1, 'City required'),
  state: z.string().length(2, 'Use 2-letter state code'),
  zipCode: z.string().regex(/^\d{5}$/, 'Must be 5 digits'),
});

const userWithAddressSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  address: addressSchema, // Nested object
});

type UserWithAddress = z.infer<typeof userWithAddressSchema>;
// {
//   name: string;
//   email: string;
//   address: {
//     street: string;
//     city: string;
//     state: string;
//     zipCode: string;
//   };
// }
```

### Array of Objects

```typescript
const itemSchema = z.object({
  name: z.string(),
  quantity: z.number().int().min(1),
  price: z.number().positive(),
});

const orderSchema = z.object({
  orderId: z.string().uuid(),
  items: z.array(itemSchema)
    .min(1, 'Order must have at least one item'),
  totalPrice: z.number().positive(),
});

type Order = z.infer<typeof orderSchema>;
// {
//   orderId: string;
//   items: Array<{
//     name: string;
//     quantity: number;
//     price: number;
//   }>;
//   totalPrice: number;
// }
```

## Schema Composition and Reusability

### Using .extend()

```typescript
const baseUserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
});

// Add more fields to base schema
const fullUserSchema = baseUserSchema.extend({
  name: z.string(),
  age: z.number(),
  role: z.enum(['user', 'admin']),
});

type FullUser = z.infer<typeof fullUserSchema>;
// {
//   id: string;
//   email: string;
//   name: string;
//   age: number;
//   role: 'user' | 'admin';
// }
```

### Using .merge()

```typescript
const nameSchema = z.object({
  firstName: z.string(),
  lastName: z.string(),
});

const contactSchema = z.object({
  email: z.string().email(),
  phone: z.string(),
});

// Merge two schemas
const personSchema = nameSchema.merge(contactSchema);

type Person = z.infer<typeof personSchema>;
// {
//   firstName: string;
//   lastName: string;
//   email: string;
//   phone: string;
// }
```

### Using .pick() and .omit()

```typescript
const userSchema = z.object({
  id: z.string(),
  email: z.string().email(),
  password: z.string(),
  name: z.string(),
});

// Pick only specific fields
const loginSchema = userSchema.pick({
  email: true,
  password: true,
});
// { email: string; password: string; }

// Omit specific fields
const publicUserSchema = userSchema.omit({
  password: true,
});
// { id: string; email: string; name: string; }
```

## Cross-Field Validation with .refine()

### Password Confirmation

```typescript
const passwordSchema = z.object({
  password: z.string()
    .min(8, 'Password must be at least 8 characters'),
  confirmPassword: z.string(),
}).refine((data) => data.password === data.confirmPassword, {
  message: 'Passwords do not match',
  path: ['confirmPassword'], // Error appears on confirmPassword field
});

type PasswordForm = z.infer<typeof passwordSchema>;
```

### Conditional Validation

```typescript
const shippingSchema = z.object({
  shippingMethod: z.enum(['pickup', 'delivery']),
  address: z.string().optional(),
}).refine(
  (data) => {
    // If delivery is selected, address is required
    if (data.shippingMethod === 'delivery') {
      return data.address && data.address.length > 0;
    }
    return true;
  },
  {
    message: 'Address required for delivery',
    path: ['address'],
  }
);
```

### Date Range Validation

```typescript
const eventSchema = z.object({
  startDate: z.date(),
  endDate: z.date(),
}).refine((data) => data.endDate > data.startDate, {
  message: 'End date must be after start date',
  path: ['endDate'],
});
```

## Safe Error Handling with .safeParse()

### Basic Safe Parsing

```typescript
const userSchema = z.object({
  email: z.string().email(),
  age: z.number().min(18),
});

// Unsafe data from user input or API
const userData = {
  email: 'invalid-email',
  age: 15,
};

// Use safeParse for validation
const result = userSchema.safeParse(userData);

if (!result.success) {
  // Validation failed - handle errors
  console.error('Validation errors:', result.error.issues);

  // Get formatted errors
  const formatted = result.error.format();
  console.log(formatted.email?._errors); // ["Invalid email address"]
  console.log(formatted.age?._errors); // ["Number must be greater than or equal to 18"]

  // Get flat errors
  const flat = result.error.flatten();
  console.log(flat.fieldErrors);
  // {
  //   email: ["Invalid email address"],
  //   age: ["Number must be greater than or equal to 18"]
  // }
} else {
  // Validation succeeded - use validated data
  const validUser = result.data; // Fully typed!
  console.log(validUser.email); // TypeScript knows this is valid
}
```

### API Response Validation

```typescript
const apiResponseSchema = z.object({
  success: z.boolean(),
  data: z.object({
    id: z.string(),
    name: z.string(),
  }),
});

async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  const json = await response.json();

  // Validate API response
  const result = apiResponseSchema.safeParse(json);

  if (!result.success) {
    throw new Error(`Invalid API response: ${result.error.message}`);
  }

  // Safe to use - data is validated
  return result.data;
}
```

## Complete Type Inference Chain Example

### Step 1: Define Zod Schema (Single Source of Truth)

```typescript
// lib/schemas/user-profile-schema.ts
import { z } from 'zod';

export const userProfileSchema = z.object({
  name: z.string()
    .min(1, 'Name is required')
    .max(100, 'Name too long'),

  email: z.string()
    .email('Invalid email address'),

  bio: z.string()
    .max(500, 'Bio must be at most 500 characters')
    .optional(),

  age: z.number()
    .int('Must be a whole number')
    .min(18, 'Must be 18 or older')
    .optional(),
});

// Step 2: Infer TypeScript type
export type UserProfileData = z.infer<typeof userProfileSchema>;
```

### Step 3: Use in React Hook Form

```typescript
// components/forms/UserProfileForm.tsx
'use client'

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { userProfileSchema, type UserProfileData } from '@/lib/schemas/user-profile-schema';

export function UserProfileForm() {
  const { register, handleSubmit } = useForm<UserProfileData>({
    resolver: zodResolver(userProfileSchema), // Schema drives validation
  });

  const onSubmit = (data: UserProfileData) => {
    // data is fully typed and validated!
  };

  return <form onSubmit={handleSubmit(onSubmit)}>{/* fields */}</form>;
}
```

### Step 4: Use in Zustand Store

```typescript
// lib/stores/user-store.ts
import { create } from 'zustand';
import { type UserProfileData } from '@/lib/schemas/user-profile-schema';

interface UserStore {
  profile: UserProfileData | null;
  updateProfile: (data: UserProfileData) => void;
}

export const useUserStore = create<UserStore>()((set) => ({
  profile: null,
  updateProfile: (data) => set({ profile: data }),
}));
```

### Result: Complete Type Safety

```
userProfileSchema (Zod)
    ↓ z.infer
UserProfileData (TypeScript type)
    ↓
useForm<UserProfileData> (React Hook Form)
    ↓
useUserStore.updateProfile(data: UserProfileData) (Zustand)
```

**All components share the same type, derived from the same schema!**

## Anti-Patterns (DO NOT DO)

### ❌ Manually Defining Types

```typescript
// WRONG: Manual type separate from schema
interface UserData {
  email: string;
  age: number;
}

const userSchema = z.object({
  email: z.string().email(),
  age: z.number(),
});

// Problem: These can drift out of sync!
```

**Correct:**
```typescript
const userSchema = z.object({
  email: z.string().email(),
  age: z.number(),
});

type UserData = z.infer<typeof userSchema>; // Always in sync!
```

### ❌ Using .parse() Without Try/Catch

```typescript
// WRONG: Throws unhandled exception on invalid data
const user = userSchema.parse(untrustedData);
```

**Correct:**
```typescript
const result = userSchema.safeParse(untrustedData);
if (!result.success) {
  // Handle error
} else {
  const user = result.data;
}
```

### ❌ Ignoring Validation Errors

```typescript
// WRONG: Not checking success flag
const result = userSchema.safeParse(data);
const user = result.data; // Could be undefined!
```

**Correct:**
```typescript
const result = userSchema.safeParse(data);
if (result.success) {
  const user = result.data; // Type-safe!
}
```

## Summary

The **zod-schema-type-inference-chain** skill establishes the foundational pattern for all data management:

1. **Define Zod schema** - Single source of truth for data structure and validation
2. **Infer TypeScript type** - Use `z.infer<typeof schema>` to generate type
3. **Use in forms** - Pass type to `useForm<Type>({ resolver: zodResolver(schema) })`
4. **Use in stores** - Pass type to Zustand store interface
5. **Validate safely** - Use `.safeParse()` for all external data

This pattern ensures absolute type safety across your entire application with zero duplication.
