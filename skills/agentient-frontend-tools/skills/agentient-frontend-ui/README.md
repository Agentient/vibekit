# agentient-frontend-ui

**Modern, accessible UI component development with shadcn/ui, Tailwind CSS, Framer Motion, and React Server Components for Next.js 14+.**

## Overview

This plugin provides comprehensive UI development capabilities for Next.js 14+ applications with a focus on:

- **shadcn/ui Components**: Copy-don't-install philosophy for full component ownership
- **Tailwind CSS**: Utility-first, mobile-first responsive design with dark mode
- **React Server Components**: Server-first architecture with minimal client-side JavaScript
- **Framer Motion**: Declarative, performant animations and micro-interactions
- **Web Accessibility**: ARIA patterns, semantic HTML, and keyboard navigation
- **TypeScript**: Strict typing with generics, utility types, and cva variants

## Installation

```bash
# Install the plugin
cd plugins
git clone <vibekit-marketplace-url>
```

## Components

### Agents (2)

#### 1. **ui-designer-agent**
- **When**: Styling, layout, responsive design, dark mode, animations, visual refinement
- **Capabilities**: Apply Tailwind utilities, create responsive layouts, add animations, theme with CSS variables
- **Default Mode**: Direct Mode (styling is iterative)
- **Tools**: Read, Write, Edit, Grep, Glob

#### 2. **component-builder-agent**
- **When**: Create new components, scaffold shadcn/ui, define TypeScript props, component architecture
- **Capabilities**: Scaffold components via CLI, structure RSC vs Client Components, define type-safe props
- **Default Mode**: Plan Mode (mandatory for new components)
- **Tools**: Read, Write, Bash, Grep, Glob

### Commands (5)

| Command | Purpose |
|---------|---------|
| `/add-component` | Scaffold shadcn/ui component using CLI (e.g., button, dialog, card) |
| `/create-variant` | Add component variants using cva and VariantProps |
| `/style-responsive` | Apply mobile-first responsive Tailwind styling |
| `/add-animation` | Add Framer Motion animations (hover, scroll, exit) |
| `/make-accessible` | Enhance component accessibility (ARIA, keyboard nav, screen readers) |

### Skills (6)

1. **shadcn-component-scaffolding** - CLI usage, component composition, file ownership patterns
2. **tailwind-utility-styling** - Utility classes, responsive design, dark mode, CSS variables
3. **react-component-architecture-rsc** - Server vs Client Components, "use client" criteria, composition patterns
4. **typescript-prop-definition** - Interface conventions, generics, utility types, cva + VariantProps
5. **framer-motion-interactive-animation** - motion components, gestures, enter/exit, scroll animations
6. **web-accessibility-patterns** - Semantic HTML, ARIA attributes, keyboard navigation, screen readers

## Quick Start

### 1. Add a shadcn/ui Component

```bash
/add-component

# Or directly:
npx shadcn-ui@latest add button dialog card
```

This installs component source code into `src/components/ui/`, which you fully own and can customize.

### 2. Create a Responsive Layout

```bash
/style-responsive
```

Apply mobile-first Tailwind utilities:
```tsx
<div className="flex flex-col md:flex-row gap-4 p-4 md:p-6">
  <div className="w-full md:w-1/3 bg-card dark:bg-card">
    {/* Sidebar */}
  </div>
  <div className="w-full md:w-2/3">
    {/* Main content */}
  </div>
</div>
```

### 3. Add Animation

```bash
/add-animation
```

```tsx
'use client';

import { motion } from 'framer-motion';

export function Card() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      whileHover={{ scale: 1.02 }}
      className="p-6 rounded-lg bg-card"
    >
      Content
    </motion.div>
  );
}
```

### 4. Make Accessible

```bash
/make-accessible
```

```tsx
<Button variant="ghost" size="icon" aria-label="Close dialog">
  <X size={16} />
</Button>
```

## Configuration

Quality constraints enforced by this plugin:

```json
{
  "QUALITY_THRESHOLD": "97",
  "RSC_DEFAULT": "true",
  "MOBILE_FIRST_RESPONSIVE": "true",
  "SHADCN_CLI_ONLY": "true",
  "CLIENT_DIRECTIVE_MINIMAL": "true",
  "ARIA_REQUIRED_INTERACTIVE": "true"
}
```

## Architectural Principles

### 1. Server Components First

**Default**: All components are React Server Components unless they require:
- State (`useState`, `useReducer`)
- Effects (`useEffect`, `useLayoutEffect`)
- Event handlers (`onClick`, `onChange`)
- Browser APIs (`window`, `localStorage`)

**Pattern**: Keep Client Components small and at the "leaves" of the component tree.

