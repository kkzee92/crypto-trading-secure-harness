"""Options strategies with defined-risk controls."""
from dataclasses import dataclass

@dataclass
class OptionsRisk:
    max_loss_pct: float = 0.02  # hard cap on premium sold relative to equity
    min_iv_rank: float = 30.0

def premium_collection_signal(iv_rank: float, min_rank: float = 30.0) -> str:
    if iv_rank >= min_rank:
        return "SELL_PREMIUM_DEFINED_RISK"
    return "HOLD"
