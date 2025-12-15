---
description: Enforces professional, human-written communication standards across all code and documentation
globs:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.md"
  - "**/*.json"
alwaysApply: true
---

# Professional Communication Standards

This skill enforces professional, human-written communication in all code, comments, commits, and documentation.

## Core Principle

Write as a senior engineer with 20+ years of experience would write. Technical, precise, and professional.

---

## Prohibited Patterns

### Emojis (Never Use)

Emojis are prohibited in:
- Source code comments
- Commit messages
- Documentation
- Error messages
- Log messages
- READMEs

### AI-Generated Tone (Never Use)

| Prohibited Phrase | Why |
|-------------------|-----|
| "Built with love" | Unprofessional filler |
| "Made with care" | Unprofessional filler |
| "Happy coding!" | AI slop |
| "Let's dive in!" | AI filler |
| "Let's get started!" | AI filler |
| "Hope this helps!" | AI tone |
| "I'm excited to..." | AI tone |

### AI Superlatives (Never Use)

- "Awesome"
- "Amazing"
- "Fantastic"
- "Wonderful"
- "Beautiful"
- "Elegant" (unless technically accurate)
- "Magic" / "Magical"
- "Powerful"

### Excessive Punctuation

- Multiple exclamation marks: `!!!`
- Excessive enthusiasm: `Great job!`
- Rhetorical questions: `Isn't that cool?`

---

## Required Patterns

### Code Comments

```typescript
// CORRECT - Factual, technical
/**
 * Validates email format and checks domain against blocklist.
 * Returns validation result with specific error details.
 */
function validateEmail(email: string): ValidationResult

// WRONG - AI tone, emoji
/**
 * Awesome function that validates emails! 
 * Let's make sure those emails are valid!
 */
```

### Commit Messages

Use Conventional Commits format:

```bash
# CORRECT
feat(auth): implement JWT refresh token rotation
fix(api): resolve race condition in concurrent requests
docs(readme): update installation instructions
refactor(utils): extract validation logic to shared module
perf(query): optimize user lookup with index hint
test(auth): add integration tests for password reset

# WRONG
Add awesome new feature
Fix bug (hope this works!)
Update docs - made with love
Ship it!
WIP
misc fixes
```

### Documentation

```markdown
# CORRECT - Technical, professional

## Authentication

This module handles user authentication using JWT tokens with 
refresh token rotation. Sessions expire after 24 hours of inactivity.

### Configuration

Set the following environment variables:
- `JWT_SECRET`: Secret key for token signing (minimum 32 characters)
- `TOKEN_EXPIRY`: Token lifetime in seconds (default: 86400)

# WRONG - AI tone

## Authentication

Welcome! This awesome module handles authentication!

We've built this with love to make your life easier!
Let's dive in and explore the amazing features!
```

### Error Messages

```typescript
// CORRECT - Clear, actionable
throw new ValidationError('Email format invalid. Expected: user@domain.com');
throw new AuthError('Session expired. Re-authentication required.');

// WRONG - Casual, unhelpful
throw new Error('Oops! Something went wrong!');
throw new Error('Invalid email :(');
```

### Log Messages

```typescript
// CORRECT - Structured, technical
logger.info('User authenticated', { userId, method: 'jwt' });
logger.error('Database connection failed', { host, port, error: err.message });

// WRONG - Casual
logger.info('Yay! User logged in!');
logger.error('Oh no! Database broke!');
```

---

## Tone Guidelines

### DO

1. **Be technical**: Use domain-specific terminology correctly
2. **Be precise**: State exactly what happens, when, and why
3. **Be concise**: Remove unnecessary words
4. **Be factual**: Describe behavior, not feelings
5. **Be helpful**: Include actionable information in errors

### DON'T

1. **Don't be casual**: No slang, colloquialisms, or humor
2. **Don't be enthusiastic**: No excitement, no exclamation marks
3. **Don't be apologetic**: No "sorry", "unfortunately", "sadly"
4. **Don't be promotional**: No selling features or capabilities
5. **Don't be chatty**: No filler phrases or small talk

---

## JSDoc Standards

```typescript
// CORRECT
/**
 * Calculates compound interest over a specified period.
 * 
 * @param principal - Initial investment amount in cents
 * @param rate - Annual interest rate as decimal (e.g., 0.05 for 5%)
 * @param periods - Number of compounding periods
 * @returns Final amount in cents, rounded to nearest integer
 * @throws {ValidationError} If any parameter is negative
 * 
 * @example
 * calculateInterest(100000, 0.05, 12) // Returns 105116
 */
function calculateInterest(
  principal: number,
  rate: number,
  periods: number
): number

// WRONG
/**
 * This awesome function calculates interest!
 * Just pass in your values and watch the magic happen!
 * 
 * @param principal - The money you start with
 * @param rate - How much interest (exciting!)
 * @returns Your new balance - hopefully more than before! 
 */
```

---

## README Structure

```markdown
# Project Name

Brief description of what the project does. One to two sentences.

## Installation

\`\`\`bash
npm install @org/package
\`\`\`

## Usage

\`\`\`typescript
import { Client } from '@org/package';

const client = new Client({
  apiKey: process.env.API_KEY
});
\`\`\`

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `API_KEY` | Authentication key | Required |
| `TIMEOUT` | Request timeout in ms | 5000 |

## API Reference

### `client.method(options)`

Description of what the method does.

**Parameters:**
- `options.param1` (string): Description

**Returns:** `Promise<Result>`

## License

MIT
```

---

## Validation Checklist

Before committing any code or documentation:

- [ ] No emojis present
- [ ] No AI-tone phrases ("awesome", "let's dive in", etc.)
- [ ] No excessive punctuation
- [ ] Commit message uses Conventional Commits format
- [ ] Comments are factual and technical
- [ ] Documentation describes behavior, not feelings
- [ ] Error messages are clear and actionable

