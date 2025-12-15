---
description: Create a new Tauri command (Rust backend function callable from frontend)
arguments:
  - name: name
    description: Command name (snake_case)
    required: true
  - name: async
    description: Whether command is async (true/false)
    required: false
    default: true
---

# Create Tauri Command

Generate a new Tauri command with proper structure and types.

## Command Structure

```
src-tauri/
├── src/
│   ├── main.rs           # Entry point with command registration
│   ├── commands/
│   │   ├── mod.rs        # Command module exports
│   │   └── user.rs       # User commands
│   └── lib.rs
```

## Rust Command Template

```rust
// src-tauri/src/commands/user.rs
use serde::{Deserialize, Serialize};
use tauri::State;
use crate::state::AppState;
use crate::error::AppError;

#[derive(Debug, Serialize, Deserialize)]
pub struct User {
    pub id: String,
    pub name: String,
    pub email: String,
}

#[derive(Debug, Deserialize)]
pub struct CreateUserInput {
    pub name: String,
    pub email: String,
}

/// Get all users
#[tauri::command]
pub async fn get_users(
    state: State<'_, AppState>,
) -> Result<Vec<User>, AppError> {
    let users = state.db.get_users().await?;
    Ok(users)
}

/// Get a single user by ID
#[tauri::command]
pub async fn get_user(
    id: String,
    state: State<'_, AppState>,
) -> Result<User, AppError> {
    let user = state.db.get_user(&id).await?;
    user.ok_or(AppError::NotFound(format!("User {} not found", id)))
}

/// Create a new user
#[tauri::command]
pub async fn create_user(
    input: CreateUserInput,
    state: State<'_, AppState>,
) -> Result<User, AppError> {
    // Validate input
    if input.name.is_empty() {
        return Err(AppError::Validation("Name is required".into()));
    }
    if !input.email.contains('@') {
        return Err(AppError::Validation("Invalid email".into()));
    }
    
    let user = state.db.create_user(input).await?;
    Ok(user)
}
```

## Register Commands

```rust
// src-tauri/src/main.rs
mod commands;
mod error;
mod state;

use commands::user::*;

fn main() {
    tauri::Builder::default()
        .manage(state::AppState::new())
        .invoke_handler(tauri::generate_handler![
            get_users,
            get_user,
            create_user,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

## Error Handling

```rust
// src-tauri/src/error.rs
use serde::Serialize;
use thiserror::Error;

#[derive(Debug, Error, Serialize)]
pub enum AppError {
    #[error("Not found: {0}")]
    NotFound(String),
    
    #[error("Validation error: {0}")]
    Validation(String),
    
    #[error("Database error: {0}")]
    Database(String),
    
    #[error("Internal error: {0}")]
    Internal(String),
}

// Make error serializable for frontend
impl From<AppError> for String {
    fn from(err: AppError) -> String {
        err.to_string()
    }
}
```

## Frontend Usage (TypeScript)

```typescript
// src/lib/tauri.ts
import { invoke } from '@tauri-apps/api/core'

interface User {
  id: string
  name: string
  email: string
}

interface CreateUserInput {
  name: string
  email: string
}

export async function getUsers(): Promise<User[]> {
  return invoke('get_users')
}

export async function getUser(id: string): Promise<User> {
  return invoke('get_user', { id })
}

export async function createUser(input: CreateUserInput): Promise<User> {
  return invoke('create_user', { input })
}
```

## Guidelines

1. **Use async commands** for I/O operations
2. **Return Result<T, E>** for proper error handling
3. **Serialize/Deserialize** with serde
4. **Use State<>** for shared state
5. **Validate input** in Rust, not just frontend
6. **Keep commands thin** - business logic in separate modules

