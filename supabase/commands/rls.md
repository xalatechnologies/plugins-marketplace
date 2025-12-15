---
description: Generate RLS policies for a table with common patterns
arguments:
  - name: table
    description: Table name to create policies for
    required: true
  - name: pattern
    description: RLS pattern (own, org, public, custom)
    required: false
    default: org
---

# Create RLS Policies Command

Generate Row Level Security policies for a table.

## Common Patterns

### Own Data Pattern (`pattern=own`)
Users can only access their own data:

```sql
-- Enable RLS
ALTER TABLE public.{table} ENABLE ROW LEVEL SECURITY;

-- Select own records
CREATE POLICY "{table}_select_own"
  ON public.{table}
  FOR SELECT
  USING (user_id = auth.uid());

-- Insert own records
CREATE POLICY "{table}_insert_own"
  ON public.{table}
  FOR INSERT
  WITH CHECK (user_id = auth.uid());

-- Update own records
CREATE POLICY "{table}_update_own"
  ON public.{table}
  FOR UPDATE
  USING (user_id = auth.uid())
  WITH CHECK (user_id = auth.uid());

-- Delete own records
CREATE POLICY "{table}_delete_own"
  ON public.{table}
  FOR DELETE
  USING (user_id = auth.uid());
```

### Organization Pattern (`pattern=org`)
Users can access data within their organization:

```sql
-- Enable RLS
ALTER TABLE public.{table} ENABLE ROW LEVEL SECURITY;

-- Helper function
CREATE OR REPLACE FUNCTION get_user_org_ids(user_id UUID)
RETURNS SETOF UUID AS $$
  SELECT org_id FROM public.org_members WHERE user_id = $1
$$ LANGUAGE SQL SECURITY DEFINER STABLE;

-- Select org records
CREATE POLICY "{table}_select_org"
  ON public.{table}
  FOR SELECT
  USING (org_id IN (SELECT get_user_org_ids(auth.uid())));

-- Insert requires org membership
CREATE POLICY "{table}_insert_org"
  ON public.{table}
  FOR INSERT
  WITH CHECK (org_id IN (SELECT get_user_org_ids(auth.uid())));

-- Update requires org membership
CREATE POLICY "{table}_update_org"
  ON public.{table}
  FOR UPDATE
  USING (org_id IN (SELECT get_user_org_ids(auth.uid())))
  WITH CHECK (org_id IN (SELECT get_user_org_ids(auth.uid())));

-- Delete only for admins
CREATE POLICY "{table}_delete_admin"
  ON public.{table}
  FOR DELETE
  USING (
    org_id IN (SELECT get_user_org_ids(auth.uid())) AND
    EXISTS (
      SELECT 1 FROM public.org_members
      WHERE user_id = auth.uid() AND org_id = {table}.org_id AND role = 'admin'
    )
  );
```

### Public Read Pattern (`pattern=public`)
Anyone can read, but only owners can modify:

```sql
-- Enable RLS
ALTER TABLE public.{table} ENABLE ROW LEVEL SECURITY;

-- Anyone can read
CREATE POLICY "{table}_select_public"
  ON public.{table}
  FOR SELECT
  USING (true);

-- Only owner can insert
CREATE POLICY "{table}_insert_owner"
  ON public.{table}
  FOR INSERT
  WITH CHECK (auth.uid() IS NOT NULL);

-- Only owner can update
CREATE POLICY "{table}_update_owner"
  ON public.{table}
  FOR UPDATE
  USING (created_by = auth.uid());

-- Only owner can delete
CREATE POLICY "{table}_delete_owner"
  ON public.{table}
  FOR DELETE
  USING (created_by = auth.uid());
```

### Role-Based Pattern

```sql
-- Role-based access
CREATE POLICY "{table}_select_role"
  ON public.{table}
  FOR SELECT
  USING (
    CASE
      WHEN get_user_role(auth.uid()) = 'admin' THEN true
      WHEN get_user_role(auth.uid()) = 'pm' THEN project_id IN (SELECT get_pm_projects(auth.uid()))
      ELSE user_id = auth.uid()
    END
  );
```

## Testing RLS

```sql
-- Test as a specific user
SET request.jwt.claim.sub = 'user-uuid-here';
SELECT * FROM public.{table};

-- Reset
RESET request.jwt.claim.sub;
```

## Guidelines

1. **Always test policies** with different user roles
2. **Use helper functions** for complex logic
3. **Mark functions as STABLE** when they only read
4. **Use SECURITY DEFINER** carefully
5. **Consider performance** of policy queries
6. **Document policy intent** with comments

