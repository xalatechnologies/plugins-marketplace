---
description: Multi-agent coordination and synthesis expertise
triggers:
  - complex tasks
  - project analysis
  - pr review
  - production readiness
  - comprehensive audit
---

# Coordination Skill

Expert multi-agent coordination and result synthesis.

## Agent Selection Matrix

```
TASK TYPE                    AGENTS TO INVOLVE
─────────────────────────────────────────────────────────
New Feature                  frontend + backend + testing
API Development              backend + supabase + testing
UI Component                 frontend + design-system + a11y
Database Changes             supabase + backend
Smart Contract               blockchain + testing (security)
Mobile Feature               mobile + testing
Desktop Feature              tauri + testing
PR Review                    code-review + testing + a11y + security
Project Analysis             repo-analysis + all relevant
Production Readiness         testing + security + performance + a11y
Compliance Check             accessibility + compliance + security
Documentation                documentation + relevant domain agent
```

## Coordination Patterns

### Parallel Execution
```typescript
async function parallelAnalysis(agents: Agent[], target: string) {
  const results = await Promise.all(
    agents.map(agent => dispatchAgent(agent, target))
  )
  return synthesize(results)
}
```

### Sequential Execution
```typescript
async function sequentialBuild(steps: AgentStep[]) {
  let context = {}
  for (const step of steps) {
    const result = await dispatchAgent(step.agent, step.task, context)
    context = { ...context, [step.agent]: result }
  }
  return context
}
```

### Conditional Branching
```typescript
async function conditionalRoute(task: string, context: Context) {
  const analysis = analyzeTask(task)
  
  if (analysis.type === 'frontend') {
    return dispatchAgent('frontend', task, context)
  } else if (analysis.type === 'backend') {
    return dispatchAgent('backend', task, context)
  } else if (analysis.isComplex) {
    return parallelAnalysis(['frontend', 'backend', 'testing'], task)
  }
}
```

## Result Synthesis

### Merging Findings
```typescript
interface AgentFinding {
  agent: string
  severity: 'critical' | 'high' | 'medium' | 'low'
  category: string
  description: string
  location?: string
  suggestion?: string
}

function synthesizeFindings(results: AgentResult[]): SynthesizedReport {
  const allFindings = results.flatMap(r => r.findings)
  
  // Group by category
  const byCategory = groupBy(allFindings, 'category')
  
  // Deduplicate similar findings
  const deduplicated = deduplicateFindings(allFindings)
  
  // Sort by severity
  const prioritized = sortBy(deduplicated, severityOrder)
  
  // Identify cross-cutting concerns
  const crossCutting = findCrossCuttingIssues(allFindings)
  
  return {
    findings: prioritized,
    byCategory,
    crossCutting,
    summary: generateSummary(prioritized),
  }
}
```

### Conflict Resolution
```typescript
function resolveConflicts(findings: Finding[]): Finding[] {
  // Find conflicting recommendations
  const conflicts = findConflicts(findings)
  
  for (const conflict of conflicts) {
    // Prefer security over performance
    // Prefer accessibility over convenience
    // Prefer standards compliance
    const resolved = resolveByPriority(conflict, PRIORITY_ORDER)
    findings = applyResolution(findings, resolved)
  }
  
  return findings
}

const PRIORITY_ORDER = [
  'security',
  'accessibility',
  'compliance',
  'correctness',
  'performance',
  'style',
]
```

## Task Generation

```typescript
function generateTasks(findings: Finding[]): Task[] {
  return findings.map(finding => ({
    id: generateTaskId(finding),
    title: findingToTaskTitle(finding),
    role: findingToRole(finding),
    priority: severityToPriority(finding.severity),
    description: finding.suggestion || finding.description,
    source: `${finding.agent}-agent`,
    phase: determinePhase(finding),
    estimate: estimateEffort(finding),
  }))
}
```

## Quality Scoring

```typescript
function calculateOverallScore(results: AgentResult[]): number {
  const weights = {
    security: 0.25,
    testing: 0.20,
    accessibility: 0.15,
    performance: 0.15,
    codeQuality: 0.15,
    documentation: 0.10,
  }
  
  let totalScore = 0
  let totalWeight = 0
  
  for (const [category, weight] of Object.entries(weights)) {
    const categoryResults = results.filter(r => r.category === category)
    if (categoryResults.length > 0) {
      const avgScore = average(categoryResults.map(r => r.score))
      totalScore += avgScore * weight
      totalWeight += weight
    }
  }
  
  return totalScore / totalWeight
}
```

## When to Use

Apply this skill when:
- Task involves multiple domains
- Comprehensive analysis needed
- Multiple perspectives required
- Synthesizing results from parallel work

