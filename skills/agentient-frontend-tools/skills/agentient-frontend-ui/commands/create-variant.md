---
name: create-variant
description: Add component variants using class-variance-authority (cva) and generate type-safe VariantProps
---

# /create-variant Command

**Purpose**: Add visual variants to components using the `cva` (class-variance-authority) library, with automatic TypeScript type generation via `VariantProps`.

## Usage

```bash
/create-variant
```

The command will interactively guide you through:
1. Selecting the component to enhance
2. Defining variant types (appearance, size, state)
3. Specifying variant options with Tailwind classes
4. Setting default variants
5. Generating TypeScript types

## What This Command Generates

1. **cva definition** with base classes and variants
2. **VariantProps type** automatically inferred from cva
3. **Component interface** extending VariantProps
4. **Updated component implementation** using variant classes

## Example Session

```
User: /create-variant

Agent: Which component would you like to add variants to?
> components/ui/button.tsx

Current variants: none

What type of variant would you like to add?
1. Appearance/Style (variant)
2. Size
3. State (disabled, loading)
4. Custom

User: 1 (Appearance)

Variant options for 'variant':
1. default (primary action)
2. destructive (dangerous action)
3. outline (secondary action)
4. ghost (tertiary action)
5. link (text link style)

Add custom options? (y/n): n

What type of variant would you like to add?
1. Size
2. State
3. Done

User: 1 (Size)

Variant options for 'size':
1. default
2. sm (small)
3. lg (large)
4. icon (icon-only button)

User: 3 (Done)

Default variant: default
Default size: default

Generating code...
✓ Updated components/ui/button.tsx
```

## Generated Code Example

```tsx
import { cva, type VariantProps } from 'class-variance-authority';
import * as React from 'react';
import { cn } from '@/lib/utils';

// cva definition with variants
const buttonVariants = cva(
  // Base classes (always applied)
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      // Appearance variants
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input hover:bg-accent hover:text-accent-foreground",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "underline-offset-4 hover:underline text-primary",
      },
      // Size variants
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

// Automatically inferred type from cva
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  // variant?: "default" | "destructive" | "outline" | "ghost" | "link"
  // size?: "default" | "sm" | "lg" | "icon"
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, ...props }, ref) => {
    return (
      <button
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);

Button.displayName = "Button";

export { Button, buttonVariants };
```

## Usage of Generated Component

```tsx
import { Button } from '@/components/ui/button';

// Uses default variant and size
<Button>Submit</Button>

// Destructive variant
<Button variant="destructive">Delete</Button>

// Small outline button
<Button variant="outline" size="sm">Cancel</Button>

// Icon-only button
<Button variant="ghost" size="icon" aria-label="Close">
  <X size={16} />
</Button>
```

## Best Practices

✅ **Do**:
- Use semantic variant names (default, destructive, outline)
- Keep base classes in the first argument to cva
- Use `VariantProps<typeof cvaFunction>` for automatic typing
- Set sensible defaultVariants
- Use the `cn()` utility to merge classes

❌ **Don't**:
- Manually type variant props (let VariantProps infer it)
- Put variant-specific classes in base classes
- Forget to set defaultVariants
- Create too many variants (keep it simple)

## Advanced Pattern: Compound Variants

```tsx
const buttonVariants = cva("base-classes", {
  variants: {
    variant: { /* ... */ },
    size: { /* ... */ },
  },
  compoundVariants: [
    {
      variant: "destructive",
      size: "sm",
      className: "text-xs font-semibold", // Special case
    },
  ],
  defaultVariants: { /* ... */ },
});
```

---

**Related Commands**: `/add-component`, `/style-responsive`
**Skill Dependencies**: `typescript-prop-definition`, `tailwind-utility-styling`
