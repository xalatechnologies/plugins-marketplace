#!/usr/bin/env python3
"""
Xala PM CI/CD Configuration Validator
Validates GitHub Actions, GitLab CI, and other CI config files
"""

import json
import sys
import re
from pathlib import Path

# CI/CD security patterns
CI_PATTERNS = [
    # Secrets exposure
    (r"\$\{\{\s*secrets\.\w+\s*\}\}.*echo", "HIGH", "Don't echo secrets - they may appear in logs"),
    (r"password:\s*['\"]?[^\s$]+", "CRITICAL", "Hardcoded password in CI config"),
    (r"api[_-]?key:\s*['\"]?[^\s$]+", "CRITICAL", "Hardcoded API key in CI config"),
    
    # Dangerous patterns
    (r"--force|--hard", "MEDIUM", "Force operations can cause data loss"),
    (r"rm\s+-rf\s+/", "CRITICAL", "Dangerous: recursive delete from root"),
    (r"chmod\s+777", "HIGH", "777 permissions are insecure"),
    
    # Best practices
    (r"pull_request:(?!.*branches)", "INFO", "Consider limiting PR trigger to specific branches"),
    (r"npm\s+install(?!\s+--frozen-lockfile)", "MEDIUM", "Use --frozen-lockfile for reproducible builds"),
    (r"pip\s+install(?!\s+-r)", "INFO", "Consider using requirements.txt for reproducibility"),
    
    # Security hardening
    (r"permissions:\s*\n\s+contents:\s*write", "HIGH", "Limit write permissions when possible"),
    (r"runs-on:\s*self-hosted", "INFO", "Self-hosted runners need security hardening"),
]

def validate_ci_config(content: str, file_path: str) -> list:
    """Validate CI/CD configuration"""
    issues = []
    
    # Only check CI config files
    ci_files = [
        ".github/workflows/",
        ".gitlab-ci.yml",
        "Jenkinsfile",
        ".travis.yml",
        "azure-pipelines.yml",
        "bitbucket-pipelines.yml"
    ]
    
    is_ci_file = any(ci in file_path for ci in ci_files)
    if not is_ci_file:
        return issues
    
    for pattern, severity, message in CI_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
            issues.append({
                "severity": severity,
                "message": message
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
    
    issues = validate_ci_config(content, file_path)
    
    if issues:
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "INFO": 3}
        issues.sort(key=lambda x: severity_order.get(x["severity"], 4))
        
        feedback = ["🔧 CI/CD Security Review:"]
        for issue in issues:
            icon = "🔴" if issue["severity"] == "CRITICAL" else "🟠" if issue["severity"] == "HIGH" else "🟡" if issue["severity"] == "MEDIUM" else "ℹ️"
            feedback.append(f"  {icon} [{issue['severity']}] {issue['message']}")
        
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

