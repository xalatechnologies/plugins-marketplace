---
description: Delegate a task to a specific agent with full context
args:
  agent: The agent handle (e.g., @backend-dev, @owasp-expert)
  task: The task description or instruction
  spec: Optional spec ID for context (e.g., SPEC-2024-001)
  priority: Optional priority (low, medium, high, critical)
---

# Delegate Command

Route a task to a specific specialized agent with proper context and tracking.

## Agent Handles

| Handle | Name | Plugin | Specialty |
|--------|------|--------|-----------|
| `@orchestrator` | Dr. Alexander Chen | `orchestrator` | Coordination, architecture decisions |
| `@frontend-dev` | Sarah Kim | `frontend` | React, UI components, accessibility |
| `@backend-dev` | Dr. Marcus Rivera | `backend` | APIs, databases, server logic |
| `@supabase-dev` | Supabase Expert | `supabase` | Postgres, RLS, Edge Functions |
| `@testing-specialist` | Dr. Elena Vasquez | `testing` | E2E, unit, integration, performance |
| `@owasp-expert` | Dr. Aisha Thompson | `security` | OWASP Top 10, secure coding |
| `@soc2-auditor` | Dr. Robert Chen | `security` | SOC2 compliance, audit prep |
| `@cybersecurity-architect` | Dr. Sarah Martinez | `security` | NIST, CIS, Zero Trust architecture |
| `@opensource-standards` | Dr. Michael Foster | `security` | OpenSSF, SBOM, license compliance |
| `@blockchain-expert` | Dr. Wei Zhang | `blockchain` | Smart contracts, DeFi security |
| `@accessibility-expert` | Dr. Maya Patel | `accessibility` | WCAG, Universal Design, a11y |
| `@compliance-officer` | Dr. Catherine Rhodes | `compliance` | GDPR, HIPAA, regulatory |
| `@devops-engineer` | James O'Brien | `devops` | CI/CD, Docker, Kubernetes |
| `@code-reviewer` | Code Review Agent | `code-review` | PR review, refactoring |
| `@docs-writer` | Documentation Agent | `documentation` | API docs, README, guides |
| `@design-dev` | Design System Agent | `design-system` | Components, design tokens |
| `@react-dev` | React Expert | `react` | Hooks, state management |
| `@mobile-dev` | Mobile Expert | `mobile` | Expo, React Native |
| `@desktop-dev` | Desktop Expert | `tauri` | Tauri, Rust, native |
| `@task-manager` | Task Manager Agent | `tasks` | Xala PM integration |

## Usage

```bash
# Delegate to specific agent
/delegate @backend-dev "Create REST API for user authentication"

# Delegate with spec context
/delegate @frontend-dev "Build login form component" --spec SPEC-2024-001

# Delegate with priority
/delegate @owasp-expert "Security review of payment module" --priority critical

# Delegate with full context
/delegate @testing-specialist "Write E2E tests for checkout flow" --spec SPEC-2024-003 --priority high
```

## Process

### Step 1: Validate Agent

1. Parse the agent handle from the command
2. Verify agent exists in the registry
3. Load agent's persona and skills

### Step 2: Build Context

1. Load the referenced spec (if provided)
2. Gather relevant project context
3. Include agent-specific standards and best practices

### Step 3: Execute Delegation

1. Switch to the target agent's persona
2. Provide full task context
3. Apply agent's operational guidelines (DO/DON'T)

### Step 4: Track in Xala PM

1. Create or update task in Xala PM
2. Log agent assignment
3. Track start time

## Output Format

```markdown
## 🎯 Task Delegated

**Agent:** @backend-dev (Dr. Marcus Rivera)
**Plugin:** backend
**Task:** Create REST API for user authentication

### Context Loaded
- Spec: SPEC-2024-001 (User Authentication)
- Relevant ACs: AC-1, AC-2, AC-3

### Agent Activated

> I am Dr. Marcus Rivera, Backend Systems Architect. I will implement 
> the authentication API following the spec requirements and my 
> operational guidelines for secure API development.

### Xala PM Tracking
- Task: PM-12345
- Status: In Progress
- Assigned: @backend-dev
```

## Examples

### Backend API Task

```
/delegate @backend-dev "Implement user registration endpoint with email verification"

🎯 Delegating to @backend-dev (Dr. Marcus Rivera)...

Agent Response:
I'll implement the registration endpoint following these principles:

✅ DO:
- Use parameterized queries for database operations
- Validate all input with Zod schema
- Hash passwords with bcrypt (cost 12)
- Return consistent error responses

❌ DON'T:
- Store passwords in plain text
- Expose internal error details
- Skip rate limiting

Implementation:
[Agent proceeds with implementation]
```

### Security Review Task

```
/delegate @owasp-expert "Review the payment module for OWASP vulnerabilities" --priority critical

🎯 Delegating to @owasp-expert (Dr. Aisha Thompson)...

Agent Response:
I'll conduct an OWASP Top 10 security review:

Checking:
- A01: Broken Access Control
- A02: Cryptographic Failures
- A03: Injection
- A07: Authentication Failures

[Agent proceeds with security review]
```

## Integration with Spec

When a spec ID is provided, the agent receives:

1. **Summary** - What the feature does
2. **Acceptance Criteria** - What must be achieved
3. **Task Context** - Which specific task from the implementation plan
4. **Best Practices** - Required standards for this feature
5. **Tests Required** - What tests the agent must write/verify

## Xala PM Integration

All delegations are tracked:

```typescript
// Automatic logging to Xala PM
await xalaPM.logActivity({
  type: 'delegation',
  agent: '@backend-dev',
  task: 'Create REST API for user authentication',
  spec: 'SPEC-2024-001',
  status: 'started',
  timestamp: new Date(),
});
```
