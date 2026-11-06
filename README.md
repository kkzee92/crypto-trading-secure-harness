# Crypto Trading Secure Harness

> Automated cryptocurrency trading information system with integrated cyber/data security architecture.
> Adapted from the AIxTech AI-agent harness model for safe, auditable, multi-asset-class trading strategies.

[![CI](https://github.com/kkzee92/crypto-trading-secure-harness/actions/workflows/ci.yml/badge.svg)](https://github.com/kkzee92/crypto-trading-secure-harness/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Licence](https://img.shields.io/badge/licence-MIT-green)

## Purpose
Provide a reference framework for building **automated crypto trading information systems** that prioritize:
- **Security & compliance** (secret scanning, no live keys in repo, PDPA-like data guards, audit trails)
- **AI-agent safety** (rules, CI gates, human review, disclosure logs)
- **Modular strategies per asset class**: Spot, Futures/Perpetuals, Options, DeFi/yield, Cross-asset, etc.
- Backtesting, risk controls, and information systems (signals, dashboards, alerts) without production secrets.

## Key Architecture
- **Agent Harness**: `AGENTS.md`, task briefs, Definition of Done = CI green + human review
- **Security Layer**: gitleaks, ruff S-rules, dependency licence allow-list, environment-only secrets, synthetic data only
- **Trading Core**: Modular strategy engines with risk gates, position sizing, circuit breakers
- **Information Systems**: Signal aggregation, multi-source data (public APIs only in demo), logging for audit
- **Cyber Defense**: Network isolation patterns, key rotation guidance, anomaly detection hooks

See `docs/architecture.md` and `docs/security-architecture.md`.

## Asset Class Strategies (Enhanced)
Each asset class has a dedicated module under `src/strategies/`:
- **Spot**: Momentum, mean-reversion, grid, DCA with volatility filters
- **Futures/Perps**: Funding-rate arb, basis trading, liquidation-aware sizing
- **Options**: Volatility surface, Greeks-based hedging, premium collection with max-loss caps
- **DeFi**: Yield farming with IL protection, liquidity provision strategies, protocol risk scoring
- **Cross-asset / Macro**: Correlation regimes, on-chain + off-chain signals

All strategies include:
- Risk parameters (max drawdown, position limits, stop-loss)
- Synthetic backtest fixtures
- Unit tests that never touch live networks or keys

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt && pip install -e .
python -m cryptotrading demo
scripts/ci_local.sh   # run all security + quality gates
```

## Security Principles
- No API keys, private keys, or seed phrases ever committed
- All market data fixtures are SYNTHETIC or public-only
- CI fails on secret patterns, personal data patterns, or insecure code
- Human review required for any strategy that can place orders

**Disclaimer**: Educational / research framework only. Not financial advice. Trading involves risk of loss.

## Licence
MIT
