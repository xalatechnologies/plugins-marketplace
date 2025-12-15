#!/usr/bin/env python3
"""
Xala PM Test Suggestion Hook
Suggests tests for new code
"""

import json
import sys
import re
from pathlib import Path

def analyze_for_tests(content: str, file_path: str) -> list:
    """Analyze code and suggest tests"""
    suggestions = []
    
    # Skip test files themselves
    if "test" in file_path.lower() or "spec" in file_path.lower():
        return suggestions
    
    # Check for functions that should be tested
    # TypeScript/JavaScript functions
    func_patterns = [
        r"export\s+(?:async\s+)?function\s+(\w+)",
        r"export\s+const\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>",
        r"export\s+const\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*:\s*\w+\s*=>",
    ]
    
    functions = []
    for pattern in func_patterns:
        matches = re.findall(pattern, content)
        functions.extend(matches)
    
    if functions:
        suggestions.append({
            "type": "unit",
            "message": f"Consider unit tests for: {', '.join(functions[:5])}"
        })
    
    # Check for React components
    if re.search(r"export\s+(?:default\s+)?function\s+\w+\([^)]*\)\s*{[^}]*return\s*\(?\s*<", content):
        suggestions.append({
            "type": "component",
            "message": "Add component tests with React Testing Library"
        })
    
    # Check for API handlers
    if re.search(r"(app\.(get|post|put|delete)|router\.(get|post|put|delete))", content):
        suggestions.append({
            "type": "integration",
            "message": "Add API integration tests"
        })
    
    # Check for hooks
    if re.search(r"export\s+(?:const|function)\s+use\w+", content):
        suggestions.append({
            "type": "hook",
            "message": "Test custom hooks with @testing-library/react-hooks"
        })
    
    return suggestions

def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)
    
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)
    
    file_path = tool_input.get("file_path", "")
    content = tool_input.get("content", tool_input.get("new_string", ""))
    
    # Only analyze TypeScript/JavaScript
    if not file_path.endswith((".ts", ".tsx", ".js", ".jsx")):
        sys.exit(0)
    
    suggestions = analyze_for_tests(content, file_path)
    
    if suggestions:
        feedback = ["🧪 Test Suggestions:"]
        for s in suggestions:
            feedback.append(f"  [{s['type']}] {s['message']}")
        
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": "\n".join(feedback)
            }
        }
        print(json.dumps(output))
    
    sys.exit(0)

if __name__ == "__main__":
    main()

