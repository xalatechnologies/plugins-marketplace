---
description: Perform comprehensive project analysis using all relevant agents
arguments:
  - name: path
    description: Path to project or repository
    required: false
    default: .
  - name: depth
    description: Analysis depth (quick, standard, deep)
    required: false
    default: standard
  - name: focus
    description: Focus areas (all, frontend, backend, security, compliance)
    required: false
    default: all
---

# Analyze Project Command

Orchestrate a comprehensive project analysis using multiple specialized agents.

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                              │
│                                                              │
│  1. Detect project type and structure                        │
│  2. Determine relevant agents                                │
│  3. Dispatch parallel analysis tasks                         │
│  4. Collect and synthesize results                           │
│  5. Generate unified report                                  │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   Frontend    │   │   Backend     │   │   Testing     │
│    Agent      │   │    Agent      │   │    Agent      │
└───────────────┘   └───────────────┘   └───────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  Accessibility│   │   Supabase    │   │   Security    │
│    Agent      │   │    Agent      │   │    Agent      │
└───────────────┘   └───────────────┘   └───────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   UNIFIED REPORT      │
                │   - Summary           │
                │   - Findings by area  │
                │   - Priorities        │
                │   - Task backlog      │
                └───────────────────────┘
```

## Phase 1: Project Detection

```typescript
interface ProjectAnalysis {
  type: 'monorepo' | 'single' | 'library'
  frameworks: string[]
  languages: string[]
  structure: {
    hasBackend: boolean
    hasFrontend: boolean
    hasDatabase: boolean
    hasMobile: boolean
    hasDesktop: boolean
    hasBlockchain: boolean
    hasTests: boolean
    hasDocs: boolean
    hasCI: boolean
  }
}

// Detect project characteristics
async function detectProject(path: string): Promise<ProjectAnalysis> {
  const files = await listFiles(path)
  
  return {
    type: detectRepoType(files),
    frameworks: detectFrameworks(files),
    languages: detectLanguages(files),
    structure: {
      hasBackend: hasDir('api') || hasDir('server') || hasFile('nest-cli.json'),
      hasFrontend: hasDir('src/components') || hasFile('next.config.js'),
      hasDatabase: hasDir('supabase') || hasFile('prisma/schema.prisma'),
      hasMobile: hasDir('apps/mobile') || hasFile('app.json'),
      hasDesktop: hasDir('src-tauri') || hasFile('tauri.conf.json'),
      hasBlockchain: hasDir('contracts') || hasFile('hardhat.config.ts'),
      hasTests: hasDir('tests') || hasDir('__tests__'),
      hasDocs: hasDir('docs') || hasFile('README.md'),
      hasCI: hasDir('.github/workflows') || hasFile('.gitlab-ci.yml'),
    }
  }
}
```

## Phase 2: Agent Selection

```typescript
function selectAgents(analysis: ProjectAnalysis): Agent[] {
  const agents: Agent[] = ['repo-analysis'] // Always include
  
  if (analysis.structure.hasFrontend) {
    agents.push('frontend', 'react', 'design-system', 'accessibility')
  }
  
  if (analysis.structure.hasBackend) {
    agents.push('backend', 'supabase')
  }
  
  if (analysis.structure.hasBlockchain) {
    agents.push('blockchain')
  }
  
  if (analysis.structure.hasMobile) {
    agents.push('mobile')
  }
  
  if (analysis.structure.hasDesktop) {
    agents.push('tauri')
  }
  
  if (analysis.structure.hasTests) {
    agents.push('testing')
  }
  
  if (analysis.structure.hasCI) {
    agents.push('devops')
  }
  
  // Always include for quality
  agents.push('compliance', 'code-review')
  
  return agents
}
```

## Phase 3: Parallel Analysis

```typescript
interface AgentResult {
  agent: string
  findings: Finding[]
  metrics: Record<string, number>
  tasks: SuggestedTask[]
  score: number
}

async function runParallelAnalysis(
  agents: Agent[],
  projectPath: string
): Promise<AgentResult[]> {
  // Run all agents in parallel
  const results = await Promise.all(
    agents.map(agent => runAgent(agent, projectPath))
  )
  
  return results
}
```

## Phase 4: Synthesize Results

```typescript
interface UnifiedReport {
  summary: {
    overallHealth: 'critical' | 'warning' | 'good' | 'excellent'
    score: number
    topIssues: Issue[]
  }
  byArea: {
    frontend?: AreaReport
    backend?: AreaReport
    security?: AreaReport
    accessibility?: AreaReport
    performance?: AreaReport
    testing?: AreaReport
  }
  prioritizedTasks: Task[]
  recommendations: string[]
}

