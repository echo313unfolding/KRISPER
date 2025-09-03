# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2   | :x:                |

## Reporting a Vulnerability

Please report security vulnerabilities to: **security-echo@protonmail.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We aim to respond within 48 hours.

## Security Considerations

KRISPER executes natural language as code. When using:

1. **Validate all inputs** - Natural language can be ambiguous
2. **Sandbox execution** - Run in isolated environments
3. **Review generated IR** - Inspect the intermediate representation before execution
4. **No eval()** - KRISPER uses structured transformations, not eval

## Known Limitations

- Pattern matching is regex-based (potential ReDoS with crafted inputs)
- No built-in sandboxing for executor modules
- Whitespace encoding is for demonstration only