# Supabase Development Plugin

Expert Supabase development agent for database design, RLS, auth, and more.

## Features

### Commands
- `/migration <name>` - Create a new database migration
- `/rls <table>` - Generate RLS policies for a table
- `/types` - Generate TypeScript types from schema

### Agent
Specialized Supabase agent with expertise in:
- PostgreSQL database design
- Row Level Security policies
- Supabase Auth
- Realtime subscriptions
- Edge Functions
- Query optimization

### Skills
- **Database Skill**: Schema design, optimization, migrations

### Hooks
- Validate new migration files
- Check for missing RLS policies

### MCP Tools
- Direct SQL querying
- Table listing and description
- RLS policy management
- Migration execution
- Type generation

## Usage

```bash
# Create a migration
/migration create_tasks_table type=table

# Generate RLS policies
/rls tasks pattern=org

# Generate TypeScript types
/types
```

## Installation

```bash
/plugin install supabase@xalapm-marketplace
```

## Best Practices

This plugin enforces:
- RLS on all user-facing tables
- Proper indexes for query patterns
- Updated_at triggers
- Type-safe database access

