# Optimize Bundle

Analyze and optimize JavaScript bundle size and loading performance for Next.js applications.

## Usage

```bash
/optimize-bundle [strategy]
```

**Parameters:**
- `strategy` (optional): Optimization focus - `size`, `loading`, `splitting`, or omit for comprehensive optimization

## What This Command Does

This command performs bundle optimization analysis and implementation:

1. **Bundle Analysis**:
   - Identify large dependencies and duplicates
   - Analyze code splitting effectiveness
   - Detect unused or redundant code
   - Measure bundle sizes (initial, route-based, shared chunks)
   - Evaluate tree-shaking effectiveness

2. **Optimization Strategies**:
   - **Size**: Minimize total bundle size through dependency optimization
   - **Loading**: Optimize loading strategy (preload, prefetch, lazy loading)
   - **Splitting**: Improve code splitting and chunk organization

3. **Implementation**:
   - Configure webpack/Next.js optimizations
   - Implement dynamic imports
   - Optimize third-party library usage
   - Set up bundle analysis in CI/CD

## Performance Engineer Agent

This command activates the **performance-engineer** agent, which will:

- Generate bundle analysis reports
- Identify optimization opportunities
- Implement code splitting improvements
- Configure build optimizations
- Set up performance budgets

## Expected Output

The agent will provide:

1. **Bundle Analysis Report**: Current bundle composition and sizes
2. **Optimization Opportunities**: Specific improvements ranked by impact
3. **Implementation Plan**: Step-by-step optimization strategy
4. **Performance Budgets**: Recommended size limits for bundles
5. **Validation**: Before/after metrics demonstrating improvements

## Examples

```bash
# Comprehensive bundle optimization
/optimize-bundle

# Focus on reducing bundle size
/optimize-bundle size

# Optimize loading performance
/optimize-bundle loading

# Improve code splitting strategy
/optimize-bundle splitting
```

## Prerequisites

- Next.js application with webpack-bundle-analyzer or similar tool
- Access to build configuration (next.config.js)
- Package.json access for dependency analysis

## Notes

- The agent will analyze current bundle composition before optimizing
- Operates in Plan Mode for structural changes
- Follows Next.js 14+ best practices for App Router
- Sets performance budgets to prevent regression
- All optimizations are tested and validated
