#!/bin/bash
#
# Validates all plugins in the marketplace.
# Checks for required files, valid JSON, and structure.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ERRORS=0
WARNINGS=0

log_error() {
    echo -e "${RED}ERROR:${NC} $1"
    ((ERRORS++))
}

log_warning() {
    echo -e "${YELLOW}WARNING:${NC} $1"
    ((WARNINGS++))
}

log_success() {
    echo -e "${GREEN}OK:${NC} $1"
}

validate_json() {
    local file="$1"
    if ! python3 -c "import json; json.load(open('$file'))" 2>/dev/null; then
        log_error "Invalid JSON: $file"
        return 1
    fi
    return 0
}

validate_plugin() {
    local plugin_dir="$1"
    local plugin_name=$(basename "$plugin_dir")
    
    echo ""
    echo "Validating: $plugin_name"
    echo "---"
    
    # Check plugin.json exists
    if [ ! -f "$plugin_dir/.claude-plugin/plugin.json" ]; then
        log_error "$plugin_name: Missing .claude-plugin/plugin.json"
        return
    fi
    
    # Validate plugin.json
    if ! validate_json "$plugin_dir/.claude-plugin/plugin.json"; then
        return
    fi
    
    # Check required fields in plugin.json
    local name=$(python3 -c "import json; print(json.load(open('$plugin_dir/.claude-plugin/plugin.json')).get('name', ''))")
    local description=$(python3 -c "import json; print(json.load(open('$plugin_dir/.claude-plugin/plugin.json')).get('description', ''))")
    
    if [ -z "$name" ]; then
        log_error "$plugin_name: plugin.json missing 'name' field"
    fi
    
    if [ -z "$description" ]; then
        log_error "$plugin_name: plugin.json missing 'description' field"
    fi
    
    # Check README exists
    if [ ! -f "$plugin_dir/README.md" ]; then
        log_warning "$plugin_name: Missing README.md"
    fi
    
    # Check hooks.json format if exists
    if [ -f "$plugin_dir/hooks/hooks.json" ]; then
        if ! validate_json "$plugin_dir/hooks/hooks.json"; then
            return
        fi
        
        # Check for hooks wrapper
        local has_hooks=$(python3 -c "import json; d=json.load(open('$plugin_dir/hooks/hooks.json')); print('hooks' in d)")
        if [ "$has_hooks" != "True" ]; then
            log_error "$plugin_name: hooks.json missing 'hooks' wrapper object"
        fi
    fi
    
    # Check for at least one of: agents, commands, skills
    local has_content=0
    [ -d "$plugin_dir/agents" ] && [ "$(ls -A "$plugin_dir/agents" 2>/dev/null)" ] && has_content=1
    [ -d "$plugin_dir/commands" ] && [ "$(ls -A "$plugin_dir/commands" 2>/dev/null)" ] && has_content=1
    [ -d "$plugin_dir/skills" ] && [ "$(ls -A "$plugin_dir/skills" 2>/dev/null)" ] && has_content=1
    
    if [ $has_content -eq 0 ]; then
        log_warning "$plugin_name: No agents, commands, or skills found"
    fi
    
    log_success "$plugin_name validated"
}

echo "==================================="
echo "Plugin Validation"
echo "==================================="

# Find all plugin directories
for dir in "$ROOT_DIR"/*/; do
    # Skip non-plugin directories
    [ -d "${dir}.claude-plugin" ] || continue
    
    validate_plugin "$dir"
done

echo ""
echo "==================================="
echo "Summary"
echo "==================================="
echo -e "Errors:   ${RED}$ERRORS${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "Validation FAILED. Please fix errors before publishing."
    exit 1
else
    echo ""
    echo -e "${GREEN}Validation PASSED.${NC}"
    exit 0
fi

