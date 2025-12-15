---
description: Invoke a specific skill for focused action
args:
  skill: The skill path (e.g., security/owasp/injection-prevention)
  target: Optional target file or path
---

# Skill Command

Invoke a specific skill for focused, specialized action.

## Skill Registry

### Security Skills (`security/`)

| Skill | Description | Use For |
|-------|-------------|---------|
| `security/owasp/injection-prevention` | SQL, command, LDAP injection | Database queries, user input |
| `security/owasp/auth-security` | Authentication patterns | Login, session, MFA |
| `security/owasp/access-control` | Authorization, RBAC | Permission checks |
| `security/soc2/audit-logging` | Audit trail implementation | Sensitive actions |
| `security/soc2/encryption` | Data encryption | Sensitive data storage |
| `security/nist/threat-modeling` | STRIDE threat analysis | Architecture review |
| `security/oss/sbom` | Software bill of materials | Dependency analysis |
| `security/oss/license-check` | License compliance | OSS usage |

### Frontend Skills (`frontend/`)

| Skill | Description | Use For |
|-------|-------------|---------|
| `frontend/react-components` | React component patterns | New components |
| `frontend/state-management` | State patterns | Complex state |
| `frontend/performance` | Performance optimization | Slow renders |
| `frontend/forms` | Form handling | User input |

### Backend Skills (`backend/`)

| Skill | Description | Use For |
|-------|-------------|---------|
| `backend/api-design` | REST/GraphQL patterns | New endpoints |
| `backend/validation` | Input validation | Request handling |
| `backend/error-handling` | Error patterns | Exception flow |
| `backend/database` | Query optimization | DB operations |

### Testing Skills (`testing/`)

| Skill | Description | Use For |
|-------|-------------|---------|
| `testing/unit` | Unit test patterns | Function testing |
| `testing/integration` | Integration patterns | Service testing |
| `testing/e2e` | E2E test patterns | User flow testing |
| `testing/performance` | Performance testing | Load testing |

### Accessibility Skills (`accessibility/`)

| Skill | Description | Use For |
|-------|-------------|---------|
| `accessibility/wcag-audit` | WCAG 2.1 AA check | UI audit |
| `accessibility/keyboard-nav` | Keyboard navigation | Focus management |
| `accessibility/screen-reader` | Screen reader compat | ARIA patterns |

### DevOps Skills (`devops/`)

| Skill | Description | Use For |
|-------|-------------|---------|
| `devops/ci-cd` | Pipeline patterns | Automation |
| `devops/docker` | Container patterns | Containerization |
| `devops/kubernetes` | K8s patterns | Orchestration |
| `devops/infrastructure` | IaC patterns | Cloud setup |

## Usage

```bash
# Invoke skill on current context
/skill security/owasp/injection-prevention

# Invoke skill on specific file
/skill security/owasp/auth-security --target src/auth/login.ts

# Invoke skill on directory
/skill accessibility/wcag-audit --target src/components/

# Chain skills
/skill backend/api-design
/skill security/owasp/injection-prevention
/skill testing/integration
```

## Process

### Step 1: Load Skill

1. Parse skill path
2. Load skill definition from plugin
3. Load associated agent persona

### Step 2: Apply to Target

1. If target specified, read file/directory
2. Apply skill patterns and checks
3. Generate recommendations or code

### Step 3: Report

Output findings with:
- Issues found
- Recommendations
- Code examples
- Verification commands

## Output Format

```markdown
## 🎯 Skill: {skill-path}

**Agent:** @{agent-handle}
**Target:** {target or "current context"}

### Analysis

| Check | Status | Details |
|-------|--------|---------|
| {Check 1} | ✅/❌ | {Details} |
| {Check 2} | ✅/❌ | {Details} |

### Findings

#### Issue 1: {Title}
**Severity:** High
**Location:** {file:line}
**Current:**
```{language}
// problematic code
```

**Recommended:**
```{language}
// fixed code
```

### Actions Taken

- [x] {Action 1}
- [ ] {Action 2 - requires manual review}

### Verification

```bash
{command to verify fix}
```
```

## Examples

### Security Skill

```
/skill security/owasp/injection-prevention --target src/db/users.ts

🎯 Skill: security/owasp/injection-prevention
Agent: @owasp-expert (Dr. Aisha Thompson)
Target: src/db/users.ts

### Analysis

| Check | Status |
|-------|--------|
| Parameterized queries | ❌ Found issues |
| Input validation | ✅ Present |
| ORM usage | ✅ Safe patterns |

### Findings

#### SQL Injection Risk (Line 45)

**Current:**
```typescript
const user = await db.raw(`SELECT * FROM users WHERE id = ${id}`);
```

**Recommended:**
```typescript
const user = await db.user.findUnique({ where: { id } });
```

### Verification
```bash
npm run lint && npm test -- --grep "users"
```
```

### Accessibility Skill

```
/skill accessibility/wcag-audit --target src/components/Button.tsx

🎯 Skill: accessibility/wcag-audit
Agent: @accessibility-expert (Dr. Maya Patel)
Target: src/components/Button.tsx

### WCAG 2.1 AA Audit

| Criterion | Status |
|-----------|--------|
| 1.1.1 Non-text Content | ✅ Pass |
| 2.1.1 Keyboard | ❌ Issue |
| 4.1.2 Name, Role, Value | ✅ Pass |

### Findings

#### 2.1.1 Keyboard: Missing focus indicator

**Current:**
```tsx
<button className="btn" onClick={onClick}>
```

**Recommended:**
```tsx
<button 
  className="btn focus:ring-2 focus:ring-blue-500" 
  onClick={onClick}
>
```
```

## Integration with Spec

Skills are assigned to tasks in specs:

```markdown
| # | Task | Agent | Plugin | Skill |
|---|------|-------|--------|-------|
| 4 | Security review | `@owasp-expert` | `security` | `owasp/injection-prevention` |
```

When `/delegate` is called, the skill context is loaded:

```bash
/delegate @owasp-expert "Review auth module" --spec SPEC-2024-001
# Automatically loads: security/owasp/auth-security skill
```

