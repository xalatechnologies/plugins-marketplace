---
description: API development expertise - design, validation, security, performance
triggers:
  - creating api endpoints
  - designing api structure
  - fixing api bugs
  - optimizing api performance
  - securing endpoints
---

# API Development Skill

Expert API development capabilities for RESTful and GraphQL APIs.

## RESTful Design Principles

### Resource Naming
```
# Good
GET  /api/v1/users              # List users
GET  /api/v1/users/:id          # Get user
POST /api/v1/users              # Create user
PUT  /api/v1/users/:id          # Update user
DELETE /api/v1/users/:id        # Delete user

# Nested resources
GET  /api/v1/users/:id/posts    # User's posts
POST /api/v1/users/:id/posts    # Create post for user

# Actions (when CRUD doesn't fit)
POST /api/v1/users/:id/activate
POST /api/v1/orders/:id/cancel
```

### Query Parameters
```
# Pagination
?page=2&limit=20

# Filtering
?status=active&role=admin

# Sorting
?sort=created_at&order=desc

# Field selection
?fields=id,name,email

# Search
?q=john
```

### Response Patterns
```typescript
// Collection response
{
  "data": [...],
  "meta": {
    "total": 100,
    "page": 1,
    "limit": 20,
    "pages": 5
  },
  "links": {
    "self": "/api/v1/users?page=1",
    "next": "/api/v1/users?page=2",
    "last": "/api/v1/users?page=5"
  }
}

// Single resource
{
  "data": { ... }
}

// Error
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      { "field": "email", "message": "Invalid email format" }
    ]
  }
}
```

## Security Patterns

### Authentication Middleware
```typescript
async function requireAuth(c: Context, next: Next) {
  const token = c.req.header('Authorization')?.replace('Bearer ', '')
  
  if (!token) {
    throw new DomainError('UNAUTHORIZED', 401, 'Missing token')
  }
  
  const user = await verifyToken(token)
  c.set('user', user)
  
  await next()
}
```

### Rate Limiting
```typescript
const rateLimit = rateLimiter({
  windowMs: 60 * 1000, // 1 minute
  max: 100, // 100 requests per minute
  keyGenerator: (c) => c.req.header('X-Forwarded-For') || 'anonymous',
  handler: (c) => {
    throw new DomainError('RATE_LIMITED', 429, 'Too many requests')
  }
})
```

### Input Sanitization
```typescript
// Always validate and sanitize
const schema = z.object({
  name: z.string().trim().min(1).max(100),
  email: z.string().email().toLowerCase(),
  html: z.string().transform(sanitizeHtml), // Sanitize HTML
})
```

## Performance Patterns

### Efficient Queries
```typescript
// ❌ N+1 problem
for (const user of users) {
  user.posts = await getPosts(user.id) // N queries
}

// ✅ Single query with join
const { data } = await supabase
  .from('users')
  .select('*, posts(*)')  // 1 query
```

### Caching
```typescript
// Simple in-memory cache
const cache = new Map()

async function getCachedData(key: string, fetcher: () => Promise<any>, ttl = 60000) {
  const cached = cache.get(key)
  if (cached && Date.now() - cached.timestamp < ttl) {
    return cached.data
  }
  
  const data = await fetcher()
  cache.set(key, { data, timestamp: Date.now() })
  return data
}
```

## When to Use

Apply this skill when:
- Designing new API endpoints
- Reviewing API security
- Optimizing database queries
- Implementing pagination/filtering
- Adding authentication/authorization

