---
description: Generate a prioritized task backlog to make the project production-ready
arguments:
  - name: target
    description: Target milestone (mvp, beta, production, enterprise)
    required: false
    default: production
---

# Production Tasks Command

Analyze the codebase and generate a prioritized task backlog for production readiness.

## Analysis Process

### 1. Identify Gaps
Based on target milestone, identify missing:
- Security measures
- Error handling
- Testing coverage
- Documentation
- Performance optimizations
- Compliance requirements

### 2. Prioritize by Impact
Categorize tasks:
- **Critical Path**: Must complete before launch
- **Recommended**: Should complete for quality
- **Backlog**: Can complete after launch

### 3. Estimate Effort
For each task:
- Time estimate (hours)
- Complexity (trivial/small/medium/large)
- Auto-fixable (yes/no)
- Dependencies (what must be done first)

### 4. Group into Phases
Organize tasks into logical phases:
- Security Hardening
- Error Handling
- Testing
- Performance
- Documentation
- Polish

## Output Format

```markdown
📋 PRODUCTION READINESS TASKS
═══════════════════════════════════════════════════════════════

Target: [MVP / Beta / Production / Enterprise]
Current Readiness: [X]%
Target Readiness: 95%

🚨 CRITICAL PATH (Must complete)
───────────────────────────────────────────────────────────────

## Phase 1: Security Hardening (Est: [X] hours)

| ID | Task | Priority | Effort | Auto-fix |
|----|------|----------|--------|----------|
| SEC-001 | Remove hardcoded API keys | Critical | 30m | ✅ |
| SEC-002 | Add CSRF protection | Critical | 2h | ⚠️ Partial |
| SEC-003 | Implement rate limiting | High | 3h | ❌ |

### SEC-001: Remove hardcoded API keys
- **Location**: src/lib/ai/openai.ts:15
- **Current**: `const API_KEY = "sk-proj-..."`
- **Fix**: Move to environment variable `OPENAI_API_KEY`
- **Commands**:
  ```bash
  # Add to .env
  echo "OPENAI_API_KEY=" >> .env.example
  ```

## Phase 2: Error Handling (Est: [X] hours)
[Similar format...]

## Phase 3: Testing (Est: [X] hours)
[Similar format...]

✅ RECOMMENDED (Should complete)
───────────────────────────────────────────────────────────────
[Similar format for recommended tasks...]

📋 BACKLOG (Can complete later)
───────────────────────────────────────────────────────────────
[Summarized list of lower priority items...]

═══════════════════════════════════════════════════════════════
SUMMARY

Critical Path Total:    [X] hours ([N] tasks)
Recommended Total:      [X] hours ([N] tasks)
Backlog Total:          [X] hours ([N] tasks)

Quick Wins (< 1 hour):  [N] tasks
Auto-fixable:           [N] tasks ([X]%)

Timeline Estimate:
- MVP:        [X] days with 1 developer
- Beta:       [X] days with 1 developer
- Production: [X] days with 1 developer

NEXT RECOMMENDED ACTION:
[Specific first step to take]
```

## Task ID Prefixes

- SEC-XXX: Security
- REL-XXX: Reliability
- PERF-XXX: Performance
- TEST-XXX: Testing
- DOC-XXX: Documentation
- COMP-XXX: Compliance
- UX-XXX: User Experience

## Guidelines

- Generate actionable, specific tasks
- Include concrete code examples for fixes
- Order by dependency (what must be done first)
- Identify quick wins (high impact, low effort)
- Group related tasks to minimize context switching
- Provide realistic time estimates

