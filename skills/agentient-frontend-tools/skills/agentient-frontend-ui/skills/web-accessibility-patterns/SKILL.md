---
name: web-accessibility-patterns
description: |
  Web accessibility patterns: semantic HTML, ARIA attributes, keyboard navigation, screen reader support, focus management.
  Keywords: "accessibility", "a11y", "aria", "screen reader", "keyboard", "semantic html"
---

# Web Accessibility Patterns

## Semantic HTML Foundation

Use correct elements:

\`\`\`tsx
// ✅ GOOD
<button onClick={handleClick}>Submit</button>
<nav>...</nav>
<main>...</main>

// ❌ BAD
<div onClick={handleClick}>Submit</div>
\`\`\`

## ARIA Attributes

### Icon-Only Buttons

\`\`\`tsx
<Button variant="ghost" size="icon" aria-label="Close dialog">
  <X size={16} />
</Button>
\`\`\`

### Form Fields

\`\`\`tsx
<div>
  <Label htmlFor="email">Email</Label>
  <Input
    id="email"
    type="email"
    aria-describedby="email-description"
    aria-invalid={!!error}
  />
  <p id="email-description" className="text-sm text-muted-foreground">
    We'll never share your email
  </p>
  {error && (
    <p id="email-error" className="text-sm text-destructive" role="alert">
      {error}
    </p>
  )}
</div>
\`\`\`

### Loading States

\`\`\`tsx
<div aria-live="polite" aria-busy={isLoading}>
  {isLoading ? <Skeleton /> : <Content />}
</div>
\`\`\`

## Keyboard Navigation

Ensure keyboard accessibility:

\`\`\`tsx
// Custom interactive element
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  }}
>
  Interactive element
</div>
\`\`\`

## Focus Management

\`\`\`tsx
<Button className="
  focus-visible:outline-none
  focus-visible:ring-2
  focus-visible:ring-ring
  focus-visible:ring-offset-2
">
  Accessible focus state
</Button>
\`\`\`

## Anti-Patterns

❌ \`<div onClick>\` instead of \`<button>\`
❌ Icon without \`aria-label\`
❌ Redundant \`aria-label\` on elements with text
❌ Missing keyboard support for custom interactive elements

✅ Semantic HTML
✅ ARIA for icons and dynamic content
✅ Keyboard navigation
✅ Focus visible styles

---

**Token Estimate**: ~2,000 tokens
