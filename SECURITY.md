# Security Policy — Crypto Trading Secure Harness

## Supported versions
Latest commit on `main` only. Demonstration / research repository.

## Reporting vulnerabilities
Do **not** open public issues for security problems. Use GitHub private vulnerability reporting (Security → Advisories).

## Built-in protections
- **gitleaks**: full history + working tree secret scan
- **ruff security rules** (bandit-style)
- **Licence allow-list** + Dependabot
- **Custom secret & key pattern tripwires**
- Environment-only credential loading
- No live trading by default (paper/dry-run)
- Synthetic data only in fixtures

## Out of scope for this demo
- Production exchange connectivity
- Real funds or private keys
- Regulatory advice

If you discover a secret or private key pattern, report privately so it can be rotated and purged.
