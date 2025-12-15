# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Xala PM Plugin Marketplace is a collection of Claude Code plugins featuring expert AI agents, spec-driven workflows, and automated code analysis. It implements a 3-Layer Context System (Standards → Product → Specs) inspired by Agent OS methodology.

## Repository Architecture

```
plugins-marketplace/
├── .claude-plugin/
│   └── marketplace.json       # Plugin registry with 22 plugins
├── xalapm-core/               # Core integration layer (required by all plugins)
│   ├── standards/             # Coding standards
│   └── .mcp.json              # MCP tool configuration
├── orchestrator/              # Master coordinator (priority 100)
├── [plugin-name]/             # Each plugin follows same structure:
│   ├── .claude-plugin/
│   │   └── plugin.json        # Plugin metadata
│   ├── agents/
│   │   └── *.md               # Agent persona definitions
│   ├── commands/
│   │   └── *.md               # Slash command definitions
│   ├── skills/
│   │   └── [skill-name]/
│   │       └── SKILL.md       # Skill definitions
│   ├── hooks/
│   │   └── hooks.json         # Event handlers
│   ├── scripts/
│   │   └── *.py               # Python automation scripts
│   └── README.md
```

## Plugin Categories

- **Core**: xalapm-core (integration protocol)
- **Orchestration**: orchestrator (multi-agent coordination)
- **Development**: frontend, backend, supabase, tauri, react, mobile, design-system
- **Security/Compliance**: blockchain, compliance, accessibility, security
- **Quality/DevOps**: testing, code-review, devops, documentation
- **Productivity**: tasks, planning, standup, project-sync, repo-analysis

## Key Conventions

### Professional Communication
- No emojis in code, comments, commits, or documentation
- Conventional Commits format: `feat:`, `fix:`, `docs:`, `refactor:`
- Technical, factual language only

### Code Standards (SOLID)
- Functions: max 30 lines
- Classes: max 200 lines
- Files: max 300 lines
- No `any` types in TypeScript
- Explicit return types
- Min 80% test coverage

### Plugin Structure Requirements
- `plugin.json` must include: name, description, version, author, keywords, license
- Agent personas use frontmatter with name/description
- Hooks use JSON format with PostToolUse/PreToolUse matchers
- Python scripts triggered via hooks for automated analysis

### Hooks Format
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/scripts/analyzer.py\"",
        "timeout": 10
      }]
    }]
  }
}
```

## Python Automation Scripts

Located in plugin `scripts/` directories:
- `review-code.py` - Code quality analysis
- `check-a11y.py` - WCAG compliance checking
- `suggest-tests.py` - Test coverage suggestions
- `security-scan.py` - Smart contract security
- `compliance-check.py` - Regulatory compliance
- `ci-validator.py` - CI/CD security validation

## Installation Testing

```bash
# List available groups
./install.sh --list

# Generate install commands for a group
./install.sh --group essential --scope project

# Scopes: --project (.claude/plugins/), --user (~/.claude/plugins/), --global (/usr/local/share/claude/plugins/)
```

## Agent Routing

Agents are auto-selected based on:
- File patterns: `*.tsx` → frontend, `api/*.ts` → backend, `*.sol` → blockchain
- Keywords: "security" → OWASP expert, "accessibility" → WCAG expert
- Default: orchestrator for architecture/coordination tasks

## Xala PM Integration

All plugins sync with Xala PM through xalapm-core MCP tools:
- `get_tasks`, `create_task`, `update_task` for task management
- `log_activity` for activity tracking
- `notify_team` for notifications
