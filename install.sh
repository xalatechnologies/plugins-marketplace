#!/bin/bash
# Xala Marketplace - Bulk Plugin Installer
# Usage: ./install.sh [--group <name>] [--scope <project|user|global>]

set -e

MARKETPLACE_NAME="xala-marketplace"
SCOPE="project"  # Default scope

print_header() {
  echo ""
  echo "╔══════════════════════════════════════════════════════════════════╗"
  echo "║           🚀 Xala Marketplace Plugin Installer                   ║"
  echo "╚══════════════════════════════════════════════════════════════════╝"
  echo ""
}

get_group_plugins() {
  case "$1" in
    essential)
      echo "xalapm-core orchestrator tasks repo-analysis"
      ;;
    fullstack)
      echo "xalapm-core frontend backend supabase react design-system testing"
      ;;
    mobile-dev)
      echo "xalapm-core mobile react design-system testing"
      ;;
    desktop-dev)
      echo "xalapm-core tauri frontend react testing"
      ;;
    blockchain-dev)
      echo "xalapm-core blockchain compliance testing"
      ;;
    devops)
      echo "xalapm-core devops testing documentation"
      ;;
    qa)
      echo "xalapm-core testing accessibility code-review"
      ;;
    pm)
      echo "xalapm-core orchestrator tasks planning standup project-sync documentation"
      ;;
    compliance)
      echo "xalapm-core compliance accessibility testing"
      ;;
    all)
      echo "xalapm-core orchestrator repo-analysis project-sync planning standup tasks compliance frontend backend supabase tauri react mobile design-system testing accessibility blockchain devops documentation code-review"
      ;;
    *)
      echo ""
      ;;
  esac
}

get_group_desc() {
  case "$1" in
    essential)
      echo "Core plugins required for Xala PM integration (4 plugins)"
      ;;
    fullstack)
      echo "Complete web development toolkit (7 plugins)"
      ;;
    mobile-dev)
      echo "Cross-platform mobile development (5 plugins)"
      ;;
    desktop-dev)
      echo "Native desktop application development (5 plugins)"
      ;;
    blockchain-dev)
      echo "Web3 and smart contract development (4 plugins)"
      ;;
    devops)
      echo "CI/CD and infrastructure automation (4 plugins)"
      ;;
    qa)
      echo "Testing and quality assurance (4 plugins)"
      ;;
    pm)
      echo "Project management and coordination (7 plugins)"
      ;;
    compliance)
      echo "Security, accessibility, and regulatory compliance (4 plugins)"
      ;;
    all)
      echo "Complete suite - all 21 plugins"
      ;;
    *)
      echo "Unknown group"
      ;;
  esac
}

get_scope_flag() {
  case "$1" in
    project)
      echo "--project"
      ;;
    user)
      echo "--user"
      ;;
    global|root)
      echo "--global"
      ;;
    *)
      echo "--project"
      ;;
  esac
}

get_scope_desc() {
  case "$1" in
    project)
      echo "📁 Project scope: Plugins installed in current project only"
      ;;
    user)
      echo "👤 User scope: Plugins available for current user across projects"
      ;;
    global|root)
      echo "🌍 Global scope: Plugins available system-wide for all users"
      ;;
    *)
      echo "📁 Project scope (default)"
      ;;
  esac
}

print_usage() {
  print_header
  echo "Usage:"
  echo "  ./install.sh --group <name> [--scope <project|user|global>]"
  echo "  ./install.sh --plugin <name> [--scope <project|user|global>]"
  echo "  ./install.sh --list"
  echo "  ./install.sh --scopes"
  echo ""
  echo "Installation Scopes:"
  echo "  --scope project   Install for current project only (default)"
  echo "  --scope user      Install for current user across all projects"
  echo "  --scope global    Install system-wide for all users (requires admin)"
  echo ""
  echo "Available Groups:"
  echo ""
  for group in essential fullstack mobile-dev desktop-dev blockchain-dev devops qa pm compliance all; do
    echo "  $group"
    echo "    $(get_group_desc $group)"
    echo ""
  done
  echo "Examples:"
  echo "  ./install.sh --group essential                    # Project install"
  echo "  ./install.sh --group fullstack --scope user       # User-wide install"
  echo "  ./install.sh --group all --scope global           # Global install"
  echo "  ./install.sh --plugin frontend --scope project    # Single plugin"
}

