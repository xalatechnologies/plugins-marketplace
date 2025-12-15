# Xala PM Plugin Marketplace

> **Spec-Driven Development for AI Coding Agents** — Inspired by [Agent OS](https://buildermethods.com/agent-os) and Blitzy Intelligence

A comprehensive collection of Claude Code plugins featuring expert AI agents, spec-driven workflows, and automated code analysis.

---

## 🎯 Philosophy

We implement the **3-Layer Context System** from Agent OS:

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: STANDARDS — How We Build                  │
│  → Coding standards, architecture patterns          │
│  → xalapm-core/standards/STANDARDS.md              │
├─────────────────────────────────────────────────────┤
│  Layer 2: PRODUCT — What We're Building            │
│  → Vision, roadmap, user personas                   │
│  → .claude/product/*.md                            │
├─────────────────────────────────────────────────────┤
│  Layer 3: SPECS — What We're Building Next         │
│  → Feature specifications with acceptance criteria  │
│  → .claude/specs/SPEC-YYYY-NNN.md                  │
└─────────────────────────────────────────────────────┘
```

---

## ⭐ Key Features

### 🧠 Expert AI Agents (30+ Years Experience)

Each agent has a distinct personality, background, and expertise:

| Agent | Persona | Expertise |
|-------|---------|-----------|
| **Chief Architect** | Dr. Alexander Chen | System design, orchestration, spec-driven development |
| **Frontend Architect** | Sarah Kim | React, accessibility, performance, design systems |
| **Backend Architect** | Dr. Marcus Rivera | APIs, databases, security, distributed systems |
| **QA Director** | Dr. Elena Vasquez | Testing strategies, verification, quality gates |
| **Security Architect** | Dr. Wei Zhang | Smart contracts, cryptography, compliance |
| **DevOps Director** | James O'Brien | CI/CD, infrastructure, reliability |
| **Compliance Officer** | Dr. Catherine Rhodes | SEC/FINRA, KYC/AML, security tokens |
| **Accessibility Director** | Dr. Maya Patel | WCAG, inclusive design, assistive tech |

### 📋 Spec-Driven Workflow

```
/spec → /implement → /verify → /deploy
```

| Command | Description |
|---------|-------------|
| `/spec {feature}` | Create comprehensive specification before coding |
| `/implement {specId}` | Implement feature following its specification |
| `/verify {specId}` | Verify implementation meets acceptance criteria |
| `/delegate {task}` | Assign tasks to specialized agents |

### 🐍 Python Script Automation

Automated code analysis runs on every file change:

| Script | Purpose | Detects |
|--------|---------|---------|
| `review-code.py` | Code quality | Security issues, TODOs, console.logs |
| `check-a11y.py` | Accessibility | WCAG violations, missing ARIA |
| `suggest-tests.py` | Test coverage | Functions needing tests |
| `security-scan.py` | Smart contracts | Reentrancy, DEX violations |
| `compliance-check.py` | Regulations | GDPR, PCI-DSS, security tokens |
| `ci-validator.py` | CI/CD security | Hardcoded secrets, permissions |

---

## 📦 Plugin Categories

### 🔮 Orchestration & Core
| Plugin | Agent | Key Commands |
|--------|-------|--------------|
| **orchestrator** | Chief Architect | `/spec`, `/implement`, `/verify`, `/delegate` |
| **xalapm-core** | — | MCP integration, standards, templates |
| **tasks** | Task Manager | `/task`, `/backlog`, `/generate-tasks` |

### 💻 Development
| Plugin | Agent | Key Commands |
|--------|-------|--------------|
| **frontend** | Frontend Architect | `/component`, `/page` |
| **backend** | Backend Architect | `/endpoint`, `/service` |
| **react** | React Expert | `/hook`, `/context` |
| **supabase** | Database Expert | `/migration`, `/rls`, `/types` |
| **tauri** | Desktop Expert | `/command`, `/plugin` |
| **mobile** | Mobile Expert | `/screen` |

### 🔒 Security & Compliance
| Plugin | Agent | Key Commands |
|--------|-------|--------------|
| **blockchain** | Security Architect | `/audit`, `/contract`, `/validator` |
| **compliance** | Compliance Officer | `/check-compliance` |
| **accessibility** | Accessibility Director | `/wcag-audit`, `/gdpr-check` |

### 🧪 Quality & DevOps
| Plugin | Agent | Key Commands |
|--------|-------|--------------|
| **testing** | QA Director | `/unit`, `/e2e`, `/performance` |
| **code-review** | Reviewer | `/review` |
| **devops** | DevOps Director | `/ci` |
| **documentation** | Docs Writer | `/docs` |

---

## 🚀 Installation

### 1. Add the Marketplace

```shell
/plugin marketplace add https://github.com/xalatechnologies/plugins-marketplace
```

### 2. Install by Role

| Group | For | Plugins |
|-------|-----|---------|
| `essential` | Getting started | 4 |
| `fullstack` | Web developers | 7 |
| `blockchain-dev` | Web3 developers | 4 |
| `qa` | Quality engineers | 4 |
| `pm` | Project managers | 7 |
| `all` | Everything (Beast Mode!) | 21 |

```bash
# Install via script
./install.sh --group fullstack --scope project

# Or manually
/plugin install xalapm-core@xala-marketplace
/plugin install orchestrator@xala-marketplace
```

### 3. Restart Claude Code

---

## 📐 Spec-Driven Development Workflow

Based on [Agent OS methodology](https://buildermethods.com/agent-os):

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  SPEC   │ ─► │ DESIGN  │ ─► │IMPLEMENT│ ─► │ VERIFY  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
  SPEC-XXX.md    Architecture   Code+Tests    Quality Gate
  Acceptance     Data Model     Delegation    Approval
  Criteria       API Design     Standards     Deployment
```

### Example Session

```
User: I need user authentication

Chief Architect: Before we write code, let's spec this out.

/spec user-authentication

📋 Creating specification SPEC-2024-001...

Questions:
1. What auth methods? (OAuth, email/password, SSO?)
2. Session management strategy?
3. Compliance requirements?

[After answering questions...]

✅ Specification created: .claude/specs/SPEC-2024-001.md

Tasks generated:
- T-001: Data model (Backend Architect)
- T-002: Auth endpoints (Backend Architect)  
- T-003: Login UI (Frontend Architect)
- T-004: Test strategy (QA Director)

/implement SPEC-2024-001 T-001

Delegating to Backend Architect (Dr. Marcus Rivera)...
```

---

## 🏗️ Project Structure

```
plugins-marketplace/
├── .claude-plugin/
│   └── marketplace.json         # Plugin registry
├── xalapm-core/
│   ├── standards/
│   │   └── STANDARDS.md        # Coding standards
│   ├── templates/
│   │   └── SPEC_TEMPLATE.md    # Specification template
│   ├── scripts/                 # Python automation
│   └── .mcp.json               # MCP tool config
├── orchestrator/
│   ├── agents/
│   │   └── orchestrator.md     # Chief Architect persona
│   ├── commands/
│   │   ├── spec.md             # /spec command
│   │   ├── implement.md        # /implement command
│   │   └── verify.md           # /verify command
│   ├── workflows/
│   │   └── spec-driven-development.md
│   └── skills/
├── frontend/
│   ├── agents/
│   │   └── frontend-dev.md     # Sarah Kim persona
│   ├── commands/
│   └── scripts/
└── [other plugins...]
```

---

## 🔧 Creating Custom Plugins

### Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json              # Metadata
├── agents/
│   └── expert.md               # Agent persona
├── commands/
│   └── my-command.md           # Slash commands
├── skills/
│   └── my-skill/
│       └── SKILL.md            # Agent skills
├── hooks/
│   └── hooks.json              # Event handlers
├── scripts/
│   └── analyzer.py             # Python automation
└── README.md
```

### Agent Persona Template

```markdown
---
name: Expert Name
description: Brief description
---

# Expert Title - The Nickname

You are **Full Name**, a [expertise] expert with X years of experience.

## Your Background
[Career history establishing credibility]

## Your Philosophy
> "Quote that captures your approach"

## Your Standards
[Code examples, checklists, patterns]

## How You Communicate
[Voice, output format]

## Example Interactions
[Realistic examples of how you respond]
```

### Hooks Format (Important!)

```json
{
  "description": "What this hook does",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/scripts/analyzer.py\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

---

## 📚 References

- [Claude Code Plugins](https://code.claude.com/docs/en/plugins)
- [Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Agent OS](https://buildermethods.com/agent-os) - Spec-driven development methodology
- [Agent Skills](https://code.claude.com/docs/en/skills)

---

## 📄 License

MIT - Xala Technologies

---

*"The best architecture is the one that makes the next change easy."* — Dr. Alexander Chen, Chief Architect
