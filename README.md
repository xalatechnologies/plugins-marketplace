# Xala PM Plugin Marketplace

A comprehensive collection of Claude Code plugins for AI-native development and project management.

## ✨ Features

- **21 Specialized Plugins** - Full-stack development, security, compliance, testing
- **Python Script Hooks** - Automated code analysis, security scanning, accessibility checks
- **LLM-Powered Hooks** - Context-aware prompts for code quality
- **MCP Integration** - Connect to external tools and services
- **Group Installation** - Install plugin bundles by role

---

## 🔥 Power Features (Beast Mode)

### Automated Code Analysis

These plugins include **Python scripts** that run automatically on file changes:

| Plugin | Script | What It Does |
|--------|--------|--------------|
| **code-review** | `review-code.py` | Detects security issues, TODOs, console.logs, TypeScript any usage |
| **accessibility** | `check-a11y.py` | WCAG compliance checking for React/JSX components |
| **testing** | `suggest-tests.py` | Suggests tests for new functions, components, hooks, APIs |
| **blockchain** | `security-scan.py` | Smart contract security (reentrancy, DEX violations, tx.origin) |
| **compliance** | `compliance-check.py` | GDPR, PCI-DSS, security token regulation checks |
| **devops** | `ci-validator.py` | CI/CD config security (secrets, permissions, hardcoded keys) |

### How It Works

```
You write code → Claude saves file → Hook runs Python script → 
Script analyzes code → Findings injected as context → Claude sees issues
```

**Example Output (Code Review):**
```
Code review findings:
[SECURITY]
  • Avoid eval() - potential code injection
[CLEANUP]
  • Remove console.log before commit
[TODO]
  • TODO comment found - track in task system
```

---

## 📦 Plugin Categories

### 🧠 Core & Orchestration
| Plugin | Description | Commands |
|--------|-------------|----------|
| **xalapm-core** | MCP integration, activity logging, session context | (auto) |
| **orchestrator** | Multi-agent coordination, task delegation | `/analyze-project`, `/delegate`, `/review-pr` |
| **tasks** | Task management with Xala PM sync | `/task`, `/backlog`, `/generate-tasks` |

### 🔍 Analysis
| Plugin | Description | Commands |
|--------|-------------|----------|
| **repo-analysis** | Analyze codebases, generate inventory, detect issues | `/analyze`, `/inventory`, `/pitfalls`, `/infer-prd` |
| **code-review** | Automated code review with Python analysis | `/review` |

### 📊 Productivity
| Plugin | Description | Commands |
|--------|-------------|----------|
| **project-sync** | Keep Xala PM in sync with your work | `/sync` |
| **planning** | Estimate tasks, break down features | `/estimate`, `/breakdown` |
| **standup** | Generate daily standups and summaries | `/standup`, `/summary` |

### 🔒 Security & Compliance
| Plugin | Description | Commands |
|--------|-------------|----------|
| **compliance** | GDPR, PCI-DSS, security token regulations | `/check-compliance` |
| **blockchain** | Smart contract security scanning | `/audit`, `/contract`, `/validator` |
| **accessibility** | WCAG compliance, GDPR checks | `/wcag-audit`, `/gdpr-check` |

### 💻 Development
| Plugin | Description | Commands |
|--------|-------------|----------|
| **frontend** | React, Remix, Next.js, Tailwind | `/component`, `/page` |
| **backend** | API design, Hono, validation, security | `/endpoint`, `/service` |
| **supabase** | Database, RLS, migrations, auth | `/migration`, `/rls`, `/types` |
| **tauri** | Desktop apps with Rust backend | `/command`, `/plugin` |
| **react** | Hooks, state, patterns, testing | `/hook`, `/context` |
| **mobile** | Expo, React Native cross-platform | `/screen` |

### 🎨 Design & Quality
| Plugin | Description | Commands |
|--------|-------------|----------|
| **design-system** | UI components, theming, accessibility | `/ui-component`, `/tokens` |
| **testing** | Unit, E2E, performance, security tests | `/unit`, `/e2e`, `/performance` |
| **documentation** | API docs, README, JSDoc | `/docs` |
| **devops** | CI/CD with security validation | `/ci` |

