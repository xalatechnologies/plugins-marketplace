---
description: Use or create Tauri plugins for native functionality
arguments:
  - name: name
    description: Plugin name (e.g., notification, fs, shell)
    required: true
---

# Tauri Plugin Command

Add and configure Tauri plugins for native functionality.

## Official Plugins

### Notification Plugin
```toml
# src-tauri/Cargo.toml
[dependencies]
tauri-plugin-notification = "2"
```

```rust
// src-tauri/src/main.rs
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_notification::init())
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```typescript
// Frontend usage
import { sendNotification } from '@tauri-apps/plugin-notification'

await sendNotification({
  title: 'Task Completed',
  body: 'Your build finished successfully!'
})
```

### File System Plugin
```toml
[dependencies]
tauri-plugin-fs = "2"
```

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_fs::init())
        .run(tauri::generate_context!())
        .expect("error");
}
```

```typescript
import { readTextFile, writeTextFile } from '@tauri-apps/plugin-fs'

// Read file
const content = await readTextFile('path/to/file.txt')

// Write file
await writeTextFile('path/to/file.txt', 'Hello, World!')
```

### Shell Plugin
```toml
[dependencies]
tauri-plugin-shell = "2"
```

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .run(tauri::generate_context!())
        .expect("error");
}
```

```typescript
import { Command } from '@tauri-apps/plugin-shell'

// Run command
const output = await Command.create('git', ['status']).execute()
console.log(output.stdout)
```

### Store Plugin (Local Storage)
```toml
[dependencies]
tauri-plugin-store = "2"
```

```typescript
import { Store } from '@tauri-apps/plugin-store'

const store = await Store.load('settings.json')
await store.set('theme', 'dark')
const theme = await store.get('theme')
await store.save()
```

### Deep Link Plugin
```toml
[dependencies]
tauri-plugin-deep-link = "2"
```

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_deep_link::init())
        .setup(|app| {
            #[cfg(any(target_os = "linux", all(debug_assertions, windows)))]
            tauri_plugin_deep_link::register("myapp", app.handle())?;
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error");
}
```

## Create Custom Plugin

```rust
// src-tauri/src/plugins/my_plugin.rs
use tauri::{
    plugin::{Builder, TauriPlugin},
    Manager, Runtime,
};

#[tauri::command]
async fn my_command() -> Result<String, String> {
    Ok("Hello from plugin!".into())
}

pub fn init<R: Runtime>() -> TauriPlugin<R> {
    Builder::new("my-plugin")
        .invoke_handler(tauri::generate_handler![my_command])
        .build()
}
```

```rust
// src-tauri/src/main.rs
mod plugins;

fn main() {
    tauri::Builder::default()
        .plugin(plugins::my_plugin::init())
        .run(tauri::generate_context!())
        .expect("error");
}
```

## Capabilities (Permissions)

```json
// src-tauri/capabilities/default.json
{
  "identifier": "default",
  "description": "Default capabilities",
  "windows": ["main"],
  "permissions": [
    "core:default",
    "notification:default",
    "fs:default",
    "shell:allow-execute"
  ]
}
```

## Guidelines

1. **Use official plugins** when available
2. **Configure capabilities** for security
3. **Handle plugin errors** gracefully
4. **Test on all platforms** (macOS, Windows, Linux)

