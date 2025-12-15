# Xala Marketplace - Installation Guide

## Quick Start

### 1. Add the Marketplace

```
/plugin marketplace add https://github.com/xalatechnologies/plugins-marketplace
```

### 2. Choose Installation Scope

| Scope | Flag | Location | Use Case |
|-------|------|----------|----------|
| **Project** | `--project` | `.claude/plugins/` | Project-specific tools |
| **User** | `--user` | `~/.claude/plugins/` | Your personal toolkit |
| **Global** | `--global` | `/usr/local/share/claude/` | Team/shared machines |

### 3. Install by Group

Choose the group that matches your role and scope.

---

## 📦 Plugin Groups

### 🎯 Essential (Recommended Start)
> Core plugins required for Xala PM integration

**Project Install (default):**
```
/plugin install xalapm-core@xala-marketplace --project
/plugin install orchestrator@xala-marketplace --project
/plugin install tasks@xala-marketplace --project
/plugin install repo-analysis@xala-marketplace --project
```

**User Install (available everywhere):**
```
/plugin install xalapm-core@xala-marketplace --user
/plugin install orchestrator@xala-marketplace --user
/plugin install tasks@xala-marketplace --user
/plugin install repo-analysis@xala-marketplace --user
```

---

### 💻 Full Stack Developer
> Complete web development toolkit

**Project Install:**
```
/plugin install xalapm-core@xala-marketplace --project
/plugin install frontend@xala-marketplace --project
/plugin install backend@xala-marketplace --project
/plugin install supabase@xala-marketplace --project
/plugin install react@xala-marketplace --project
/plugin install design-system@xala-marketplace --project
/plugin install testing@xala-marketplace --project
```

**User Install:**
```
/plugin install xalapm-core@xala-marketplace --user
/plugin install frontend@xala-marketplace --user
/plugin install backend@xala-marketplace --user
/plugin install supabase@xala-marketplace --user
/plugin install react@xala-marketplace --user
/plugin install design-system@xala-marketplace --user
/plugin install testing@xala-marketplace --user
```

---

### 📱 Mobile Developer
> Cross-platform mobile development

**Project Install:**
```
/plugin install xalapm-core@xala-marketplace --project
/plugin install mobile@xala-marketplace --project
/plugin install react@xala-marketplace --project
/plugin install design-system@xala-marketplace --project
/plugin install testing@xala-marketplace --project
```

---

### 🖥️ Desktop Developer
> Native desktop application development

**Project Install:**
```
/plugin install xalapm-core@xala-marketplace --project
/plugin install tauri@xala-marketplace --project
/plugin install frontend@xala-marketplace --project
/plugin install react@xala-marketplace --project
/plugin install testing@xala-marketplace --project
```

---

### ⛓️ Blockchain Developer
> Web3 and smart contract development

**Project Install:**
```
/plugin install xalapm-core@xala-marketplace --project
/plugin install blockchain@xala-marketplace --project
/plugin install compliance@xala-marketplace --project
/plugin install testing@xala-marketplace --project
```

---

### 🚀 DevOps Engineer
> CI/CD and infrastructure automation

**User Install (recommended for DevOps):**
```
/plugin install xalapm-core@xala-marketplace --user
/plugin install devops@xala-marketplace --user
/plugin install testing@xala-marketplace --user
/plugin install documentation@xala-marketplace --user
```

---

### 🔍 QA Engineer
> Testing and quality assurance

**User Install:**
```
/plugin install xalapm-core@xala-marketplace --user
/plugin install testing@xala-marketplace --user
/plugin install accessibility@xala-marketplace --user
/plugin install code-review@xala-marketplace --user
```

---

### 📊 Project Manager
> Project management and coordination

**User Install (recommended for PM):**
```
/plugin install xalapm-core@xala-marketplace --user
/plugin install orchestrator@xala-marketplace --user
/plugin install tasks@xala-marketplace --user
/plugin install planning@xala-marketplace --user
/plugin install standup@xala-marketplace --user
/plugin install project-sync@xala-marketplace --user
/plugin install documentation@xala-marketplace --user
```

