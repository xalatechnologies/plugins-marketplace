# Backend Development Plugin

Expert backend development agent for APIs, services, and server-side logic.

## Features

### Commands
- `/endpoint <path> <method>` - Create a new API endpoint
- `/service <name>` - Create a new service with business logic

### Agent
Specialized backend agent with expertise in:
- RESTful API design
- Hono and Express frameworks
- PostgreSQL and Supabase
- Authentication/authorization
- Security best practices

### Skills
- **API Skill**: Design, validation, security, performance

### Hooks
- Auto-check security on new API endpoints
- Verify error handling in services

### MCP Tools
- PostgreSQL query execution
- Query plan analysis

## Usage

```bash
# Create a REST endpoint
/endpoint /api/v1/users POST framework=hono

# Create a service
/service UserService entity=user
```

## Installation

```bash
/plugin install backend@xalapm-marketplace
```

