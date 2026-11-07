# Cyber & Data Security Architecture

## Threat Model (High Level)
- Credential leakage (API keys, private keys, seed phrases)
- Unauthorized live trading or withdrawal
- Data exfiltration of proprietary signals, positions, or PII
- Supply-chain attacks on dependencies or models
- AI agent introducing insecure code, secrets, or logic bugs
- Anomalous activity (flash crashes, oracle manipulation, exchange hacks)
- Insider or compromised CI/CD pipelines

## Controls
1. **Secret Management**: Environment variables + external vault (HashiCorp Vault, AWS Secrets Manager, etc. for prod). Never in repo or logs. Key rotation policy documented.
2. **Scanning**: gitleaks + custom patterns for exchange API key formats on every commit/PR; secret scanning in CI.
3. **Least Privilege**: Paper-trading mode default; live mode requires explicit flag + multi-factor human approval. Trade-only API keys, no withdrawal permissions.
4. **Audit Trail**: AI disclosure logs, review logs, structured logging with automatic redaction of sensitive fields. Immutable logs where possible.
5. **Dependency Security**: Licence allow-list, Dependabot, pinned versions, SBOMs.
6. **Network**: Offline tests by default; injectable HTTP clients; no hardcoded credentials; TLS everywhere; network segmentation for trading engines.
7. **Risk Gates**: Hard limits on position size, daily loss, leverage, drawdown — enforced in code before any order intent. Circuit breakers.
8. **Encryption**: Data at rest (AES-256) for any stored market data or signals; in transit (TLS 1.3+). No plain-text sensitive data.
9. **Monitoring & Anomaly Detection**: Hooks for unusual order sizes, rapid position changes, funding rate extremes, or price deviations. Alert on deviations from expected behavior.
10. **Zero Trust**: Continuous verification, micro-segmentation, least-privilege service accounts.
11. **Data Security / Privacy**: Synthetic data only in repo. No personal data. PDPA/GDPR-style guards in CI. Data minimization.
12. **Incident Response**: Documented playbook for key compromise, anomalous trades, or exchange issues. Kill-switch capability.

## Asset-Class Specific Security Notes
- **BTC**: Focus on cold storage for long-term holdings; API key scoping (trade-only).
- **ETH / Staking**: Secure validator or staking service isolation; smart contract risk assessment.
- **Futures / Perps**: Additional liquidation and margin checks; leverage hard caps.
- **Options**: Max-loss hard caps; defined-risk only in automated mode.
- **DeFi**: Private key isolation (never store seeds); use hardware wallet or secure enclave patterns in prod; protocol audit status tracking; impermanent loss and smart contract risk scoring.
- **Stables**: Peg monitoring; counterparty risk (issuer).
- **Alts / Meme**: Strict position limits; higher monitoring for volatility and liquidity.

## AI-Agent Specific
- AGENTS.md forbids loading real keys or personal data into prompts.
- CI tripwires for secret patterns and personal data.
- Human review mandatory for any code that can generate order intents.

See also `AGENTS.md`, `SECURITY.md`, and CI workflows.
