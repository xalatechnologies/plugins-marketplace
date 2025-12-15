---
description: Comprehensive PR review using multiple specialized agents
arguments:
  - name: pr
    description: PR number or branch name
    required: false
  - name: focus
    description: Focus areas (all, security, performance, a11y)
    required: false
    default: all
---

# Review PR Command

Orchestrate a comprehensive PR review using specialized agents.

## Review Workflow

```
                    ┌────────────────┐
                    │   PR CHANGES   │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  ORCHESTRATOR  │
                    │  Analyze Diff  │
                    └───────┬────────┘
                            │
    ┌───────────────────────┼───────────────────────┐
    │                       │                       │
    ▼                       ▼                       ▼
┌────────────┐      ┌────────────┐      ┌────────────┐
│ Code Style │      │  Security  │      │   Tests    │
│   Agent    │      │   Agent    │      │   Agent    │
└────────────┘      └────────────┘      └────────────┘
    │                       │                       │
    ▼                       ▼                       ▼
┌────────────┐      ┌────────────┐      ┌────────────┐
│Performance │      │   A11y     │      │  Docs      │
│   Agent    │      │   Agent    │      │   Agent    │
└────────────┘      └────────────┘      └────────────┘
    │                       │                       │
    └───────────────────────┼───────────────────────┘
                            │
                    ┌───────▼────────┐
                    │ UNIFIED REVIEW │
                    │    REPORT      │
                    └────────────────┘
```

## Agent Dispatch Logic

```typescript
function selectReviewAgents(changedFiles: string[]): Agent[] {
  const agents: Agent[] = ['code-review'] // Always
  
  // Frontend changes
  if (changedFiles.some(f => /\.(tsx?|jsx?)$/.test(f) && f.includes('components'))) {
    agents.push('frontend', 'react', 'accessibility')
  }
  
  // Backend changes
  if (changedFiles.some(f => f.includes('/api/') || f.includes('/server/'))) {
    agents.push('backend')
  }
  
  // Database changes
  if (changedFiles.some(f => f.includes('supabase') || f.includes('.sql'))) {
    agents.push('supabase')
  }
  
  // Smart contract changes
  if (changedFiles.some(f => /\.sol$/.test(f))) {
    agents.push('blockchain')
  }
  
  // Test changes or missing tests
  agents.push('testing')
  
  // Always check security
  agents.push('testing') // Security skill
  
  return agents
}
```

## Review Categories

### 1. Code Quality
- Naming conventions
- File size limits
- DRY violations
- SOLID principles
- Code comments

### 2. Security
- Input validation
- SQL injection
- XSS vulnerabilities
- Authentication/authorization
- Secrets in code

### 3. Performance
- N+1 queries
- Bundle size impact
- Unnecessary re-renders
- Memory leaks
- Caching opportunities

### 4. Testing
- Test coverage for changes
- Edge cases covered
- Integration tests needed
- E2E test updates

### 5. Accessibility
- ARIA attributes
- Keyboard navigation
- Color contrast
- Screen reader compatibility

### 6. Documentation
- README updates needed
- JSDoc comments
- API documentation
- Changelog entry

## Output Format

```
📋 PR REVIEW: feature/user-notifications (#142)
═══════════════════════════════════════════════════════════════

Branch: feature/user-notifications → main
Author: @developer
Files Changed: 24 (+1,245 / -356)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REVIEW STATUS: 🟡 NEEDS CHANGES

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
───────────────────────────────────────────────────────────────

Overall this PR implements user notifications well, but there
are security concerns with the notification dispatch and
missing accessibility attributes on the notification badges.

Agents deployed: code-review, frontend, backend, testing, a11y

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 BLOCKING ISSUES (Must Fix)
───────────────────────────────────────────────────────────────

[SECURITY] Missing rate limiting on notification send
📍 src/app/api/notifications/send/route.ts:23
💡 Add rate limiting middleware to prevent spam abuse

```typescript
// Current
export async function POST(request: Request) {
  const { userId, message } = await request.json()
  await sendNotification(userId, message)
}

// Suggested
export async function POST(request: Request) {
  const { userId, message } = await request.json()
  await rateLimiter.check(request, { max: 10, window: '1m' })
  await sendNotification(userId, message)
}
```

[SECURITY] No input validation on notification message
📍 src/app/api/notifications/send/route.ts:24
💡 Validate and sanitize message content

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟠 SHOULD FIX
───────────────────────────────────────────────────────────────

[A11Y] NotificationBadge missing aria-label
📍 src/components/NotificationBadge.tsx:15
💡 Add aria-label for screen reader users

```tsx
// Current
<span className="badge">{count}</span>

// Suggested
<span className="badge" aria-label={`${count} unread notifications`}>
  {count}
</span>
```

[TESTING] No tests for notification sending
📍 Missing: tests/api/notifications.test.ts
💡 Add unit tests for the notification API

[PERFORMANCE] NotificationList re-renders on every poll
📍 src/components/NotificationList.tsx:42
💡 Use React.memo or useMemo for list items

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 SUGGESTIONS
───────────────────────────────────────────────────────────────

[STYLE] Consider extracting notification types to separate file
[DOCS] Update API documentation with new endpoints
[REFACTOR] NotificationService.ts is 280 lines - consider splitting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ WHAT'S GOOD
───────────────────────────────────────────────────────────────

• Clean component structure
• Good use of TypeScript types
• Proper error handling in hooks
• WebSocket implementation is solid
• Good separation of concerns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHECKLIST
───────────────────────────────────────────────────────────────
☐ Fix rate limiting (blocking)
☐ Add input validation (blocking)
☐ Add aria-label to badge
☐ Add notification API tests
☐ Memoize NotificationList items
☐ Update API documentation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create tasks in Xala PM for these issues? (y/n)
```

## Usage

```bash
# Review current branch changes
/review-pr

# Review specific PR
/review-pr pr=142

# Focus on security only
/review-pr focus=security

# Full review
/review-pr focus=all
```

