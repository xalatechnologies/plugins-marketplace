---
description: Database design and optimization expertise for Supabase/PostgreSQL
triggers:
  - creating database tables
  - writing sql queries
  - designing data models
  - optimizing queries
  - working with rls
---

# Database Development Skill

Expert PostgreSQL and Supabase database capabilities.

## Schema Design Patterns

### Soft Deletes
```sql
CREATE TABLE public.items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  -- ... other columns
  deleted_at TIMESTAMPTZ,
  
  -- Partial index for active records
  CONSTRAINT items_active EXCLUDE WHERE (deleted_at IS NULL)
);

-- View for active records
CREATE VIEW public.active_items AS
  SELECT * FROM public.items WHERE deleted_at IS NULL;
```

### Audit Trail
```sql
CREATE TABLE public.audit_log (
  id BIGSERIAL PRIMARY KEY,
  table_name TEXT NOT NULL,
  record_id UUID NOT NULL,
  action TEXT NOT NULL CHECK (action IN ('INSERT', 'UPDATE', 'DELETE')),
  old_data JSONB,
  new_data JSONB,
  user_id UUID REFERENCES auth.users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.audit_log (table_name, record_id, action, old_data, new_data, user_id)
  VALUES (
    TG_TABLE_NAME,
    COALESCE(NEW.id, OLD.id),
    TG_OP,
    CASE WHEN TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN to_jsonb(OLD) END,
    CASE WHEN TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN to_jsonb(NEW) END,
    auth.uid()
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

### Multi-tenancy
```sql
-- Organization-based multi-tenancy
CREATE TABLE public.organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL
);

-- All tables reference org_id
CREATE TABLE public.projects (
  id UUID PRIMARY KEY,
  org_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
  name TEXT NOT NULL
);

-- RLS enforces tenant isolation
CREATE POLICY "projects_org_isolation"
  ON public.projects
  USING (org_id = current_setting('app.current_org_id')::UUID);
```

## Query Optimization

### Use EXPLAIN ANALYZE
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.*, COUNT(t.id) as task_count
FROM users u
LEFT JOIN tasks t ON t.assignee_id = u.id
WHERE u.org_id = 'xxx'
GROUP BY u.id;
```

### Index Strategies
```sql
-- B-tree for equality/range (default)
CREATE INDEX idx_tasks_status ON tasks(status);

-- Composite for multi-column queries
CREATE INDEX idx_tasks_project_status ON tasks(project_id, status);

-- Partial for filtered queries
CREATE INDEX idx_tasks_active ON tasks(assignee_id)
  WHERE status IN ('backlog', 'in_progress');

-- GIN for JSONB/arrays
CREATE INDEX idx_tasks_labels ON tasks USING GIN(labels);

-- GiST for full-text search
CREATE INDEX idx_tasks_search ON tasks USING GiST(to_tsvector('english', title || ' ' || description));
```

### Batch Operations
```typescript
// ❌ Slow: Individual inserts
for (const item of items) {
  await supabase.from('items').insert(item)
}

// ✅ Fast: Batch insert
await supabase.from('items').insert(items)

// ✅ Upsert for idempotency
await supabase.from('items').upsert(items, { onConflict: 'id' })
```

## Common Patterns

### Pagination
```typescript
// Offset pagination (simple but slow for large offsets)
const { data } = await supabase
  .from('items')
  .select('*')
  .range(page * limit, (page + 1) * limit - 1)

// Cursor pagination (efficient for large datasets)
const { data } = await supabase
  .from('items')
  .select('*')
  .gt('created_at', cursor)
  .order('created_at')
  .limit(20)
```

### Full-text Search
```sql
-- Add search column
ALTER TABLE public.tasks ADD COLUMN search_vector tsvector
  GENERATED ALWAYS AS (to_tsvector('english', coalesce(title, '') || ' ' || coalesce(description, ''))) STORED;

CREATE INDEX idx_tasks_fts ON tasks USING GIN(search_vector);

-- Query
SELECT * FROM tasks
WHERE search_vector @@ to_tsquery('english', 'bug & priority');
```

## When to Use

Apply this skill when:
- Designing new tables
- Writing complex queries
- Optimizing slow operations
- Setting up RLS
- Creating migrations

