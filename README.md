# Xala PM Plugin Marketplace

A comprehensive collection of Claude Code plugins for AI-native development and project management.

## 📦 Plugin Categories

### 🔍 Analysis
| Plugin | Description | Commands |
|--------|-------------|----------|
| **repo-analysis** | Analyze codebases, generate inventory, detect issues | `/analyze`, `/inventory`, `/pitfalls`, `/infer-prd`, `/production-tasks` |

### 📊 Productivity
| Plugin | Description | Commands |
|--------|-------------|----------|
| **project-sync** | Keep Xala PM in sync with your work | `/sync`, `/sync start`, `/sync done` |
| **planning** | Estimate tasks, break down features | `/estimate`, `/breakdown` |
| **standup** | Generate daily standups and summaries | `/standup`, `/summary` |

### 🔒 Security
| Plugin | Description | Commands |
|--------|-------------|----------|
| **compliance** | Check regulatory rules for security tokens | `/check-compliance` |

### 💻 Development
| Plugin | Description | Commands |
|--------|-------------|----------|
| **frontend** | React, Remix, Next.js, Tailwind | `/component`, `/page` |
| **backend** | API design, Hono, validation, security | `/endpoint`, `/service` |
| **supabase** | Database, RLS, migrations, auth | `/migration`, `/rls`, `/types` |
| **tauri** | Desktop apps with Rust backend | `/command`, `/plugin` |
| **react** | Hooks, state, patterns, testing | `/hook`, `/context` |

### 🎨 Design
| Plugin | Description | Commands |
|--------|-------------|----------|
| **design-system** | UI components, theming, accessibility | `/ui-component`, `/tokens` |

---

## 🚀 Installation

### Prerequisites
- [Claude Code](https://code.claude.com/docs/) installed
- Xala PM project cloned locally

### Add the Marketplace

```bash
# Start Claude Code
claude

# Add the Xala PM marketplace
/plugin marketplace add /path/to/xalapm/plugins
```

### Install All Plugins

```bash
# Analysis
/plugin install repo-analysis@xalapm-marketplace

# Productivity
/plugin install project-sync@xalapm-marketplace
/plugin install planning@xalapm-marketplace
/plugin install standup@xalapm-marketplace

# Security
/plugin install compliance@xalapm-marketplace

# Development
/plugin install frontend@xalapm-marketplace
/plugin install backend@xalapm-marketplace
/plugin install supabase@xalapm-marketplace
/plugin install tauri@xalapm-marketplace
/plugin install react@xalapm-marketplace

# Design
/plugin install design-system@xalapm-marketplace
```

### Restart Claude Code
After installing, restart Claude Code to activate the plugins.

---

## 📋 Plugin Structure

Each plugin follows the standard Claude Code plugin structure:

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
├── hooks/                    # Event handlers
│   └── hooks.json
├── .mcp.json                 # MCP tool configuration
└── README.md                 # Plugin documentation
```

---

## 🛠 MCP Tool Integrations

Plugins integrate with various MCP servers for extended functionality:

| Plugin | MCP Servers | Capabilities |
|--------|-------------|--------------|
| **frontend** | Browser, Lighthouse | Testing, performance audits |
| **backend** | PostgreSQL | Query execution, explain plans |
| **supabase** | Supabase | Schema management, migrations |
| **tauri** | Rust Analyzer | Code analysis, cargo commands |
| **react** | React DevTools | Component inspection, profiling |
| **design-system** | Storybook, Figma | Documentation, design specs |

---

## 🔧 Development

### Creating New Plugins

1. Create plugin directory:
```bash
mkdir -p my-plugin/.claude-plugin
mkdir -p my-plugin/{commands,agents,skills/my-skill,hooks}
```

2. Create plugin manifest:
```json
// my-plugin/.claude-plugin/plugin.json
{
  "name": "my-plugin",
  "description": "My custom plugin",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

3. Add commands (`commands/*.md`), agents (`agents/*.md`), skills (`skills/*/SKILL.md`), hooks (`hooks/hooks.json`)

4. Add to marketplace manifest:
```json
// plugins/.claude-plugin/marketplace.json
{
  "plugins": [
    {
      "name": "my-plugin",
      "source": "./my-plugin",
      "description": "My custom plugin"
    }
  ]
}
```

5. Install and test:
```bash
/plugin uninstall my-plugin@xalapm-marketplace
/plugin install my-plugin@xalapm-marketplace
```

### Testing Plugins Locally

```bash
# Uninstall current version
/plugin uninstall plugin-name@xalapm-marketplace

# Reinstall to pick up changes
/plugin install plugin-name@xalapm-marketplace

# Restart Claude Code
```

---

## 📚 Reference

- [Claude Code Plugin Documentation](https://github.com/anthropics/claude-code/tree/main/plugins)
- [Claude Code Docs](https://code.claude.com/docs/)
- [Xala PM Documentation](/docs/)

---

## 📄 License

MIT - Xala Technologies
