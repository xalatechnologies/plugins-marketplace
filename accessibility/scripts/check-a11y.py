#!/usr/bin/env python3
"""
Xala PM Accessibility Checker
Checks UI code for WCAG compliance issues
"""

import json
import sys
import re

# WCAG patterns to check
A11Y_PATTERNS = [
    # Images
    (r"<img[^>]+(?!alt=)[^>]*>", "WCAG 1.1.1", "Image missing alt attribute"),
    (r"alt\s*=\s*['\"]['\"]", "WCAG 1.1.1", "Empty alt attribute - use alt='' only for decorative images"),
    
    # Forms
    (r"<input[^>]+(?!aria-label|aria-labelledby|id)[^>]*>", "WCAG 1.3.1", "Input missing label association"),
    (r"<button[^>]*>\s*<(svg|img)[^>]*>\s*</button>", "WCAG 4.1.2", "Icon button needs aria-label"),
    
    # Interactive elements
    (r"onClick\s*=.*<div", "WCAG 2.1.1", "Use button/a for clickable elements, not div"),
    (r"tabIndex\s*=\s*['\"]?[2-9]", "WCAG 2.4.3", "Avoid tabindex > 1, disrupts natural order"),
    
    # Color and contrast
    (r"color:\s*#[a-fA-F0-9]{3}(?![a-fA-F0-9])", "WCAG 1.4.3", "Check 3-digit hex color contrast ratio"),
    
    # ARIA
    (r"aria-hidden\s*=\s*['\"]true['\"][^>]*focusable", "ARIA", "Hidden element should not be focusable"),
    (r"role\s*=\s*['\"]button['\"][^>]*(?!tabIndex)", "ARIA", "Custom button role needs tabIndex='0'"),
]

def check_accessibility(content: str, file_path: str) -> list:
    """Check content for accessibility issues"""
    issues = []
    
    # Only check TSX/JSX files
    if not file_path.endswith((".tsx", ".jsx")):
        return issues
    
    for pattern, criterion, message in A11Y_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
        if matches:
            issues.append({
                "criterion": criterion,
                "message": message,
                "count": len(matches)
            })
    
    return issues

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
    
    issues = check_accessibility(content, file_path)
    
    if issues:
        feedback = ["♿ Accessibility Review:"]
        for issue in issues:
            feedback.append(f"  [{issue['criterion']}] {issue['message']}")
        
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

