# Agent Registry

> Complete reference of all available agents for task delegation and routing.

## Quick Reference

| Handle | Name | Plugin | Primary Use |
|--------|------|--------|-------------|
| `@orchestrator` | Dr. Alexander Chen | `orchestrator` | Coordination, architecture |
| `@frontend-dev` | Sarah Kim | `frontend` | React, UI, accessibility |
| `@backend-dev` | Dr. Marcus Rivera | `backend` | APIs, databases |
| `@supabase-dev` | Supabase Expert | `supabase` | Postgres, RLS, migrations |
| `@testing-specialist` | Dr. Elena Vasquez | `testing` | All testing types |
| `@owasp-expert` | Dr. Aisha Thompson | `security` | OWASP Top 10, ASVS |
| `@soc2-auditor` | Dr. Robert Chen | `security` | SOC2 compliance |
| `@cybersecurity-architect` | Dr. Sarah Martinez | `security` | NIST, CIS, Zero Trust |
| `@opensource-standards` | Dr. Michael Foster | `security` | OpenSSF, SBOM |
| `@blockchain-expert` | Dr. Wei Zhang | `blockchain` | Smart contracts |
| `@accessibility-expert` | Dr. Maya Patel | `accessibility` | WCAG, Universal Design |
| `@compliance-officer` | Dr. Catherine Rhodes | `compliance` | GDPR, regulatory |
| `@devops-engineer` | James O'Brien | `devops` | CI/CD, infrastructure |
| `@code-reviewer` | Code Review Agent | `code-review` | PR review, quality |
| `@docs-writer` | Documentation Agent | `documentation` | API docs, README |
| `@design-dev` | Design System Agent | `design-system` | Components, tokens |
| `@react-dev` | React Expert | `react` | Hooks, state |
| `@mobile-dev` | Mobile Expert | `mobile` | Expo, React Native |
| `@desktop-dev` | Desktop Expert | `tauri` | Tauri, Rust |
| `@task-manager` | Task Manager Agent | `tasks` | Xala PM integration |

---

## Agent Details

### Development Agents

#### @orchestrator
- **Name:** Dr. Alexander Chen
- **Plugin:** `orchestrator`
- **File:** `orchestrator/agents/orchestrator.md`
- **Expertise:** System architecture, team coordination, spec-driven development
- **Use For:** Architecture decisions, task delegation, spec creation

#### @frontend-dev
- **Name:** Sarah Kim
- **Plugin:** `frontend`
- **File:** `frontend/agents/frontend-dev.md`
- **Expertise:** React, TypeScript, CSS, accessibility, performance
- **Use For:** UI components, styling, client-side logic

#### @backend-dev
- **Name:** Dr. Marcus Rivera
- **Plugin:** `backend`
- **File:** `backend/agents/backend-dev.md`
- **Expertise:** APIs, databases, server architecture, security
- **Use For:** REST/GraphQL APIs, server logic, data modeling

#### @supabase-dev
- **Name:** Supabase Expert
- **Plugin:** `supabase`
- **File:** `supabase/agents/supabase-dev.md`
- **Expertise:** PostgreSQL, RLS, Edge Functions, Auth
- **Use For:** Database schema, migrations, Supabase features

#### @react-dev
- **Name:** React Expert
- **Plugin:** `react`
- **File:** `react/agents/react-dev.md`
- **Expertise:** React patterns, hooks, state management
- **Use For:** Complex React architecture, performance

---

### Security Agents

#### @owasp-expert
- **Name:** Dr. Aisha Thompson
- **Plugin:** `security`
- **File:** `security/agents/owasp-expert.md`
- **Expertise:** OWASP Top 10, ASVS, secure coding
- **Use For:** Security reviews, vulnerability detection

#### @soc2-auditor
- **Name:** Dr. Robert Chen
- **Plugin:** `security`
- **File:** `security/agents/soc2-auditor.md`
- **Expertise:** SOC2 Type II, Trust Service Criteria
- **Use For:** Compliance audits, evidence collection

#### @cybersecurity-architect
- **Name:** Dr. Sarah Martinez
- **Plugin:** `security`
- **File:** `security/agents/cybersecurity-architect.md`
- **Expertise:** NIST CSF, CIS Controls, Zero Trust
- **Use For:** Security architecture, threat modeling

#### @opensource-standards
- **Name:** Dr. Michael Foster
- **Plugin:** `security`
- **File:** `security/agents/opensource-standards.md`
- **Expertise:** OpenSSF, SLSA, SBOM, licensing
- **Use For:** Dependency security, OSS compliance

---

### Quality Agents

