---
description: Secure access control implementation patterns
globs: ["**/*.ts", "**/*.js", "**/*.py"]
---

# Access Control Security (OWASP A01)

## Core Principles

1. **Deny by Default** - No access unless explicitly granted
2. **Least Privilege** - Minimum permissions needed
3. **Fail Securely** - Errors result in denied access
4. **Verify Every Request** - No trust assumptions

## RBAC Implementation

### ✅ Secure Pattern

```typescript
// Define permissions
const permissions = {
  'user:read': ['user', 'admin'],
  'user:write': ['admin'],
  'user:delete': ['admin'],
} as const;

// Middleware
function authorize(permission: string) {
  return (req, res, next) => {
    const userRole = req.user?.role;
    
    if (!userRole) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    
    const allowedRoles = permissions[permission];
    if (!allowedRoles?.includes(userRole)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    
    next();
  };
}

// Usage
app.delete('/users/:id', 
  authenticate,
  authorize('user:delete'),
  deleteUser
);
```

### ❌ Insecure Patterns

```typescript
// Trusting client-side role - NEVER
app.delete('/users/:id', (req, res) => {
  if (req.body.isAdmin) { // Client can fake this!
    deleteUser(req.params.id);
  }
});

// No authorization check - NEVER
app.delete('/users/:id', (req, res) => {
  deleteUser(req.params.id); // Anyone can delete!
});
```

## Object-Level Authorization

```typescript
// ✅ Verify ownership
app.get('/orders/:id', authenticate, async (req, res) => {
  const order = await db.order.findUnique({
    where: { id: req.params.id }
  });
  
  // Check ownership
  if (order.userId !== req.user.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  
  res.json(order);
});
```

## Audit Logging

```typescript
// Log all sensitive actions
async function authorizedAction(user, action, resource) {
  const allowed = await checkPermission(user, action, resource);
  
  await auditLog.create({
    userId: user.id,
    action,
    resource,
    allowed,
    timestamp: new Date(),
    ip: user.ip,
  });
  
  return allowed;
}
```

