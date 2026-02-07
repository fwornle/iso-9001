# REF-06: Risk Register

=== ":material-lightning-bolt: Quick (~1h)"

    **ISO 9001 Clause 6.1** | **Owner:** QMR | **Review:** Quarterly

    ## Risk Assessment: 5x5 Matrix (Likelihood x Impact)

    | Score | Level | Action |
    |:-----:|:-----:|--------|
    | 1-4 | Low (Green) | Accept and monitor |
    | 5-9 | Medium (Yellow) | Reduce with mitigation |
    | 10-15 | High (Orange) | Active mitigation required |
    | 16-25 | Critical (Red) | Immediate action, escalate |

    ## Top Risks

    | ID | Risk | Score | Level | Mitigation |
    |----|------|:-----:|:-----:|------------|
    | R-001 | Single point of failure in data ingestion | 15 | High | Redundant paths, automated failover |
    | R-002 | Key person dependency for simulation | 16 | Critical | Cross-training, runbooks |
    | R-004 | Data breach in driving data storage | 10 | High | Encryption, RBAC, pen testing |
    | R-005 | Regulatory change requiring re-qualification | 12 | High | Regulatory monitoring, modular approach |
    | R-006 | Open-source supply chain vulnerability | 12 | High | Dependency scanning, SBOM |

    > Be ready to discuss 2-3 examples of risks identified and how they were mitigated.

=== ":material-book-open-variant: Essential (~3h)"

    **ISO 9001 Clause 6.1** | **Owner:** QMR | **Review:** Quarterly

    ## Risk Methodology

    **Likelihood:** 1 (Rare) to 5 (Almost Certain) | **Impact:** 1 (Negligible) to 5 (Critical)

    | Score | Level | Action |
    |:-----:|:-----:|--------|
    | 1-4 | Low | Accept and monitor |
    | 5-9 | Medium | Reduce with mitigation |
    | 10-15 | High | Active mitigation required |
    | 16-25 | Critical | Immediate action, escalate |

    ## Risk Register

    | ID | Risk | L | I | Score | Level | Owner | Mitigation | Status |
    |----|------|:-:|:-:|:-----:|:-----:|-------|------------|--------|
    | R-001 | Single point of failure in data ingestion | 3 | 5 | 15 | High | _[Name]_ | Redundant paths, automated failover | In Progress |
    | R-002 | Key person dependency for simulation | 4 | 4 | 16 | Critical | _[Name]_ | Cross-training, runbooks, pair rotations | In Progress |
    | R-003 | Cloud cost overrun | 3 | 3 | 9 | Medium | _[Name]_ | FinOps, cost alerts, reserved instances | Monitoring |
    | R-004 | Data breach in driving data | 2 | 5 | 10 | High | _[Name]_ | Encryption, RBAC, pen testing | In Progress |
    | R-005 | Regulatory change requiring re-qualification | 3 | 4 | 12 | High | _[Name]_ | Regulatory monitoring, modular approach | Monitoring |
    | R-006 | Supply chain vulnerability (OSS) | 3 | 4 | 12 | High | _[Name]_ | Dependency scanning, SBOM, approved list | In Progress |
    | R-007 | Cloud provider region outage | 2 | 5 | 10 | High | _[Name]_ | Multi-AZ, DR plan, regular DR testing | Implemented |
    | R-008 | Talent attrition | 4 | 3 | 12 | High | _[Name]_ | Compensation, learning budget, culture | Ongoing |

    ## Opportunity Register

    | ID | Opportunity | Score | Owner | Status |
    |----|------------|:-----:|-------|--------|
    | O-001 | New GPU instances for simulation speedup | 16 | _[Name]_ | Evaluating |
    | O-002 | Simulation-as-a-service for partner OEMs | 10 | _[Name]_ | Proposed |
    | O-003 | Open-source frameworks to reduce maintenance | 9 | _[Name]_ | Evaluating |