---

### 🔒 Compliance Officer
> Security, accessibility, and regulatory compliance

**User Install:**
```
/plugin install xalapm-core@xala-marketplace --user
/plugin install compliance@xala-marketplace --user
/plugin install accessibility@xala-marketplace --user
/plugin install testing@xala-marketplace --user
```

---

### 🌟 Complete Suite - Global Install
> Install everything system-wide for all users

**Global Install (requires admin):**
```
/plugin install xalapm-core@xala-marketplace --global
/plugin install orchestrator@xala-marketplace --global
/plugin install repo-analysis@xala-marketplace --global
/plugin install project-sync@xala-marketplace --global
/plugin install planning@xala-marketplace --global
/plugin install standup@xala-marketplace --global
/plugin install tasks@xala-marketplace --global
/plugin install compliance@xala-marketplace --global
/plugin install frontend@xala-marketplace --global
/plugin install backend@xala-marketplace --global
/plugin install supabase@xala-marketplace --global
/plugin install tauri@xala-marketplace --global
/plugin install react@xala-marketplace --global
/plugin install mobile@xala-marketplace --global
/plugin install design-system@xala-marketplace --global
/plugin install testing@xala-marketplace --global
/plugin install accessibility@xala-marketplace --global
/plugin install blockchain@xala-marketplace --global
/plugin install devops@xala-marketplace --global
/plugin install documentation@xala-marketplace --global
/plugin install code-review@xala-marketplace --global
```

---

## 🛠️ Using the Install Script

The install script generates commands for any group and scope combination:

```bash
# List all groups
./install.sh --list

# List scope options
./install.sh --scopes

# Generate project install commands
./install.sh --group essential --scope project

# Generate user install commands  
./install.sh --group fullstack --scope user

# Generate global install commands
./install.sh --group all --scope global

# Single plugin with scope
./install.sh --plugin frontend --scope user
```

### Examples

```bash
# Developer starting a new web project
./install.sh --group fullstack --scope project

# DevOps setting up their machine
./install.sh --group devops --scope user

# Admin setting up shared workstation
./install.sh --group all --scope global
```

---

## 📍 Understanding Scopes

### Project Scope (`--project`)
```
your-project/
└── .claude/
    └── plugins/          ← Plugins installed here
        ├── xalapm-core/
        ├── frontend/
        └── ...
```
- ✅ Plugins only work in this project
- ✅ Each project can have different plugins
- ✅ Clean separation between projects
- ✅ Version controlled with project (optional)

### User Scope (`--user`)
```
~/.claude/
└── plugins/              ← Plugins installed here
    ├── xalapm-core/
    ├── frontend/
    └── ...
```
- ✅ Your plugins follow you across projects
- ✅ Personal configuration persists
- ✅ Good for your standard development toolkit
- ✅ No admin required

### Global Scope (`--global`)
```
/usr/local/share/claude/
└── plugins/              ← Plugins installed here
    ├── xalapm-core/
    ├── frontend/
    └── ...
```
- ✅ Available to all users on machine
- ✅ Consistent tooling across team
- ✅ Single install for shared workstations
- ⚠️ Requires admin/sudo privileges

---

## 🔄 Scope Priority

When the same plugin exists in multiple scopes, project takes priority:

```
1. Project (.claude/plugins/)      ← Highest priority
2. User (~/.claude/plugins/)
3. Global (/usr/local/share/)      ← Lowest priority
```

---

## After Installation

1. **Restart Claude Code** to activate plugins
2. Run `/plugin list` to verify installation
3. Start using your commands!

### Verify Scope

```
/plugin list --project   # Show project plugins
/plugin list --user      # Show user plugins
/plugin list --global    # Show global plugins
/plugin list             # Show all active plugins
```

---

## Uninstall

To remove plugins, use the same scope flag:

```bash
# Project uninstall
/plugin uninstall xalapm-core@xala-marketplace --project

# User uninstall
/plugin uninstall xalapm-core@xala-marketplace --user

# Global uninstall (requires admin)
/plugin uninstall xalapm-core@xala-marketplace --global
```
