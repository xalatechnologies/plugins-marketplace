#!/usr/bin/env python3
"""
Xala PM Smart Contract Security Scanner
Scans Solidity/Rust contracts for security vulnerabilities
"""

import json
import sys
import re

# Security patterns for smart contracts
SOLIDITY_PATTERNS = [
    # Critical vulnerabilities
    (r"\.call\{value:", "CRITICAL", "Reentrancy risk - use ReentrancyGuard"),
    (r"tx\.origin", "CRITICAL", "Never use tx.origin for authorization"),
    (r"delegatecall\(", "CRITICAL", "delegatecall is dangerous - verify target"),
    (r"selfdestruct\(", "CRITICAL", "selfdestruct can lock funds forever"),
    
    # High severity
    (r"block\.(timestamp|number)", "HIGH", "Block values can be manipulated by miners"),
    (r"\.transfer\(|\.send\(", "HIGH", "Use call{value:} instead of transfer/send"),
    (r"assembly\s*\{", "HIGH", "Inline assembly bypasses safety checks"),
    (r"unchecked\s*\{", "MEDIUM", "Unchecked math - verify no overflow possible"),
    
    # Security token specific
    (r"swap|exchange|dex|uniswap|sushiswap|pancake", "CRITICAL", "Security tokens CANNOT trade on DEX"),
    (r"liquidity\s*pool|lp\s*token|amm", "CRITICAL", "Security tokens CANNOT have liquidity pools"),
    
    # Best practices
    (r"public\s+\w+\s*;(?!.*immutable)", "MEDIUM", "Consider making state variables private"),
    (r"function\s+\w+\([^)]*\)\s+public(?!\s+view|\s+pure)", "INFO", "Consider access control for public functions"),
]

RUST_PATTERNS = [
    # Solana/Anchor patterns
    (r"#\[account\(mut\)\]", "INFO", "Mutable account - verify ownership check"),
    (r"invoke_signed", "HIGH", "CPI call - verify PDA seeds"),
    (r"unsafe\s*\{", "HIGH", "Unsafe block - requires careful review"),
]

def scan_contract(content: str, file_path: str) -> list:
    """Scan contract for security issues"""
    issues = []
    
    if file_path.endswith(".sol"):
        patterns = SOLIDITY_PATTERNS
    elif file_path.endswith(".rs"):
        patterns = RUST_PATTERNS
    else:
        return issues
    
    for pattern, severity, message in patterns:
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
    
    # Only scan contract files
    if not file_path.endswith((".sol", ".rs")):
        sys.exit(0)
    
    issues = scan_contract(content, file_path)
    
    if issues:
        # Sort by severity
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "INFO": 3}
        issues.sort(key=lambda x: severity_order.get(x["severity"], 4))
        
        critical_count = sum(1 for i in issues if i["severity"] == "CRITICAL")
        
        feedback = ["🔐 Smart Contract Security Scan:"]
        if critical_count > 0:
            feedback.append(f"  ⚠️  {critical_count} CRITICAL issues found!")
        
        for issue in issues:
            icon = "🔴" if issue["severity"] == "CRITICAL" else "🟠" if issue["severity"] == "HIGH" else "🟡"
            feedback.append(f"  {icon} [{issue['severity']}] {issue['message']}")
        
        # Block if critical issues in security token code
        if critical_count > 0:
            output = {
                "decision": "block",
                "reason": "\n".join(feedback),
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": "\n".join(feedback)
                }
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

