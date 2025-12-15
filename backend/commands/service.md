---
description: Create a new service with business logic, proper typing, and error handling
arguments:
  - name: name
    description: Service name (e.g., UserService)
    required: true
  - name: entity
    description: Primary entity this service manages
    required: false
---

# Create Service Command

Generate a new service module for business logic.

## Service Structure

```
src/services/
└── user/
    ├── index.ts           # Re-exports
    ├── user.service.ts    # Main service
    ├── user.types.ts      # Types
    └── user.test.ts       # Tests
```

## Service Template

```typescript
// src/services/user/user.service.ts
import { z } from 'zod'
import { createClient } from '@/lib/supabase/server'
import { DomainError } from '@/domain/errors'
import type { Database } from '@/types/database'

// Types
type User = Database['public']['Tables']['users']['Row']
type UserInsert = Database['public']['Tables']['users']['Insert']
type UserUpdate = Database['public']['Tables']['users']['Update']

// Validation schemas
const createUserSchema = z.object({
  email: z.string().email('Invalid email address'),
  name: z.string().min(2, 'Name must be at least 2 characters'),
  role: z.enum(['user', 'admin']).default('user'),
})

const updateUserSchema = createUserSchema.partial()

// Service class
export class UserService {
  constructor(private supabase: ReturnType<typeof createClient>) {}

  /**
   * Get all users with optional filtering
   */
  async list(options?: {
    limit?: number
    offset?: number
    role?: string
  }): Promise<User[]> {
    let query = this.supabase
      .from('users')
      .select('*')
      .order('created_at', { ascending: false })

    if (options?.limit) {
      query = query.limit(options.limit)
    }
    if (options?.offset) {
      query = query.range(options.offset, options.offset + (options.limit || 10) - 1)
    }
    if (options?.role) {
      query = query.eq('role', options.role)
    }

    const { data, error } = await query

    if (error) {
      throw new DomainError('FETCH_FAILED', 500, 'Failed to fetch users', error)
    }

    return data
  }

  /**
   * Get a single user by ID
   */
  async getById(id: string): Promise<User> {
    const { data, error } = await this.supabase
      .from('users')
      .select('*')
      .eq('id', id)
      .single()

    if (error) {
      if (error.code === 'PGRST116') {
        throw new DomainError('NOT_FOUND', 404, `User ${id} not found`)
      }
      throw new DomainError('FETCH_FAILED', 500, 'Failed to fetch user', error)
    }

    return data
  }

  /**
   * Create a new user
   */
  async create(input: z.infer<typeof createUserSchema>): Promise<User> {
    // Validate input
    const validated = createUserSchema.parse(input)

    // Check for duplicates
    const existing = await this.findByEmail(validated.email)
    if (existing) {
      throw new DomainError('DUPLICATE', 409, 'User with this email already exists')
    }

    // Create user
    const { data, error } = await this.supabase
      .from('users')
      .insert(validated)
      .select()
      .single()

    if (error) {
      throw new DomainError('CREATE_FAILED', 500, 'Failed to create user', error)
    }

    return data
  }

  /**
   * Update an existing user
   */
  async update(id: string, input: z.infer<typeof updateUserSchema>): Promise<User> {
    // Validate input
    const validated = updateUserSchema.parse(input)

    // Ensure user exists
    await this.getById(id)

    // Update user
    const { data, error } = await this.supabase
      .from('users')
      .update(validated)
      .eq('id', id)
      .select()
      .single()

    if (error) {
      throw new DomainError('UPDATE_FAILED', 500, 'Failed to update user', error)
    }

    return data
  }

  /**
   * Delete a user
   */
  async delete(id: string): Promise<void> {
    // Ensure user exists
    await this.getById(id)

    const { error } = await this.supabase
      .from('users')
      .delete()
      .eq('id', id)

    if (error) {
      throw new DomainError('DELETE_FAILED', 500, 'Failed to delete user', error)
    }
  }

  /**
   * Find user by email
   */
  async findByEmail(email: string): Promise<User | null> {
    const { data, error } = await this.supabase
      .from('users')
      .select('*')
      .eq('email', email)
      .single()

    if (error) {
      if (error.code === 'PGRST116') {
        return null
      }
      throw new DomainError('FETCH_FAILED', 500, 'Failed to find user', error)
    }

    return data
  }
}

// Factory function
export function createUserService(supabase: ReturnType<typeof createClient>) {
  return new UserService(supabase)
}
```

## Guidelines

1. **Single Responsibility**: One service per entity/domain
2. **Dependency Injection**: Pass Supabase client to constructor
3. **Validation**: Always validate input with Zod
4. **Error Handling**: Use DomainError for all errors
5. **Type Safety**: Use database types from Supabase
6. **Documentation**: JSDoc all public methods
7. **Testing**: Write unit tests for all methods

