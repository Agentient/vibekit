# Profile Code

Profile application code to identify performance bottlenecks in frontend and backend systems.

## Usage

```bash
/profile-code [target] [scope]
```

**Parameters:**
- `target` (optional): Code area to profile - `frontend`, `backend`, or omit for full-stack profiling
- `scope` (optional): Specific file/function/component to profile

## What This Command Does

This command performs deep code profiling to identify performance bottlenecks:

1. **Frontend Profiling**:
   - React component render performance (React DevTools Profiler)
   - JavaScript execution time (Chrome DevTools Performance)
   - Layout thrashing and reflow detection
   - Memory leaks and retention analysis
   - Event handler performance

2. **Backend Profiling**:
   - Python function execution time (cProfile, py-spy)
   - CPU usage patterns
   - Memory allocation and garbage collection
   - I/O bottlenecks
   - Database query performance
   - API endpoint response times

3. **Full-Stack Profiling**:
   - End-to-end request tracing
   - Server-side rendering performance
   - Data fetching and serialization overhead
   - Network latency and payload size

## Performance Engineer Agent

This command activates the **performance-engineer** agent, which will:

- Set up appropriate profiling tools
- Execute profiling sessions
- Analyze profiling data to identify bottlenecks
- Recommend specific code optimizations
- Implement performance improvements

## Expected Output

The agent will provide:

1. **Profiling Report**: Detailed analysis of execution time and resource usage
2. **Bottleneck Identification**: Functions/components causing performance issues
3. **Root Cause Analysis**: Why the bottleneck exists
4. **Optimization Recommendations**: Specific code improvements
5. **Implementation**: Optimized code with before/after metrics

## Examples

```bash
# Profile entire application
/profile-code

# Profile frontend React components
/profile-code frontend

# Profile backend Python code
/profile-code backend

# Profile specific component
/profile-code frontend src/components/ProductList.tsx

# Profile specific API endpoint
/profile-code backend src/api/users.py
```

## Prerequisites

- **Frontend**: Browser DevTools or React DevTools Profiler
- **Backend**: Python profiling tools (cProfile, py-spy, memory_profiler)
- Application running in development or profiling mode
- Representative workload or test scenario

## Notes

- The agent profiles under realistic load conditions
- Identifies both CPU and memory performance issues
- Operates in Plan Mode for optimization implementation
- Validates improvements with comparative profiling
- Follows language-specific performance best practices
- All optimizations maintain code correctness and readability