=== ":material-book-open-page-variant: Full"

    ## DDD Unit — Data Driven Development | AD/ADAS Tooling

    **Document Owner:** QMR
    **Last Review:** YYYY-MM-DD
    **Next Review:** YYYY-MM-DD
    **Review Frequency:** Quarterly

    ---

    ## 1. Risk Assessment Methodology

    ### 1.1 Likelihood Scale

    | Score | Level | Description |
    |-------|-------|-------------|
    | 1 | Rare | < 5% probability in next 12 months |
    | 2 | Unlikely | 5–20% probability |
    | 3 | Possible | 20–50% probability |
    | 4 | Likely | 50–80% probability |
    | 5 | Almost Certain | > 80% probability |

    ### 1.2 Impact Scale

    | Score | Level | Description |
    |-------|-------|-------------|
    | 1 | Negligible | Minor inconvenience, no SLA impact |
    | 2 | Minor | Reduced performance, workaround available |
    | 3 | Moderate | SLA breach for some users, significant effort to resolve |
    | 4 | Major | Major service outage, data integrity concern, customer escalation |
    | 5 | Critical | Complete service failure, data loss, safety-relevant impact, regulatory breach |

    ### 1.3 Risk Matrix

    ```mermaid
    quadrantChart
        title Risk Assessment Matrix (Likelihood × Impact)
        x-axis Low Impact --> High Impact
        y-axis Low Likelihood --> High Likelihood
        quadrant-1 High Risk - Mitigate
        quadrant-2 Medium Risk - Monitor
        quadrant-3 Low Risk - Accept
        quadrant-4 Medium Risk - Reduce
    ```

    | Risk Score | Level | Action Required |
    |------------|-------|-----------------|
    | 1–4 | **Low** (Green) | Accept and monitor |
    | 5–9 | **Medium** (Yellow) | Reduce — define mitigation actions |
    | 10–15 | **High** (Orange) | Mitigate — active mitigation required |
    | 16–25 | **Critical** (Red) | Immediate action — escalate to management |

    ---

    ## 2. Risk Register

    | ID | Risk Description | Category | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level | Owner | Mitigation Actions | Status | Target Date | Residual Risk |
    |----|-----------------|----------|:-----------------:|:------------:|:----------:|:----------:|-------|-------------------|--------|-------------|:-------------:|
    | R-001 | Single point of failure in data ingestion pipeline | Technical | 3 | 5 | 15 | High | [Name] | Implement redundant ingestion paths, automated failover | In Progress | YYYY-MM-DD | 6 |
    | R-002 | Key person dependency for simulation infrastructure | People | 4 | 4 | 16 | Critical | [Name] | Cross-training program, comprehensive runbooks, pair rotations | In Progress | YYYY-MM-DD | 8 |
    | R-003 | Cloud cost overrun impacting budget | Financial | 3 | 3 | 9 | Medium | [Name] | FinOps practices, cost alerts, reserved instances | Monitoring | YYYY-MM-DD | 4 |
    | R-004 | Data breach in driving data storage | Security | 2 | 5 | 10 | High | [Name] | Encryption at rest/transit, RBAC, penetration testing, security audits | In Progress | YYYY-MM-DD | 5 |
    | R-005 | Regulatory change requiring tool re-qualification | Compliance | 3 | 4 | 12 | High | [Name] | Regulatory monitoring, modular qualification approach, legal counsel engagement | Monitoring | YYYY-MM-DD | 8 |
    | R-006 | Supply chain vulnerability in open-source dependencies | Technical | 3 | 4 | 12 | High | [Name] | Dependency scanning (Snyk), SBOM generation, approved dependency list | In Progress | YYYY-MM-DD | 6 |
    | R-007 | Loss of cloud provider availability (region outage) | Infrastructure | 2 | 5 | 10 | High | [Name] | Multi-AZ deployment, disaster recovery plan, regular DR testing | Implemented | YYYY-MM-DD | 4 |
    | R-008 | Talent attrition in competitive AD market | People | 4 | 3 | 12 | High | [Name] | Competitive compensation, learning budget, interesting projects, team culture | Ongoing | YYYY-MM-DD | 8 |
    | R-009 | *[Add your risks]* | | | | | | | | | | |

    ---

    ## 3. Opportunity Register

    | ID | Opportunity | Category | Likelihood | Benefit | Score | Owner | Actions | Status |
    |----|------------|----------|:----------:|:-------:|:-----:|-------|---------|--------|
    | O-001 | Leverage new GPU instances for simulation speedup | Technical | 4 | 4 | 16 | [Name] | PoC with new instance types, benchmark comparison | Evaluating |
    | O-002 | Offer simulation-as-a-service to partner OEMs | Business | 2 | 5 | 10 | [Name] | Market analysis, management proposal | Proposed |
    | O-003 | Adopt open-source frameworks to reduce maintenance | Technical | 3 | 3 | 9 | [Name] | Evaluate OpenAD Kit, ROS2 tooling | Evaluating |
    | O-004 | *[Add your opportunities]* | | | | | | | |

    ---

    ## 4. Review Log

    | Date | Reviewer | Risks Added/Changed | Outcome |
    |------|----------|-------------------|---------|
    | YYYY-MM-DD | [Name] | Initial creation | Baseline established |
    | | | | |

    ---

    *ISO 9001:2015 Reference: Clause 6.1*