function synthesizeResults(results: AgentResult[]): UnifiedReport {
  // Aggregate findings
  const allFindings = results.flatMap(r => r.findings)
  
  // Calculate overall score
  const overallScore = calculateWeightedScore(results)
  
  // Prioritize issues
  const topIssues = prioritizeIssues(allFindings)
  
  // Generate task backlog
  const tasks = generateTaskBacklog(allFindings, results)
  
  return {
    summary: {
      overallHealth: scoreToHealth(overallScore),
      score: overallScore,
      topIssues: topIssues.slice(0, 10),
    },
    byArea: groupByArea(results),
    prioritizedTasks: tasks,
    recommendations: generateRecommendations(results),
  }
}
```

## Output Format

```
🎯 PROJECT ANALYSIS REPORT
═══════════════════════════════════════════════════════════════

Project: xala-pm
Path: /Volumes/Development/Xala Products/PM dashboard
Type: Monorepo (Next.js + Supabase)
Analyzed: 2024-12-15

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL HEALTH: 🟡 WARNING (Score: 72/100)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AGENTS DEPLOYED
───────────────────────────────────────────────────────────────
✅ repo-analysis    │ ✅ frontend    │ ✅ backend
✅ react            │ ✅ supabase    │ ✅ testing
✅ accessibility    │ ✅ compliance  │ ✅ code-review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOP 10 ISSUES (Prioritized)
───────────────────────────────────────────────────────────────

1. 🔴 [SECURITY] Missing rate limiting on auth endpoints
   Source: backend-agent, testing-agent
   Impact: Critical
   
2. 🔴 [ACCESSIBILITY] 12 components missing keyboard navigation
   Source: accessibility-agent, frontend-agent
   Impact: High (WCAG violation)

3. 🟠 [TESTING] Test coverage 42% (target: 80%)
   Source: testing-agent
   Impact: High

4. 🟠 [BACKEND] N+1 query in /api/projects endpoint
   Source: backend-agent, supabase-agent
   Impact: Medium

5. 🟡 [FRONTEND] 8 components exceed 200 lines
   Source: frontend-agent, code-review-agent
   Impact: Medium

[... more issues ...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AREA BREAKDOWN
───────────────────────────────────────────────────────────────

📱 FRONTEND (Score: 78/100)
   ├── Components: 156 files
   ├── Issues: 12 (3 high, 9 medium)
   └── Coverage: 45%

⚙️ BACKEND (Score: 71/100)
   ├── Endpoints: 32
   ├── Issues: 8 (2 critical, 3 high)
   └── Coverage: 38%

♿ ACCESSIBILITY (Score: 65/100)
   ├── WCAG 2.1 AA: Partial
   ├── Issues: 15 (5 high)
   └── Automated score: 82

🧪 TESTING (Score: 58/100)
   ├── Unit tests: 124
   ├── E2E tests: 8
   └── Coverage: 42%

🔒 SECURITY (Score: 75/100)
   ├── Dependencies: 2 high vulns
   ├── Headers: 4/6 configured
   └── Auth: MFA not enforced

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GENERATED TASK BACKLOG (Top 20)
───────────────────────────────────────────────────────────────

Priority: Critical
├── t-sec-1: Add rate limiting to auth endpoints [4h] @backend
├── t-sec-2: Update vulnerable dependencies [1h] @devops
└── t-a11y-1: Fix keyboard navigation in modals [3h] @frontend

Priority: High
├── t-test-1: Increase unit test coverage to 80% [16h] @all
├── t-be-1: Fix N+1 query in projects API [2h] @backend
├── t-a11y-2: Add alt text to 24 images [2h] @frontend
└── t-fe-1: Refactor large components [8h] @frontend

[... more tasks ...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATIONS
───────────────────────────────────────────────────────────────

1. IMMEDIATE: Address security vulnerabilities before next deploy
2. THIS SPRINT: Focus on accessibility fixes for WCAG compliance
3. ONGOING: Increase test coverage with each PR
4. TECHNICAL DEBT: Schedule refactoring of large components

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create these tasks in Xala PM? (y/n)
```

## Usage

```bash
# Full project analysis
/analyze-project

# Quick analysis
/analyze-project depth=quick

# Focus on specific areas
/analyze-project focus=security,testing

# Analyze specific path
/analyze-project path=apps/web
```

