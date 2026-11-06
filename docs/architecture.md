# Architecture Overview

```mermaid
flowchart TB
    subgraph Harness
        A[AGENTS.md / Task Briefs]
        B[CI Gates: lint, test, gitleaks, licence]
        C[Human Review + Audit Log]
    end
    subgraph Security
        S1[Secret Scanning]
        S2[Env-only Credentials]
        S3[Synthetic Data Guards]
        S4[Circuit Breakers / Risk Gates]
    end
    subgraph Trading Core
        T1[Data Ingestion - public/synthetic]
        T2[Signal Engine]
        T3[Strategy Modules per Asset Class]
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
- `src/cryptotrading/` — package root
- `src/strategies/` — asset-class specific strategies
- `src/risk/` — position sizing, stops, circuit breakers
- `src/security/` — helpers for key handling, logging redaction
- `fixtures/` — SYNTHETIC market data
- `docs/` — security architecture, strategy notes, disclosure logs
