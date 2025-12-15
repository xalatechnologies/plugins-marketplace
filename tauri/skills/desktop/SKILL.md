---
description: Desktop app development expertise for Tauri
triggers:
  - creating tauri commands
  - working with tauri plugins
  - desktop app features
  - native system integration
  - cross-platform development
---

# Desktop Development Skill

Expert Tauri desktop development capabilities.

## Project Structure

```
my-tauri-app/
├── src/                    # Frontend (React/Vue/Svelte)
│   ├── lib/
│   │   └── tauri.ts        # Typed Tauri wrappers
│   └── ...
├── src-tauri/
│   ├── Cargo.toml          # Rust dependencies
│   ├── tauri.conf.json     # Tauri configuration
│   ├── capabilities/       # Security permissions
│   │   └── default.json
│   └── src/
│       ├── main.rs         # Entry point
│       ├── lib.rs          # Library entry
│       ├── commands/       # Tauri commands
│       │   ├── mod.rs
│       │   └── *.rs
│       ├── state.rs        # App state
│       └── error.rs        # Error types
```

## State Management

```rust
// src-tauri/src/state.rs
use std::sync::Mutex;
use tokio::sync::RwLock;

pub struct AppState {
    pub db: DatabaseClient,
    pub settings: RwLock<Settings>,
    pub cache: Mutex<Cache>,
}

impl AppState {
    pub fn new() -> Self {
        Self {
            db: DatabaseClient::new(),
            settings: RwLock::new(Settings::default()),
            cache: Mutex::new(Cache::new()),
        }
    }
}
```

## Window Management

```rust
use tauri::Manager;

// Create new window
#[tauri::command]
async fn open_settings(app: tauri::AppHandle) -> Result<(), String> {
    let _window = tauri::WebviewWindowBuilder::new(
        &app,
        "settings",
        tauri::WebviewUrl::App("settings".into()),
    )
    .title("Settings")
    .inner_size(600.0, 400.0)
    .resizable(false)
    .build()
    .map_err(|e| e.to_string())?;
    
    Ok(())
}

// Close window
#[tauri::command]
async fn close_window(window: tauri::Window) -> Result<(), String> {
    window.close().map_err(|e| e.to_string())
}
```

## System Tray

```rust
use tauri::{
    menu::{Menu, MenuItem},
    tray::TrayIconBuilder,
    Manager,
};

fn setup_tray(app: &tauri::App) -> Result<(), Box<dyn std::error::Error>> {
    let quit = MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
    let show = MenuItem::with_id(app, "show", "Show Window", true, None::<&str>)?;
    
    let menu = Menu::with_items(app, &[&show, &quit])?;
    
    let _tray = TrayIconBuilder::new()
        .icon(app.default_window_icon().unwrap().clone())
        .menu(&menu)
        .on_menu_event(|app, event| match event.id.as_ref() {
            "quit" => app.exit(0),
            "show" => {
                if let Some(window) = app.get_webview_window("main") {
                    window.show().unwrap();
                    window.set_focus().unwrap();
                }
            }
            _ => {}
        })
        .build(app)?;
    
    Ok(())
}
```

## Keyboard Shortcuts

```rust
use tauri::Manager;

fn setup_shortcuts(app: &tauri::App) -> Result<(), Box<dyn std::error::Error>> {
    // Global shortcut
    app.global_shortcut().on_shortcut("CmdOrCtrl+Shift+P", |app, _event, _shortcut| {
        if let Some(window) = app.get_webview_window("main") {
            window.emit("command-palette", ()).unwrap();
        }
    })?;
    
    Ok(())
}
```

## Auto-Update

```toml
# Cargo.toml
[dependencies]
tauri-plugin-updater = "2"
```

```rust
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_updater::Builder::new().build())
        .run(tauri::generate_context!())
        .expect("error");
}
```

```typescript
import { check } from '@tauri-apps/plugin-updater'

const update = await check()
if (update?.available) {
  await update.downloadAndInstall()
}
```

## When to Use

Apply this skill when:
- Creating Tauri commands
- Integrating native features
- Setting up plugins
- Managing application state
- Handling cross-platform differences

