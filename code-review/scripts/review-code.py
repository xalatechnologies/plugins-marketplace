#!/usr/bin/env python3
"""
Xala PM Code Review Hook
Analyzes code changes for common issues and patterns
"""

import json
import sys
import re
from pathlib import Path

# Patterns to check for in code
CODE_PATTERNS = [
    # Security issues
    (r"eval\s*\(", "security", "Avoid eval() - potential code injection"),
    (r"innerHTML\s*=", "security", "Use textContent instead of innerHTML to prevent XSS"),
    (r"password.*=.*['\"][^'\"]+['\"]", "security", "Hardcoded password detected"),
    (r"api[_-]?key.*=.*['\"][^'\"]+['\"]", "security", "Hardcoded API key detected"),
    
    # Performance issues
    (r"\.forEach\(.*\.push\(", "performance", "Consider using map() instead of forEach+push"),
    (r"document\.querySelector.*for\s*\(", "performance", "Move querySelector outside loop"),
    
    # Best practices
    (r"console\.log\(", "cleanup", "Remove console.log before commit"),
    (r"// TODO", "todo", "TODO comment found - track in task system"),
    (r"// FIXME", "todo", "FIXME comment found - create task"),
    (r"any\s*[;,\)]", "typescript", "Avoid 'any' type - use specific types"),
    
    # React patterns
    (r"useState\([^)]*\)\s*//", "react", "Consider adding type to useState"),
    (r"useEffect\(\s*\(\)\s*=>\s*\{[^}]*fetch", "react", "Add cleanup for fetch in useEffect"),
]

def analyze_content(content: str, file_path: str) -> list:
    """Analyze code content for issues"""
    issues = []
    
    for pattern, category, message in CODE_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append({
                "category": category,
                "message": message,
                "file": file_path
            })
    
    return issues

def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)  # No input, continue
    
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    
    # Only analyze Write/Edit operations
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)
    
    file_path = tool_input.get("file_path", "")
    content = tool_input.get("content", tool_input.get("new_string", ""))
    
    # Skip non-code files
    code_extensions = {".ts", ".tsx", ".js", ".jsx", ".py", ".rs", ".go", ".sol"}
    if not any(file_path.endswith(ext) for ext in code_extensions):
        sys.exit(0)
    
    # Analyze the code
    issues = analyze_content(content, file_path)
    
    if issues:
        # Group by category
        by_category = {}
        for issue in issues:
            cat = issue["category"]
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(issue["message"])
        
        # Build feedback message
        feedback = []
        for cat, messages in by_category.items():
            feedback.append(f"[{cat.upper()}]")
            for msg in messages:
                feedback.append(f"  • {msg}")
        
        # Return as additional context for Claude
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "Code review findings:\n" + "\n".join(feedback)
            }
        }
        print(json.dumps(output))
    
    sys.exit(0)

if __name__ == "__main__":
    main()

