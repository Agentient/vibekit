# Agentient Performance Plugin

Performance optimization plugin for Next.js 14+, React 18+, and Python applications. Provides expert guidance on Core Web Vitals optimization, bundle analysis, advanced caching strategies, and profiling tools.

## Overview

The `agentient-performance` plugin transforms Claude Code into a specialized performance engineer capable of diagnosing bottlenecks and implementing optimization strategies across your full-stack application.

## Key Capabilities

- **Performance Analysis**: Diagnose performance issues using Chrome DevTools and Python profilers
- **Core Web Vitals Optimization**: Achieve LCP < 2.5s, INP < 200ms, CLS < 0.1
- **Bundle Optimization**: Analyze and reduce JavaScript bundle size
- **Caching Strategy**: Implement multi-layer caching (browser, CDN, server, database)
- **Code Profiling**: Identify computational bottlenecks in React and Python
- **Full-Stack Optimization**: Frontend and backend performance improvements

## Installation

This plugin is part of the vibekit marketplace and is automatically available when the marketplace is installed.

### Dependencies

This plugin depends on:
- `agentient-frontend-foundation` - Core Next.js and React knowledge
- `agentient-python-core` - Python backend fundamentals

These dependencies will be automatically loaded when needed.

## Usage

### Commands

The plugin provides four specialized commands:

#### `/analyze-performance`

Perform comprehensive performance analysis across frontend and backend systems.

```bash
# Full-stack analysis
/analyze-performance

# Frontend-specific
/analyze-performance frontend

# Backend-specific
/analyze-performance backend
```

#### `/optimize-bundle`

Analyze and optimize JavaScript bundle size.

```bash
# Comprehensive bundle optimization
/optimize-bundle

# Focus on reducing size
/optimize-bundle size

# Optimize loading strategy
/optimize-bundle loading
```

#### `/cache-strategy`

Design and implement caching strategies.

```bash
# Multi-layer caching strategy
/cache-strategy

# Specific layer
/cache-strategy browser
/cache-strategy cdn
/cache-strategy server
```

#### `/profile-code`

Profile application code to identify bottlenecks.

```bash
# Full-stack profiling
/profile-code

# Frontend React components
/profile-code frontend

# Backend Python code
/profile-code backend

# Specific file
/profile-code frontend src/components/ProductList.tsx
```

### Agent

The **performance-engineer** agent is automatically activated when you use performance-related commands or work on performance optimization tasks.

The agent:
- Operates in Plan Mode for non-trivial optimizations
- Provides evidence-based recommendations backed by profiling data
- Explains tradeoffs and performance impacts
- Ensures changes are validated with measurements

## Skills

The plugin includes six specialized skills that are automatically activated based on context:

### Always-Loaded Skills

- **browser-runtime-performance-profiling**: Chrome DevTools mastery, Core Web Vitals tracking

### On-Demand Skills

- **nextjs-rsc-performance-patterns**: Next.js 14+ RSC optimization, streaming, caching
- **react-concurrency-and-memoization**: React 18+ concurrency, strategic memoization
- **frontend-bundle-analysis-and-optimization**: Bundle size reduction, code splitting
- **python-advanced-profiling-and-optimization**: Python profiling, memory optimization
- **advanced-caching-strategies**: Multi-layer caching implementation

Skills are loaded automatically when relevant keywords, file patterns, or modes are detected.

## Technology Stack

- **Frontend**: Next.js 14+, React 18+, React Server Components
- **Backend**: Python 3.13, FastAPI, Firebase Functions
- **Infrastructure**: GCP, Firebase, Vercel
- **Profiling Tools**: Chrome DevTools, Lighthouse, React Profiler, cProfile, py-spy
- **Monitoring**: Web Vitals API, Performance Observer API

## Performance Targets

This plugin helps you achieve:

- **LCP (Largest Contentful Paint)**: < 2.5 seconds
- **INP (Interaction to Next Paint)**: < 200ms
- **CLS (Cumulative Layout Shift)**: < 0.1
- **Initial JS Bundle**: < 170 KB (compressed)
- **API Response Time**: < 100ms (p50), < 500ms (p99)
- **Total Page Weight**: < 1 MB

## Examples

### Example 1: Optimize Next.js Page Performance

```typescript
// Before: Client-side fetching with waterfall
'use client'
import { useState, useEffect } from 'react'

export default function ProductPage({ id }) {
  const [product, setProduct] = useState(null)

  useEffect(() => {
    fetch(`/api/products/${id}`)
      .then(r => r.json())
      .then(setProduct)
  }, [id])

  return product ? <ProductDetails product={product} /> : <Loading />
}

// After: Server Component with streaming
import { Suspense } from 'react'

async function ProductDetails({ id }: { id: string }) {
  const product = await fetch(`https://api.example.com/products/${id}`, {
    next: { revalidate: 3600 }
  }).then(r => r.json())

  return <ProductInfo product={product} />
}

export default function ProductPage({ params }: { params: { id: string } }) {
  return (
    <Suspense fallback={<ProductSkeleton />}>
      <ProductDetails id={params.id} />
    </Suspense>
  )
}
```

### Example 2: Python API Response Caching

```python
# Before: No caching
@app.get("/api/products")
async def get_products():
    products = await db.fetch_all("SELECT * FROM products")
    return products

# After: Redis caching with 5-minute TTL
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379)

@app.get("/api/products")
async def get_products():
    cache_key = "products:all"

    # Check cache
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    # Cache miss - query database
    products = await db.fetch_all("SELECT * FROM products")

    # Store in cache for 5 minutes
    redis_client.setex(cache_key, 300, json.dumps(products))

    return products
```

### Example 3: React Component Optimization

```typescript
// Before: Unnecessary re-renders
function UserDashboard({ users }) {
  return users.map(user => <UserCard user={user} />)
}

// After: Memoization + useTransition
import { useMemo, useTransition, useState } from 'react'

const UserCard = memo(function UserCard({ user }) {
  return <div>{user.name}</div>
})

function UserDashboard({ users }) {
  const [filter, setFilter] = useState('')
  const [isPending, startTransition] = useTransition()

  const filteredUsers = useMemo(() => {
    return users.filter(u => u.name.includes(filter))
  }, [users, filter])

  const handleFilterChange = (value: string) => {
    setFilter(value) // Urgent

    startTransition(() => {
      // Non-urgent filtering happens without blocking input
    })
  }

  return (
    <>
      <input value={filter} onChange={(e) => handleFilterChange(e.target.value)} />
      {isPending && <Spinner />}
      {filteredUsers.map(user => <UserCard key={user.id} user={user} />)}
    </>
  )
}
```

## Best Practices

1. **Measure First**: Always profile before optimizing
2. **Start with Quick Wins**: Image optimization, caching headers, static rendering
3. **Progressive Enhancement**: Optimize incrementally, validate improvements
4. **Monitor Continuously**: Set up Real User Monitoring (RUM) for ongoing tracking
5. **Set Performance Budgets**: Enforce bundle size and timing limits in CI/CD
6. **Use Plan Mode**: Let the agent plan complex optimizations before implementing

## Hooks

The plugin includes performance-related hooks:

- **pre-commit**: Warns when frontend files change, suggests bundle analysis
- **post-build**: Reminds to review bundle size after builds
- **performance-check**: Prompts Core Web Vitals verification before production deployments

## Version

1.0.0

## License

Copyright © 2024 Agentient Labs. All rights reserved.

## Support

For issues, questions, or contributions, contact Agentient Labs at contact@agentient.dev.
