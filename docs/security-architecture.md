# Cyber & Data Security Architecture

## Threat Model (High Level)
- Credential leakage (API keys, private keys)
- Unauthorized live trading
- Data exfiltration of personal or proprietary signals
- Supply-chain attacks on dependencies
- AI agent introducing insecure code or secrets

## Controls
1. **Secret Management**: Environment variables + external vault (recommended for prod). Never in repo.
2. **Scanning**: gitleaks on every commit/PR; custom patterns for common exchange key formats.
3. **Least Privilege**: Paper-trading mode default; live mode requires explicit flag + human approval.
4. **Audit Trail**: AI disclosure logs, review logs, structured logging with redaction.
5. **Dependency Security**: Licence allow-list, Dependabot, pinned versions.
6. **Network**: Offline tests; injectable HTTP clients; no hardcoded endpoints with credentials.
7. **Risk Gates**: Hard limits on position size, daily loss, leverage — enforced before any order.

## Asset-Class Specific Security Notes
- **Spot**: Focus on API key scoping (trade-only, no withdrawal).
- **Futures**: Additional liquidation and margin checks.
- **Options**: Max-loss hard caps.
- **DeFi**: Private key isolation; never store seeds; use hardware wallet or secure enclave patterns in prod.

See also `AGENTS.md` and `SECURITY.md`.
