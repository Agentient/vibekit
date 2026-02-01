# Analyze Performance

Analyze application performance metrics and identify optimization opportunities across frontend and backend systems.

## Usage

```bash
/analyze-performance [target]
```

**Parameters:**
- `target` (optional): Specific area to analyze - `frontend`, `backend`, `full-stack`, or omit for comprehensive analysis

## What This Command Does

This command performs a comprehensive performance analysis:

1. **Frontend Analysis**:
   - Core Web Vitals assessment (LCP, FID, CLS)
   - JavaScript bundle size analysis
   - Network waterfall analysis
   - Render performance evaluation
   - Resource loading optimization opportunities

2. **Backend Analysis**:
   - API response time profiling
   - Database query performance
   - Server-side rendering performance
   - Function execution time analysis
   - Memory usage patterns

3. **Full-Stack Analysis**:
   - End-to-end request flow analysis
   - Cache hit rates and effectiveness
   - Third-party service latency
   - Overall user experience metrics

## Performance Engineer Agent

This command activates the **performance-engineer** agent, which will:

- Conduct baseline performance measurements
- Identify performance bottlenecks and anti-patterns
- Prioritize optimization opportunities by impact
- Generate actionable recommendations
- Propose an optimization implementation plan

## Expected Output

The agent will provide:

1. **Current Performance Metrics**: Baseline measurements across key indicators
2. **Bottleneck Analysis**: Identified issues ranked by severity
3. **Optimization Recommendations**: Specific improvements with expected impact
4. **Implementation Plan**: Prioritized steps to achieve performance goals
5. **Success Criteria**: Target metrics to validate improvements

## Examples

```bash
# Comprehensive performance analysis
/analyze-performance

# Frontend-specific analysis
/analyze-performance frontend

# Backend-specific analysis
/analyze-performance backend

# Full-stack analysis
/analyze-performance full-stack
```

## Prerequisites

- Application must be running or accessible for profiling
- For frontend: Browser DevTools access or Lighthouse CLI
- For backend: Monitoring tools or profiling capabilities enabled

## Notes

- The agent will measure first before recommending optimizations
- Analysis results provide data-driven prioritization of improvements
- The agent operates in Plan Mode for subsequent optimization work
- All recommendations follow industry best practices and Core Web Vitals guidelines
