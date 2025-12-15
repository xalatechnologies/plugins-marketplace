# Tauri Desktop Development Plugin

Expert Tauri development agent for native desktop applications.

## Features

### Commands
- `/command <name>` - Create a new Tauri command
- `/plugin <name>` - Add and configure Tauri plugins

### Agent
Specialized desktop agent with expertise in:
- Tauri v2 framework
- Rust backend development
- Cross-platform (macOS, Windows, Linux)
- Native system integration
- IPC communication

### Skills
- **Desktop Skill**: Window management, tray, shortcuts, auto-update

### Hooks
- Check Tauri command patterns
- Verify dependency compatibility

### MCP Tools
- Rust analyzer integration
- Cargo commands
- Tauri development/build

## Usage

```bash
# Create a new command
/command get_user_profile async=true

# Add a plugin
/plugin notification
/plugin store
```

## Installation

```bash
/plugin install tauri@xalapm-marketplace
```

## Key Patterns

- Use async commands for I/O
- Return Result<T, E> for errors
- Use State<> for shared state
- Configure capabilities for security
- Test on all target platforms

