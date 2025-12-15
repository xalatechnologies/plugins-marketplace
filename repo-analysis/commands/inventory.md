---
description: Generate a detailed project structure inventory with module purposes and dependencies
arguments:
  - name: format
    description: Output format (tree, markdown, json)
    required: false
    default: markdown
---

# Project Inventory Command

Generate a comprehensive inventory of the project structure.

## What to Include

### 1. Directory Structure
Create a visual tree showing:
- All directories with their purpose
- Key files with brief descriptions
- Configuration files

### 2. Module Breakdown
For each major module/directory:
- **Purpose**: What does this module do?
- **Exports**: What does it provide to other modules?
- **Dependencies**: What does it import from elsewhere?
- **Status**: Complete / Partial / Stub

### 3. Entry Points
Identify and document:
- Application entry points (main files)
- Route handlers (API endpoints, pages)
- CLI commands
- Background jobs/workers

### 4. External Dependencies
List:
- Production dependencies with versions
- Development dependencies
- Peer dependencies
- Flag any with known vulnerabilities

### 5. Configuration Files
Document:
- Build configuration (webpack, vite, etc.)
- TypeScript/ESLint/Prettier settings
- CI/CD configuration
- Docker/deployment config

## Output Format

Based on the format argument:

**tree**: ASCII tree visualization
**markdown**: Detailed markdown document
**json**: Structured JSON for programmatic use

## Example Output (markdown)

```markdown
# Project Inventory: [Name]

## Overview
- **Type**: [Web app / API / Library / Monorepo]
- **Language**: [Primary language]
- **Framework**: [Main framework]

## Directory Structure
[Tree visualization]

## Modules

### `/src/components`
- **Purpose**: UI components
- **Key Files**: Button.tsx, Card.tsx, Modal.tsx
- **Dependencies**: React, Radix UI
- **Status**: ✅ Complete

### `/src/services`
- **Purpose**: Business logic and API calls
- **Key Files**: auth.ts, api.ts
- **Dependencies**: Supabase, fetch
- **Status**: ⚠️ Partial (missing error handling)

[Continue for all modules...]

## Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| react | 18.2.0 | UI framework |
| supabase | 2.x | Backend |
...
```

