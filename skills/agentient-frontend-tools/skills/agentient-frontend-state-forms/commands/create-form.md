# Create Form with Zod Validation

Generate a React Hook Form 7.x component with Zod 4.1.12+ schema validation for Next.js 14+ applications.

## Instructions

You will create a fully typed, validated form component following the Type Inference Chain pattern:
**Zod schema → z.infer<typeof> → useForm<Type> → validation & submission**

### 1. Gather Requirements

Ask the user for:
- **Form name** (e.g., "Login", "UserProfile", "Signup")
- **Fields** needed with:
  - Field name
  - Field type (text, email, number, select, checkbox, textarea, date, etc.)
  - Validation rules (required, min/max length, pattern, custom)
  - Placeholder/label text
- **Submission behavior**:
  - API endpoint to POST to?
  - Update Zustand store?
  - Redirect after success?

### 2. Generate Zod Schema

Create schema at `lib/schemas/[name]-schema.ts`:

```typescript
import { z } from 'zod';

/**
 * Validation schema for [Name] form
 */
export const [name]Schema = z.object({
  // Text field with min/max length
  [fieldName]: z.string()
    .min(1, 'This field is required')
    .max(100, 'Maximum 100 characters'),

  // Email field
  email: z.string()
    .email('Invalid email address'),

  // Number field with range
  age: z.number()
    .int('Must be a whole number')
    .min(18, 'Must be 18 or older')
    .max(120, 'Invalid age'),

  // Optional field
  middleName: z.string().optional(),

  // Enum/select field
  role: z.enum(['user', 'admin', 'moderator'], {
    errorMap: () => ({ message: 'Please select a valid role' })
  }),

  // Boolean/checkbox
  acceptTerms: z.boolean()
    .refine((val) => val === true, {
      message: 'You must accept the terms and conditions'
    }),

  // URL validation
  website: z.string()
    .url('Invalid URL format')
    .optional(),

  // Custom validation with regex
  username: z.string()
    .min(3, 'Minimum 3 characters')
    .regex(/^[a-zA-Z0-9_]+$/, 'Only letters, numbers, and underscores allowed'),
});

// Cross-field validation (if needed)
// Example: password confirmation
// export const [name]Schema = z.object({
//   password: z.string().min(8, 'Minimum 8 characters'),
//   confirmPassword: z.string(),
// }).refine((data) => data.password === data.confirmPassword, {
//   message: 'Passwords do not match',
//   path: ['confirmPassword'], // Error appears on confirmPassword field
// });

/**
 * TypeScript type inferred from schema (Type Inference Chain)
 */
export type [Name]FormData = z.infer<typeof [name]Schema>;
```

### 3. Generate Form Component

Create form at `components/forms/[Name]Form.tsx`:

```typescript
'use client'

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { [name]Schema, type [Name]FormData } from '@/lib/schemas/[name]-schema';

/**
 * [Name] form component with Zod validation
 */
export function [Name]Form() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting, isDirty, isValid },
    reset,
  } = useForm<[Name]FormData>({
    resolver: zodResolver([name]Schema),
    mode: 'onBlur', // Validate on blur
    defaultValues: {
      [field]: '',
      // ... default values for all fields
    },
  });

  const onSubmit = async (data: [Name]FormData) => {
    try {
      // data is fully typed and validated
      console.log('Form data:', data);

      // Submit to API
      const response = await fetch('/api/[endpoint]', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Submission failed');
      }

      // Optional: Update Zustand store
      // const updateStore = useMyStore.getState().updateData;
      // updateStore(data);

      // Reset form on success
      reset();

      // Show success message or redirect
      alert('Form submitted successfully!');

    } catch (error) {
      console.error('Submission error:', error);
      alert('Failed to submit form. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 max-w-md">
      {/* TEXT INPUT FIELD */}
      <div>
        <label htmlFor="[fieldName]" className="block text-sm font-medium text-gray-700 mb-1">
          [Label Text]
        </label>
        <input
          id="[fieldName]"
          type="text"
          {...register('[fieldName]')}
          placeholder="[Placeholder]"
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {errors.[fieldName] && (
          <p className="mt-1 text-sm text-red-600">
            {errors.[fieldName]?.message}
          </p>
        )}
      </div>

      {/* EMAIL INPUT FIELD */}
      <div>
        <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
          Email
        </label>
        <input
          id="email"
          type="email"
          {...register('email')}
          placeholder="you@example.com"
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {errors.email && (
          <p className="mt-1 text-sm text-red-600">
            {errors.email.message}
          </p>
        )}
      </div>

      {/* SELECT/DROPDOWN FIELD */}
      <div>
        <label htmlFor="role" className="block text-sm font-medium text-gray-700 mb-1">
          Role
        </label>
        <select
          id="role"
          {...register('role')}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="">Select a role</option>
          <option value="user">User</option>
          <option value="admin">Admin</option>
          <option value="moderator">Moderator</option>
        </select>
        {errors.role && (
          <p className="mt-1 text-sm text-red-600">
            {errors.role.message}
          </p>
        )}
      </div>

      {/* CHECKBOX FIELD */}
      <div className="flex items-start">
        <input
          id="acceptTerms"
          type="checkbox"
          {...register('acceptTerms')}
          className="mt-1 h-4 w-4 text-blue-600 border-gray-300 rounded"
        />
        <label htmlFor="acceptTerms" className="ml-2 text-sm text-gray-700">
          I accept the terms and conditions
        </label>
        {errors.acceptTerms && (
          <p className="mt-1 text-sm text-red-600">
            {errors.acceptTerms.message}
          </p>
        )}
      </div>

      {/* TEXTAREA FIELD */}
      <div>
        <label htmlFor="bio" className="block text-sm font-medium text-gray-700 mb-1">
          Bio
        </label>
        <textarea
          id="bio"
          {...register('bio')}
          rows={4}
          placeholder="Tell us about yourself..."
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {errors.bio && (
          <p className="mt-1 text-sm text-red-600">
            {errors.bio.message}
          </p>
        )}
      </div>

      {/* SUBMIT BUTTON */}
      <button
        type="submit"
        disabled={isSubmitting || !isDirty}
        className="w-full py-2 px-4 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
      >
        {isSubmitting ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  );
}
```

