# REF-13: CAPA Log (Corrective and Preventive Action)

=== ":material-lightning-bolt: Quick (~1h)"

    **ISO 9001 Clause 10.2** | **Owner:** QMR | **Review:** Monthly

    ## CAPA Process

    ```mermaid
    graph LR
        A["Nonconformity"] --> B["Contain"]
        B --> C["Root Cause<br/>(5-Why)"]
        C --> D["Corrective<br/>Action"]
        D --> E["Verify<br/>Effectiveness"]
        E -->|OK| F["Close"]
        E -->|Not OK| C
        style A fill:#c0392b,color:#fff
        style C fill:#e67e22,color:#fff
        style D fill:#2471a3,color:#fff
        style F fill:#196f3d,color:#fff
    ```

    **Sources:** Audit findings, customer complaints, incidents, management review, process deviations

    ## CAPA Register Template

    | CAPA # | Date | Source | Description | Severity | Root Cause | Corrective Action | Owner | Due | Status |
    |:------:|:----:|:------:|-------------|:--------:|------------|-------------------|-------|:---:|:------:|
    | CA-001 | | | | Crit/Major/Minor | | | | | ☐ |

    > Effectiveness check at 30/60/90 days. Recurring issues trigger process changes, not just fixes.

=== ":material-book-open-variant: Essential (~3h)"

    **ISO 9001 Clause 10.2** | **Owner:** QMR | **Review:** Monthly

    ## CAPA Process

    ```mermaid
    graph TD
        A["Nonconformity Source"] --> B["Log in CAPA Register"]
        B --> C["Assign Owner"]
        C --> D["Immediate Containment"]
        D --> E["Root Cause Analysis"]
        E --> F["Define Corrective Action"]
        F --> G["Implement Action"]
        G --> H["Verify Effectiveness"]
        H -->|"Effective"| I["Close CAPA"]
        H -->|"Not Effective"| E
        I --> J["Update Risk Register & Lessons Learned"]
        style A fill:#c0392b,color:#fff
        style E fill:#e67e22,color:#fff
        style G fill:#2471a3,color:#fff
        style I fill:#196f3d,color:#fff
    ```

    **Sources:** Internal audit findings, customer complaints, production incidents, external audit findings, management review actions, process deviations

    ## Root Cause Methods

    | Method | When |
    |--------|------|
    | **5-Why** | Most nonconformities |
    | **Fishbone (Ishikawa)** | Complex, multiple causes |
    | **Fault Tree** | Critical/safety issues |
    | **Timeline Analysis** | Complex incident sequences |

    ## CAPA Register

    | CAPA # | Date | Source | Description | Severity | Root Cause | Containment | Corrective Action | Owner | Due | Status | Eff. Check | Effective? |
    |:------:|:----:|:------:|-------------|:--------:|------------|-------------|-------------------|-------|:---:|:------:|:----------:|:----------:|
    | CA-001 | | | | | | | | | | ☐ | | ☐ |

    ## Example CAPA

    | Field | Example |
    |-------|---------|
    | **CAPA #** | CA-001 |
    | **Source** | Production Incident INC-2026-042 |
    | **Description** | Reprocessing pipeline produced corrupted output due to race condition |
    | **Severity** | Critical |
    | **Root Cause** | Shared mutable state without proper locking; insufficient concurrent test coverage |
    | **Containment** | Halted pipeline, re-processed impacted datasets, notified teams |
    | **Corrective Action** | Thread-safe data handling, concurrent integration tests, integrity checksums |
    | **Effectiveness** | 90-day check: no recurrence, all outputs pass integrity checks |

    ## Dashboard Metrics

    | Metric | Current | Previous | Trend |
    |--------|:-------:|:--------:|:-----:|
    | Open CAPAs | _[#]_ | _[#]_ | ↑↓→ |
    | Avg time to close | _[days]_ | _[days]_ | ↑↓→ |
    | Effectiveness rate | _[%]_ | _[%]_ | ↑↓→ |
    | Recurring issues | _[#]_ | _[#]_ | ↑↓→ |

=== ":material-book-open-page-variant: Full"

    ## DDD Unit — Data Driven Development | AD/ADAS Tooling

    **Document Owner:** QMR
    **Last Review:** YYYY-MM-DD
    **Review Frequency:** Monthly

    ---

    ## 1. Purpose

    Tracks all corrective and preventive actions from nonconformities, audit findings, customer complaints, and incidents, as required by ISO 9001:2015 Clause 10.2.

    ---

    ## 2. CAPA Process

    ```mermaid
    graph TD
        A["Nonconformity Source"] --> B["Log in CAPA Register"]
        B --> C["Assign Owner"]
        C --> D["Immediate Containment"]
        D --> E["Root Cause Analysis"]
        E --> F["Define Corrective Action"]
        F --> G["Implement Action"]
        G --> H["Verify Effectiveness"]
        H -->|"Effective"| I["Close CAPA"]
        H -->|"Not Effective"| E
        I --> J["Update Risk Register<br/>Share Lessons Learned"]

        subgraph "Sources"
            S1["Internal Audit Finding"]
            S2["Customer Complaint"]
            S3["Production Incident"]
            S4["External Audit Finding"]
            S5["Management Review Action"]
            S6["Process Deviation"]
        end
        S1 & S2 & S3 & S4 & S5 & S6 --> A

        style A fill:#c0392b,color:#fff
        style E fill:#e67e22,color:#fff
        style G fill:#2471a3,color:#fff
        style H fill:#7d3c98,color:#fff
        style I fill:#196f3d,color:#fff
    ```

    ---

    ## 3. Root Cause Analysis Methods

    | Method | When to Use | Description |
    |--------|------------|-------------|
    | **5-Why** | Most nonconformities | Ask "Why?" iteratively until root cause is found |
    | **Fishbone (Ishikawa)** | Complex issues with multiple potential causes | Categorize causes: People, Process, Technology, Environment |
    | **Fault Tree Analysis** | Critical/safety-related issues | Top-down deductive analysis |
    | **Timeline Analysis** | Incidents with complex sequence of events | Map events chronologically to find trigger |

    ---

    ## 4. CAPA Register

    | CAPA # | Date Opened | Source | Description | Severity | Root Cause Method | Root Cause | Containment Action | Corrective Action | Owner | Due Date | Status | Effectiveness Check Date | Effective? | Date Closed |
    |:------:|:----------:|:------:|-------------|:--------:|:-----------------:|------------|-------------------|-------------------|-------|:--------:|:------:|:------------------------:|:----------:|:-----------:|
    | CA-001 | YYYY-MM-DD | _[Source]_ | _[Description of nonconformity]_ | Critical / Major / Minor | 5-Why | _[Root cause]_ | _[Immediate action taken]_ | _[Corrective action]_ | _[Name]_ | YYYY-MM-DD | ☐ Open | YYYY-MM-DD | ☐ Yes / ☐ No | YYYY-MM-DD |
    | CA-002 | | | | | | | | | | | | | | |
    | CA-003 | | | | | | | | | | | | | | |

    ---

    ## 5. Example CAPA Entry (for reference)

    | Field | Example |
    |-------|---------|
    | **CAPA #** | CA-001 |
    | **Date Opened** | 2026-01-15 |
    | **Source** | Production Incident INC-2026-042 |
    | **Description** | Reprocessing pipeline produced corrupted output for 3 datasets due to race condition in parallel processing |
    | **Severity** | Critical |
    | **Root Cause Method** | 5-Why |
    | **Root Cause** | Shared mutable state in pipeline worker threads without proper locking; insufficient integration test coverage for concurrent scenarios |
    | **Containment** | Immediately halted affected pipeline runs; manually re-processed impacted datasets; notified affected AD teams |
    | **Corrective Action** | (1) Implemented thread-safe data handling with immutable data structures; (2) Added concurrent integration tests; (3) Added data integrity checksums at pipeline output |
    | **Owner** | [Data Engineering Lead] |
    | **Due Date** | 2026-02-15 |
    | **Status** | ✅ Closed |
    | **Effectiveness Check** | 2026-03-15 — No recurrence; all pipeline outputs pass integrity checks |
    | **Effective?** | ✅ Yes |
    | **Date Closed** | 2026-03-15 |

    ---

    ## 6. CAPA Dashboard Metrics

    | Metric | Current Period | Previous Period | Trend |
    |--------|:-------------:|:--------------:|:-----:|
    | Open CAPAs | _[#]_ | _[#]_ | ↑↓→ |
    | CAPAs opened this period | _[#]_ | _[#]_ | ↑↓→ |
    | CAPAs closed this period | _[#]_ | _[#]_ | ↑↓→ |
    | Average time to close | _[days]_ | _[days]_ | ↑↓→ |
    | Overdue CAPAs | _[#]_ | _[#]_ | ↑↓→ |
    | Effectiveness rate | _[%]_ | _[%]_ | ↑↓→ |
    | Recurring issues | _[#]_ | _[#]_ | ↑↓→ |

    ---

    ## 7. Lessons Learned Register

    | CAPA # | Lesson | Shared With | Date Shared | Applied To |
    |:------:|--------|-------------|:-----------:|------------|
    | CA-001 | _[Key learning]_ | _[Teams/All-hands]_ | YYYY-MM-DD | _[Process/standard updated]_ |
    | | | | | |

    ---

    ## 8. Review Log

    | Date | Reviewer | Changes Made |
    |------|----------|-------------|
    | YYYY-MM-DD | [Name] | Initial creation |

    ---

    *ISO 9001:2015 Reference: Clause 10.2*
