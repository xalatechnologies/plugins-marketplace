---
description: Create a new Supabase migration with proper structure and RLS policies
arguments:
  - name: name
    description: Migration name (e.g., create_users_table)
    required: true
  - name: type
    description: Migration type (table, rls, function, trigger, index)
    required: false
    default: table
---

# Create Migration Command

Generate a new Supabase migration file.

## File Location
```
supabase/migrations/
└── YYYYMMDDHHMMSS_migration_name.sql
```

## Table Migration Template

```sql
-- supabase/migrations/20241215120000_create_users.sql

-- Create table
CREATE TABLE IF NOT EXISTS public.users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'user' CHECK (role IN ('user', 'admin', 'pm')),
  org_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
  avatar_url TEXT,
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS users_org_id_idx ON public.users(org_id);
CREATE INDEX IF NOT EXISTS users_email_idx ON public.users(email);
CREATE INDEX IF NOT EXISTS users_role_idx ON public.users(role);

-- Enable RLS
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

-- RLS Policies

-- Users can read their own data
CREATE POLICY "users_select_own"
  ON public.users
  FOR SELECT
  USING (auth.uid() = id);

-- Users can read org members
CREATE POLICY "users_select_org"
  ON public.users
  FOR SELECT
  USING (org_id IN (
    SELECT org_id FROM public.users WHERE id = auth.uid()
  ));

-- Only admins can insert users
CREATE POLICY "users_insert_admin"
  ON public.users
  FOR INSERT
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM public.users
      WHERE id = auth.uid() AND role = 'admin'
    )
  );

-- Users can update their own profile
CREATE POLICY "users_update_own"
  ON public.users
  FOR UPDATE
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

-- Updated at trigger
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_updated_at
  BEFORE UPDATE ON public.users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();

-- Grant permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON public.users TO authenticated;
GRANT SELECT ON public.users TO anon;
```

## RLS-Only Migration

```sql
-- supabase/migrations/20241215120100_users_rls.sql

-- Drop existing policies
DROP POLICY IF EXISTS "users_select_own" ON public.users;

-- Recreate with updated logic
CREATE POLICY "users_select_own"
  ON public.users
  FOR SELECT
  USING (
    auth.uid() = id OR
    auth.uid() IN (
      SELECT user_id FROM public.team_members WHERE org_id = users.org_id
    )
  );
```

## Function Migration

```sql
-- supabase/migrations/20241215120200_get_user_stats.sql

CREATE OR REPLACE FUNCTION get_user_stats(user_id UUID)
RETURNS TABLE (
  tasks_completed INT,
  tasks_in_progress INT,
  avg_completion_time INTERVAL
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    COUNT(*) FILTER (WHERE status = 'done')::INT,
    COUNT(*) FILTER (WHERE status = 'in_progress')::INT,
    AVG(completed_at - created_at) FILTER (WHERE status = 'done')
  FROM public.tasks
  WHERE assignee_id = user_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

## Index Migration

```sql
-- supabase/migrations/20241215120300_add_tasks_indexes.sql

-- Composite index for common queries
CREATE INDEX CONCURRENTLY IF NOT EXISTS tasks_project_status_idx
  ON public.tasks(project_id, status);

-- Partial index for active tasks
CREATE INDEX CONCURRENTLY IF NOT EXISTS tasks_active_idx
  ON public.tasks(assignee_id)
  WHERE status IN ('backlog', 'in_progress', 'review');

-- GIN index for JSONB
CREATE INDEX CONCURRENTLY IF NOT EXISTS tasks_metadata_idx
  ON public.tasks USING GIN(metadata);
```

## Guidelines

1. **Always enable RLS** on new tables
2. **Create appropriate indexes** for query patterns
3. **Use SECURITY DEFINER** carefully (only when needed)
4. **Add updated_at triggers** for all tables
5. **Use proper constraints** (CHECK, UNIQUE, REFERENCES)
6. **Grant appropriate permissions** (authenticated, anon)
7. **Use CONCURRENTLY** for index creation on large tables

