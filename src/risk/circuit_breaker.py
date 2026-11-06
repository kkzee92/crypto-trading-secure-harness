"""Simple circuit breaker for trading systems."""
from dataclasses import dataclass

@dataclass
class CircuitBreaker:
    max_consecutive_losses: int = 3
    max_drawdown_pct: float = 0.10
    triggered: bool = False

    def check(self, consecutive_losses: int, drawdown: float) -> bool:
        if consecutive_losses >= self.max_consecutive_losses or drawdown >= self.max_drawdown_pct:
            self.triggered = True
            return False  # halt trading
        return True
