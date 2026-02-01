---
name: typescript-prop-definition
description: |
  TypeScript interface conventions, JSDoc comments, generics, utility types, and cva + VariantProps patterns.
  Keywords: "props", "interface", "types", "typescript", "generics", "VariantProps"
---

# TypeScript Prop Definition

## Interface Convention

Use \`interface\` for component props:

\`\`\`tsx
/**
 * Props for the Button component
 */
interface ButtonProps {
  /** Button text or content */
  children: React.ReactNode;
  /** Click handler */
  onClick?: () => void;
  /** Whether button is disabled */
  disabled?: boolean;
}

export function Button({ children, onClick, disabled }: ButtonProps) {
  // ...
}
\`\`\`

## JSDoc Comments

Document each prop:

\`\`\`tsx
interface UserCardProps {
  /** User's full name */
  name: string;
  /** User's email address */
  email: string;
  /** Optional avatar URL */
  avatarUrl?: string;
}
\`\`\`

## Generics for Reusable Components

\`\`\`tsx
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
  keyExtractor: (item: T) => string;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map(item => (
        <li key={keyExtractor(item)}>
          {renderItem(item)}
        </li>
      ))}
    </ul>
  );
}
\`\`\`

## Utility Types

### Extending Native Props

\`\`\`tsx
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'destructive';
}
\`\`\`

### Pick/Omit

\`\`\`tsx
type UserPublicInfo = Pick<User, 'name' | 'email'>;
type UserWithoutPassword = Omit<User, 'password'>;
\`\`\`

### Partial

\`\`\`tsx
type PartialUser = Partial<User>; // All fields optional
\`\`\`

## cva + VariantProps Pattern

\`\`\`tsx
import { cva, type VariantProps } from 'class-variance-authority';

const buttonVariants = cva("base-classes", {
  variants: {
    variant: {
      default: "...",
      destructive: "...",
    },
    size: {
      default: "...",
      sm: "...",
    },
  },
  defaultVariants: {
    variant: "default",
    size: "default",
  },
});

// Automatically inferred type from cva
interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  // variant?: "default" | "destructive"
  // size?: "default" | "sm"
}
\`\`\`

## Anti-Patterns

❌ Using \`any\` type
❌ Missing JSDoc comments
❌ Manually typing variants (use VariantProps)
❌ \`children: any\` (use \`React.ReactNode\`)

✅ Explicit interface with JSDoc
✅ Use VariantProps for cva
✅ Leverage utility types

---

**Token Estimate**: ~2,800 tokens
