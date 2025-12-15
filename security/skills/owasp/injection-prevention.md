---
description: Prevent injection attacks (SQL, NoSQL, Command, LDAP)
globs: ["**/*.ts", "**/*.js", "**/*.py", "**/*.java", "**/*.go"]
---

# Injection Prevention (OWASP A03)

## Detection Patterns

### SQL Injection Risks

```regex
# String concatenation in queries
(query|sql|execute).*\$\{.*\}
(query|sql|execute).*\+\s*['"]
f["'].*SELECT.*\{.*\}
```

### Command Injection Risks

```regex
exec\(.*\$\{
child_process\.exec\(.*\+
os\.system\(.*\+
subprocess\.(run|call|Popen).*shell=True
```

## Prevention Rules

### ✅ Always Use

1. **Parameterized Queries**
```typescript
// Safe
db.query('SELECT * FROM users WHERE id = $1', [userId]);
```

2. **ORMs with Escaping**
```typescript
// Safe
await prisma.user.findUnique({ where: { id: userId } });
```

3. **Prepared Statements**
```java
// Safe
PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
stmt.setInt(1, userId);
```

### ❌ Never Use

1. String concatenation in queries
2. Template literals with user input
3. `eval()` with user input
4. `shell=True` with user input
5. Direct command execution with user input

## Remediation

When injection risk is detected:

1. Replace string concatenation with parameterized queries
2. Use ORM methods instead of raw queries
3. Validate and sanitize all user input
4. Apply allowlist validation for expected values
5. Escape special characters if raw query is unavoidable

