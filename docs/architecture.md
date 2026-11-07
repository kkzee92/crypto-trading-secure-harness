# Architecture Overview

```mermaid
flowchart TB
    subgraph Harness
        A[AGENTS.md / Task Briefs]
        B[CI Gates: lint, test, gitleaks, licence]
        C[Human Review + Audit Log]
    end
    subgraph Security
        S1[Secret Scanning + Encryption]
        S2[Env-only Credentials + Vault]
        S3[Synthetic Data Guards]
        S4[Circuit Breakers / Risk Gates]
        S5[Anomaly Detection Hooks]
        S6[Zero Trust / Least Privilege]
    end
    subgraph Trading Core
        T1[Data Ingestion - public/synthetic]
        T2[Signal Engine]
        T3[Strategy Modules per Asset Class<br/>BTC/ETH/ALT/STABLE/DEFI/MEME]
        T4[Risk & Position Manager]
        T5[Execution - paper by default]
        T6[Information System / Dashboard / Alerts]
    end
    A --> B --> C
    B --> Security
    Security --> Trading Core
    T3 --> T4 --> T5
    T1 --> T2 --> T3
    T5 --> T6
```

## Modules
- `src/cryptotrading/` — package root and demo entrypoint
- `src/strategies/` — asset-class specific strategies (spot, futures, options, defi, asset_classes.py)
- `src/risk/` — position sizing, stops, circuit breakers
- `src/info_system.py` — signal aggregation and audit logging
- `src/security/` — helpers for key handling, logging redaction (extend as needed)
- `fixtures/` — SYNTHETIC market data
- `docs/` — security architecture, strategy notes, disclosure logs

## Data Flow
1. Ingest public or synthetic market data.
2. Generate asset-class-aware signals.
3. Apply risk gates and circuit breakers.
4. Log to information system (audit trail).
5. (Optional paper) simulate execution; never live without explicit human gates.
