---
description: Authentication and session security best practices
globs: ["**/*.ts", "**/*.js", "**/*.py"]
---

# Authentication Security (OWASP A07)

## Password Security

### ✅ Secure Password Hashing

```typescript
import bcrypt from 'bcrypt';

// Hash password
const hash = await bcrypt.hash(password, 12); // Cost factor 12+

// Verify password
const valid = await bcrypt.compare(password, storedHash);
```

### ❌ Never Do

```typescript
// Weak hash - NEVER
crypto.createHash('md5').update(password);
crypto.createHash('sha1').update(password);

// Plain text - NEVER EVER
db.user.create({ password: password });
```

## Session Security

### ✅ Secure Session Configuration

```typescript
app.use(session({
  name: '__Host-session', // Secure prefix
  secret: crypto.randomBytes(32).toString('hex'),
  cookie: {
    httpOnly: true,      // No JS access
    secure: true,        // HTTPS only
    sameSite: 'strict',  // CSRF protection
    maxAge: 3600000,     // 1 hour
  },
  resave: false,
  saveUninitialized: false,
}));
```

### Session ID Requirements

- Minimum 128 bits of entropy
- Cryptographically random
- Regenerate on authentication
- Invalidate on logout

## MFA Implementation

```typescript
import { authenticator } from 'otplib';

// Generate secret
const secret = authenticator.generateSecret();

// Verify token
const isValid = authenticator.verify({
  token: userToken,
  secret: userSecret,
});
```

## Rate Limiting

```typescript
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  message: 'Too many login attempts',
});

app.post('/login', loginLimiter, loginHandler);
```