---

## 🚀 Installation

### 1. Add the Marketplace

```
/plugin marketplace add https://github.com/xalatechnologies/plugins-marketplace
```

### 2. Install by Group

| Group | Description | Plugins |
|-------|-------------|---------|
| `essential` | Core Xala PM integration | 4 |
| `fullstack` | Web development toolkit | 7 |
| `mobile-dev` | Cross-platform mobile | 5 |
| `desktop-dev` | Native desktop apps | 5 |
| `blockchain-dev` | Web3 & smart contracts | 4 |
| `devops` | CI/CD automation | 4 |
| `qa` | Testing & quality | 4 |
| `pm` | Project management | 7 |
| `compliance` | Security & accessibility | 4 |
| `all` | Complete suite (Beast Mode!) | 21 |

### 3. Use Install Script

```bash
# List available groups
./install.sh --list

# Install by group
./install.sh --group fullstack --scope project
./install.sh --group all --scope user

# See scope details
./install.sh --scopes
```

### Scopes

| Scope | Location | Use Case |
|-------|----------|----------|
| `project` | `.claude/plugins/` | Single project (default) |
| `user` | `~/.claude/plugins/` | All your projects |
| `global` | `/usr/local/share/claude/plugins/` | System-wide |

### 4. Restart Claude Code

> 📖 See [INSTALL.md](./INSTALL.md) for detailed documentation.

---

## 📋 Plugin Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                 # Slash commands
│   └── command-name.md
├── agents/                   # Specialized agents
│   └── agent-name.md
├── skills/                   # Agent Skills
│   └── skill-name/
│       └── SKILL.md
├── hooks/                    # Event handlers (hooks wrapper required!)
│   └── hooks.json
├── scripts/                  # Python/Bash scripts for hooks
│   └── analyzer.py
├── .mcp.json                 # MCP tool configuration
└── README.md                 # Plugin documentation
```

### Hooks Format (Important!)

Plugin hooks require the `hooks` wrapper:

```json
{
  "description": "Plugin description",
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

**Hook Types:**
- `type: "command"` - Run bash/Python scripts
- `type: "prompt"` - LLM-powered evaluation

**Environment Variables:**
- `${CLAUDE_PLUGIN_ROOT}` - Plugin directory path
- `${CLAUDE_PROJECT_DIR}` - Project root path

---

## 🐍 Writing Python Hook Scripts

Scripts receive JSON input via stdin and output JSON to stdout:

```python
#!/usr/bin/env python3
import json
import sys

# Read hook input
input_data = json.load(sys.stdin)
tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})

# Your analysis logic here
issues = analyze(tool_input.get("content", ""))

# Return feedback to Claude
if issues:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "Found issues: " + ", ".join(issues)
        }
    }
    print(json.dumps(output))

sys.exit(0)
```

---

## 🛠 MCP Tool Integrations

Plugins integrate with MCP servers for extended functionality:

| Plugin | MCP Tools | Capabilities |
|--------|-----------|--------------|
| **xalapm-core** | Xala PM MCP | Tasks, activities, phases, dashboard |
| **frontend** | Browser | Component testing, screenshots |
| **backend** | PostgreSQL | Query execution, explain plans |
| **supabase** | Supabase | Schema management, migrations |
| **tauri** | Rust Analyzer | Code analysis, cargo commands |
| **design-system** | Storybook | Component documentation |

---

## 🔧 Development

### Creating New Plugins

```bash
# Create structure
mkdir -p my-plugin/.claude-plugin
mkdir -p my-plugin/{commands,agents,skills/my-skill,hooks,scripts}

# Create plugin.json
cat > my-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-plugin",
  "description": "My custom plugin",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
EOF

# Add to marketplace.json and install
```

### Testing Changes

```bash
/plugin uninstall my-plugin@xala-marketplace
/plugin install my-plugin@xala-marketplace
# Restart Claude Code
```

---

## 📚 Reference

- [Claude Code Plugin Documentation](https://code.claude.com/docs/en/plugins)
- [Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference)
- [Xala PM Documentation](/docs/)

---

## 📄 License

MIT - Xala Technologies
