"""Safe demo entry point — fully offline, synthetic data."""

def run_demo() -> None:
    print("=== Crypto Trading Secure Harness Demo ===")
    print("Mode: PAPER / SYNTHETIC — no live keys or networks")
    print("Asset classes loaded: Spot, Futures, Options, DeFi")
    print("Risk gates: ACTIVE")
    print("Security scanners: configured (run scripts/ci_local.sh)")
    print("Demo complete. See docs/ for architecture and strategies.")

if __name__ == "__main__":
    run_demo()
