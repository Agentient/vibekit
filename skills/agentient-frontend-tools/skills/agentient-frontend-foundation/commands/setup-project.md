# Setup Next.js 14+ Project Command

You are scaffolding a new Next.js 14+ project with an opinionated, production-ready structure that enforces best practices for React Server Components, TypeScript strict mode, and maintainability.

## Task Overview

Create a new Next.js 14+ project with:
1. App Router architecture (not Pages Router)
2. TypeScript in strict mode
3. Opinionated folder structure
4. Essential configuration files
5. Baseline dependencies
6. Development tooling setup

## Prerequisites Check

Before starting, verify:
- [ ] Node.js 20.x LTS is installed (`node --version`)
- [ ] npm or yarn or pnpm is available
- [ ] Project name is decided (kebab-case recommended)
- [ ] Target directory is empty or doesn't exist yet

## Execution Instructions

### Step 1: Initialize Next.js Project

Run the official Next.js installer with the following options:

```bash
npx create-next-app@latest [project-name] \
  --typescript \
  --app \
  --tailwind \
  --eslint \
  --src-dir \
  --import-alias "@/*"
```

**Configuration Choices** (when prompted):
- ✅ TypeScript: Yes
- ✅ ESLint: Yes
- ✅ Tailwind CSS: Yes
- ✅ `src/` directory: Yes
- ✅ App Router: Yes
- ✅ Import alias (@/*): Yes
- ❌ Turbopack: No (optional, can enable later)

### Step 2: Navigate to Project

```bash
cd [project-name]
```

### Step 3: Install Additional Dependencies

#### Core Dependencies

```bash
npm install zod@^4.1.12 \
            zustand@^5.0.2 \
            react-hook-form@^7.0.0 \
            @hookform/resolvers \
            lucide-react
```

**Purpose**:
- `zod`: Runtime validation and type-safe schemas
- `zustand`: Lightweight state management (when needed)
- `react-hook-form`: Form handling for Client Components
- `@hookform/resolvers`: Zod integration for react-hook-form
- `lucide-react`: Icon library

#### Development Dependencies

```bash
npm install -D @types/node@^20 \
              prettier@^3.0.0 \
              prettier-plugin-tailwindcss \
              eslint-config-prettier
```

**Purpose**:
- `@types/node`: Node.js type definitions
- `prettier`: Code formatting
- `prettier-plugin-tailwindcss`: Auto-sort Tailwind classes
- `eslint-config-prettier`: Disable ESLint rules that conflict with Prettier

### Step 4: Create Opinionated Folder Structure

Create the following directory structure inside the `src/` folder:

```bash
mkdir -p src/app/{api,actions}
mkdir -p src/components/{ui,forms,layouts}
mkdir -p src/lib/{utils,validations}
mkdir -p src/types/{api,models}
mkdir -p src/hooks
mkdir -p src/styles
mkdir -p public/images
mkdir -p docs/adr
```

**Resulting Structure**:

```
[project-name]/
├── src/
│   ├── app/                      # Next.js App Router
│   │   ├── api/                  # API Route handlers
│   │   ├── actions/              # Server Actions
│   │   ├── layout.tsx            # Root layout (Server Component)
│   │   ├── page.tsx              # Home page (Server Component)
│   │   ├── loading.tsx           # Global loading state
│   │   └── error.tsx             # Global error boundary
│   ├── components/
│   │   ├── ui/                   # Reusable UI components (buttons, inputs, etc.)
│   │   ├── forms/                # Form components (with validation)
│   │   └── layouts/              # Layout components (headers, footers, etc.)
│   ├── lib/
│   │   ├── utils/                # Utility functions
│   │   └── validations/          # Zod schemas
│   ├── types/
│   │   ├── api/                  # API request/response types
│   │   └── models/               # Data model types
│   ├── hooks/                    # Custom React hooks (for Client Components)
│   └── styles/                   # Global styles, CSS modules
├── public/
│   └── images/                   # Static images
├── docs/
│   └── adr/                      # Architecture Decision Records
├── .env.local                    # Local environment variables (create this)
├── .env.example                  # Example env vars (create this)
├── .gitignore                    # Git ignore rules
├── tsconfig.json                 # TypeScript configuration
├── next.config.js                # Next.js configuration
├── tailwind.config.ts            # Tailwind CSS configuration
├── .eslintrc.json                # ESLint configuration
├── .prettierrc                   # Prettier configuration (create this)
└── package.json                  # Project dependencies
```

### Step 5: Configure TypeScript (Strict Mode)

Edit `tsconfig.json` to enforce strict mode:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "dom", "dom.iterable"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

**Key Strict Settings**:
- `"strict": true` - Enables all strict type-checking options
- `"noUncheckedIndexedAccess": true` - Array/object access returns T | undefined
- `"noImplicitOverride": true` - Require explicit override keyword

### Step 6: Configure Prettier

Create `.prettierrc` in the project root:

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "plugins": ["prettier-plugin-tailwindcss"]
}
```

Create `.prettierignore`:

```
.next
node_modules
out
build
dist
*.min.js
```

### Step 7: Update ESLint Configuration

Edit `.eslintrc.json` to add Prettier integration:

```json
{
  "extends": [
    "next/core-web-vitals",
    "prettier"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
    "@typescript-eslint/no-explicit-any": "error"
  }
}
```

**Key Rules**:
- Enforce unused variable errors (with underscore prefix exception)
- Explicitly ban the `any` type

### Step 8: Create Utility Files

#### `src/lib/utils/cn.ts` (Tailwind class merging utility)

```typescript
import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Utility for merging Tailwind CSS classes
 * Combines clsx for conditional classes and twMerge for deduplication
 */
export function cn(...inputs: ClassValue[]): string {
  return twMerge(clsx(inputs));
}
```

Install dependencies for this utility:

```bash
npm install clsx tailwind-merge
```

#### `src/lib/validations/common.ts` (Common Zod schemas)

```typescript
import { z } from 'zod';

/**
 * Common Zod validation schemas
 * Reusable across the application
 */

export const emailSchema = z.string().email('Invalid email address');

export const uuidSchema = z.string().uuid('Invalid UUID format');

export const nonEmptyStringSchema = z.string().min(1, 'This field is required');

export const passwordSchema = z
  .string()
  .min(8, 'Password must be at least 8 characters')
  .regex(/[A-Z]/, 'Password must contain at least one uppercase letter')
  .regex(/[a-z]/, 'Password must contain at least one lowercase letter')
  .regex(/[0-9]/, 'Password must contain at least one number');
```

#### `src/types/api/common.ts` (API response types)

```typescript
/**
 * Standard API response wrapper types
 * Ensures consistent API response structure across all endpoints
 */

export type ApiResponse<T> = ApiSuccessResponse<T> | ApiErrorResponse;

export interface ApiSuccessResponse<T> {
  success: true;
  data: T;
  meta?: {
    page?: number;
    limit?: number;
    total?: number;
  };
}

export interface ApiErrorResponse {
  success: false;
  error: ApiError;
}

export interface ApiError {
  code: string;
  message: string;
  details?: Record<string, string[]>;
}
```

### Step 9: Create Environment Variable Template

Create `.env.example`:

```bash
# App
NEXT_PUBLIC_APP_URL=http://localhost:3000

# API
NEXT_PUBLIC_API_URL=http://localhost:3000/api

# Database (example)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Authentication (example)
# NEXTAUTH_SECRET=your-secret-here
# NEXTAUTH_URL=http://localhost:3000

# Third-Party Services (examples)
# STRIPE_SECRET_KEY=sk_test_...
# STRIPE_PUBLISHABLE_KEY=pk_test_...
```

Create `.env.local` (copy from .env.example and fill in real values):

```bash
cp .env.example .env.local
```

**Note**: `.env.local` is already in `.gitignore` by default.

### Step 10: Update package.json Scripts

Add helpful scripts to `package.json`:

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "format": "prettier --write \"src/**/*.{ts,tsx,js,jsx,json,css,md}\"",
    "format:check": "prettier --check \"src/**/*.{ts,tsx,js,jsx,json,css,md}\"",
    "type-check": "tsc --noEmit"
  }
}
```

### Step 11: Create Initial ADR

Create `docs/adr/001-adopt-nextjs-app-router.md`:

```markdown
# ADR-001: Adopt Next.js 14+ App Router with React Server Components

**Date**: [Today's Date]
**Status**: Accepted
**Deciders**: [Your Name/Team Name]

## Context

We are starting a new Next.js project and must choose between the Pages Router (legacy) and the App Router (modern).

## Decision

We will use Next.js 14+ with the **App Router** and adopt **React Server Components** (RSC) as the default rendering strategy.

## Consequences

### Positive Consequences
- **Better Performance**: Server Components reduce client-side JavaScript bundle size
- **Improved SEO**: Server-side rendering by default improves search engine indexing
- **Modern Patterns**: Access to the latest Next.js features (Server Actions, streaming, etc.)
- **Future-Proof**: App Router is the future direction of Next.js

### Negative Consequences
- **Learning Curve**: Team must understand Server vs Client Component boundaries
- **Migration Difficulty**: Harder to migrate away from Next.js if needed (framework lock-in)

### Mitigation Strategies
- Provide team training on Server Components patterns
- Document common patterns in ADRs and code examples
- Use TypeScript strict mode to catch common mistakes at compile-time

## Alternatives Considered

### Alternative 1: Pages Router
- **Pros**: More mature, extensive community resources
- **Cons**: Legacy approach, missing modern features
- **Why Rejected**: Not future-proof, Pages Router is in maintenance mode

### Alternative 2: Different Framework (Remix, SvelteKit)
- **Pros**: Other frameworks have their own strengths
- **Cons**: Smaller ecosystems, less enterprise adoption
- **Why Rejected**: Next.js has the largest ecosystem and best Vercel integration

## References
- [Next.js App Router Documentation](https://nextjs.org/docs/app)
- [React Server Components](https://react.dev/reference/rsc/server-components)
```

### Step 12: Verify Setup

Run these commands to verify everything works:

```bash
# Type check
npm run type-check

# Lint check
npm run lint

# Format check
npm run format:check

# Development server
npm run dev
```

Visit `http://localhost:3000` to see the default Next.js welcome page.

### Step 13: Git Initialization (if not already done)

```bash
git init
git add .
git commit -m "Initial Next.js 14+ project setup with strict TypeScript and opinionated structure"
```

## Summary of What Was Created

✅ **Project Structure**:
- Next.js 14+ with App Router
- TypeScript in strict mode
- Organized folder structure (app/, components/, lib/, types/, etc.)

✅ **Configuration**:
- `tsconfig.json` with strict settings
- `.prettierrc` for code formatting
- `.eslintrc.json` with Prettier integration
- Environment variable templates

✅ **Dependencies**:
- Core: Next.js, React, TypeScript
- Validation: Zod
- State: Zustand (when needed)
- Forms: React Hook Form
- Icons: lucide-react
- Dev: Prettier, ESLint

✅ **Utilities**:
- `cn()` for Tailwind class merging
- Common Zod schemas (email, UUID, password)
- Standard API response types

✅ **Documentation**:
- Initial ADR documenting App Router decision
- Environment variable template

## Next Steps

After project setup is complete:

1. **Define your data models** in `src/types/models/`
2. **Create API contracts** with `/api-contract` command
3. **Build your first page** with `/create-page` command
4. **Set up authentication** (if needed)
5. **Add database** (if needed - Prisma, Drizzle, or Firebase)
6. **Configure deployment** (Vercel, AWS, GCP)

---

**Project setup complete! You now have a production-ready Next.js 14+ foundation with best practices enforced.**
