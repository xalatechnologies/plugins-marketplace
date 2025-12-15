# Orchestrator Agent Plugin

Master coordinator that manages and delegates to all specialized agents in the Xala PM ecosystem.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/analyze-project` | Comprehensive project analysis using all relevant agents |
| `/review-pr` | Multi-agent PR review |
| `/delegate` | Route task to appropriate specialized agent |

### Agent

The Orchestrator is the master coordinator with capabilities to:
- Understand user intent and route to correct agents
- Coordinate multi-agent workflows
- Synthesize findings from multiple agents
- Generate unified reports
- Create prioritized task backlogs

### Skills

- **Coordination Skill**: Multi-agent coordination, parallel execution, result synthesis

### Hooks

- Initialize agents on session start
- Propose multi-agent approach for complex tasks
- Suggest related agents after task completion

## Available Agents

### Development
| Agent | Specialty |
|-------|-----------|
| `frontend` | React, Remix, Next.js, UI |
| `backend` | API, Hono, NestJS |
| `supabase` | Database, RLS, migrations |
| `react` | Hooks, context, patterns |
| `tauri` | Desktop apps (Rust) |
| `mobile` | Expo, React Native |
| `blockchain` | Web3, Solidity, validators |
| `design-system` | UI components, tokens |

### Quality
| Agent | Specialty |
|-------|-----------|
| `testing` | E2E, unit, performance |
| `accessibility` | WCAG, GDPR, NSM |
| `code-review` | PR review, quality |
| `compliance` | Security tokens |

### Operations
| Agent | Specialty |
|-------|-----------|
| `devops` | CI/CD, Docker |
| `documentation` | Docs, README |

### Analysis
| Agent | Specialty |
|-------|-----------|
| `repo-analysis` | Codebase analysis |
| `planning` | Estimation, breakdown |
| `tasks` | Task management |

## Coordination Patterns

### Parallel Analysis
For comprehensive reviews:
```
                    ┌→ Frontend Agent ─┐
User Request ───────┼→ Backend Agent ──┼───→ Unified Report
                    └→ Testing Agent ──┘
```

### Sequential Execution
For feature development:
```
User Request → Backend → Frontend → Testing → Done
```

### Conditional Routing
For ambiguous tasks:
```
User Request → Analyze → Route to appropriate agent(s)
```

## Usage Examples

```bash
# Full project analysis
/analyze-project depth=deep

# PR review
/review-pr pr=142

# Delegate to specific agent
/delegate "Create user registration API" agent=backend

# Auto-route based on task
/delegate "Add accessibility to form components"
→ Routes to: accessibility, frontend
```

## Installation

```bash
/plugin install orchestrator@xalapm-marketplace
```

## Priority

The Orchestrator has priority 100 (highest) to ensure it handles routing before other agents.

