#!/usr/bin/env python3
"""
Xala PM Compliance Checker
Validates code against regulatory requirements (GDPR, Security Tokens, etc.)
"""

import json
import sys
import re

# Compliance patterns
COMPLIANCE_PATTERNS = {
    "security_token": [
        (r"(swap|trade|exchange)\s*\(", "CRITICAL", "Security tokens CANNOT be traded on exchanges"),
        (r"(uniswap|sushiswap|pancake|dex|curve)", "CRITICAL", "Security tokens CANNOT use DEX protocols"),
        (r"(liquidity|pool|amm)", "CRITICAL", "Security tokens CANNOT have liquidity pools"),
        (r"transfer\s*\([^)]+\)(?!.*whitelist)", "HIGH", "Transfers must verify whitelist"),
        (r"mint\s*\([^)]+\)(?!.*onlyOwner|onlyAdmin)", "HIGH", "Minting requires access control"),
    ],
    "gdpr": [
        (r"(email|phone|address|ssn|social.?security)", "INFO", "PII field - ensure consent & encryption"),
        (r"localStorage\.setItem.*user", "HIGH", "Don't store user data in localStorage without consent"),
        (r"cookie.*=(?!.*consent)", "MEDIUM", "Set cookies only after user consent"),
        (r"analytics|tracking|pixel", "INFO", "Analytics requires user consent under GDPR"),
    ],
    "pci_dss": [
        (r"credit.?card|card.?number|cvv|cvc", "CRITICAL", "Never store raw card data - use tokenization"),
        (r"console\.log.*card", "CRITICAL", "Never log card data"),
    ]
}

def check_compliance(content: str, file_path: str) -> list:
    """Check for compliance issues"""
    issues = []
    
    # Determine which patterns to apply based on file content/path
    patterns_to_check = []
    
    # Security token patterns for Solidity
    if file_path.endswith(".sol"):
        patterns_to_check.extend(COMPLIANCE_PATTERNS["security_token"])
    
    # GDPR for frontend code
    if file_path.endswith((".tsx", ".jsx", ".ts", ".js")):
        patterns_to_check.extend(COMPLIANCE_PATTERNS["gdpr"])
    
    # PCI-DSS for any code
    patterns_to_check.extend(COMPLIANCE_PATTERNS["pci_dss"])
    
    for pattern, severity, message in patterns_to_check:
        if re.search(pattern, content, re.IGNORECASE):
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
    
    issues = check_compliance(content, file_path)
    
    if issues:
        critical = [i for i in issues if i["severity"] == "CRITICAL"]
        
        feedback = ["📋 Compliance Review:"]
        if critical:
            feedback.append(f"  ⛔ {len(critical)} CRITICAL compliance violations!")
        
        for issue in issues:
            icon = "⛔" if issue["severity"] == "CRITICAL" else "⚠️" if issue["severity"] == "HIGH" else "ℹ️"
            feedback.append(f"  {icon} [{issue['severity']}] {issue['message']}")
        
        # Block on critical compliance issues
        if critical:
            output = {
                "decision": "block",
                "reason": "\n".join(feedback)
            }
        else:
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

