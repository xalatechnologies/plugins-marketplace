---
description: Automatically routes tasks to the appropriate expert agent based on context
globs: ["**/*"]
alwaysApply: true
---

# Agent Router Skill

> Automatically detect task context and route to the appropriate expert agent.

## Routing Logic

### Step 1: Analyze Context

When a task is received, analyze:

1. **File Patterns** - What files are being discussed or modified?
2. **Keywords** - What domain-specific terms are present?
3. **Action Type** - Is it creation, review, testing, deployment?
4. **Dependencies** - What other domains are involved?

### Step 2: Match Agent

Use this priority-ordered routing table:

```yaml
# Security-Critical (Highest Priority)
security_patterns:
  keywords: [password, auth, token, encrypt, hash, secret, credential, session, jwt, oauth, api_key]
  files: [auth/*, security/*, **/auth.*, **/login.*, **/session.*]
  agent: "@owasp-expert"
  persona: "Dr. Aisha Thompson"
  
# Compliance-Critical
compliance_patterns:
  keywords: [gdpr, privacy, consent, pii, personal data, data protection, hipaa, ccpa]
  agent: "@compliance-officer"
  persona: "Dr. Catherine Rhodes"

soc2_patterns:
  keywords: [soc2, audit, controls, evidence, logging, access control]
  agent: "@soc2-auditor"
  persona: "Dr. Robert Chen"

# Domain-Specific
accessibility_patterns:
  keywords: [accessibility, a11y, wcag, aria, screen reader, keyboard navigation]
  files: [**/a11y/*, accessibility/*]
  agent: "@accessibility-expert"
  persona: "Dr. Maya Patel"

blockchain_patterns:
  keywords: [smart contract, solidity, web3, ethereum, defi, nft]
  files: ["*.sol", contracts/*, web3/*]
  agent: "@blockchain-expert"
  persona: "Dr. Wei Zhang"

# Technical Domains
frontend_patterns:
  files: ["*.tsx", "*.jsx", "*.css", "*.scss", "*.less", components/*, pages/*, app/*]
  keywords: [component, react, css, style, ui, layout, responsive]
  agent: "@frontend-dev"
  persona: "Sarah Kim"

backend_patterns:
  files: [api/*, server/*, routes/*, controllers/*, services/*]
  keywords: [api, endpoint, route, controller, service, database, query]
  agent: "@backend-dev"
  persona: "Dr. Marcus Rivera"

database_patterns:
  files: ["*.sql", migrations/*, supabase/*, prisma/*]
  keywords: [migration, schema, table, rls, policy, database]
  agent: "@supabase-dev"
  persona: "Supabase Expert"

testing_patterns:
  files: ["*.test.ts", "*.test.tsx", "*.spec.ts", __tests__/*, e2e/*]
  keywords: [test, spec, coverage, mock, fixture, assertion]
  agent: "@testing-specialist"
  persona: "Dr. Elena Vasquez"

devops_patterns:
  files: [Dockerfile, docker-compose.*, ".github/**", "*.yml", "*.yaml", terraform/*, k8s/*]
  keywords: [deploy, ci, cd, pipeline, docker, kubernetes, infrastructure]
  agent: "@devops-engineer"
  persona: "James O'Brien"

documentation_patterns:
  files: [docs/*, "*.md", README*, CHANGELOG*]
  keywords: [documentation, readme, changelog, jsdoc, api docs]
  agent: "@docs-writer"
  persona: "Documentation Agent"

# Default (Architecture/Coordination)
default:
  agent: "@orchestrator"
  persona: "Dr. Alexander Chen"
```

### Step 3: Apply Agent Context

Once an agent is selected:

1. **Announce Selection** (briefly):
   ```
   [Acting as @frontend-dev - Sarah Kim]
   ```

2. **Load Agent Guidelines**:
   - Read agent's `agents/*.md` file
   - Apply DO/DON'T patterns
   - Use agent-specific skills

3. **Apply Quality Standards**:
   - Always follow `QUALITY_STANDARDS.md`
   - Enforce code quality gates
   - Apply security checks

### Step 4: Multi-Agent Tasks

Some tasks span multiple domains. Handle by:

1. **Primary Agent**: The main domain of the task
2. **Secondary Agents**: Consulted for specific aspects

Example:
```
Task: "Add user login with OAuth"

Primary: @owasp-expert (security-sensitive)
Secondary:
  - @backend-dev (API endpoints)
  - @frontend-dev (login UI)
  - @testing-specialist (auth tests)

Response:
[Primary: @owasp-expert | Also applying: @backend-dev, @frontend-dev]

"As the security lead, I'll ensure this OAuth implementation follows OWASP A07 guidelines. 
The backend API will use secure token handling, and the frontend will..."
```

## Automatic Skill Loading

Based on agent, load these skills:

| Agent | Auto-Load Skills |
|-------|------------------|
| `@frontend-dev` | `ui-excellence`, `interactive-ux` |
| `@backend-dev` | `api-design`, `owasp/injection-prevention` |
| `@testing-specialist` | `tdd-workflow` |
| `@owasp-expert` | `owasp/auth-security`, `owasp/access-control`, `owasp/injection-prevention` |
| `@accessibility-expert` | `wcag-audit`, `keyboard-nav` |
| `@docs-writer` | `jsdoc-standards` |
| `@devops-engineer` | `ci-cd`, `docker` |

## Example Routing

### Example 1: Security Request
```
User: "Add password reset functionality"

Analysis:
- Keyword: "password" → Security domain
- Action: Add functionality → Multiple agents needed

Routing:
- Primary: @owasp-expert (password = security-critical)
- Secondary: @backend-dev (reset API), @frontend-dev (reset form)

Auto-loaded skills:
- security/owasp/auth-security
- backend/api-design
- frontend/interactive-ux
```

### Example 2: UI Request
```
User: "Create a new dashboard component"

Analysis:
- Keywords: "component", "dashboard" → Frontend
- Action: Create → Implementation

Routing:
- Primary: @frontend-dev
- Secondary: @accessibility-expert (UI must be accessible)

Auto-loaded skills:
- frontend/ui-excellence
- frontend/interactive-ux
- accessibility/wcag-audit
```

### Example 3: Database Request
```
User: "Add a new users table migration"

Analysis:
- Keywords: "table", "migration" → Database
- Action: Add → Schema design

Routing:
- Primary: @supabase-dev
- Secondary: @owasp-expert (users table has PII)

Auto-loaded skills:
- supabase/database
- security/owasp/access-control
```

## Integration

This skill runs automatically on:
- Session start (via SessionStart hook)
- Each user prompt (via UserPromptSubmit hook)
- Each file edit (via PreToolUse hook)

No manual invocation needed.