#### @testing-specialist
- **Name:** Dr. Elena Vasquez
- **Plugin:** `testing`
- **File:** `testing/agents/testing-specialist.md`
- **Expertise:** E2E, unit, integration, performance testing
- **Use For:** All testing tasks, QA

#### @code-reviewer
- **Name:** Code Review Agent
- **Plugin:** `code-review`
- **File:** `code-review/agents/reviewer.md`
- **Expertise:** Code quality, refactoring, best practices
- **Use For:** PR reviews, code improvements

#### @accessibility-expert
- **Name:** Dr. Maya Patel
- **Plugin:** `accessibility`
- **File:** `accessibility/agents/compliance-expert.md`
- **Expertise:** WCAG 2.1, Universal Design, assistive tech
- **Use For:** Accessibility audits, inclusive design

---

### Compliance Agents

#### @compliance-officer
- **Name:** Dr. Catherine Rhodes
- **Plugin:** `compliance`
- **File:** `compliance/agents/compliance-officer.md`
- **Expertise:** GDPR, HIPAA, PCI-DSS, regulatory
- **Use For:** Data privacy, regulatory compliance

---

### Infrastructure Agents

#### @devops-engineer
- **Name:** James O'Brien
- **Plugin:** `devops`
- **File:** `devops/agents/devops-engineer.md`
- **Expertise:** CI/CD, Docker, Kubernetes, IaC
- **Use For:** Pipelines, deployment, infrastructure

---

### Specialized Agents

#### @blockchain-expert
- **Name:** Dr. Wei Zhang
- **Plugin:** `blockchain`
- **File:** `blockchain/agents/blockchain-expert.md`
- **Expertise:** Smart contracts, DeFi, security auditing
- **Use For:** Web3 development, contract security

#### @mobile-dev
- **Name:** Mobile Expert
- **Plugin:** `mobile`
- **File:** `mobile/agents/mobile-dev.md`
- **Expertise:** Expo, React Native, iOS/Android
- **Use For:** Cross-platform mobile apps

#### @desktop-dev
- **Name:** Desktop Expert
- **Plugin:** `tauri`
- **File:** `tauri/agents/desktop-dev.md`
- **Expertise:** Tauri, Rust, native desktop
- **Use For:** Desktop applications

#### @design-dev
- **Name:** Design System Agent
- **Plugin:** `design-system`
- **File:** `design-system/agents/design-dev.md`
- **Expertise:** Design tokens, component libraries
- **Use For:** Design system maintenance

#### @docs-writer
- **Name:** Documentation Agent
- **Plugin:** `documentation`
- **File:** `documentation/agents/docs-writer.md`
- **Expertise:** Technical writing, API docs
- **Use For:** Documentation, README, guides

#### @task-manager
- **Name:** Task Manager Agent
- **Plugin:** `tasks`
- **File:** `tasks/agents/task-manager.md`
- **Expertise:** Task management, Xala PM
- **Use For:** Task CRUD, PM integration

---

## Usage

### Delegate to Agent

```bash
/delegate @backend-dev "Create user authentication API"
```

### Delegate with Context

```bash
/delegate @owasp-expert "Security review" --spec SPEC-2024-001
```

### Invoke Agent Skill

```bash
/skill security/owasp/injection-prevention
```

### Assign Agent to Task

```bash
/task create "Build login form" --agent @frontend-dev
```

---

## Agent Selection Guide

### "I need to build..."

| Need | Recommended Agent |
|------|-------------------|
| REST API | `@backend-dev` |
| React component | `@frontend-dev` |
| Database schema | `@supabase-dev` |
| Mobile app | `@mobile-dev` |
| Desktop app | `@desktop-dev` |
| Smart contract | `@blockchain-expert` |

### "I need to check..."

| Need | Recommended Agent |
|------|-------------------|
| Security vulnerabilities | `@owasp-expert` |
| SOC2 compliance | `@soc2-auditor` |
| Accessibility | `@accessibility-expert` |
| GDPR compliance | `@compliance-officer` |
| Code quality | `@code-reviewer` |
| Dependencies | `@opensource-standards` |

### "I need to test..."

| Need | Recommended Agent |
|------|-------------------|
| Unit tests | `@testing-specialist` |
| E2E tests | `@testing-specialist` |
| Integration tests | `@testing-specialist` |
| Performance tests | `@testing-specialist` |

### "I need to deploy..."

| Need | Recommended Agent |
|------|-------------------|
| CI/CD pipeline | `@devops-engineer` |
| Docker | `@devops-engineer` |
| Kubernetes | `@devops-engineer` |
| Infrastructure | `@devops-engineer` |

