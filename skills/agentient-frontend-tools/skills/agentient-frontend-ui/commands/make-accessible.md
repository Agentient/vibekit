---
name: make-accessible
description: Enhance component accessibility with ARIA attributes, semantic HTML, keyboard navigation, and screen reader support
---

# /make-accessible Command

**Purpose**: Audit and enhance component accessibility following WAI-ARIA best practices, ensuring components are usable by keyboard, screen readers, and assistive technologies.

## Usage

```bash
/make-accessible
```

The command analyzes the selected component and provides accessibility improvements.

## Core Accessibility Principles

### 1. Semantic HTML Foundation

Use correct HTML elements for their intended purpose:

```tsx
// ✅ GOOD: Semantic elements
<button onClick={handleClick}>Submit</button>
<nav>...</nav>
<main>...</main>
<article>...</article>

// ❌ BAD: Generic elements with handlers
<div onClick={handleClick}>Submit</div>
<div>Navigation</div>
```

### 2. ARIA Attributes

Use ARIA to enhance semantics when HTML alone isn't sufficient:

```tsx
// Icon-only button
<Button variant="ghost" size="icon" aria-label="Close dialog">
  <X size={16} />
</Button>

// Button with loading state
<Button 
  disabled={isLoading}
  aria-busy={isLoading}
  aria-label={isLoading ? "Submitting..." : "Submit form"}
>
  {isLoading ? <Loader2 className="animate-spin" /> : "Submit"}
</Button>

// Form field with description and error
<div>
  <Label htmlFor="email">Email</Label>
  <Input
    id="email"
    type="email"
    aria-describedby="email-description email-error"
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
```

### 3. Keyboard Navigation

Ensure all interactive elements are keyboard accessible:

```tsx
// Custom interactive component
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
  aria-label="Custom action"
>
  Click or press Enter/Space
</div>

// Focus visible styles
<Button className="
  focus-visible:outline-none
  focus-visible:ring-2
  focus-visible:ring-ring
  focus-visible:ring-offset-2
">
  Accessible focus state
</Button>
```

## Common Accessibility Patterns

### Icon Accessibility

```tsx
import { Check, X, AlertTriangle } from 'lucide-react';

// Decorative icon (hidden from screen readers)
<span className="flex items-center gap-2">
  <Check className="text-green-600" aria-hidden="true" />
  <span>Success</span>
</span>

// Icon-only button (requires label)
<Button variant="ghost" size="icon" aria-label="Delete item">
  <X size={16} />
</Button>

// Icon with visible text (no aria-label needed)
<Button>
  <AlertTriangle size={16} className="mr-2" aria-hidden="true" />
  Warning
</Button>
```

### Form Accessibility

```tsx
<form>
  {/* Label association */}
  <div className="space-y-2">
    <Label htmlFor="username">Username</Label>
    <Input
      id="username"
      name="username"
      required
      aria-required="true"
      aria-invalid={!!errors.username}
      aria-describedby="username-error"
    />
    {errors.username && (
      <p id="username-error" className="text-sm text-destructive" role="alert">
        {errors.username}
      </p>
    )}
  </div>

  {/* Checkbox with description */}
  <div className="flex items-start space-x-2">
    <Checkbox
      id="terms"
      aria-describedby="terms-description"
    />
    <div className="grid gap-1.5 leading-none">
      <label
        htmlFor="terms"
        className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
      >
        Accept terms and conditions
      </label>
      <p id="terms-description" className="text-sm text-muted-foreground">
        You agree to our Terms of Service and Privacy Policy.
      </p>
    </div>
  </div>
</form>
```

### Dialog/Modal Accessibility

```tsx
'use client';

import { Dialog, DialogContent } from '@/components/ui/dialog';
import { useEffect, useRef } from 'react';

export function AccessibleDialog({ open, onClose }) {
  const closeButtonRef = useRef<HTMLButtonElement>(null);

  // Focus trap and initial focus
  useEffect(() => {
    if (open) {
      closeButtonRef.current?.focus();
    }
  }, [open]);

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent
        aria-labelledby="dialog-title"
        aria-describedby="dialog-description"
      >
        <DialogHeader>
          <DialogTitle id="dialog-title">Confirmation</DialogTitle>
          <DialogDescription id="dialog-description">
            Are you sure you want to proceed?
          </DialogDescription>
        </DialogHeader>
        <DialogFooter>
          <Button variant="outline" onClick={onClose}>
            Cancel
          </Button>
          <Button ref={closeButtonRef} onClick={handleConfirm}>
            Confirm
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
```

### Loading/Skeleton States

```tsx
// Loading state with aria-live
<div aria-live="polite" aria-busy={isLoading}>
  {isLoading ? (
    <div className="space-y-2">
      <Skeleton className="h-4 w-full" />
      <Skeleton className="h-4 w-3/4" />
    </div>
  ) : (
    <div>{content}</div>
  )}
</div>

// Screen reader only text
<span className="sr-only">Loading...</span>
```

## ARIA Roles Reference

| Role | When to Use |
|------|-------------|
| `button` | Interactive element that triggers an action |
| `link` | Navigation to another page/section |
| `alert` | Important message requiring attention |
| `dialog` | Modal window |
| `menu` | Application menu (not navigation) |
| `checkbox` | Toggle selection |
| `radio` | Mutually exclusive options |
| `tab` | Tab in a tablist |
| `status` | Live region with status updates |

## Testing Accessibility

### Keyboard Testing

- Tab through all interactive elements
- Verify focus visible styles
- Test Enter/Space on custom interactive elements
- Verify Escape closes modals/dialogs
- Test arrow keys for list navigation (if applicable)

### Screen Reader Testing

- Use NVDA (Windows) or VoiceOver (Mac)
- Verify all interactive elements are announced
- Check that icon-only buttons have labels
- Ensure form errors are announced
- Verify live regions update properly

### Automated Testing

```bash
# Install axe-core for automated testing
npm install -D @axe-core/react

# Or use browser extensions:
# - axe DevTools
# - WAVE
# - Lighthouse
```

## Best Practices

✅ **Do**:
- Use semantic HTML elements
- Provide text alternatives for images/icons
- Ensure keyboard navigation works
- Use proper ARIA labels and descriptions
- Test with screen readers
- Maintain color contrast ratios (4.5:1 minimum)
- Provide focus visible styles

❌ **Don't**:
- Use `<div>` with `onClick` instead of `<button>`
- Add redundant `aria-label` to elements with visible text
- Use `aria-label` on non-interactive elements
- Rely solely on color to convey information
- Disable focus outlines without replacement
- Use `tabIndex` values other than 0 or -1

---

**Related Commands**: `/add-component`, `/style-responsive`
**Skill Dependencies**: `web-accessibility-patterns`
