---
description: Code review expertise
triggers:
  - reviewing code
  - pr review
  - code quality
  - refactoring
---

# Code Review Skill

## Quick Patterns

### Identify Issues

```typescript
// 🔴 Security: SQL injection
const query = `SELECT * FROM users WHERE id = ${userId}`
// Fix: Use parameterized queries

// 🔴 Bug: Race condition
const [count, setCount] = useState(0)
const increment = () => setCount(count + 1) // Stale closure
// Fix: setCount(c => c + 1)

// 🟠 Quality: Magic number
if (retries > 3) { }
// Fix: const MAX_RETRIES = 3

// 🟠 Performance: N+1 query
for (const user of users) {
  const profile = await getProfile(user.id) // N queries!
}
// Fix: Batch query or join

// 🟡 Style: Inconsistent naming
const userData = {}
const profileInfo = {}
// Fix: Be consistent (data or info, not both)
```

### Suggest Refactoring

```typescript
// Before: Long function
function processOrder(order) {
  // validation (20 lines)
  // calculation (30 lines)
  // notification (15 lines)
}

// After: Single responsibility
function processOrder(order) {
  validateOrder(order)
  const total = calculateTotal(order)
  notifyCustomer(order, total)
}
```

### Review Comments

```typescript
// 🔴 BLOCKING
// This will cause a memory leak. The event listener is added
// on every render but never removed.
useEffect(() => {
  window.addEventListener('resize', handleResize)
}) // Missing cleanup!

// Suggested fix:
useEffect(() => {
  window.addEventListener('resize', handleResize)
  return () => window.removeEventListener('resize', handleResize)
}, [])


// 🟠 SHOULD FIX
// Consider extracting this validation logic to a Zod schema.
// It would be more maintainable and provide better type inference.
if (!email || !email.includes('@') || email.length < 5) {
  // ...
}


// 🟡 SUGGESTION
// Nice work on the error handling! One minor suggestion:
// consider adding the error code to help with debugging.
throw new Error('User not found')
// → throw new NotFoundError('User not found', { code: 'USER_404' })


// ✅ PRAISE
// Love the use of early returns here - makes the logic
// much easier to follow than nested if statements!
```

## PR Review Template

```markdown
## Summary
Brief overview of what this PR does.

## Review

### 🔴 Blocking Issues
1. [Issue description with line reference]

### 🟠 Should Fix
1. [Issue description]

### 🟡 Suggestions
1. [Optional improvement]

### ✅ What's Good
- [Positive observation]

## Verdict
- [ ] Approve
- [x] Request changes
- [ ] Comment only
```

## When to Use

Apply when:
- Reviewing PRs or code changes
- Analyzing code quality
- Suggesting refactoring
- Checking for common issues

