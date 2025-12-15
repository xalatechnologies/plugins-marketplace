---
description: Generate or update documentation
arguments:
  - name: type
    description: Doc type (readme, api, changelog, all)
    required: true
  - name: target
    description: Target file or directory
    required: false
---

# Documentation Command

Generate and maintain project documentation.

## README Template

```markdown
# Project Name

Brief description of what this project does.

## Features

- ✅ Feature 1
- ✅ Feature 2
- 🚧 Feature 3 (in progress)

## Quick Start

### Prerequisites

- Node.js >= 20
- pnpm >= 9

### Installation

```bash
# Clone the repository
git clone https://github.com/org/project.git
cd project

# Install dependencies
pnpm install

# Set up environment
cp .env.example .env
# Edit .env with your values

# Start development server
pnpm dev
```

## Project Structure

```
src/
├── app/              # Routes and pages
├── components/       # UI components
├── lib/              # Utilities and helpers
└── services/         # External services
```

## Scripts

| Command | Description |
|---------|-------------|
| `pnpm dev` | Start development server |
| `pnpm build` | Build for production |
| `pnpm lint` | Run linter |
| `pnpm test` | Run tests |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SUPABASE_URL` | Yes | Supabase project URL |
| `SUPABASE_ANON_KEY` | Yes | Supabase anon key |
| `SESSION_SECRET` | Yes | Session encryption secret |

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

## License

MIT © [Xala Technologies](https://xalatechnologies.com)
```

## API Documentation

```typescript
/**
 * User service for managing user accounts.
 * 
 * @example
 * ```typescript
 * const userService = new UserService(supabase)
 * const user = await userService.getById('123')
 * ```
 */
export class UserService {
  /**
   * Get a user by their ID.
   * 
   * @param id - The unique user identifier
   * @returns The user object or null if not found
   * @throws {NotFoundError} When user doesn't exist
   * 
   * @example
   * ```typescript
   * const user = await userService.getById('user_123')
   * console.log(user.email) // 'user@example.com'
   * ```
   */
  async getById(id: string): Promise<User | null> {
    // implementation
  }

  /**
   * Create a new user account.
   * 
   * @param data - User creation data
   * @param data.email - User's email address
   * @param data.name - User's display name
   * @returns The created user
   * @throws {ValidationError} When data is invalid
   * @throws {ConflictError} When email already exists
   */
  async create(data: CreateUserInput): Promise<User> {
    // implementation
  }
}
```

## Changelog Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- New feature description

### Changed
- Changed behavior description

### Fixed
- Bug fix description

## [1.2.0] - 2024-12-15

### Added
- User notifications system (#142)
- Dark mode toggle (#138)

### Changed
- Updated dashboard layout for better UX (#140)

### Fixed
- Fixed login redirect issue (#139)

## [1.1.0] - 2024-12-01

### Added
- Initial release with core features
```

## OpenAPI/Swagger

```yaml
openapi: 3.0.3
info:
  title: Xala PM API
  version: 1.0.0
  description: Project management API

servers:
  - url: https://api.xalapm.com/v1

paths:
  /users/{id}:
    get:
      summary: Get user by ID
      operationId: getUserById
      tags:
        - Users
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
          format: email
        name:
          type: string
```

