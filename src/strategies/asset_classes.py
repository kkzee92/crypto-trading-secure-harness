"""Asset-class specific trading strategies (educational, synthetic data only).

Strategies tailored by asset type:
- BTC: Digital gold / store-of-value — vol-targeting HODL + momentum filter
- ETH: Smart-contract platform — staking yield + relative strength
- Major Alts (SOL, etc.): Higher beta — tighter stops, momentum
- Stables: Yield / arb / mean-reversion around peg
- DeFi / Yield tokens: Protocol risk scoring + IL awareness
- Meme / High-vol: Extreme risk limits, small size only

All functions are pure and offline-testable. No live keys or orders.
"""
from dataclasses import dataclass
from typing import Literal

Signal = Literal["BUY", "SELL", "HOLD", "REDUCE"]

@dataclass
class AssetRiskProfile:
    max_position_pct: float
    stop_loss_pct: float
    max_leverage: float = 1.0
    vol_target: float | None = None  # annualized vol target if applicable

# Pre-defined profiles per asset class
PROFILES = {
    "BTC": AssetRiskProfile(max_position_pct=0.20, stop_loss_pct=0.15, max_leverage=1.0, vol_target=0.40),
    "ETH": AssetRiskProfile(max_position_pct=0.15, stop_loss_pct=0.12, max_leverage=1.5, vol_target=0.50),
    "ALT": AssetRiskProfile(max_position_pct=0.05, stop_loss_pct=0.08, max_leverage=2.0),
    "STABLE": AssetRiskProfile(max_position_pct=0.50, stop_loss_pct=0.005, max_leverage=1.0),
    "DEFI": AssetRiskProfile(max_position_pct=0.03, stop_loss_pct=0.10, max_leverage=1.0),
    "MEME": AssetRiskProfile(max_position_pct=0.01, stop_loss_pct=0.25, max_leverage=1.0),
}

def btc_store_of_value_strategy(
    prices: list[float],
    current_vol: float,
    equity: float,
    current_position_value: float,
) -> Signal:
    """BTC as digital gold: accumulate on dips when vol is not extreme."""
    profile = PROFILES["BTC"]
    if len(prices) < 30:
        return "HOLD"
    # Simple momentum + vol filter
    ma20 = sum(prices[-20:]) / 20
    if prices[-1] > ma20 * 1.02 and current_vol < (profile.vol_target or 1.0):
        signal = "BUY"
    elif prices[-1] < ma20 * 0.95:
        signal = "REDUCE"
    else:
        signal = "HOLD"
    # Risk gate
    if signal == "BUY" and current_position_value >= equity * profile.max_position_pct:
        return "HOLD"
    return signal

def eth_platform_strategy(
    eth_prices: list[float],
    btc_prices: list[float],
    staking_apy: float,
) -> Signal:
    """ETH: relative strength vs BTC + staking yield consideration."""
    if len(eth_prices) < 20 or len(btc_prices) < 20:
        return "HOLD"
    eth_ret = (eth_prices[-1] / eth_prices[-20]) - 1
    btc_ret = (btc_prices[-1] / btc_prices[-20]) - 1
    if eth_ret > btc_ret + 0.05 and staking_apy > 0.03:
        return "BUY"
    if eth_ret < btc_ret - 0.10:
        return "REDUCE"
    return "HOLD"

def altcoin_momentum(
    prices: list[float],
    lookback: int = 10,
) -> Signal:
    """Higher-beta alts: aggressive momentum with tight risk."""
    if len(prices) < lookback + 1:
        return "HOLD"
    if prices[-1] > max(prices[-lookback:-1]):
        return "BUY"
    if prices[-1] < min(prices[-lookback:-1]) * 0.97:
        return "SELL"
    return "HOLD"

def stable_peg_monitor(price: float, peg: float = 1.0, tolerance: float = 0.005) -> Signal:
    """Stables: alert or trade around peg deviations."""
    if abs(price - peg) > tolerance:
        return "REDUCE" if price > peg else "BUY"  # mean reversion idea
    return "HOLD"

def apply_asset_risk(
    signal: Signal,
    asset_class: str,
    equity: float,
    position_value: float,
) -> Signal:
    """Enforce asset-class specific position limits."""
    profile = PROFILES.get(asset_class, PROFILES["ALT"])
    if signal in ("BUY",) and position_value > equity * profile.max_position_pct:
        return "HOLD"
    return signal
