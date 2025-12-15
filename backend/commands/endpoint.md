---
description: Create a new API endpoint with validation, error handling, and documentation
arguments:
  - name: path
    description: API path (e.g., /api/v1/users)
    required: true
  - name: method
    description: HTTP method (GET, POST, PUT, DELETE)
    required: true
  - name: framework
    description: Backend framework (hono, nextjs, remix)
    required: false
    default: hono
---

# Create Endpoint Command

Generate a new API endpoint with proper structure, validation, and error handling.

## Hono Endpoint

```typescript
// app/api/v1/users/route.ts
import { Hono } from 'hono'
import { zValidator } from '@hono/zod-validator'
import { z } from 'zod'
import { createClient } from '@/lib/supabase/server'
import { DomainError } from '@/domain/errors'

const app = new Hono()

// Request validation schema
const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2).max(100),
  role: z.enum(['user', 'admin']).default('user'),
})

// Response type
interface UserResponse {
  id: string
  email: string
  name: string
  role: string
  created_at: string
}

// GET /api/v1/users
app.get('/', async (c) => {
  const supabase = createClient(c.req.raw)
  
  const { data, error } = await supabase
    .from('users')
    .select('*')
    .order('created_at', { ascending: false })
  
  if (error) {
    throw new DomainError('FETCH_FAILED', 500, 'Failed to fetch users')
  }
  
  return c.json(data)
})

// POST /api/v1/users
app.post('/', zValidator('json', createUserSchema), async (c) => {
  const body = c.req.valid('json')
  const supabase = createClient(c.req.raw)
  
  const { data, error } = await supabase
    .from('users')
    .insert(body)
    .select()
    .single()
  
  if (error) {
    if (error.code === '23505') {
      throw new DomainError('DUPLICATE', 409, 'User already exists')
    }
    throw new DomainError('CREATE_FAILED', 500, 'Failed to create user')
  }
  
  return c.json(data, 201)
})

export default app
```

## Next.js API Route

```typescript
// app/api/v1/users/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { z } from 'zod'
import { createClient } from '@/lib/supabase/server'
import { safeParseOrThrow } from '@/domain/validators'

const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2).max(100),
})

export async function GET() {
  const supabase = await createClient()
  
  const { data, error } = await supabase
    .from('users')
    .select('*')
  
  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }
  
  return NextResponse.json(data)
}

export async function POST(request: NextRequest) {
  const body = await request.json()
  const validated = safeParseOrThrow(createUserSchema, body)
  
  const supabase = await createClient()
  
  const { data, error } = await supabase
    .from('users')
    .insert(validated)
    .select()
    .single()
  
  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }
  
  return NextResponse.json(data, { status: 201 })
}
```

## Remix Action/Loader

```typescript
// app/routes/api.v1.users.ts
import { json, type ActionFunctionArgs, type LoaderFunctionArgs } from '@remix-run/node'
import { z } from 'zod'
import { createClient } from '@/services/supabase.server'
import { safeParseOrThrow } from '@/domain/validators'

const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2).max(100),
})

export async function loader({ request }: LoaderFunctionArgs) {
  const supabase = createClient(request)
  
  const { data, error } = await supabase
    .from('users')
    .select('*')
  
  if (error) {
    return json({ error: error.message }, { status: 500 })
  }
  
  return json(data)
}

export async function action({ request }: ActionFunctionArgs) {
  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, { status: 405 })
  }
  
  const body = await request.json()
  const validated = safeParseOrThrow(createUserSchema, body)
  
  const supabase = createClient(request)
  
  const { data, error } = await supabase
    .from('users')
    .insert(validated)
    .select()
    .single()
  
  if (error) {
    return json({ error: error.message }, { status: 500 })
  }
  
  return json(data, { status: 201 })
}
```

## Guidelines

1. **Always validate input** with Zod schemas
2. **Use DomainError** for consistent error handling
3. **Return proper HTTP status codes**
4. **Document endpoints** with OpenAPI comments
5. **Log important operations** for debugging
6. **Rate limit** sensitive endpoints
7. **Authenticate** protected routes

