---
name: tailwind-utility-styling
description: |
  Tailwind CSS utility-first styling, mobile-first responsive design, dark mode, CSS variables, and cva variants.
  Keywords: "style", "tailwind", "responsive", "dark mode", "mobile-first", "css variables"
---

# Tailwind CSS Utility Styling

## Core Utility Classes

### Layout

\`\`\`tsx
// Flexbox
<div className="flex justify-center items-center gap-4">

// Grid
<div className="grid grid-cols-3 gap-6">

// Positioning
<div className="relative">
  <div className="absolute top-0 right-0">
\`\`\`

### Spacing

\`\`\`tsx
// Padding: p-{size}
<div className="p-4">           // 1rem (16px)
<div className="px-6 py-4">    // Horizontal/vertical

// Margin: m-{size}
<div className="mt-8 mb-4">    // Top/bottom
<div className="mx-auto">      // Center horizontally
\`\`\`

### Typography

\`\`\`tsx
<h1 className="text-3xl font-bold leading-tight">
<p className="text-base text-muted-foreground">
\`\`\`

## Mobile-First Responsive (MANDATORY)

Start with mobile (unprefixed), add breakpoints:

\`\`\`tsx
<div className="
  flex flex-col         // Mobile: stack
  md:flex-row           // Medium+: horizontal
  gap-4 md:gap-6        // Responsive gap
">
\`\`\`

Breakpoints: \`sm:\` (640px), \`md:\` (768px), \`lg:\` (1024px), \`xl:\` (1280px)

## Dark Mode

Use \`dark:\` prefix:

\`\`\`tsx
<div className="bg-white dark:bg-zinc-900 text-zinc-900 dark:text-zinc-100">
\`\`\`

## CSS Variables (REQUIRED)

Use semantic variables, never hardcoded colors:

\`\`\`tsx
// ✅ GOOD
<Button className="bg-primary text-primary-foreground">
<Alert className="bg-destructive text-destructive-foreground">

// ❌ BAD
<Button className="bg-blue-500 text-white">
\`\`\`

Available variables:
- \`background\`, \`foreground\`
- \`card\`, \`card-foreground\`
- \`primary\`, \`primary-foreground\`
- \`secondary\`, \`muted\`, \`accent\`
- \`destructive\`, \`border\`, \`input\`, \`ring\`

## cva for Variants

\`\`\`tsx
import { cva } from 'class-variance-authority';

const buttonVariants = cva(
  "base classes here",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground",
        destructive: "bg-destructive",
      },
      size: {
        default: "h-10 px-4",
        sm: "h-9 px-3",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);
\`\`\`

---

**Token Estimate**: ~2,500 tokens
