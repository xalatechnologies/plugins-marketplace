---
description: Autonomous repository analysis capability - Claude will use this skill when analyzing codebases
triggers:
  - analyzing a repository
  - understanding a codebase
  - assessing code quality
  - identifying technical debt
  - preparing for production
---

# Repository Analysis Skill

You have the ability to comprehensively analyze code repositories. Use this skill when:

- The user asks about the state of a codebase
- You need to understand a project's structure
- You're assessing production readiness
- You're identifying issues or technical debt
- You're planning development work

## How to Use This Skill

### Quick Analysis
When you need a fast overview:
1. Check package.json/go.mod/requirements.txt for project type
2. Read README.md for context
3. List directory structure for architecture
4. Identify entry points

### Deep Analysis
When you need comprehensive understanding:
1. Map the full directory structure
2. Identify all modules and their purposes
3. Trace data flows (routes → services → database)
4. Check configuration files for settings
5. Review test coverage
6. Identify patterns and anti-patterns

### Issue Detection
When looking for problems:
1. Search for common security patterns (hardcoded secrets, etc.)
2. Check for files over 300 lines
3. Look for TODO/FIXME comments
4. Verify error handling
5. Check for missing tests

## Output Guidelines

Always structure your analysis output clearly:

```
📦 [Project Name]

🎯 Purpose: [One sentence description]

📊 Quick Stats:
- Language: [Primary language]
- Framework: [Main framework]
- Files: [Count]
- Test Coverage: [Percentage or "Unknown"]

✅ Strengths:
- [Positive finding 1]
- [Positive finding 2]

⚠️ Concerns:
- [Issue 1 with location]
- [Issue 2 with location]

🎯 Recommendations:
1. [Most important action]
2. [Second priority]
```

## Integration with Xala PM

When the Xala PM MCP tools are available, you can:
- Create tasks from identified issues
- Update project health scores
- Log analysis activities
- Sync findings to the dashboard

Always check if these tools are available and use them when appropriate.

