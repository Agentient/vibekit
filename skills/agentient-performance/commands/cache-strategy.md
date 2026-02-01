# Cache Strategy

Design and implement multi-layer caching strategies for optimal application performance.

## Usage

```bash
/cache-strategy [layer]
```

**Parameters:**
- `layer` (optional): Specific caching layer - `browser`, `cdn`, `server`, `database`, or omit for comprehensive strategy

## What This Command Does

This command designs and implements caching strategies across multiple layers:

1. **Browser Caching**:
   - HTTP caching headers (Cache-Control, ETag, Last-Modified)
   - Service Worker caching strategies
   - LocalStorage/SessionStorage optimization
   - IndexedDB for large datasets

2. **CDN Caching**:
   - Static asset caching configuration
   - Cache invalidation strategies
   - Regional distribution optimization
   - Purge and revalidation policies

3. **Server Caching**:
   - Next.js ISR (Incremental Static Regeneration)
   - React cache() and server-side memoization
   - In-memory caching (Redis)
   - API response caching

4. **Database Caching**:
   - Query result caching
   - Connection pooling
   - Prepared statement caching
   - Read replica strategies

## Performance Engineer Agent

This command activates the **performance-engineer** agent, which will:

- Analyze current caching implementation
- Design multi-layer caching strategy
- Implement cache invalidation policies
- Configure cache headers and TTLs
- Set up monitoring for cache effectiveness

## Expected Output

The agent will provide:

1. **Current Caching Analysis**: Existing cache usage and effectiveness
2. **Caching Strategy Design**: Multi-layer approach with rationale
3. **Implementation Plan**: Step-by-step configuration and code changes
4. **Invalidation Strategy**: Cache freshness and purge policies
5. **Monitoring Setup**: Metrics to track cache hit rates and performance

## Examples

```bash
# Comprehensive caching strategy
/cache-strategy

# Focus on browser caching
/cache-strategy browser

# Optimize CDN caching
/cache-strategy cdn

# Implement server-side caching
/cache-strategy server

# Database query caching
/cache-strategy database
```

## Prerequisites

- Understanding of application data freshness requirements
- Access to caching infrastructure (Redis, CDN configuration)
- Next.js application with App Router (for RSC caching)

## Notes

- The agent considers data freshness requirements and cache invalidation
- Operates in Plan Mode for architectural caching changes
- Implements stale-while-revalidate patterns where appropriate
- Monitors cache hit rates to validate effectiveness
- Follows Next.js 14+ caching best practices (React cache, unstable_cache)
- All strategies balance performance with data freshness
