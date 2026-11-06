# Strategy Modules by Asset Class

Each subdirectory contains:
- Strategy implementation (pure functions where possible)
- Risk parameters
- Synthetic backtest example
- Tests

## Spot
Momentum, mean-reversion, grid trading with volatility targeting.

## Futures / Perpetuals
Funding rate arbitrage, basis trading, liquidation-distance sizing.

## Options
Volatility harvesting, delta-neutral strategies, defined-risk premium selling.

## DeFi
Yield strategies with impermanent-loss awareness, protocol risk scoring.

All strategies enforce:
- Maximum position size as % of equity
- Stop-loss / take-profit
- Circuit breaker on consecutive losses or drawdown
