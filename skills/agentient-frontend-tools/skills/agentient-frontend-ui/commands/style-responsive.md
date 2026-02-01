---
name: style-responsive
description: Apply mobile-first responsive Tailwind CSS styling with breakpoints, dark mode, and semantic theme variables
---

# /style-responsive Command

**Purpose**: Apply mobile-first responsive design using Tailwind CSS utility classes, with proper breakpoints, dark mode support, and semantic CSS variables.

## Usage

```bash
/style-responsive
```

The command analyzes the selected component and suggests responsive improvements based on mobile-first principles.

## Mobile-First Strategy

**Core Principle**: Start with mobile (unprefixed), scale up with breakpoints.

```tsx
// ✅ GOOD: Mobile first
<div className="
  flex flex-col        // Mobile: vertical stack
  md:flex-row          // Medium+: horizontal
  gap-4 md:gap-6       // Responsive spacing
  p-4 md:p-6 lg:p-8    // Scale padding
">

// ❌ BAD: Desktop first
<div className="lg:flex-row flex-col">
```

## Tailwind Breakpoints

| Breakpoint | Min Width | Typical Device |
|------------|-----------|----------------|
| (default) | 0px | Mobile portrait |
| `sm:` | 640px | Mobile landscape |
| `md:` | 768px | Tablet |
| `lg:` | 1024px | Laptop |
| `xl:` | 1280px | Desktop |
| `2xl:` | 1536px | Large desktop |

## Common Responsive Patterns

### Layout: Stack to Side-by-Side

```tsx
<div className="
  flex flex-col md:flex-row
  gap-4
">
  <aside className="w-full md:w-1/4">Sidebar</aside>
  <main className="w-full md:w-3/4">Content</main>
</div>
```

### Grid: Responsive Columns

```tsx
<div className="
  grid
  grid-cols-1          // Mobile: 1 column
  sm:grid-cols-2       // Small: 2 columns
  md:grid-cols-3       // Medium: 3 columns
  lg:grid-cols-4       // Large: 4 columns
  gap-4 md:gap-6
">
  {items.map(item => <Card key={item.id} />)}
</div>
```

### Typography: Responsive Sizes

```tsx
<h1 className="
  text-2xl md:text-3xl lg:text-4xl
  font-bold
  leading-tight md:leading-snug
">
  Headline
</h1>

<p className="
  text-sm md:text-base lg:text-lg
  text-muted-foreground
">
  Body text scales with viewport
</p>
```

### Spacing: Responsive Padding/Margin

```tsx
<section className="
  px-4 md:px-6 lg:px-8
  py-8 md:py-12 lg:py-16
  max-w-7xl mx-auto
">
  {children}
</section>
```

## Dark Mode Support

Use the `dark:` prefix with semantic CSS variables:

```tsx
// Automatic theming with CSS variables
<Card className="bg-card text-card-foreground border-border">

// Explicit dark mode overrides
<div className="
  bg-white dark:bg-zinc-900
  text-zinc-900 dark:text-zinc-100
  border-zinc-200 dark:border-zinc-800
">
```

## Semantic CSS Variables

**Always use semantic variables** defined in `globals.css`:

```tsx
// ✅ GOOD: Semantic variables (auto dark mode)
<Button className="bg-primary text-primary-foreground">
<Alert className="bg-destructive text-destructive-foreground">
<Card className="bg-card text-card-foreground border-border">

// ❌ BAD: Hardcoded colors
<Button className="bg-blue-500 text-white">
<Alert className="bg-red-600 text-white">
```

Available semantic variables:
- `background`, `foreground`
- `card`, `card-foreground`
- `popover`, `popover-foreground`
- `primary`, `primary-foreground`
- `secondary`, `secondary-foreground`
- `muted`, `muted-foreground`
- `accent`, `accent-foreground`
- `destructive`, `destructive-foreground`
- `border`, `input`, `ring`

## Example: Complete Responsive Component

```tsx
export function FeatureSection() {
  return (
    <section className="
      // Container
      px-4 md:px-6 lg:px-8
      py-12 md:py-16 lg:py-24
      max-w-7xl mx-auto
    ">
      {/* Heading */}
      <h2 className="
        text-3xl md:text-4xl lg:text-5xl
        font-bold tracking-tight
        text-center
        mb-4 md:mb-6
      ">
        Features
      </h2>
      
      {/* Description */}
      <p className="
        text-base md:text-lg
        text-muted-foreground
        text-center
        max-w-2xl mx-auto
        mb-12 md:mb-16
      ">
        Discover what makes our product unique
      </p>
      
      {/* Grid */}
      <div className="
        grid
        grid-cols-1 sm:grid-cols-2 lg:grid-cols-3
        gap-6 md:gap-8
      ">
        {features.map(feature => (
          <Card key={feature.id} className="
            p-6
            hover:shadow-lg
            transition-shadow
            dark:hover:shadow-primary/10
          ">
            <h3 className="text-xl font-semibold mb-2">
              {feature.title}
            </h3>
            <p className="text-muted-foreground">
              {feature.description}
            </p>
          </Card>
        ))}
      </div>
    </section>
  );
}
```

## Best Practices

✅ **Do**:
- Start with mobile (unprefixed)
- Use semantic CSS variables
- Test across breakpoints
- Use `max-w-*` and `mx-auto` for content width
- Apply `dark:` variants for dark mode
- Use consistent spacing scale (4, 6, 8, 12, 16, 24...)

❌ **Don't**:
- Start with `lg:` or `xl:` prefixes
- Use hardcoded colors (bg-blue-500)
- Forget to test mobile viewport
- Use arbitrary values excessively (w-[347px])
- Mix responsive and non-responsive patterns inconsistently

---

**Related Commands**: `/add-component`, `/create-variant`
**Skill Dependencies**: `tailwind-utility-styling`
