---
description: Technical documentation expertise
triggers:
  - writing documentation
  - updating readme
  - api documentation
  - jsdoc
---

# Documentation Skill

## README Patterns

### Badges

```markdown
[![CI](https://github.com/org/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/org/repo/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![npm](https://img.shields.io/npm/v/package-name.svg)](https://www.npmjs.com/package/package-name)
```

### Table of Contents

```markdown
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
```

### Collapsible Sections

```markdown
<details>
<summary>Advanced Configuration</summary>

Content that is initially hidden...

</details>
```

## JSDoc Patterns

### Function Documentation

```typescript
/**
 * Short description (one line).
 * 
 * Longer description with more details.
 * Can be multiple paragraphs.
 * 
 * @param param1 - Description of param1
 * @param param2 - Description of param2
 * @returns Description of return value
 * @throws {ErrorType} When this error occurs
 * 
 * @example
 * ```typescript
 * const result = myFunction('value', { option: true })
 * ```
 */
```

### Type Documentation

```typescript
/**
 * Represents a user in the system.
 * 
 * @property id - Unique identifier
 * @property email - User's email address
 * @property createdAt - Account creation timestamp
 */
interface User {
  id: string
  email: string
  createdAt: Date
}
```

### Module Documentation

```typescript
/**
 * @module UserService
 * @description Provides user management functionality.
 * 
 * This module handles:
 * - User creation and deletion
 * - Profile updates
 * - Authentication helpers
 * 
 * @example
 * ```typescript
 * import { UserService } from '@/services/user'
 * const service = new UserService(supabase)
 * ```
 */
```

## Changelog Patterns

### Semantic Versioning

```markdown
## [MAJOR.MINOR.PATCH] - YYYY-MM-DD

### Added (new features)
### Changed (changes in existing functionality)
### Deprecated (soon-to-be removed features)
### Removed (removed features)
### Fixed (bug fixes)
### Security (vulnerability fixes)
```

### Linking to Issues/PRs

```markdown
### Fixed
- Fixed login redirect issue ([#139](https://github.com/org/repo/issues/139))
```

## When to Use

Apply when:
- Creating new projects
- Adding new features
- Changing APIs
- Releasing versions

