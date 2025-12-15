# Product Requirements Document: [Product/Feature Name]

> **PRD ID:** PRD-{YYYY}-{NNN}
> **Status:** Draft | Review | Approved | In Progress | Complete
> **Created:** {date}
> **Xala PM Epic:** [Link to Xala PM epic]

---

## 1. Overview

### Problem Statement
[What problem are we solving?]

### Solution
[High-level description of the solution]

### Success Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| [Metric 1] | [Target] | [How measured] |
| [Metric 2] | [Target] | [How measured] |

---

## 2. User Stories

| ID | As a... | I want to... | So that... | Priority | Agent |
|----|---------|--------------|------------|----------|-------|
| US-1 | [user type] | [action] | [benefit] | High | `@frontend-dev` |
| US-2 | [user type] | [action] | [benefit] | Medium | `@backend-dev` |
| US-3 | [user type] | [action] | [benefit] | Low | `@mobile-dev` |

---

## 3. Specifications

> Each user story breaks down into detailed specs with agent assignments.

### US-1: [User Story Title]

| Spec ID | Description | Assigned Agent |
|---------|-------------|----------------|
| SPEC-{YYYY}-001 | [Spec title] | `@frontend-dev` |
| SPEC-{YYYY}-002 | [Spec title] | `@backend-dev` |

**Create specs:**
```bash
/spec [feature-name] --prd PRD-{YYYY}-{NNN} --user-story US-1
```

---

## 4. Technical Architecture

### Architecture Owner
**Agent:** `@orchestrator` (Dr. Alexander Chen)

### System Components

| Component | Description | Owner Agent | Plugin |
|-----------|-------------|-------------|--------|
| Frontend | React/Next.js UI | `@frontend-dev` | `frontend` |
| Backend API | REST/GraphQL API | `@backend-dev` | `backend` |
| Database | PostgreSQL/Supabase | `@supabase-dev` | `supabase` |
| Auth | Authentication | `@owasp-expert` | `security` |
| Mobile | React Native app | `@mobile-dev` | `mobile` |
| Desktop | Tauri app | `@desktop-dev` | `tauri` |

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Layer                            │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │  Web    │  │ Mobile  │  │ Desktop │  │  API    │        │
│  │@frontend│  │@mobile  │  │@desktop │  │ Client  │        │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
└───────┼────────────┼────────────┼────────────┼──────────────┘
        │            │            │            │
        └────────────┴────────────┴────────────┘
                          │
┌─────────────────────────┼───────────────────────────────────┐
│                    API Gateway                               │
│                    @backend-dev                              │
└─────────────────────────┼───────────────────────────────────┘
                          │
┌─────────────────────────┼───────────────────────────────────┐
│                   Service Layer                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Auth    │  │ Users   │  │ Core    │  │ Notify  │        │
│  │@owasp   │  │@backend │  │@backend │  │@backend │        │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
└───────┼────────────┼────────────┼────────────┼──────────────┘
        │            │            │            │
        └────────────┴────────────┴────────────┘
                          │
┌─────────────────────────┼───────────────────────────────────┐
│                   Data Layer                                 │
│                   @supabase-dev                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Non-Functional Requirements

### Security Requirements

| Requirement | Standard | Owner Agent | Verification |
|-------------|----------|-------------|--------------|
| Authentication | OAuth2 + JWT | `@owasp-expert` | Security audit |
| Authorization | RBAC | `@owasp-expert` | Access review |
| Data encryption | AES-256 | `@cybersecurity-architect` | Compliance scan |
| Input validation | OWASP ASVS | `@owasp-expert` | `/security-scan` |
| Dependency security | OpenSSF | `@opensource-standards` | SBOM audit |
| SOC2 compliance | Type II | `@soc2-auditor` | Audit prep |

### Performance Requirements

| Metric | Target | Owner Agent |
|--------|--------|-------------|
| Page load | < 2s | `@frontend-dev` |
| API response | < 200ms | `@backend-dev` |
| Availability | 99.9% | `@devops-engineer` |

