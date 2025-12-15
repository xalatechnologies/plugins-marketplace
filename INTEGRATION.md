# Claude CLI & Cursor Integration

> Automatic agent routing works out-of-the-box with both Claude CLI and Cursor.

## Quick Start

### For Claude CLI

1. **Add the marketplace:**
   ```bash
   claude
   /plugin marketplace add https://github.com/xalatechnologies/plugins-marketplace
   ```

2. **Install the core plugin:**
   ```bash
   /plugin install xalapm-core@xala-marketplace
   ```

3. **That's it!** The hooks and skills automatically:
   - Route tasks to appropriate agents
   - Apply quality standards
   - Load relevant skills based on context

### For Cursor

1. **Copy the cursor rules to your project:**
   ```bash
   cp xalapm-core/.cursorrules /path/to/your/project/.cursorrules
   ```

2. **Copy the CLAUDE.md file:**
   ```bash
   cp xalapm-core/CLAUDE.md /path/to/your/project/CLAUDE.md
   ```

3. **Cursor reads these automatically** and applies agent routing.

---

## How Automatic Routing Works

### File-Based Routing

When you're working on a file, the system detects the file type and applies the right agent:

| You're Editing | Agent Selected | Expertise Applied |
|----------------|----------------|-------------------|
| `Button.tsx` | `@frontend-dev` | React, UI excellence, accessibility |
| `api/users.ts` | `@backend-dev` | API design, validation, security |
| `users.test.ts` | `@testing-specialist` | TDD, coverage, test patterns |
| `auth/login.ts` | `@owasp-expert` | OWASP A07, secure auth |
| `schema.sql` | `@supabase-dev` | Database design, RLS |
| `deploy.yml` | `@devops-engineer` | CI/CD, automation |

### Keyword-Based Routing

Your request is analyzed for domain keywords:

| Your Request Contains | Agent Selected |
|----------------------|----------------|
| "password", "auth", "token" | `@owasp-expert` |
| "accessibility", "a11y", "wcag" | `@accessibility-expert` |
| "gdpr", "privacy", "consent" | `@compliance-officer` |
| "soc2", "audit", "controls" | `@soc2-auditor` |
| "smart contract", "solidity" | `@blockchain-expert` |
| "deploy", "ci/cd", "docker" | `@devops-engineer` |

### Example: Natural Conversation

```
You: "Add a password reset feature"

[Automatic routing detects: "password" → security-sensitive]

Claude/Cursor responds as @owasp-expert:
"I'll implement password reset following OWASP A07 guidelines:

1. Generate cryptographically secure reset token (256-bit)
2. Token expires in 15 minutes
3. One-time use (invalidated after use)
4. Rate limit: 3 requests per hour per email
5. No information leakage (same response for valid/invalid emails)

Let me start with the backend API..."
```

---

## Configuration Files

### `.cursorrules` (For Cursor)

Place in your project root. Cursor reads this automatically.

```bash
cp xalapm-core/.cursorrules /your/project/.cursorrules
```

### `CLAUDE.md` (For Claude CLI)

Claude CLI reads this for project context.

```bash
cp xalapm-core/CLAUDE.md /your/project/CLAUDE.md
```

### `hooks.json` (For Claude CLI Plugins)

Automatically loaded when you install the plugin:

```bash
/plugin install xalapm-core@xala-marketplace
```

---

## Verify It's Working

### In Claude CLI

Start a session and you should see:
```
[Session initialized with Xala PM agent routing]
```

Ask about a security topic:
```
You: "How should I store user passwords?"

Response starts with:
[Acting as @owasp-expert - Dr. Aisha Thompson]
"Never store passwords in plain text. Use bcrypt with cost factor 12+..."
```

### In Cursor

Open a React component file and ask for changes:
```
You: "Add loading state to this button"

Response starts with:
[Acting as @frontend-dev - Sarah Kim]
"I'll add a loading state with proper UX patterns..."
```

---

## Full Plugin Installation

For the complete experience, install all relevant plugins:

### Essential (Everyone)
```bash
/plugin install xalapm-core@xala-marketplace
/plugin install orchestrator@xala-marketplace
```

### Development
```bash
/plugin install frontend@xala-marketplace
/plugin install backend@xala-marketplace
/plugin install testing@xala-marketplace
```

### Security & Compliance
```bash
/plugin install security@xala-marketplace
/plugin install compliance@xala-marketplace
/plugin install accessibility@xala-marketplace
```

### Or use the install script:
```bash
./install.sh --group fullstack
./install.sh --group security
```

---

## Customization

### Override Agent Selection

You can always explicitly request a specific agent:

```
You: "@owasp-expert Review this code for security issues"
```

### Disable Auto-Routing

Remove or comment out the SessionStart hook in `hooks/hooks.json`:

```json
{
  "hooks": {
    // "SessionStart": [ ... ]  // Commented out
  }
}
```

### Add Custom Routing Rules

Edit `xalapm-core/skills/agent-router.md` to add your own patterns:

```yaml
my_custom_patterns:
  keywords: [my-keyword, another-keyword]
  files: [my-domain/*, **/my-pattern.*]
  agent: "@my-agent"
  persona: "My Custom Expert"
```

---

## Troubleshooting

### Agent not automatically selected?

1. Check hooks are enabled:
   ```bash
   /plugin list  # Verify xalapm-core is installed
   ```

2. Verify hooks.json is valid:
   ```bash
   cat xalapm-core/hooks/hooks.json | jq .
   ```

3. Restart Claude CLI session

### Cursor not applying rules?

1. Verify `.cursorrules` is in project root
2. Check file isn't in `.gitignore`
3. Restart Cursor

### Want to see routing decisions?

Add to your prompt:
```
"(Show your agent selection reasoning)"
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Your Request                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Context Analysis                           │
│  • File patterns                                             │
│  • Keywords                                                  │
│  • Action type                                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Agent Router                              │
│  • Match to routing rules                                    │
│  • Select primary agent                                      │
│  • Identify secondary agents                                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Agent Activation                           │
│  • Load agent persona                                        │
│  • Apply agent guidelines (DO/DON'T)                        │
│  • Load relevant skills                                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  Quality Standards                           │
│  • QUALITY_STANDARDS.md always applied                       │
│  • Security checks for sensitive contexts                    │
│  • Accessibility checks for UI contexts                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Response                                  │
│  [Acting as @agent-name - Persona Name]                     │
│  Expert-level implementation with quality gates              │
└─────────────────────────────────────────────────────────────┘
```

---

## Best Practices

1. **Let routing happen naturally** - Don't over-specify agents
2. **Trust the expertise** - Agents know their domain
3. **Check for multi-domain tasks** - Some tasks need multiple agents
4. **Quality is automatic** - Standards are always enforced
5. **Security is prioritized** - Security agents take precedence

---

*Questions? Check the agent registry at `xalapm-core/AGENT_REGISTRY.md`*

