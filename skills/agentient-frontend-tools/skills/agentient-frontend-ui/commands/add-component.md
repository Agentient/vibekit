---
name: add-component
description: Scaffold shadcn/ui components using the official CLI, installing source code directly into your project
---

# /add-component Command

**Purpose**: Add shadcn/ui components to your project using the official CLI. Components are copied as source code into `src/components/ui/`, giving you full ownership and customization ability.

## Usage

```bash
/add-component
```

Or specify components directly:

```bash
/add-component button dialog card
```

## What This Command Does

1. Executes `npx shadcn-ui@latest add [component]`
2. Installs component source code into `src/components/ui/`
3. Updates `components.json` configuration
4. Installs any peer dependencies
5. Provides import statements and usage examples

## Available Components

Common components:
- **button** - Versatile button with variants
- **card** - Container with header, content, footer
- **dialog** - Modal dialog/popup
- **input** - Form input field
- **select** - Dropdown select menu
- **checkbox** - Checkbox with label
- **radio-group** - Radio button group
- **switch** - Toggle switch
- **textarea** - Multi-line text input
- **label** - Form field label
- **badge** - Small status indicator
- **alert** - Alert/notification box
- **avatar** - User avatar with fallback
- **separator** - Visual divider
- **skeleton** - Loading placeholder

Full list: https://ui.shadcn.com/docs/components

## Example Session

```
User: /add-component

Agent: Which shadcn/ui components would you like to add?

Available categories:
1. Form components (button, input, select, checkbox)
2. Layout components (card, separator, tabs)
3. Feedback components (alert, toast, dialog)
4. Data display (table, badge, avatar)

User: Form components

Agent: Adding form components...

$ npx shadcn-ui@latest add button input select checkbox label

✓ Created src/components/ui/button.tsx
✓ Created src/components/ui/input.tsx
✓ Created src/components/ui/select.tsx
✓ Created src/components/ui/checkbox.tsx
✓ Created src/components/ui/label.tsx
✓ Updated components.json

Usage examples:

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

<Button variant="default">Submit</Button>
<Input type="email" placeholder="Email" />
```

## Component Composition Pattern

shadcn/ui components are often composed of multiple parts:

```tsx
// Dialog is composed of multiple primitives
import {
  Dialog,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from '@/components/ui/dialog';

function DeleteConfirmation() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="destructive">Delete</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Are you sure?</DialogTitle>
          <DialogDescription>
            This action cannot be undone.
          </DialogDescription>
        </DialogHeader>
        <DialogFooter>
          <Button variant="outline">Cancel</Button>
          <Button variant="destructive">Delete</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
```

## Best Practices

✅ **Do**:
- Use the CLI to add components (ensures correct configuration)
- Customize the source code after installation (you own it!)
- Compose primitives to build complex UIs
- Check the shadcn/ui docs for component-specific patterns

❌ **Don't**:
- Try to `npm install @shadcn/ui` (it's not distributed as a package)
- Manually copy code from the website (bypasses dependency checks)
- Modify the CLI-generated `components.json` manually

## Troubleshooting

**Issue**: "Command not found: shadcn-ui"
**Solution**: Use `npx shadcn-ui@latest add` (npx downloads and runs it)

**Issue**: "Project not initialized"
**Solution**: Run `npx shadcn-ui@latest init` first to set up configuration

**Issue**: "Component already exists"
**Solution**: The CLI will prompt to overwrite. Choose 'yes' to update to the latest version.

---

**Related Commands**: `/create-variant`, `/style-responsive`
**Skill Dependencies**: `shadcn-component-scaffolding`
