# 🛡️ Security Policy — Vibe UI Skills Suite

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.4.x   | :white_check_mark: |
| 2.3.x   | :white_check_mark: |
| < 2.3   | :x:                |

---

## 🚨 Reporting a Vulnerability

We take the security and integrity of our AI Agent skill definitions and shell/PowerShell installers seriously. If you discover a security issue (e.g., installer vulnerability, unsafe code execution, or prompt injection vulnerability in agent instructions), please do **NOT** open a public issue.

Instead, please report vulnerabilities via:
1. **GitHub Security Advisory:** Submit a private report via the [Security Advisories](https://github.com/omid-io/vibe-ui-suite/security/advisories) tab.
2. **Direct Email:** Contact the maintainer at `3ntimental@gmail.com` with the subject `[SECURITY] Vibe UI Suite Vulnerability Report`.

### What to Include:
- A clear description of the vulnerability and potential attack vector.
- Steps to reproduce or proof-of-concept (PoC).
- Recommended mitigations or patches if available.

---

## 🛡️ Supply Chain & Safe Installer Guidelines

- **Safe Backup by Default:** The official installers (`install.sh` and `install.ps1`) preserve existing skill directories by creating `.bak` backups before applying updates (unless explicitly overridden with `--force` / `-Force`).
- **Verification:** When running automated installations, always verify the source repository: `https://github.com/omid-io/vibe-ui-suite`.
- **Zero Remote Execution:** Skills contain pure Markdown instructions and zero remote JavaScript execution or telemetry tracking.
