"""Spot trading strategies with risk controls (educational)."""
from dataclasses import dataclass
from typing import Protocol

@dataclass
class RiskParams:
    max_position_pct: float = 0.05  # 5% of equity
    stop_loss_pct: float = 0.02
    max_daily_loss_pct: float = 0.03

class Signal(Protocol):
    def generate(self, prices: list[float]) -> str: ...  # "BUY", "SELL", "HOLD"

def momentum_signal(prices: list[float], lookback: int = 20) -> str:
    if len(prices) < lookback + 1:
        return "HOLD"
    recent = prices[-lookback:]
    if prices[-1] > max(recent[:-1]):
        return "BUY"
    if prices[-1] < min(recent[:-1]):
        return "SELL"
    return "HOLD"

def apply_risk_gate(signal: str, equity: float, position_value: float, params: RiskParams) -> str:
    """Enforce position limits before acting on signal."""
    if signal == "BUY" and position_value > equity * params.max_position_pct:
        return "HOLD"  # already at limit
    return signal
