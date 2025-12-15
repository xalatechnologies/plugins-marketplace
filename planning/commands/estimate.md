---
description: Estimate effort for a task or feature based on codebase analysis
arguments:
  - name: task
    description: Task description or ID to estimate
    required: true
---

# Estimate Command

Analyze the codebase and provide effort estimates for a task.

## Estimation Process

### 1. Understand the Task
- Parse the task description
- Identify what needs to be built/changed
- Determine scope boundaries

### 2. Analyze Codebase Impact
- Identify files that will be affected
- Count components to create/modify
- Check for existing patterns to reuse
- Identify dependencies

### 3. Consider Complexity Factors
- **Technical complexity**: New patterns, external APIs, etc.
- **Testing requirements**: Unit, integration, E2E
- **Documentation needs**: API docs, user docs
- **Review complexity**: Security implications, breaking changes

### 4. Generate Estimate

## Output Format

```
📊 TASK ESTIMATION
═══════════════════════════════════════════════════════════════

Task: [Task description]

🎯 Scope Analysis:
- Files to modify: [count]
- New files: [count]
- Tests to write: [count]
- Complexity: [Low/Medium/High]

⏱️ Effort Estimate:

| Component | Optimistic | Realistic | Pessimistic |
|-----------|------------|-----------|-------------|
| Implementation | 2h | 4h | 6h |
| Testing | 1h | 2h | 3h |
| Documentation | 30m | 1h | 1.5h |
| Review & Polish | 30m | 1h | 2h |
| **Total** | **4h** | **8h** | **12.5h** |

📌 Assumptions:
- [Assumption 1]
- [Assumption 2]

⚠️ Risks:
- [Risk 1]: Could add [X] hours
- [Risk 2]: Could add [X] hours

💡 Recommendations:
- [Suggestion to reduce complexity]
- [Alternative approach if applicable]

Confidence: [High/Medium/Low]
```

## Estimation Guidelines

- Be conservative - add buffer for unknowns
- Include testing time (typically 30-50% of implementation)
- Factor in review cycles
- Consider learning curve for new technologies
- Account for integration testing