list_all() {
  print_header
  echo "📦 Plugin Groups:"
  echo ""
  for group in essential fullstack mobile-dev desktop-dev blockchain-dev devops qa pm compliance all; do
    echo "  [$group] $(get_group_desc $group)"
    echo "    └── $(get_group_plugins $group)"
    echo ""
  done
}

list_scopes() {
  print_header
  echo "📍 Installation Scopes:"
  echo ""
  echo "  project (default)"
  echo "    📁 Installs plugins in .claude/plugins/ within current project"
  echo "    ✓ Plugins only available when working in this project"
  echo "    ✓ Great for project-specific tooling"
  echo "    ✓ Keeps projects isolated"
  echo ""
  echo "  user"
  echo "    👤 Installs plugins in ~/.claude/plugins/"
  echo "    ✓ Plugins available across all your projects"
  echo "    ✓ Personal configuration persists"
  echo "    ✓ Good for your standard toolkit"
  echo ""
  echo "  global"
  echo "    🌍 Installs plugins in /usr/local/share/claude/plugins/"
  echo "    ✓ Plugins available to all users on this machine"
  echo "    ✓ Requires admin/sudo privileges"
  echo "    ✓ Good for team/shared workstations"
  echo ""
}

generate_commands() {
  local group=$1
  local scope=$2
  local plugins=$(get_group_plugins "$group")
  local scope_flag=$(get_scope_flag "$scope")
  
  if [ -z "$plugins" ]; then
    echo "❌ Unknown group: $group"
    echo "Run ./install.sh --list to see available groups"
    exit 1
  fi
  
  print_header
  echo "📋 Install commands for group: $group"
  echo "   $(get_group_desc $group)"
  echo ""
  echo "$(get_scope_desc $scope)"
  echo ""
  echo "Copy and paste these commands into Claude Code:"
  echo ""
  echo "─────────────────────────────────────────────────"
  for plugin in $plugins; do
    echo "/plugin install $plugin@$MARKETPLACE_NAME $scope_flag"
  done
  echo "─────────────────────────────────────────────────"
  echo ""
}

install_plugin() {
  local plugin=$1
  local scope=$2
  local scope_flag=$(get_scope_flag "$scope")
  
  print_header
  echo "📦 Install command for: $plugin"
  echo ""
  echo "$(get_scope_desc $scope)"
  echo ""
  echo "/plugin install $plugin@$MARKETPLACE_NAME $scope_flag"
  echo ""
}

# Parse arguments
GROUP=""
PLUGIN=""
ACTION=""

while [ $# -gt 0 ]; do
  case "$1" in
    --group|-g)
      ACTION="group"
      GROUP="$2"
      shift 2
      ;;
    --plugin|-p)
      ACTION="plugin"
      PLUGIN="$2"
      shift 2
      ;;
    --scope|-s)
      SCOPE="$2"
      shift 2
      ;;
    --list|-l)
      ACTION="list"
      shift
      ;;
    --scopes)
      ACTION="scopes"
      shift
      ;;
    --help|-h)
      ACTION="help"
      shift
      ;;
    *)
      echo "❌ Unknown option: $1"
      print_usage
      exit 1
      ;;
  esac
done

# Execute action
case "$ACTION" in
  group)
    if [ -z "$GROUP" ]; then
      echo "❌ Please specify a group name"
      exit 1
    fi
    generate_commands "$GROUP" "$SCOPE"
    ;;
  plugin)
    if [ -z "$PLUGIN" ]; then
      echo "❌ Please specify a plugin name"
      exit 1
    fi
    install_plugin "$PLUGIN" "$SCOPE"
    ;;
  list)
    list_all
    ;;
  scopes)
    list_scopes
    ;;
  help|"")
    print_usage
    ;;
esac
