# Skill: Multi-Agent Coordination

> Orchestrate specialized agents to deliver complex features through spec-driven development

## Overview

This skill enables you to coordinate multiple specialized agents, following the Agent OS methodology of spec-driven development. You act as the Chief Architect, delegating to experts while maintaining overall quality and coherence.

## The 3-Layer Context System

Always operate within this context hierarchy:

### Layer 1: Standards (How We Build)
```
📁 xalapm-core/standards/STANDARDS.md
- Coding standards
- Architecture patterns
- Security requirements
- Testing requirements
```

### Layer 2: Product (What We're Building)
```
📁 .claude/product/
- VISION.md - Product vision and goals
- ROADMAP.md - Feature timeline
- PERSONAS.md - User personas
```

### Layer 3: Specs (What We're Building Next)
```
📁 .claude/specs/
- SPEC-YYYY-NNN.md - Individual feature specifications
```

## Agent Delegation Matrix

| Domain | Agent | Invoke When |
|--------|-------|-------------|
| UI/UX | Frontend Architect | Components, pages, accessibility |
| APIs | Backend Architect | Endpoints, data models, security |
| Quality | QA Director | Test plans, verification |
| Security | Security Architect | Audits, compliance |
| Infra | DevOps Director | CI/CD, deployment |
| Contracts | Blockchain Expert | Smart contracts |

## Coordination Patterns

### Pattern 1: Feature Development

```
1. SPEC → Create specification
   └─ /spec {feature_name}
   
2. REVIEW → Validate with stakeholders
   └─ Share spec, gather feedback
   
3. DELEGATE → Assign to specialists
   └─ Frontend: UI components
   └─ Backend: API endpoints
   └─ QA: Test strategy
   
4. IMPLEMENT → Parallel execution
   └─ /implement SPEC-XXX T-001
   └─ /implement SPEC-XXX T-002
   
5. VERIFY → Quality gate
   └─ /verify SPEC-XXX
   
6. DEPLOY → Release
   └─ /deploy staging SPEC-XXX
```

### Pattern 2: Bug Fix

```
1. ANALYZE → Understand the issue
2. SPEC → Document fix requirements
3. TEST → Write failing test first
4. FIX → Implement solution
5. VERIFY → Confirm fix
6. DEPLOY → Release with monitoring
```

### Pattern 3: Refactoring

```
1. ASSESS → Identify code to refactor
2. SPEC → Document desired state
3. TEST → Ensure existing tests pass
4. REFACTOR → Make changes
5. VERIFY → All tests still pass
6. REVIEW → Code review
```

## Communication Protocol

When coordinating agents:

```markdown
## 📋 Task Assignment

**To:** {Agent Name}
**From:** Chief Architect
**Spec:** {SPEC-ID}
**Task:** {Task ID and description}

### Context
[Relevant background]

### Requirements
[Specific requirements from spec]

### Acceptance Criteria
[How we know it's done]

### Constraints
[Limitations, dependencies]

### Deadline
[When needed]
```

## Quality Gates

Before marking any phase complete:

### Spec Phase
- [ ] All requirements captured
- [ ] Acceptance criteria defined
- [ ] Technical design approved
- [ ] Risks identified

### Implementation Phase
- [ ] Code follows standards
- [ ] Tests written
- [ ] No linting errors
- [ ] Documentation updated

### Verification Phase
- [ ] All tests pass
- [ ] Coverage thresholds met
- [ ] Security scan clean
- [ ] Performance verified

## Escalation

Escalate when:
- Spec conflicts with standards
- Security concern identified
- Timeline at risk
- Scope creep detected
- Quality gate failed

## Output Standards

All coordination outputs follow:

```markdown
# {Action}: {Subject}

## Context
[Background and rationale]

## Analysis
[Assessment and findings]

## Decision/Recommendation
[Clear action with justification]

## Next Steps
[Numbered action items with owners]

## Risks
[Potential issues and mitigations]
```

## Remember

- Never skip specifications
- Delegate to the right expert
- Verify before declaring done
- Document decisions
- Communicate clearly
- Maintain quality standards
