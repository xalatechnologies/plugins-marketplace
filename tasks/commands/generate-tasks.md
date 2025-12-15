---
description: Automatically generate tasks from code analysis, PRD, or work context
arguments:
  - name: source
    description: Source for task generation (code, prd, diff, issue)
    required: true
  - name: target
    description: Target file, PR, or issue reference
    required: false
---

# Generate Tasks Command

Automatically create tasks based on various sources.

## Sources

### From Code Analysis (`/generate-tasks code`)

Analyze the codebase and generate tasks for improvements.

```
/generate-tasks code
/generate-tasks code focus=security
/generate-tasks code path=src/api
```

**Process:**
1. Run `/analyze` or `/pitfalls` on codebase
2. Convert issues to actionable tasks
3. Estimate effort for each
4. Assign appropriate roles
5. Create tasks in Xala PM

**Output:**
```
🔍 TASK GENERATION FROM CODE ANALYSIS
═══════════════════════════════════════════════════════════════

Analyzed: 156 files
Issues found: 23
Tasks generated: 15 (grouped similar issues)

GENERATED TASKS
──────────────────────────────────────────────────────────────

🔴 Critical (2)
┌─────────────────────────────────────────────────────────────┐
│ NEW: Remove hardcoded API keys                              │
├─────────────────────────────────────────────────────────────┤
│ Role: backend | Est: 1h | Phase: 2                          │
│ Files: src/lib/ai/openai.ts:15, src/services/stripe.ts:8    │
│ Description: Move API keys to environment variables         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ NEW: Add input validation to user endpoints                 │
├─────────────────────────────────────────────────────────────┤
│ Role: backend | Est: 4h | Phase: 2                          │
│ Files: src/app/api/v1/users/route.ts (5 endpoints)          │
│ Description: Add Zod validation to all user API endpoints   │
└─────────────────────────────────────────────────────────────┘

🟠 High (5)
[... more tasks ...]

──────────────────────────────────────────────────────────────
Create these 15 tasks in Xala PM? (y/n/select)
```

### From Git Diff (`/generate-tasks diff`)

Generate tasks from code changes in a PR or branch.

```
/generate-tasks diff
/generate-tasks diff branch=feature/auth
/generate-tasks diff pr=123
```

**Process:**
1. Get diff from branch or PR
2. Analyze changes for:
   - Missing tests
   - Documentation needs
   - Follow-up refactoring
   - Performance concerns
3. Generate follow-up tasks

**Output:**
```
🔀 TASK GENERATION FROM DIFF
═══════════════════════════════════════════════════════════════

Branch: feature/oauth-integration
Files changed: 12
Lines: +456 / -89

FOLLOW-UP TASKS NEEDED
──────────────────────────────────────────────────────────────

📝 Documentation
├── NEW: Document OAuth flow in README
│   Role: frontend | Est: 1h
│   Reason: New feature needs user documentation

🧪 Testing
├── NEW: Add E2E tests for OAuth login
│   Role: frontend | Est: 3h
│   Reason: No E2E tests for new auth flows
│
└── NEW: Add unit tests for token refresh
    Role: backend | Est: 2h
    Reason: Token refresh logic untested

🔧 Tech Debt
└── NEW: Refactor auth middleware for clarity
    Role: backend | Est: 2h
    Reason: auth.server.ts now 280 lines, should split

──────────────────────────────────────────────────────────────
Create these 4 tasks? (y/n)
```

### From Issue/Bug Report (`/generate-tasks issue`)

Break down an issue into implementation tasks.

```
/generate-tasks issue "Users can't reset password on mobile"
/generate-tasks issue github=#456
```

**Process:**
1. Analyze issue description
2. Identify affected components
3. Break into sub-tasks
4. Estimate each task
5. Create linked tasks

**Output:**
```
🐛 TASK GENERATION FROM ISSUE
═══════════════════════════════════════════════════════════════

Issue: Users can't reset password on mobile
Source: Bug report

ANALYSIS
──────────────────────────────────────────────────────────────
Likely causes:
1. Responsive layout issue on reset form
2. Email link not mobile-friendly
3. Touch target sizes too small

GENERATED TASKS
──────────────────────────────────────────────────────────────

Parent: t4-1 "Fix mobile password reset"
│
├── t4-1a: Investigate password reset on mobile [1h]
│   Role: frontend | Priority: high
│   Description: Reproduce and identify root cause
│
├── t4-1b: Fix responsive layout on reset form [2h]
│   Role: frontend | Priority: high
│   Depends on: t4-1a
│
├── t4-1c: Test password reset on iOS and Android [1h]
│   Role: frontend | Priority: high
│   Depends on: t4-1b
│
└── t4-1d: Add mobile E2E test for password reset [2h]
    Role: frontend | Priority: medium
    Depends on: t4-1c

Total estimate: 6h

──────────────────────────────────────────────────────────────
Create these linked tasks? (y/n)
```

### From PRD (`/generate-tasks prd`)

Generate implementation tasks from a PRD or feature spec.

```
/generate-tasks prd path=docs/PRD.md
/generate-tasks prd feature="User Notifications"
```

**Process:**
1. Parse PRD/feature spec
2. Extract user stories
3. Break into technical tasks
4. Assign roles and phases
5. Create task hierarchy

## Guidelines

1. **Review before creating** - Always confirm generated tasks
2. **Estimate conservatively** - Add buffer for unknowns
3. **Link related tasks** - Set dependencies and parents
4. **Assign to phases** - Keep work organized
5. **Log generation** - Activity log shows task origins

