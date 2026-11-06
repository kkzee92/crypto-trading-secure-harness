"""DeFi / yield strategies with protocol risk awareness."""
from dataclasses import dataclass

@dataclass
class DeFiRisk:
    max_protocol_risk_score: float = 3.0  # 1-10 scale
    il_tolerance_pct: float = 0.05

def yield_signal(apy: float, protocol_risk: float, max_risk: float = 3.0) -> str:
    if protocol_risk <= max_risk and apy > 0.05:
        return "PROVIDE_LIQUIDITY"
    return "HOLD"