### 4. Export from Forms Index

If `components/forms/index.ts` doesn't exist, create it:

```typescript
// components/forms/index.ts
export * from './[Name]Form';
// ... other form exports
```

## Critical Requirements

### Type Inference Chain (MANDATORY)
The form MUST follow this exact pattern:

1. ✅ Define Zod schema first
2. ✅ Infer TypeScript type with `z.infer<typeof schema>`
3. ✅ Pass type to `useForm<Type>({ resolver: zodResolver(schema) })`
4. ❌ NEVER manually write a type that mirrors the schema

### React Hook Form v7 Syntax (MANDATORY)
- ✅ MUST use `'use client'` directive at top of file
- ✅ MUST use spread syntax: `{...register('fieldName')}`
- ✅ MUST use `zodResolver` from `@hookform/resolvers/zod`
- ❌ NEVER use v6 ref-based registration: `ref={register}`
- ❌ NEVER mix Zod validation with RHF validation rules

### Error Handling (MANDATORY)
- ✅ MUST display error for each field: `errors.fieldName?.message`
- ✅ MUST show loading state during submission: `isSubmitting`
- ✅ MUST disable submit button while submitting or form not dirty
- ✅ Error messages MUST be user-friendly (defined in Zod schema)

### Validation Rules
ALL validation MUST be in the Zod schema, including:
- ✅ Required fields (`.min(1, 'Required')`)
- ✅ Email validation (`.email('Invalid email')`)
- ✅ Min/max length (`.min(3).max(100)`)
- ✅ Custom patterns (`.regex(/pattern/, 'Error message')`)
- ✅ Custom validators (`.refine()`)

## Quality Checklist

Before completing, verify:

- [ ] Zod schema defined at `lib/schemas/[name]-schema.ts`
- [ ] TypeScript type inferred with `z.infer<typeof schema>`
- [ ] Form component has `'use client'` directive
- [ ] Form uses `useForm<Type>({ resolver: zodResolver(schema) })`
- [ ] All fields use spread register: `{...register('fieldName')}`
- [ ] Error display for each field
- [ ] Submit button shows loading state (`isSubmitting`)
- [ ] Submit button disabled when submitting or not dirty
- [ ] Form resets after successful submission
- [ ] All validation rules in Zod schema (not in register)
- [ ] No manual types that mirror Zod schema
- [ ] User-friendly error messages

## Anti-Patterns to Avoid

### ❌ Breaking the Type Inference Chain
```typescript
// WRONG: Manually defining type
interface MyFormData { email: string; password: string; }

// CORRECT: Infer from Zod schema
type MyFormData = z.infer<typeof mySchema>;
```

### ❌ Using v6 Registration
```typescript
// WRONG: v6 ref pattern
<input name="email" ref={register} />

// CORRECT: v7 spread pattern
<input {...register('email')} />
```

### ❌ Mixing Validation Sources
```typescript
// WRONG: Validation in both places
const schema = z.object({ email: z.string().email() });
<input {...register('email', { required: 'Required' })} />

// CORRECT: All validation in Zod schema
const schema = z.object({ email: z.string().email().min(1, 'Required') });
<input {...register('email')} />
```

### ❌ Not Showing Loading State
```typescript
// WRONG: No loading feedback
<button type="submit">Submit</button>

// CORRECT: Show loading state
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? 'Submitting...' : 'Submit'}
</button>
```

## Output Format

Provide:
1. Zod schema file at `lib/schemas/[name]-schema.ts`
2. Form component at `components/forms/[Name]Form.tsx`
3. Updated index files (if needed)
4. Usage example showing how to use the form in a page
5. Documentation comments explaining:
   - Form purpose
   - Field descriptions
   - Validation rules
   - Submission behavior

The generated form must be production-ready, fully typed, validated, and follow all React Hook Form v7 + Zod v4 best practices.
