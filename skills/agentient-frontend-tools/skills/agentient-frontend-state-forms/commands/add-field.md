# Add Field to Existing Form

Add a new field to an existing React Hook Form with corresponding Zod validation.

## Instructions

You will update both the Zod schema and form component to add a new validated field.

### 1. Gather Requirements

Ask the user for:
- **Which form** to modify (filename or form name)
- **New field details**:
  - Field name
  - Field type (text, email, number, select, checkbox, textarea, date, etc.)
  - Validation rules (required, min/max, pattern, custom)
  - Label text
  - Placeholder (optional)
  - Default value (optional)

### 2. Update Zod Schema

Locate the schema file (usually `lib/schemas/[name]-schema.ts`) and add the new field:

```typescript
export const [name]Schema = z.object({
  // ... existing fields

  // Add new field with validation
  [newFieldName]: z.[type]()
    .[validationMethod]('Error message')
    .[additionalValidation](), // e.g., .optional()
});

// Type is automatically updated via z.infer
export type [Name]FormData = z.infer<typeof [name]Schema>;
```

**Validation Examples**:
- Text: `z.string().min(1, 'Required').max(100, 'Too long')`
- Email: `z.string().email('Invalid email')`
- Number: `z.number().int().min(0).max(100)`
- Optional: `z.string().optional()`
- Enum/Select: `z.enum(['option1', 'option2'])`
- URL: `z.string().url('Invalid URL')`
- Checkbox: `z.boolean().refine((val) => val === true, 'Must accept')`

### 3. Update Form Component

Locate the form component (usually `components/forms/[Name]Form.tsx`) and add the field UI:

```typescript
{/* Add new field in appropriate location */}
<div>
  <label htmlFor="[newFieldName]" className="block text-sm font-medium text-gray-700 mb-1">
    [Label Text]
  </label>

  {/* For text/email/number inputs */}
  <input
    id="[newFieldName]"
    type="[inputType]"
    {...register('[newFieldName]')}
    placeholder="[Placeholder]"
    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
  />

  {/* For select/dropdown */}
  <select
    id="[newFieldName]"
    {...register('[newFieldName]')}
    className="w-full px-3 py-2 border border-gray-300 rounded-md"
  >
    <option value="">Select...</option>
    <option value="option1">Option 1</option>
    <option value="option2">Option 2</option>
  </select>

  {/* For checkbox */}
  <input
    id="[newFieldName]"
    type="checkbox"
    {...register('[newFieldName]')}
    className="h-4 w-4 text-blue-600 border-gray-300 rounded"
  />

  {/* For textarea */}
  <textarea
    id="[newFieldName]"
    {...register('[newFieldName]')}
    rows={4}
    placeholder="[Placeholder]"
    className="w-full px-3 py-2 border border-gray-300 rounded-md"
  />

  {/* Error display (REQUIRED) */}
  {errors.[newFieldName] && (
    <p className="mt-1 text-sm text-red-600">
      {errors.[newFieldName]?.message}
    </p>
  )}
</div>
```

### 4. Update Default Values (if needed)

If the field should have a default value, update the `defaultValues` in `useForm`:

```typescript
const { register, ... } = useForm<[Name]FormData>({
  resolver: zodResolver([name]Schema),
  defaultValues: {
    // ... existing defaults
    [newFieldName]: '', // or appropriate default
  },
});
```

## Critical Requirements

### Type Safety (MANDATORY)
- ✅ Add field to Zod schema FIRST
- ✅ TypeScript type is auto-updated via `z.infer<typeof schema>`
- ❌ NEVER manually update the TypeScript type
- ❌ NEVER add validation rules in `register()` - use Zod schema

### React Hook Form v7 (MANDATORY)
- ✅ MUST use spread syntax: `{...register('[newFieldName]')}`
- ✅ MUST display error: `errors.[newFieldName]?.message`
- ❌ NEVER use v6 ref-based registration

### Validation (MANDATORY)
- ✅ ALL validation rules in Zod schema
- ✅ User-friendly error messages
- ✅ Appropriate validation for field type (email, URL, etc.)

## Quality Checklist

Before completing, verify:

- [ ] Field added to Zod schema with validation
- [ ] Field added to form component with proper input type
- [ ] Error display added for field
- [ ] Default value added (if applicable)
- [ ] Validation rules appropriate for field type
- [ ] Error messages are user-friendly
- [ ] TypeScript auto-completion works for new field
- [ ] No manual type modifications made

## Example: Adding an "Age" Field

**Step 1: Update Schema**
```typescript
export const userSchema = z.object({
  name: z.string().min(1, 'Name required'),
  email: z.string().email('Invalid email'),

  // NEW FIELD
  age: z.number()
    .int('Must be a whole number')
    .min(18, 'Must be 18 or older')
    .max(120, 'Invalid age'),
});
```

**Step 2: Update Form Component**
```typescript
{/* NEW FIELD */}
<div>
  <label htmlFor="age">Age</label>
  <input
    id="age"
    type="number"
    {...register('age', { valueAsNumber: true })} // Convert string to number
  />
  {errors.age && <p className="error">{errors.age.message}</p>}
</div>
```

**Note**: For number inputs, use `valueAsNumber: true` option in register to ensure the value is converted to a number.

## Output Format

Show the diff of changes made to:
1. The Zod schema file (lines added)
2. The form component file (lines added)
3. Explanation of:
   - Where the field was added
   - What validation rules apply
   - Any special considerations (like `valueAsNumber`)

The field must integrate seamlessly with the existing form's validation and error handling.
