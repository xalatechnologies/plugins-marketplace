---
description: Break down a large feature or epic into smaller, actionable tasks
arguments:
  - name: feature
    description: Feature or epic description to break down
    required: true
---

# Breakdown Command

Decompose a large feature into smaller, actionable tasks.

## Breakdown Process

### 1. Understand the Feature
- Parse the feature description
- Identify the end goal
- Determine acceptance criteria

### 2. Identify Components
- UI components needed
- API endpoints required
- Database changes
- Business logic
- Tests

### 3. Create Task Hierarchy
```
Epic
└── Feature
    └── User Story
        └── Task
            └── Subtask
```

### 4. Sequence Tasks
- Identify dependencies
- Order by dependency
- Group by sprint/phase

## Output Format

```
📋 FEATURE BREAKDOWN
═══════════════════════════════════════════════════════════════

Feature: [Feature name]

🎯 Goal: [What this feature achieves]

📝 Acceptance Criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

───────────────────────────────────────────────────────────────

## Tasks

### Phase 1: Foundation (Est: [X]h)

#### T1: [Task name]
- **Description**: [What to do]
- **Effort**: [X]h
- **Dependencies**: None
- **Role**: [backend/frontend/etc.]
- **Acceptance**:
  - [ ] [Specific criterion]

#### T2: [Task name]
- **Description**: [What to do]
- **Effort**: [X]h
- **Dependencies**: T1
- **Role**: [backend/frontend/etc.]

### Phase 2: Core Implementation (Est: [X]h)

[Continue with more tasks...]

### Phase 3: Polish & Testing (Est: [X]h)

[Testing and polish tasks...]

───────────────────────────────────────────────────────────────

## Summary

| Phase | Tasks | Total Effort |
|-------|-------|--------------|
| Foundation | 3 | 8h |
| Core | 5 | 16h |
| Polish | 3 | 6h |
| **Total** | **11** | **30h** |

## Dependency Graph

```
T1 ──► T2 ──► T4
  │         ▲
  └──► T3 ──┘
              └──► T5
```

## Recommended Sprint Allocation

Sprint 1: T1, T2, T3 (Foundation)
Sprint 2: T4, T5, T6 (Core)
Sprint 3: T7, T8 (Polish)
```

## Guidelines

- Keep tasks atomic (completable in < 1 day)
- Each task should be independently testable
- Include clear acceptance criteria
- Consider parallelization opportunities
- Account for integration points

