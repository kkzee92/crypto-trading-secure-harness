"""Offline tests for asset-class specific strategies."""
from src.strategies.asset_classes import (
    btc_store_of_value_strategy,
    eth_platform_strategy,
    altcoin_momentum,
    stable_peg_monitor,
    apply_asset_risk,
    PROFILES,
)

def test_btc_strategy_basic():
    prices = [100.0] * 25 + [105.0]
    assert btc_store_of_value_strategy(prices, current_vol=0.3, equity=10000, current_position_value=0) in ("BUY", "HOLD")

def test_eth_relative_strength():
    eth = [100.0] * 19 + [120.0]
    btc = [100.0] * 19 + [105.0]
    assert eth_platform_strategy(eth, btc, staking_apy=0.04) == "BUY"

def test_alt_momentum():
    prices = [100, 101, 102, 110]
    assert altcoin_momentum(prices, lookback=3) == "BUY"

def test_stable_peg():
    assert stable_peg_monitor(1.0) == "HOLD"
    assert stable_peg_monitor(1.02) == "REDUCE"

def test_risk_gate_btc():
    # At limit
    assert apply_asset_risk("BUY", "BTC", 10000, 2100) == "HOLD"
    # Under limit
    assert apply_asset_risk("BUY", "BTC", 10000, 1000) == "BUY"

def test_profiles_exist():
    assert "BTC" in PROFILES
    assert PROFILES["MEME"].max_position_pct <= 0.02
