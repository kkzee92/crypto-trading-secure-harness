# AGENTS.md - Rules for AI coding agents in this crypto trading harness

These rules apply to any AI coding assistant working in this repository.

## 1. Scope and autonomy
- Work only on the current task brief. One task = one branch = one PR.
- Never push to main or merge your own PR.
- Never weaken CI gates, coverage thresholds, or security checks.

## 2. Data, privacy & secrets (critical for trading systems)
- Use **only synthetic fixtures** or clearly labelled public data.
- **Never** include real API keys, private keys, seed phrases, wallet addresses with balances, exchange credentials, or personal data.
- Secrets must be read from environment variables only (e.g. `EXCHANGE_API_KEY`).
- gitleaks and custom secret scanners run in CI — treat any flag as a hard stop.

## 3. Trading & risk rules
- All strategies must include explicit risk controls: max position size, stop-loss, circuit breaker, max daily loss.
- Order placement code must be behind a dry-run / paper-trading flag by default.
- Never hardcode live trading endpoints or credentials.
- Backtests must use synthetic or historical public data only.

## 4. Engineering rules
- Python 3.10+, prefer stdlib + approved deps.
- Tests first or alongside; tests must be fully offline.
- Run `scripts/ci_local.sh` before requesting review.

## 5. Disclosure
- Every AI-assisted commit must include trailers:
  `AI-Assisted: yes (<tool>)`
  `Human-Review: pending|<name, date>`
- Update `docs/ai-disclosure-log.md`.

## 6. Definition of Done
CI green (including security gates) + documented human review.
