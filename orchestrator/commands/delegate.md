---
description: Delegate a task to the appropriate specialized agent
arguments:
  - name: task
    description: Task description or type
    required: true
  - name: agent
    description: Specific agent to use (auto if not specified)
    required: false
---

# Delegate Command

Route tasks to the most appropriate specialized agent.

## Agent Registry

```typescript
const AGENT_REGISTRY = {
  // Analysis
  'repo-analysis': {
    triggers: ['analyze repo', 'project structure', 'codebase overview'],
    capabilities: ['inventory', 'prd-inference', 'pitfall-detection'],
  },
  
  // Development
  'frontend': {
    triggers: ['react', 'component', 'ui', 'page', 'layout'],
    capabilities: ['create-component', 'create-page', 'styling'],
  },
  'backend': {
    triggers: ['api', 'endpoint', 'server', 'rest'],
    capabilities: ['create-endpoint', 'create-service', 'validation'],
  },
  'supabase': {
    triggers: ['database', 'migration', 'rls', 'query', 'schema'],
    capabilities: ['migration', 'rls-policy', 'type-generation'],
  },
  'react': {
    triggers: ['hook', 'context', 'state', 'effect'],
    capabilities: ['create-hook', 'create-context', 'optimization'],
  },
  'blockchain': {
    triggers: ['contract', 'solidity', 'web3', 'validator', 'ethereum'],
    capabilities: ['create-contract', 'audit', 'deploy', 'web3-call'],
  },
  'tauri': {
    triggers: ['desktop', 'tauri', 'rust', 'native'],
    capabilities: ['create-command', 'plugin-setup'],
  },
  'mobile': {
    triggers: ['mobile', 'expo', 'react-native', 'ios', 'android'],
    capabilities: ['create-screen', 'navigation', 'native-modules'],
  },
  
  // Quality
  'testing': {
    triggers: ['test', 'e2e', 'unit', 'coverage', 'performance'],
    capabilities: ['e2e-test', 'unit-test', 'performance-test', 'security-test'],
  },
  'accessibility': {
    triggers: ['wcag', 'a11y', 'accessibility', 'gdpr', 'compliance'],
    capabilities: ['wcag-audit', 'gdpr-check', 'nsm-audit'],
  },
  'code-review': {
    triggers: ['review', 'pr', 'quality', 'refactor'],
    capabilities: ['review-code', 'suggest-refactor'],
  },
  
  // Design
  'design-system': {
    triggers: ['design', 'ui-component', 'tokens', 'theme'],
    capabilities: ['create-ui-component', 'define-tokens'],
  },
  
  // DevOps
  'devops': {
    triggers: ['deploy', 'ci', 'cd', 'docker', 'kubernetes'],
    capabilities: ['setup-ci', 'create-dockerfile', 'deploy'],
  },
  
  // Documentation
  'documentation': {
    triggers: ['docs', 'readme', 'api-docs', 'changelog'],
    capabilities: ['generate-docs', 'update-readme', 'api-reference'],
  },
  
  // Project Management
  'tasks': {
    triggers: ['task', 'backlog', 'sprint', 'todo'],
    capabilities: ['create-task', 'update-task', 'backlog-manage'],
  },
  'planning': {
    triggers: ['estimate', 'plan', 'breakdown', 'story'],
    capabilities: ['estimate', 'breakdown'],
  },
}
```

## Routing Logic

```typescript
function routeToAgent(task: string): Agent {
  const taskLower = task.toLowerCase()
  
  // Check each agent's triggers
  for (const [agent, config] of Object.entries(AGENT_REGISTRY)) {
    if (config.triggers.some(trigger => taskLower.includes(trigger))) {
      return agent as Agent
    }
  }
  
  // Default to orchestrator for complex tasks
  return 'orchestrator'
}

// Multi-agent routing for complex tasks
function routeToMultipleAgents(task: string): Agent[] {
  const agents: Agent[] = []
  const taskLower = task.toLowerCase()
  
  for (const [agent, config] of Object.entries(AGENT_REGISTRY)) {
    if (config.triggers.some(trigger => taskLower.includes(trigger))) {
      agents.push(agent as Agent)
    }
  }
  
  return agents.length > 0 ? agents : ['orchestrator']
}
```

## Usage Examples

```bash
# Auto-route based on task description
/delegate "Create a user registration form with validation"
→ Routes to: frontend, react

/delegate "Set up RLS policies for the users table"
→ Routes to: supabase

/delegate "Audit the smart contract for vulnerabilities"
→ Routes to: blockchain

/delegate "Add E2E tests for the checkout flow"
→ Routes to: testing

/delegate "Make the dashboard accessible"
→ Routes to: accessibility, frontend

# Explicit agent selection
/delegate "Create login component" agent=frontend

# Complex multi-agent task
/delegate "Review and improve the entire authentication system"
→ Routes to: backend, frontend, testing, security, code-review
```

## Response Format

```
🎯 TASK DELEGATION
═══════════════════════════════════════════════════════════════

Task: "Create a user registration form with validation"

ROUTING DECISION
───────────────────────────────────────────────────────────────
Primary Agent:  frontend
Supporting:     react
Reason:         Task involves UI component creation with form handling

DELEGATED TO: @frontend-agent
───────────────────────────────────────────────────────────────

[Frontend Agent takes over with /component create command...]
```