### Accessibility Requirements

| Standard | Level | Owner Agent | Verification |
|----------|-------|-------------|--------------|
| WCAG 2.1 | AA | `@accessibility-expert` | Axe audit |
| Keyboard nav | Full | `@frontend-dev` | Manual test |
| Screen reader | Compatible | `@accessibility-expert` | NVDA/VO test |

### Compliance Requirements

| Regulation | Requirement | Owner Agent |
|------------|-------------|-------------|
| GDPR | Data privacy | `@compliance-officer` |
| PCI-DSS | Payment security | `@soc2-auditor` |
| SOC2 | Security controls | `@soc2-auditor` |

---

## 6. Implementation Phases

### Phase 1: Foundation
**Duration:** 2 weeks

| Task | Agent | Plugin | Specs |
|------|-------|--------|-------|
| Database schema | `@supabase-dev` | `supabase` | SPEC-001 |
| Auth system | `@owasp-expert` | `security` | SPEC-002 |
| API foundation | `@backend-dev` | `backend` | SPEC-003 |
| CI/CD setup | `@devops-engineer` | `devops` | SPEC-004 |

### Phase 2: Core Features
**Duration:** 4 weeks

| Task | Agent | Plugin | Specs |
|------|-------|--------|-------|
| Feature A | `@backend-dev` + `@frontend-dev` | `backend`, `frontend` | SPEC-005-010 |
| Feature B | `@backend-dev` + `@frontend-dev` | `backend`, `frontend` | SPEC-011-015 |

### Phase 3: Polish & Launch
**Duration:** 2 weeks

| Task | Agent | Plugin |
|------|-------|--------|
| Security audit | `@owasp-expert` | `security` |
| Accessibility audit | `@accessibility-expert` | `accessibility` |
| Performance optimization | `@frontend-dev` + `@backend-dev` | `frontend`, `backend` |
| Documentation | `@docs-writer` | `documentation` |

---

## 7. Xala PM Integration

### Epic Structure

```
PRD-2024-001: [Product Name]
├── US-1: [User Story 1]
│   ├── SPEC-2024-001 → Tasks PM-001, PM-002, PM-003
│   └── SPEC-2024-002 → Tasks PM-004, PM-005
├── US-2: [User Story 2]
│   └── SPEC-2024-003 → Tasks PM-006, PM-007
└── US-3: [User Story 3]
    └── SPEC-2024-004 → Tasks PM-008, PM-009
```

### Commands

```bash
# Create PRD in Xala PM
/prd create "[Product Name]" --status draft

# Create epic from PRD
/epic create --prd PRD-2024-001

# Create specs from user stories
/spec [feature] --prd PRD-2024-001 --user-story US-1

# Track progress
/prd status PRD-2024-001
```

### Progress Tracking

| Phase | Progress | Specs | Tasks | Agent Coverage |
|-------|----------|-------|-------|----------------|
| Phase 1 | 45% | 4/4 | 12/20 | 3 agents active |
| Phase 2 | 0% | 0/10 | 0/40 | - |
| Phase 3 | 0% | 0/3 | 0/15 | - |

---

## 8. Review & Approval

### Required Reviews

| Review Type | Agent | Status |
|-------------|-------|--------|
| Architecture | `@orchestrator` | ⬜ Pending |
| Security | `@owasp-expert` | ⬜ Pending |
| Accessibility | `@accessibility-expert` | ⬜ Pending |
| Compliance | `@compliance-officer` | ⬜ Pending |
| Technical | `@backend-dev`, `@frontend-dev` | ⬜ Pending |

### Sign-off

| Role | Agent | Name | Date | Approved |
|------|-------|------|------|----------|
| Product Owner | - | [Name] | | ⬜ |
| Tech Lead | `@orchestrator` | Dr. Alexander Chen | | ⬜ |
| Security | `@owasp-expert` | Dr. Aisha Thompson | | ⬜ |
| QA Lead | `@testing-specialist` | Dr. Elena Vasquez | | ⬜ |

