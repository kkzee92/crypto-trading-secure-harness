"""Offline tests for strategy risk gates."""
from src.strategies.spot import momentum_signal, apply_risk_gate, RiskParams
from src.strategies.futures import funding_arb_signal, check_liquidation_distance
from src.risk.circuit_breaker import CircuitBreaker

def test_momentum_basic():
    prices = [100, 101, 102, 103, 110]
    assert momentum_signal(prices, lookback=3) == "BUY"

def test_risk_gate_blocks_oversized():
    params = RiskParams(max_position_pct=0.05)
    assert apply_risk_gate("BUY", 10000, 600, params) == "HOLD"

def test_funding_arb():
    assert funding_arb_signal(0.001) == "SHORT_PERP_LONG_SPOT"
    assert funding_arb_signal(0.0) == "HOLD"

def test_liq_distance():
    assert check_liquidation_distance(100, 80, 0.15) is True
    assert check_liquidation_distance(100, 90, 0.15) is False

def test_circuit_breaker():
    cb = CircuitBreaker(max_consecutive_losses=2)
    assert cb.check(3, 0.01) is False
    assert cb.triggered is True
