---
name: shadcn-component-scaffolding
description: |
  shadcn/ui CLI usage, component installation, composition patterns, and file ownership philosophy.
  Keywords: "add component", "install shadcn", "scaffold", "cli", "components.json"
---

# shadcn/ui Component Scaffolding

## Overview

shadcn/ui is a collection of re-usable components that you copy into your project. Unlike traditional component libraries, you own the code.

## CLI Usage (MANDATORY)

**ONLY way to add components**:

\`\`\`bash
npx shadcn-ui@latest add button dialog card
\`\`\`

**Why CLI only**:
- Resolves dependencies automatically
- Updates components.json
- Installs peer packages
- Ensures correct configuration

## Component Composition

Most shadcn/ui components are composed of multiple parts:

\`\`\`tsx
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from '@/components/ui/card';

function ProfileCard({ user }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{user.name}</CardTitle>
        <CardDescription>{user.email}</CardDescription>
      </CardHeader>
      <CardContent>
        <p>{user.bio}</p>
      </CardContent>
      <CardFooter>
        <Button>Edit Profile</Button>
      </CardFooter>
    </Card>
  );
}
\`\`\`

## File Ownership

After installation, the component source code is in your project at \`src/components/ui/[component].tsx\`. You can:
- Modify the code freely
- Add custom variants
- Change styling
- Extend functionality

## Anti-Patterns

❌ \`npm install @shadcn/ui\` - Not distributed as package
❌ Manually copying from website - Bypasses dependency checks
❌ Importing from non-existent package

✅ Always use: \`npx shadcn-ui@latest add [component]\`

---

**Token Estimate**: ~1,500 tokens