```tsx
// ✅ GOOD: Server Component parent, Client Component leaf
// app/posts/page.tsx (Server Component)
import { LikeButton } from './LikeButton';

export default async function PostPage() {
  const post = await fetchPost(); // Direct data fetching

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
      <LikeButton postId={post.id} /> {/* Small Client Component */}
    </article>
  );
}

// components/LikeButton.tsx (Client Component)
'use client';

export function LikeButton({ postId }) {
  const [liked, setLiked] = useState(false);
  return <button onClick={() => setLiked(!liked)}>Like</button>;
}
```

### 2. Mobile-First Responsive Design

All styles start with mobile (unprefixed), scale up with breakpoints:

```tsx
<div className="
  grid grid-cols-1     // Mobile: 1 column
  sm:grid-cols-2       // Small: 2 columns
  md:grid-cols-3       // Medium: 3 columns
  lg:grid-cols-4       // Large: 4 columns
  gap-4                // Consistent gap
"/>
```

### 3. Theme with CSS Variables

Use semantic variables defined in `globals.css`, not hardcoded colors:

```tsx
// ❌ BAD
<div className="bg-zinc-900 text-white">

// ✅ GOOD
<div className="bg-background text-foreground">
<Button className="bg-primary text-primary-foreground">
<Alert className="bg-destructive text-destructive-foreground">
```

### 4. Component Composition Over Configuration

Build complex UIs by composing shadcn/ui primitives:

```tsx
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

function UserCard({ user }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{user.name}</CardTitle>
      </CardHeader>
      <CardContent>
        <p>{user.bio}</p>
      </CardContent>
      <CardFooter>
        <Button>View Profile</Button>
      </CardFooter>
    </Card>
  );
}
```

## Anti-Patterns (Blocked by Validation)

❌ Using `'use client'` on page.tsx or layout.tsx (forces entire route client-rendered)
❌ Installing shadcn/ui via npm (it's not distributed as a package)
❌ Hardcoded colors (`bg-blue-500`) instead of theme variables (`bg-primary`)
❌ Desktop-first responsive design (use mobile-first with `sm:`, `md:`, `lg:`)
❌ Using `<div onClick>` instead of semantic `<button>`
❌ Animating layout properties (margin, padding) instead of transform (x, y, scale)
❌ Icon-only buttons without `aria-label`

## Dependencies

**Required**: `agentient-frontend-foundation` (for RSC patterns, TypeScript conventions, design tokens)

**Optional**: `agentient-security` (for secure component patterns, XSS prevention)

## Examples

### Example 1: Complete Button Component with Variants

```tsx
// components/ui/button.tsx
import * as React from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils';

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input hover:bg-accent hover:text-accent-foreground",
        ghost: "hover:bg-accent hover:text-accent-foreground",
      },
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

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {}

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

### Example 2: Animated Card with Scroll Trigger

```tsx
'use client';

import { motion } from 'framer-motion';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

export function FeatureCard({ title, description }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.5 }}
    >
      <Card className="hover:shadow-lg transition-shadow">
        <CardHeader>
          <CardTitle>{title}</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-muted-foreground">{description}</p>
        </CardContent>
      </Card>
    </motion.div>
  );
}
```

### Example 3: Accessible Icon Button

```tsx
import { X } from 'lucide-react';
import { Button } from '@/components/ui/button';

function CloseButton({ onClose }: { onClose: () => void }) {
  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={onClose}
      aria-label="Close dialog"
    >
      <X size={16} />
    </Button>
  );
}
```

## Troubleshooting

### Issue: "Can't import Button from @shadcn/ui"

**Solution**: shadcn/ui is not distributed as an npm package. Components are added to your project:
```bash
npx shadcn-ui@latest add button
# Then import from your local components
import { Button } from '@/components/ui/button';
```

### Issue: "Hydration error with Server Component"

**Solution**: You're likely using state/effects in a Server Component. Add `'use client'` directive or restructure to separate interactive parts.

### Issue: "Animation doesn't exit smoothly"

**Solution**: Wrap the component in `<AnimatePresence>` and add an `exit` prop:
```tsx
<AnimatePresence>
  {isVisible && (
    <motion.div exit={{ opacity: 0 }} />
  )}
</AnimatePresence>
```

## Contributing

When extending this plugin:
1. Follow 3-tier progressive disclosure for skills
2. Ensure agents include RSC-first patterns
3. Add validation rules to `component_validator.sh`
4. Test with real shadcn/ui components

## License

Part of the vibekit marketplace.

## Support

- **Documentation**: See individual skills and commands
- **Issues**: Report to vibekit marketplace repository
- **Questions**: Use `/help` or consult the ui-designer-agent or component-builder-agent

---

**Version**: 1.0.0
**Confidence Level**: 97%
**Target Stack**: shadcn/ui (latest), Tailwind CSS 3.4+, Framer Motion (latest), Next.js 14+, React 18+, TypeScript 5.3+
**Maintained by**: Agentient Labs
