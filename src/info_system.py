"""Simple information system for aggregating signals across asset classes.
Educational only. Uses synthetic or public data in production use cases.
"""
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class SignalRecord:
    asset: str
    asset_class: str
    signal: str
    confidence: float
    timestamp: str
    notes: str = ""

class TradingInfoSystem:
    """Aggregates and logs signals with audit trail."""
    def __init__(self):
        self.signals: List[SignalRecord] = []
        self.risk_alerts: List[str] = []

    def add_signal(self, record: SignalRecord) -> None:
        self.signals.append(record)
        # Simple anomaly check
        if record.confidence > 0.9 and record.signal == "BUY":
            self.risk_alerts.append(f"High confidence BUY on {record.asset} — review size")

    def summary(self) -> Dict:
        by_class = {}
        for s in self.signals:
            by_class.setdefault(s.asset_class, []).append(s.signal)
        return {
            "total_signals": len(self.signals),
            "by_asset_class": {k: len(v) for k, v in by_class.items()},
            "alerts": self.risk_alerts[-5:],  # last 5
        }
