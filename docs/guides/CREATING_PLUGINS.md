# Creating Plugins

Step-by-step guide to creating custom plugins for the Xala PM marketplace.

---

## Plugin Structure

Every plugin follows this structure:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        # Required: Plugin metadata
├── README.md              # Required: Plugin documentation
├── agents/
│   └── expert.md          # Agent persona definition
├── commands/
│   └── my-command.md      # Slash commands
├── skills/
│   └── my-skill/
│       └── SKILL.md       # Agent skills
├── hooks/
│   └── hooks.json         # Event handlers
└── scripts/
    └── analyzer.py        # Automation scripts
```

---

## Step 1: Create Plugin Manifest

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "my-plugin",
  "description": "What this plugin does in one sentence",
  "version": "1.0.0",
  "author": {
    "name": "Your Name or Organization"
  },
  "category": "development",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "license": "MIT"
}
```

**Category options:**
- `development` - Frontend, backend, mobile
- `testing` - Unit, E2E, performance
- `security` - Security scanning, compliance
- `devops` - CI/CD, infrastructure
- `documentation` - Docs generation
- `orchestration` - Workflow management

---

## Step 2: Create README

Every plugin needs a README.md:

```markdown
# Plugin Name

Brief description of what this plugin provides.

## Features

- Feature 1
- Feature 2

## Commands

### `/command-name`

Description of what this command does.

**Usage:**
\`\`\`
/command-name <arg1> <arg2>
\`\`\`

## Agent

Name and brief description of the agent persona.

## Configuration

Any configuration requirements.
```

---

## Step 3: Create Agent Persona (Optional)

Create `agents/expert.md`:

```markdown
---
name: Agent Name
description: One-line description
---

# Title - The Expert

You are **Full Name**, a [domain] expert with [X] years of experience.

## Background

[2-3 paragraphs establishing expertise and credibility]

## Philosophy

> "Quote that captures your approach"

[Expand on core beliefs]

## Operational Guidelines

### DO

- Specific action 1
- Specific action 2
- Specific action 3

### DO NOT

- Specific anti-pattern 1
- Specific anti-pattern 2
- Specific anti-pattern 3

## Communication Style

How you communicate:
- Tone
- Format preferences
- Level of detail

## Example Interaction

### User Request
"Example user request"

### Your Response
"How you would respond, demonstrating your expertise and style"
```

---

## Step 4: Create Commands

Create `commands/my-command.md`:

```markdown
---
description: Brief description for /help
---

# Command Name

Detailed instructions for Claude on executing this command.

## Parameters

- `param1` (required): Description of first parameter
- `param2` (optional): Description of optional parameter

## Process

1. First step Claude should take
2. Second step
3. Third step

## Output Format

Describe the expected output format.

## Examples

### Example 1: Basic Usage

Input:
\`\`\`
/my-command value1
\`\`\`

Expected behavior:
[Describe what happens]

### Example 2: With Options

Input:
\`\`\`
/my-command value1 --option
\`\`\`

Expected behavior:
[Describe what happens]

## Error Handling

How to handle common errors:

| Error | Resolution |
|-------|------------|
| Missing param1 | Prompt user for required value |
| Invalid value | Explain valid options |
```

---

## Step 5: Create Skills (Optional)

Create `skills/my-skill/SKILL.md`:

```markdown
---
description: What this skill provides
globs:
  - "**/*.ts"
  - "**/*.tsx"
alwaysApply: false
---

# Skill Name

Instructions for Claude when this skill is active.

## When to Apply

Apply this skill when:
- Condition 1
- Condition 2

## Guidelines

### Pattern 1: Name

Description and examples.

\`\`\`typescript
// Example code
\`\`\`

### Pattern 2: Name

Description and examples.

## Checklist

Before completing work, verify:

- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3
```

---

## Step 6: Create Hooks (Optional)

Create `hooks/hooks.json`:

```json
{
  "description": "What these hooks do",
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Instructions for session start"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Instructions before writing files"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/scripts/analyzer.py\" \"${TOOL_INPUT}\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Hook Types

| Event | When Triggered |
|-------|----------------|
| `SessionStart` | New Claude session begins |
| `PreToolUse` | Before any tool is used |
| `PostToolUse` | After any tool is used |
| `Stop` | Session ends |

### Hook Actions

| Type | Purpose |
|------|---------|
| `prompt` | Add instructions to context |
| `command` | Run shell command |

### Matchers

| Matcher | Matches |
|---------|---------|
| `Write` | File write operations |
| `Edit` | File edit operations |
| `Read` | File read operations |
| `.*` | All operations |

---

## Step 7: Create Scripts (Optional)

Create `scripts/analyzer.py`:

```python
#!/usr/bin/env python3
"""
Script description.
"""

import sys
import json


def analyze(file_path: str) -> dict:
    """
    Analyze the given file.
    
    Args:
        file_path: Path to file to analyze
        
    Returns:
        Analysis results
    """
    results = {
        "issues": [],
        "suggestions": []
    }
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Your analysis logic here
        
    except Exception as e:
        results["error"] = str(e)
    
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: analyzer.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    results = analyze(file_path)
    
    if results["issues"]:
        print(f"Found {len(results['issues'])} issues:")
        for issue in results["issues"]:
            print(f"  - {issue}")
    else:
        print("No issues found.")


if __name__ == "__main__":
    main()
```

Make executable:
```bash
chmod +x scripts/analyzer.py
```

---

## Step 8: Register in Marketplace

Add plugin to `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "my-plugin",
      "source": "./my-plugin",
      "description": "What this plugin does",
      "category": "development"
    }
  ]
}
```

---

## Step 9: Test Locally

1. Add marketplace locally:
   ```shell
   /plugin marketplace add /path/to/plugins-marketplace
   ```

2. Install plugin:
   ```shell
   /plugin install my-plugin@xala-marketplace
   ```

3. Restart Claude Code

4. Test commands:
   ```shell
   /my-command
   ```

---

## Validation Checklist

Before submitting:

- [ ] `plugin.json` has all required fields
- [ ] README.md documents all features
- [ ] Commands have clear instructions
- [ ] Hooks follow correct JSON format
- [ ] Scripts are executable
- [ ] No emojis in code/comments/docs
- [ ] Professional language throughout
- [ ] Tested locally with Claude Code

