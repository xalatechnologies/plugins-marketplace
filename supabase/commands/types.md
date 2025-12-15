---
description: Generate TypeScript types from Supabase schema
---

# Generate Types Command

Generate TypeScript types from the current Supabase schema.

## Usage

```bash
# Generate types from remote
npx supabase gen types typescript --project-id YOUR_PROJECT_ID > src/types/database.ts

# Generate types from local
npx supabase gen types typescript --local > src/types/database.ts
```

## Generated Types Structure

```typescript
// src/types/database.ts
export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      users: {
        Row: {
          id: string
          email: string
          name: string
          role: string
          org_id: string
          created_at: string
          updated_at: string
        }
        Insert: {
          id?: string
          email: string
          name: string
          role?: string
          org_id: string
          created_at?: string
          updated_at?: string
        }
        Update: {
          id?: string
          email?: string
          name?: string
          role?: string
          org_id?: string
          created_at?: string
          updated_at?: string
        }
      }
      // ... more tables
    }
    Views: {
      // ...
    }
    Functions: {
      // ...
    }
    Enums: {
      // ...
    }
  }
}
```

## Helper Types

```typescript
// src/types/entities.ts
import type { Database } from './database'

// Table row types
export type User = Database['public']['Tables']['users']['Row']
export type Task = Database['public']['Tables']['tasks']['Row']
export type Project = Database['public']['Tables']['projects']['Row']

// Insert types
export type UserInsert = Database['public']['Tables']['users']['Insert']
export type TaskInsert = Database['public']['Tables']['tasks']['Insert']

// Update types
export type UserUpdate = Database['public']['Tables']['users']['Update']
export type TaskUpdate = Database['public']['Tables']['tasks']['Update']

// With relationships
export type UserWithOrg = User & {
  organization: Organization
}

export type TaskWithAssignee = Task & {
  assignee: User | null
}
```

## Client Type Usage

```typescript
// src/lib/supabase/client.ts
import { createBrowserClient } from '@supabase/ssr'
import type { Database } from '@/types/database'

export function createClient() {
  return createBrowserClient<Database>(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
```

## Type-Safe Queries

```typescript
// Now fully typed!
const { data } = await supabase
  .from('users')
  .select('id, name, email')
  .eq('org_id', orgId)
  .single()

// data is typed as Pick<User, 'id' | 'name' | 'email'> | null
```

## Guidelines

1. **Regenerate types** after schema changes
2. **Create helper types** for common patterns
3. **Use strict mode** in TypeScript
4. **Add to CI/CD** to catch type mismatches

