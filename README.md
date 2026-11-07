# Crypto Trading Secure Harness

> Automated cryptocurrency trading information system with integrated cyber/data security architecture.
> Adapted from the AIxTech AI-agent harness model for safe, auditable, multi-asset-class trading strategies.

[![CI](https://github.com/kkzee92/crypto-trading-secure-harness/actions/workflows/ci.yml/badge.svg)](https://github.com/kkzee92/crypto-trading-secure-harness/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Licence](https://img.shields.io/badge/licence-MIT-green)

## Purpose
Provide a reference framework for building **automated crypto trading information systems** that prioritize:
- **Security & compliance** (secret scanning, no live keys in repo, PDPA-like data guards, audit trails, encryption, anomaly detection)
- **AI-agent safety** (rules, CI gates, human review, disclosure logs)
- **Modular strategies per asset class**: BTC (store-of-value), ETH (platform/staking), major alts, stables, DeFi/yield, memes, futures, options, etc.
- Backtesting, risk controls, and information systems (signals, dashboards, alerts) without production secrets.

## Key Architecture
- **Agent Harness**: `AGENTS.md`, task briefs, Definition of Done = CI green + human review
- **Security Layer**: gitleaks, ruff S-rules, dependency licence allow-list, environment-only secrets, synthetic data only, encryption guidance, zero-trust patterns
- **Trading Core**: Modular strategy engines with asset-class-specific risk profiles, position sizing, circuit breakers
- **Information Systems**: Signal aggregation (`src/info_system.py`), multi-source data (public/synthetic only in demo), logging for audit
- **Cyber Defense**: Network isolation patterns, key rotation guidance, anomaly detection hooks, kill-switch concepts

See `docs/architecture.md` and `docs/security-architecture.md`.

## Asset Class Strategies (Enhanced)
Each asset class has dedicated logic under `src/strategies/`:
- **BTC**: Digital gold / store-of-value — vol-targeting HODL + momentum filter, larger position allowance
- **ETH**: Smart-contract platform — relative strength vs BTC + staking yield consideration
- **Major Alts**: Higher beta — momentum with tighter stops and smaller size
- **Stables**: Peg monitoring and mean-reversion / yield ideas
- **DeFi / Yield**: Protocol risk scoring, IL awareness, very small size
- **Meme / High-vol**: Extreme risk limits (1% max position)
- **Spot**: Momentum, mean-reversion, grid, DCA with volatility filters
- **Futures/Perps**: Funding-rate arb, basis trading, liquidation-aware sizing
- **Options**: Volatility surface ideas, Greeks-based hedging, premium collection with max-loss caps

All strategies include:
- Asset-class specific risk parameters (max drawdown, position limits, stop-loss, leverage caps)
- Synthetic backtest fixtures (never live data with secrets)
- Unit tests that never touch live networks or keys

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt && pip install -e .
python -m cryptotrading demo
# Run tests
pytest
# Local CI gates (if scripts present)
scripts/ci_local.sh
```

## Security Principles
- No API keys, private keys, or seed phrases ever committed
- All market data fixtures are SYNTHETIC or public-only
- CI fails on secret patterns, personal data patterns, or insecure code
- Human review required for any strategy that can place orders
- Encryption, least privilege, audit trails, and anomaly detection as core design principles

**Disclaimer**: Educational / research framework only. Not financial advice. Trading involves substantial risk of loss. This system defaults to paper trading and contains no production credentials or live order execution.

## Licence
MIT
