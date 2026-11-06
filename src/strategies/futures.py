"""Futures / perpetual strategies with funding and liquidation awareness."""
from dataclasses import dataclass

@dataclass
class FuturesRisk:
    max_leverage: float = 3.0
    liquidation_buffer_pct: float = 0.15  # stay 15% away from liq price
    funding_threshold: float = 0.0005

def funding_arb_signal(funding_rate: float, threshold: float = 0.0005) -> str:
    """Simple funding rate arbitrage idea (spot vs perp)."""
    if funding_rate > threshold:
        return "SHORT_PERP_LONG_SPOT"
    if funding_rate < -threshold:
        return "LONG_PERP_SHORT_SPOT"
    return "HOLD"

def check_liquidation_distance(entry: float, liq_price: float, buffer: float = 0.15) -> bool:
    distance = abs(entry - liq_price) / entry
    return distance >= buffer
