# Quickstart Guide

Get up and running with Xala PM plugins in 5 minutes.

---

## Prerequisites

- Claude Code installed and working
- Git installed
- Terminal access

---

## Step 1: Add the Marketplace

In Claude Code, run:

```shell
/plugin marketplace add https://github.com/xalatechnologies/plugins-marketplace
```

Or for local development:

```shell
/plugin marketplace add /path/to/local/plugins-marketplace
```

---

## Step 2: Install Plugins

### Option A: Install by Group (Recommended)

```bash
# Download and run install script
./install.sh --group essential --scope project
```

Available groups:
| Group | Description | Plugins |
|-------|-------------|---------|
| `essential` | Core functionality | xalapm-core, orchestrator, tasks, documentation |
| `fullstack` | Web development | + frontend, backend, supabase, testing |
| `blockchain-dev` | Web3 development | + blockchain, security, compliance |
| `qa` | Quality engineering | + testing, code-review, accessibility |
| `all` | Everything | All 21 plugins |

### Option B: Install Individual Plugins

```shell
/plugin install xalapm-core@xala-marketplace
/plugin install orchestrator@xala-marketplace
/plugin install frontend@xala-marketplace
```

---

## Step 3: Restart Claude Code

After installation, restart Claude Code to activate plugins.

---

## Step 4: Verify Installation

```shell
/help
```

You should see new commands like `/spec`, `/implement`, `/component`, etc.

---

## First Commands to Try

### Create a Specification

```
/spec user-authentication
```

Creates a detailed specification before coding.

### Generate a Component

```
/component Button primary
```

Generates a React component following UI standards.

### Create an API Endpoint

```
/endpoint POST /api/users
```

Generates a backend API endpoint.

### Run Quality Gate

```
/quality-gate SPEC-2024-001
```

Verifies implementation meets all standards.

---

## Understanding the Workflow

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  SPEC   │ ─> │ DESIGN  │ ─> │IMPLEMENT│ ─> │ VERIFY  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

1. **Spec First**: Create specification with acceptance criteria
2. **Design**: Define architecture and data models
3. **Implement**: Code following the specification
4. **Verify**: Run quality gates and tests

---

## Agent Routing

Agents are selected automatically based on context:

| File Type | Agent Activated |
|-----------|-----------------|
| `.tsx`, `.jsx`, `.css` | Frontend Developer (Sarah Kim) |
| `api/`, `server/` | Backend Developer (Dr. Marcus Rivera) |
| `.test.ts`, `.spec.ts` | Testing Specialist (Dr. Elena Vasquez) |
| `auth/`, `security/` | OWASP Expert (Dr. Aisha Thompson) |

No need to specify agents manually - they engage based on what you're working on.

---

## Key Files to Know

| File | Purpose |
|------|---------|
| `xalapm-core/CLAUDE.md` | Agent routing rules (Claude CLI) |
| `xalapm-core/.cursorrules` | Agent routing rules (Cursor) |
| `xalapm-core/standards/QUALITY_STANDARDS.md` | Quality standards |
| `xalapm-core/templates/SPEC_TEMPLATE.md` | Specification template |

---

## Next Steps

- Read the [Developer Guide](./DEVELOPER_GUIDE.md) for in-depth usage
- Check [Plugin Reference](../plugins/) for individual plugin docs
- See [CONTRIBUTING.md](../CONTRIBUTING.md) to add your own plugins

