# agentient-frontend-analytics

Privacy-compliant analytics integration for Next.js 14+ with Firebase/GA4, type-safe event tracking, and consent-first architecture.

**Confidence**: 99% | **Category**: Frontend | **Version**: 1.0.0

## Key Features

- **Consent-First Architecture**: All tracking gated by explicit user consent
- **Type-Safe Event Tracking**: Compile-time validation of event names and parameters
- **GA4 Best Practices**: Generic event names + specific parameters (500 event limit mitigation)
- **Privacy Compliance**: GDPR/CCPA ready with consent management integration
- **Next.js 14+ Optimized**: Client components, App Router, server-side safety

## Critical Patterns

### 1. Event Taxonomy Design (500 Event Limit)
GA4 has a hard limit of 500 unique event names. Use generic events with parameters:
- ❌ `click_header_logo`, `click_footer_logo` (2 events)
- ✅ `click_element` + `{location: 'header_logo'}` (1 event)

### 2. Type-Safe Event Map
```typescript
interface EventMap {
  purchase: { value: number; currency: string; items: Item[] };
  sign_up: { method: 'google' | 'email' };
  page_view: { page_title: string; page_location: string };
}

function trackEvent<K extends keyof EventMap>(
  name: K,
  params: EventMap[K]
): void
```

### 3. Consent-First Initialization
```typescript
// WRONG - initializes before consent
const analytics = getAnalytics(app);

// CORRECT - waits for consent
if (await hasConsent()) {
  const analytics = getAnalytics(app);
}
```

## Components

- **Agent**: analytics-engineer-agent
- **Commands**: /setup-analytics, /create-event, /track-conversion, /validate-analytics
- **Skills** (6): Firebase/GA4 initialization, taxonomy design, type-safe tracking, conversion tracking, privacy compliance, debugging/validation

## Dependencies

**Required**: agentient-security (consent management), agentient-frontend-foundation (TypeScript patterns)

---

**Generated with Claude Code** | Version 1.0.0
