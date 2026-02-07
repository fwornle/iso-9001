# REF-02: Stakeholder Register

=== ":material-lightning-bolt: Quick (~1h)"

    **ISO 9001 Clause 4.2** | **Owner:** PO / QMR

    ## Key Stakeholders

    | Stakeholder | Needs | How We Address |
    |-------------|-------|----------------|
    | **AD/ADAS SW Engineers** | Reliable, fast, well-documented tools | SLAs, documentation, support channels, sprint reviews |
    | **AD Function Owners** | Tools enabling compliant validation | Tool qualification evidence |
    | **Unit Management** | Efficient delivery, strategic alignment | OKRs, management reviews, KPI dashboards |
    | **InfoSec Team** | Compliance with security policies | Security assessments, vulnerability mgmt |
    | **Data Protection Officer** | GDPR compliance | DPIAs, anonymization |

    > Key principle: We maintain a stakeholder register and gather requirements through regular syncs, SLAs, compliance requirements, and our internal tooling portal.

=== ":material-book-open-variant: Essential (~3h)"

    **ISO 9001 Clause 4.2** | **Owner:** PO / QMR

    ## Stakeholder Register

    | # | Stakeholder | Needs & Expectations | How We Address | Priority |
    |---|-------------|---------------------|----------------|:--------:|
    | 1 | AD/ADAS SW Engineers | Reliable, fast tools; responsive support | SLAs, user docs, feedback sessions | High |
    | 2 | AD Function Owners | Compliant validation tools (ISO 26262) | Tool qualification evidence | High |
    | 3 | Unit Management | Quality delivery, strategic alignment | OKRs, KPI dashboards | High |
    | 4 | Corporate Management | AD program success, cost efficiency | Strategic roadmap alignment | High |
    | 5 | InfoSec Team | Security policy compliance | Security assessments, vuln mgmt | High |
    | 6 | Data Protection Officer | GDPR compliance | DPIAs, anonymization | High |
    | 7 | Works Council | Fair conditions, transparency | Compliance with agreements | Medium |
    | 8 | Cloud Providers (AWS/Azure) | Predictable consumption | Procurement, service reviews | Medium |
    | 9 | Third-Party Tool Vendors | Clear requirements | Evaluation process, SLAs | Medium |
    | 10 | New Team Members | Clear onboarding | Structured 30-60-90 day plan | Medium |

    ```mermaid
    quadrantChart
        title Stakeholder Influence vs Interest
        x-axis Low Interest --> High Interest
        y-axis Low Influence --> High Influence
        quadrant-1 Manage Closely
        quadrant-2 Keep Satisfied
        quadrant-3 Monitor
        quadrant-4 Keep Informed
        AD SW Engineers: [0.9, 0.6]
        AD Function Owners: [0.7, 0.8]
        Unit Management: [0.8, 0.9]
        Corporate Mgmt: [0.5, 0.95]
        InfoSec Team: [0.6, 0.7]
        Cloud Providers: [0.4, 0.3]
    ```

=== ":material-book-open-page-variant: Full"

    ## DDD Unit — Data Driven Development | AD/ADAS Tooling

    **Document Owner:** Product Owner / QMR
    **Last Review:** YYYY-MM-DD
    **Next Review:** YYYY-MM-DD

    ---

    ## 1. Purpose

    Identifies all relevant interested parties, their needs and expectations, and how we address them, as required by ISO 9001:2015 Clause 4.2.

    ---

    ## 2. Stakeholder Register

    | # | Stakeholder | Category | Needs & Expectations | How We Address Them | Monitoring Method | Priority |
    |---|-------------|----------|---------------------|---------------------|-------------------|----------|
    | 1 | **AD/ADAS SW Engineers** | Primary Customer | Reliable, fast, well-documented tools; low-friction onboarding; responsive support | SLAs, user documentation, support channels, regular feedback sessions | NPS surveys, support tickets, sprint reviews | High |
    | 2 | **AD Function Owners** | Internal Customer | Tools that enable compliant validation (ISO 26262, ASPICE) | Tool qualification evidence, compliance documentation | Quarterly alignment meetings | High |
    | 3 | **Unit Management** | Management | Efficient resource use, strategic alignment, quality delivery | OKRs, management reviews, KPI dashboards | Monthly reporting, management review | High |
    | 4 | **Corporate Management** | Top Management | Contribution to AD program success, cost efficiency | Strategic roadmap alignment, budget reporting | Quarterly business review | High |
    | 5 | **Information Security Team** | Internal Regulator | Compliance with InfoSec policies, secure data handling | Security assessments, vulnerability management | Audit results, security metrics | High |
    | 6 | **Data Protection Officer** | Internal Regulator | GDPR compliance, lawful data processing | Data protection impact assessments, anonymization | DPO reviews, compliance checks | High |
    | 7 | **Works Council** | Employee Rep | Fair working conditions, transparent processes | Compliance with agreements, open communication | Regular consultation | Medium |
    | 8 | **Cloud Providers (AWS/Azure)** | Supplier | Predictable consumption, timely payment, feedback | Procurement processes, service reviews | SLA monitoring, cost tracking | Medium |
    | 9 | **Third-Party Tool Vendors** | Supplier | Clear requirements, fair evaluation | Vendor evaluation process, contractual SLAs | Performance reviews | Medium |
    | 10 | **Regulatory Bodies** | External | Compliance with applicable regulations | Regulatory monitoring, compliance processes | Legal team coordination | Medium |
    | 11 | **Open-Source Communities** | External | Responsible usage, contribution back | License compliance, upstream contributions | License scanning | Low |
    | 12 | **New Team Members** | Internal | Clear onboarding, learning opportunities | Structured onboarding, mentoring, documentation | 30-60-90 day feedback | Medium |

    ---

    ## 3. Stakeholder Influence/Interest Matrix

    ```mermaid
    quadrantChart
        title Stakeholder Influence vs Interest
        x-axis Low Interest --> High Interest
        y-axis Low Influence --> High Influence
        quadrant-1 Manage Closely
        quadrant-2 Keep Satisfied
        quadrant-3 Monitor
        quadrant-4 Keep Informed
        AD SW Engineers: [0.9, 0.6]
        AD Function Owners: [0.7, 0.8]
        Unit Management: [0.8, 0.9]
        Corporate Mgmt: [0.5, 0.95]
        InfoSec Team: [0.6, 0.7]
        Cloud Providers: [0.4, 0.3]
        Works Council: [0.3, 0.5]
    ```

    ---

    ## 4. Review Log

    | Date | Reviewer | Changes Made |
    |------|----------|-------------|
    | YYYY-MM-DD | [Name] | Initial creation |
    | | | |

    ---

    *ISO 9001:2015 Reference: Clause 4.2*
