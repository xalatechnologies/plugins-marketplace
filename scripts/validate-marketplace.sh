#!/bin/bash
#
# Validates the marketplace.json file.
# Checks schema, plugin references, and consistency.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
MARKETPLACE_FILE="$ROOT_DIR/.claude-plugin/marketplace.json"

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

echo "==================================="
echo "Marketplace Validation"
echo "==================================="
echo ""

# Check file exists
if [ ! -f "$MARKETPLACE_FILE" ]; then
    log_error "marketplace.json not found at $MARKETPLACE_FILE"
    exit 1
fi

# Validate JSON syntax
echo "Checking JSON syntax..."
if ! python3 -c "import json; json.load(open('$MARKETPLACE_FILE'))" 2>/dev/null; then
    log_error "Invalid JSON in marketplace.json"
    exit 1
fi
log_success "JSON syntax valid"

# Check required fields
echo "Checking required fields..."
python3 << EOF
import json
import sys

with open('$MARKETPLACE_FILE') as f:
    data = json.load(f)

errors = []
warnings = []

# Check name
if not data.get('name'):
    errors.append("Missing 'name' field")

# Check owner
if not data.get('owner', {}).get('name'):
    errors.append("Missing 'owner.name' field")

# Check plugins array
if not data.get('plugins'):
    errors.append("Missing 'plugins' array")
else:
    for i, plugin in enumerate(data['plugins']):
        if not plugin.get('name'):
            errors.append(f"Plugin {i}: missing 'name'")
        if not plugin.get('source'):
            errors.append(f"Plugin {i}: missing 'source'")
        if not plugin.get('description'):
            warnings.append(f"Plugin {i} ({plugin.get('name', 'unknown')}): missing 'description'")

for e in errors:
    print(f"ERROR: {e}")
for w in warnings:
    print(f"WARNING: {w}")

sys.exit(1 if errors else 0)
EOF

if [ $? -eq 0 ]; then
    log_success "Required fields present"
else
    ((ERRORS++))
fi

# Check plugin sources exist
echo "Checking plugin sources..."
python3 << EOF
import json
import os

with open('$MARKETPLACE_FILE') as f:
    data = json.load(f)

root_dir = '$ROOT_DIR'
missing = []

for plugin in data.get('plugins', []):
    source = plugin.get('source', '')
    if source.startswith('./'):
        path = os.path.join(root_dir, source[2:])
    else:
        path = os.path.join(root_dir, source)
    
    if not os.path.isdir(path):
        missing.append(f"{plugin['name']}: {source}")

if missing:
    print("Missing plugin directories:")
    for m in missing:
        print(f"  - {m}")
else:
    print("All plugin sources exist")
EOF

# Check for duplicate plugin names
echo "Checking for duplicates..."
python3 << EOF
import json
from collections import Counter

with open('$MARKETPLACE_FILE') as f:
    data = json.load(f)

names = [p.get('name') for p in data.get('plugins', [])]
duplicates = [name for name, count in Counter(names).items() if count > 1]

if duplicates:
    print(f"ERROR: Duplicate plugin names: {duplicates}")
else:
    print("No duplicate plugin names")
EOF

echo ""
echo "==================================="
echo "Summary"
echo "==================================="

# Count plugins
plugin_count=$(python3 -c "import json; print(len(json.load(open('$MARKETPLACE_FILE')).get('plugins', [])))")
echo "Total plugins: $plugin_count"

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo -e "${RED}Validation FAILED.${NC}"
    exit 1
else
    echo ""
    echo -e "${GREEN}Validation PASSED.${NC}"
    exit 0
fi

