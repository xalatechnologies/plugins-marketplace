# Spec-Driven Development Workflow

> The complete workflow for building features the right way, every time.

## Philosophy

Based on [Agent OS](https://buildermethods.com/agent-os) methodology:
- **Specifications before code** - Define what "done" means first
- **Verification built-in** - Tests are part of the spec, not afterthought
- **Expert delegation** - Right agent for the right task
- **Incremental delivery** - Small, verified changes

## The Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPEC-DRIVEN DEVELOPMENT                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │  PLAN   │ ─► │  SPEC   │ ─► │ DESIGN  │ ─► │  TASKS  │     │
│  │ Product │    │ Feature │    │Technical│    │ Backlog │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│       │              │              │              │            │
│       ▼              ▼              ▼              ▼            │
│   Vision.md      SPEC-XXX.md    Architecture    T-001..N       │
│   Roadmap.md     Acceptance     Data Model      Estimates      │
│   Personas.md    Criteria       API Design      Assignments    │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │IMPLEMENT│ ─► │  TEST   │ ─► │ VERIFY  │ ─► │ DEPLOY  │     │
│  │  Code   │    │  Write  │    │  Gate   │    │ Release │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│       │              │              │              │            │
│       ▼              ▼              ▼              ▼            │
│   Components     Unit Tests     Coverage       Staging         │
│   Services       Integration    Acceptance     Production      │
│   APIs           E2E Tests      Security       Monitoring      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Plan Product

**Owner:** Product Manager / Stakeholder
**Output:** Product context files

### Artifacts

```markdown
# .claude/product/VISION.md
- Product vision statement
- Target users
- Value proposition
- Success metrics

# .claude/product/ROADMAP.md
- Quarterly goals
- Feature priorities
- Dependencies

# .claude/product/PERSONAS.md
- User personas with goals/pain points
```

### Example Vision

```markdown
# Product Vision: Xala PM

## Vision Statement
Xala PM is an AI-native project management platform that helps development 
teams ship faster by automating project coordination and providing 
intelligent insights.

## Target Users
- Small to medium development teams (5-50)
- Agile/Scrum practitioners
- Technical project managers

## Value Proposition
- 50% reduction in status update meetings
- Automated task tracking from code activity
- AI-powered sprint planning

## Success Metrics
| Metric | Target |
|--------|--------|
| Daily Active Users | 1000+ |
| Task Completion Rate | +30% |
| NPS Score | 50+ |
```

## Phase 2: Shape Spec

**Owner:** Chief Architect (you)
**Command:** `/spec {feature}`
**Output:** Feature specification

### Process

1. Understand the feature request
2. Ask clarifying questions
3. Draft specification using template
4. Include acceptance criteria
5. Get stakeholder sign-off

### Quality Checklist

- [ ] Problem clearly stated
- [ ] Success metrics defined
- [ ] User stories with acceptance criteria
- [ ] Technical design outlined
- [ ] Risks identified
- [ ] Testing strategy defined

## Phase 3: Create Tasks

**Owner:** Chief Architect (you)
**Command:** `/breakdown {specId}`
**Output:** Task backlog

### Task Format

```markdown
## T-001: [Task Title]

**Spec:** SPEC-2024-001
**Requirement:** FR-001
**Agent:** Frontend Architect
**Estimate:** 2 hours

### Description
[What needs to be done]

### Acceptance Criteria
[How we know it's done]

### Dependencies
[What must be done first]
```

### Task Categories

1. **Foundation** - Data models, API setup
2. **Implementation** - Core functionality
3. **Integration** - Connect components
4. **Verification** - Testing, QA
5. **Documentation** - User/dev docs
6. **Deployment** - Release prep

## Phase 4: Implement

**Owner:** Specialized Agents
**Command:** `/implement {specId} {taskId}`
**Output:** Working code with tests

### Implementation Rules

1. **Load context first** - Read spec, standards
2. **Write tests alongside** - TDD when possible
3. **Follow standards** - No shortcuts
4. **Document decisions** - ADRs for significant choices
5. **Commit frequently** - Small, focused commits

### Agent Assignments

| Agent | Implements |
|-------|-----------|
| Frontend Architect | UI components, pages, styles |
| Backend Architect | APIs, services, data access |
| QA Director | Test infrastructure, test data |
| DevOps Director | CI/CD, deployment configs |
| Security Architect | Security features, audits |

## Phase 5: Verify

**Owner:** QA Director
**Command:** `/verify {specId}`
**Output:** Verification report

### Verification Matrix

| Level | What | Coverage |
|-------|------|----------|
| Unit | Functions, components | 80%+ |
| Integration | API contracts, DB | Key paths |
| E2E | User journeys | Critical 5 |
| Security | Vulnerabilities | All code |
| Performance | Response times | Under load |

### Quality Gates

Must pass ALL:
- [ ] All tests pass
- [ ] Coverage thresholds met
- [ ] No critical security issues
- [ ] Performance within targets
- [ ] Accessibility compliant (if UI)
- [ ] Documentation complete

## Phase 6: Deploy

**Owner:** DevOps Director
**Command:** `/deploy {environment} {specId}`
**Output:** Running feature

### Deployment Stages

```
Development → Staging → Production
     ↓            ↓          ↓
   Auto        E2E Tests   Approval
              + Smoke      Required
```

### Pre-Production Checklist

- [ ] Staging tests pass
- [ ] Feature flag configured
- [ ] Rollback plan documented
- [ ] Monitoring alerts set
- [ ] Runbook updated
- [ ] Stakeholder approval

### Post-Deployment

- [ ] Smoke tests pass
- [ ] Metrics normal
- [ ] No error spikes
- [ ] Feature flag enabled for %
- [ ] User feedback collected

## Continuous Improvement

After each feature:

### Retrospective

```markdown
## Feature Retro: {Feature Name}

### What Went Well
- [List successes]

### What Could Improve
- [List opportunities]

### Action Items
- [ ] [Improvement 1]
- [ ] [Improvement 2]
```

### Metrics to Track

| Metric | Target |
|--------|--------|
| Spec-to-Deploy Time | < 1 sprint |
| Bug Escape Rate | < 5% |
| Rework Rate | < 10% |
| Test Coverage | > 80% |

---

*"The goal is not to ship features faster, but to ship the right features right."*

