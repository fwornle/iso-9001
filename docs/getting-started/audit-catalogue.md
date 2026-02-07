# ISO 9001:2015 Audit Preparation Catalogue

=== ":material-lightning-bolt: Quick (~1h)"

    > **Scope:** DDD unit — tooling for AD/ADAS data engineering, storage, simulation, and reprocessing.

    ## ISO 9001 at a Glance (PDCA)

    ```mermaid
    graph LR
        subgraph "Plan"
            C4["4 - Context"]
            C5["5 - Leadership"]
            C6["6 - Planning"]
        end
        subgraph "Do"
            C7["7 - Support"]
            C8["8 - Operation"]
        end
        subgraph "Check"
            C9["9 - Performance"]
        end
        subgraph "Act"
            C10["10 - Improvement"]
        end
        C4 --> C5 --> C6 --> C7 --> C8 --> C9 --> C10
        C10 -->|Continual Improvement| C4
        style C4 fill:#4A90D9,color:#fff
        style C5 fill:#4A90D9,color:#fff
        style C6 fill:#4A90D9,color:#fff
        style C7 fill:#7B68EE,color:#fff
        style C8 fill:#7B68EE,color:#fff
        style C9 fill:#E8A838,color:#fff
        style C10 fill:#D94A4A,color:#fff
    ```

    ---

    ## Top Questions Per Clause

    | # | Likely Auditor Question | Key Points for Your Answer |
    |---|-------------------------|---------------------------|
    | **4.1** | What does your unit do? | DDD unit: data engineering, simulation, reprocessing tools for AD/ADAS engineers |
    | **4.3** | What is the scope of your QMS? | Design, development, deployment & maintenance of data/simulation tooling. Physical product clauses excluded. |
    | **5.1** | How does management demonstrate commitment? | Quarterly management reviews, quality policy sign-off, budget allocation for quality |
    | **5.2** | Can you show me your quality policy? | Have it printed! Reliable, scalable, secure tooling; continual improvement; data-driven decisions |
    | **6.1** | How do you identify and manage risks? | Risk register reviewed quarterly, 5x5 matrix, each risk has owner & mitigation. Give 2-3 examples |
    | **6.2** | What are your quality objectives? | Availability >= 99.5%, MTTR < 4h, NPS >= 40, zero data integrity incidents, 100% release pass rate |
    | **7.2** | How do you ensure competence? | Competency matrix per role, structured onboarding (30-60-90), training plans, annual reviews |
    | **7.5** | How do you control documents? | Confluence with version control & approvals; Git with branch protection; retention policy |
    | **8.3** | How do you control design & development? | SDLC: Requirements -> ADRs -> Implementation -> Code review (2 approvers) -> Testing -> Staging -> Prod |
    | **9.1** | What do you monitor and measure? | Uptime, MTTR, error rates, deploy frequency, NPS, test coverage — Grafana dashboards |
    | **9.2** | Do you conduct internal audits? | Yes, annual program, trained independent auditors, results feed into management review |
    | **9.3** | How often is management review? | Quarterly + annual comprehensive. Covers KPIs, audits, CAPAs, risks, resources |
    | **10.2** | How do you handle nonconformities? | Contain -> root cause (5-Why) -> corrective action -> verify effectiveness (30/60/90 days) -> lessons learned |

    ---

    ## Auditor Tips

    1. **Be honest.** Never fabricate evidence
    2. **Show, don't tell.** Have Jira, Confluence, Grafana, Git open
    3. **Stay in scope.** Answer what's asked — don't volunteer problems
    4. **STAR method:** Situation -> Task -> Action -> Result
    5. **One spokesperson per topic.** Agree beforehand who answers what

=== ":material-book-open-variant: Essential (~3h)"

    > **Scope:** DDD unit — tooling for AD/ADAS data engineering, storage, simulation, and reprocessing.

    ```mermaid
    graph LR
        subgraph "Plan"
            C4["4 - Context"]
            C5["5 - Leadership"]
            C6["6 - Planning"]
        end
        subgraph "Do"
            C7["7 - Support"]
            C8["8 - Operation"]
        end
        subgraph "Check"
            C9["9 - Performance"]
        end
        subgraph "Act"
            C10["10 - Improvement"]
        end
        C4 --> C5 --> C6 --> C7 --> C8 --> C9 --> C10
        C10 -->|Continual Improvement| C4
        style C4 fill:#4A90D9,color:#fff
        style C5 fill:#4A90D9,color:#fff
        style C6 fill:#4A90D9,color:#fff
        style C7 fill:#7B68EE,color:#fff
        style C8 fill:#7B68EE,color:#fff
        style C9 fill:#E8A838,color:#fff
        style C10 fill:#D94A4A,color:#fff
    ```

    ---

    ## Clause 4: Context of the Organization

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 4.1.1 | **What does your unit do?** | "DDD unit — we develop tooling for data engineering, storage, simulation, and reprocessing for AD/ADAS engineers." |
    | 4.1.2 | **What are the key issues affecting your QMS?** | External: AD regulation, cloud costs, sensor tech changes. Internal: rapid growth, tech debt, knowledge silos. Ref: [Context Analysis](../qms-framework/context-analysis.md) |
    | 4.2.1 | **Who are your interested parties?** | AD/ADAS engineers (primary), management, regulatory bodies, cloud providers, InfoSec, works council. Ref: [Stakeholder Register](../qms-framework/stakeholder-register.md) |
    | 4.3.1 | **What is the scope of your QMS?** | Design, development, deployment & maintenance of data/simulation tools. Physical product clauses excluded with justification. Ref: [QMS Scope](../qms-framework/qms-scope.md) |
    | 4.4.1 | **Can you show me your process map?** | Yes — [QMS Process Map](process-map.md) showing management, core, and support processes |

    ## Clause 5: Leadership

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 5.1.1 | **How does management demonstrate commitment?** | Quarterly management reviews, quality policy sign-off, quality budget allocation, active promotion in all-hands |
    | 5.2.1 | **Can you show me your quality policy?** | Have it printed. Commits to: reliability, compliance, data-driven decisions, continual improvement. Ref: [Quality Policy](../qms-framework/quality-policy.md) |
    | 5.3.1 | **Who is responsible for the QMS?** | QMR [Name] reporting to unit lead. Day-to-day quality owned by team quality champions. Ref: [RACI Matrix](../qms-framework/raci-matrix.md) |

    ## Clause 6: Planning

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 6.1.1 | **How do you identify and manage risks?** | Risk register, quarterly review, 5x5 matrix, each risk has owner + mitigation. Be ready with 2-3 examples. Ref: [Risk Register](../planning/risk-register.md) |
    | 6.2.1 | **What are your quality objectives?** | Availability >= 99.5%, MTTR < 4h, NPS >= 40, zero data integrity incidents, 100% release pass, >= 80% test coverage. Ref: [Quality Objectives](../planning/quality-objectives.md) |
    | 6.2.2 | **How do you measure progress?** | Each objective has KPI, measurement method, frequency, owner. Tracked in Grafana, reviewed monthly + quarterly |

    ## Clause 7: Support

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 7.1.1 | **How do you provide resources?** | Quarterly OKR planning covers staffing, cloud capacity, licenses, training budgets |
    | 7.2.1 | **How do you ensure competence?** | Competency matrix per role, structured onboarding (30-60-90), annual development plans. Ref: [Competency Matrix](../support/competency-matrix.md) |
    | 7.4.1 | **How do you manage QMS communications?** | Communication matrix: what, when, to whom, how. Standups, sprint reviews, all-hands, management reviews. Ref: [Communication Matrix](../support/communication-matrix.md) |
    | 7.5.1 | **How do you control documents?** | Confluence with version control + approvals; Git with branch protection + code review; retention policy |

    ## Clause 8: Operation

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.1.1 | **How do you plan operations?** | Agile/Scrum, 2-week sprints, epics trace to OKRs, Definition of Done, ADRs for major decisions |
    | 8.3.1 | **How do you plan design & development?** | SDLC: Requirements -> Architecture (ADRs) -> Implementation -> Code review (2+ approvers) -> Testing -> Staging -> Production |
    | 8.3.5 | **How do you verify and validate?** | Verification: unit/integration/E2E tests, static analysis, security scanning. Validation: UAT with customers, SLA monitoring |
    | 8.4.1 | **How do you evaluate suppliers?** | Evaluation scorecard (technical, reliability, security, cost), category-based review frequency. Ref: [Supplier Evaluation](../operations/supplier-evaluation.md) |
    | 8.7.1 | **How do you handle nonconforming outputs?** | Bug severity classification (Critical -> Low), immediate incident response + rollback for critical, tracked in Jira, RCA for Critical/High |

    ## Clause 9: Performance Evaluation

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 9.1.1 | **What do you monitor and measure?** | Availability, response times, error rates, deploy frequency, MTTR, test coverage, NPS, SLA compliance |
    | 9.2.1 | **Do you conduct internal audits?** | Annual program, trained independent auditors, findings documented, results in management review. Ref: [Internal Audit Program](../performance/internal-audit-program.md) |
    | 9.3.1 | **How often is management review?** | Quarterly + annual comprehensive. Covers: KPIs, audit results, CAPAs, risks, resources, improvements. Ref: [Management Review](../performance/management-review.md) |

    ## Clause 10: Improvement

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 10.1.1 | **How do you pursue continual improvement?** | Sprint retrospectives, DORA metrics, blameless post-mortems, innovation days |
    | 10.2.1 | **How do you handle nonconformities?** | Contain -> investigate (5-Why/Fishbone) -> corrective action -> verify effectiveness (30/60/90 days) -> update risk register -> lessons learned. Ref: [CAPA Log](../improvement/capa-log.md) |

    ---

    ## Documents to Have Ready

    | Document | Reference | Status |
    |----------|-----------|:------:|
    | Context Analysis | [REF-01](../qms-framework/context-analysis.md) | ☐ |
    | Stakeholder Register | [REF-02](../qms-framework/stakeholder-register.md) | ☐ |
    | QMS Scope | [REF-03](../qms-framework/qms-scope.md) | ☐ |
    | Quality Policy | [REF-04](../qms-framework/quality-policy.md) | ☐ |
    | RACI Matrix | [REF-05](../qms-framework/raci-matrix.md) | ☐ |
    | Risk Register | [REF-06](../planning/risk-register.md) | ☐ |
    | Quality Objectives | [REF-07](../planning/quality-objectives.md) | ☐ |
    | Competency Matrix | [REF-08](../support/competency-matrix.md) | ☐ |
    | Communication Matrix | [REF-09](../support/communication-matrix.md) | ☐ |
    | Supplier Evaluation | [REF-10](../operations/supplier-evaluation.md) | ☐ |
    | Internal Audit Program | [REF-11](../performance/internal-audit-program.md) | ☐ |
    | Management Review | [REF-12](../performance/management-review.md) | ☐ |
    | CAPA Log | [REF-13](../improvement/capa-log.md) | ☐ |
    | Process Map | [QMS Process Map](process-map.md) | ☐ |

    ---

    ## Auditor Tips

    1. **Be honest.** Never fabricate evidence
    2. **Show, don't tell.** Have Jira, Confluence, Grafana, Git open
    3. **Stay in scope.** Answer what's asked — don't volunteer problems
    4. **STAR method:** Situation -> Task -> Action -> Result
    5. **One spokesperson per topic.** Agree beforehand who answers what
    6. **"We are on a journey."** Auditors respect honest improvement over fake perfection

=== ":material-book-open-page-variant: Full"

    ## Data Driven Development (DDD) Unit — Tools for AD/ADAS Validation & Development

    > **Scope:** This catalogue covers all clauses of ISO 9001:2015 relevant to our unit.
    > We develop and maintain tooling for data engineering, storage, simulation, and reprocessing
    > used by software engineers working on Autonomous Driving (AD) and Advanced Driver Assistance Systems (ADAS).

    ---

    ## How to Use This Document

    1. **Before the audit:** Review each clause section, ensure you can speak to each question
    2. **During the audit:** Use the suggested answers as guidance — speak naturally, not scripted
    3. **Reference documents:** Each section links to supporting documents you should have ready
    4. **Key principle:** Auditors want to see that processes exist, are followed, are measured, and are improved

    ---

    ## ISO 9001:2015 Clause Overview

    ```mermaid
    graph LR
        subgraph "Plan"
            C4["4 - Context of the<br/>Organization"]
            C5["5 - Leadership"]
            C6["6 - Planning"]
        end
        subgraph "Do"
            C7["7 - Support"]
            C8["8 - Operation"]
        end
        subgraph "Check"
            C9["9 - Performance<br/>Evaluation"]
        end
        subgraph "Act"
            C10["10 - Improvement"]
        end
        C4 --> C5 --> C6 --> C7 --> C8 --> C9 --> C10
        C10 -->|"Continual<br/>Improvement"| C4
        style C4 fill:#4A90D9,color:#fff
        style C5 fill:#4A90D9,color:#fff
        style C6 fill:#4A90D9,color:#fff
        style C7 fill:#7B68EE,color:#fff
        style C8 fill:#7B68EE,color:#fff
        style C9 fill:#E8A838,color:#fff
        style C10 fill:#D94A4A,color:#fff
    ```

    ---

    ## Table of Contents

    - [Clause 4: Context of the Organization](#clause-4-context-of-the-organization)
    - [Clause 5: Leadership](#clause-5-leadership)
    - [Clause 6: Planning](#clause-6-planning)
    - [Clause 7: Support](#clause-7-support)
    - [Clause 8: Operation](#clause-8-operation)
    - [Clause 9: Performance Evaluation](#clause-9-performance-evaluation)
    - [Clause 10: Improvement](#clause-10-improvement)
    - [Cross-Cutting Topics](#cross-cutting-topics)

    ---

    ## Clause 4: Context of the Organization

    ### 4.1 Understanding the Organization and Its Context

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 4.1.1 | **What does your unit do? Describe your scope.** | "We are the Data Driven Development (DDD) unit. We develop and maintain tooling for data engineering, storage, simulation, and reprocessing. Our customers are SW engineers working on Autonomous Driving and ADAS functions. We provide the infrastructure and tools that enable them to validate and develop perception, planning, and control algorithms using real-world and simulated driving data." |
    | 4.1.2 | **What are the key external and internal issues that affect your ability to achieve the intended outcomes of the QMS?** | **External:** Regulatory landscape for AD (UN R157, EU AI Act), semiconductor supply constraints, evolving sensor technology, OEM platform changes, cybersecurity requirements (ISO 21434). **Internal:** Rapid growth, cloud cost management, cross-team dependencies, talent retention in a competitive AD market, technical debt in legacy tooling. *Reference:* [Context Analysis (SWOT)](../qms-framework/context-analysis.md) |
    | 4.1.3 | **How do you monitor and review these issues?** | "We conduct quarterly context reviews as part of our management review cycle. External issues are tracked via our regulatory watch list and industry event participation. Internal issues surface through retrospectives, team health checks, and OKR reviews." |

    ### 4.2 Understanding the Needs and Expectations of Interested Parties

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 4.2.1 | **Who are your interested parties?** | AD/ADAS SW engineers (primary customers), management (budget & strategy), regulatory bodies, data providers (fleet data owners), cloud infrastructure providers (AWS/Azure), partner OEM teams, works council, information security team. |
    | 4.2.2 | **How do you determine their requirements?** | "We maintain a stakeholder register. Requirements are captured through: regular syncs with AD teams (sprint reviews), SLAs with platform consumers, compliance requirements from InfoSec and legal, and feedback via our internal tooling portal." *Reference:* [Stakeholder Register](../qms-framework/stakeholder-register.md) |

    ### 4.3 Scope of the QMS

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 4.3.1 | **What is the scope of your QMS?** | "Design, development, deployment, and maintenance of data engineering tools, simulation environments, data storage solutions, and reprocessing pipelines for Autonomous Driving and ADAS software validation. This includes CI/CD toolchains, data cataloguing, simulation-as-a-service, and large-scale data replay infrastructure." |
    | 4.3.2 | **Are any clauses excluded?** | "We do not manufacture physical products, so aspects of Clause 8 related to production, delivery of physical goods, and post-delivery activities for hardware do not apply. We have documented this exclusion with justification." *Reference:* [QMS Scope Statement](../qms-framework/qms-scope.md) |

    ### 4.4 QMS and Its Processes

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 4.4.1 | **Can you show me your process landscape / process map?** | "Yes — here is our process map showing our core, management, and support processes." *Reference:* [QMS Process Map](process-map.md) |
    | 4.4.2 | **How do you determine inputs, outputs, sequence, and interaction of processes?** | "Each process has a documented process description with defined inputs, outputs, responsible roles, KPIs, and interfaces. These are maintained in our Confluence space and reviewed annually." |

    ```mermaid
    graph TB
        subgraph "Management Processes"
            MP1["Strategic Planning<br/>& OKRs"]
            MP2["Management Review"]
            MP3["Risk Management"]
        end
        subgraph "Core Processes"
            CP1["Requirements<br/>Engineering"]
            CP2["Tool Design &<br/>Architecture"]
            CP3["Development<br/>(Agile/Scrum)"]
            CP4["Testing &<br/>Validation"]
            CP5["Deployment &<br/>Release"]
            CP6["Operations &<br/>Monitoring"]
        end
        subgraph "Support Processes"
            SP1["HR & Competence<br/>Management"]
            SP2["Infrastructure &<br/>Cloud Mgmt"]
            SP3["Document &<br/>Config Control"]
            SP4["Supplier / Vendor<br/>Management"]
        end
        MP1 --> CP1
        CP1 --> CP2 --> CP3 --> CP4 --> CP5 --> CP6
        CP6 -->|"Feedback"| CP1
        MP2 --> MP1
        MP3 --> CP1
        SP1 --> CP3
        SP2 --> CP5
        SP3 --> CP3
        SP4 --> SP2
        style MP1 fill:#4A90D9,color:#fff
        style MP2 fill:#4A90D9,color:#fff
        style MP3 fill:#4A90D9,color:#fff
        style CP1 fill:#50C878,color:#fff
        style CP2 fill:#50C878,color:#fff
        style CP3 fill:#50C878,color:#fff
        style CP4 fill:#50C878,color:#fff
        style CP5 fill:#50C878,color:#fff
        style CP6 fill:#50C878,color:#fff
        style SP1 fill:#E8A838,color:#fff
        style SP2 fill:#E8A838,color:#fff
        style SP3 fill:#E8A838,color:#fff
        style SP4 fill:#E8A838,color:#fff
    ```

    ---

    ## Clause 5: Leadership

    ### 5.1 Leadership and Commitment

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 5.1.1 | **How does top management demonstrate commitment to the QMS?** | "Our unit lead participates in quarterly management reviews, signs off on the quality policy, allocates budget for quality initiatives (tooling, training, audits), and actively promotes quality objectives in all-hands meetings and OKR planning." |
    | 5.1.2 | **How does leadership ensure a customer focus?** | "We conduct quarterly NPS surveys with our AD/ADAS engineering teams, track tool adoption metrics, maintain a public roadmap shaped by user feedback, and our unit lead personally attends key customer escalation meetings." |
    | 5.1.3 | **How are quality responsibilities communicated?** | "Quality roles are defined in our RACI matrix. Every team has a designated quality champion. The QMS responsibilities are part of onboarding and are documented in our team wiki." |

    ### 5.2 Quality Policy

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 5.2.1 | **Can you show me your quality policy?** | *Have this printed and posted.* "Our quality policy commits us to delivering reliable, scalable, and secure tooling that enables our AD/ADAS engineers to validate autonomous driving functions with confidence. We commit to continual improvement, compliance with applicable requirements, and data-driven decision-making." *Reference:* [Quality Policy](../qms-framework/quality-policy.md) |
    | 5.2.2 | **How is the quality policy communicated?** | "It's posted on our Confluence landing page, included in onboarding materials, referenced in sprint retrospectives, and displayed in our team area. All team members have acknowledged it." |

    ### 5.3 Roles, Responsibilities, and Authorities

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 5.3.1 | **Who is responsible for the QMS?** | "Our Quality Management Representative is [Name], who reports directly to the unit lead. Day-to-day quality is owned by each team's quality champion. The QMR coordinates audits, manages the document system, and reports on QMS performance." |
    | 5.3.2 | **How are roles and responsibilities defined?** | "Through our RACI matrix, job descriptions, and team charters. These are documented in Confluence and reviewed during management reviews." *Reference:* [RACI Matrix](../qms-framework/raci-matrix.md) |

    ---

    ## Clause 6: Planning

    ### 6.1 Actions to Address Risks and Opportunities

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 6.1.1 | **How do you identify and manage risks?** | "We maintain a risk register that is reviewed quarterly. Risks are categorized by likelihood and impact using a 5×5 matrix. Each risk has an owner, mitigation actions, and a target date. We use FMEA for critical tool components." *Reference:* [Risk Register](../planning/risk-register.md) |
    | 6.1.2 | **Can you give me an example of a risk you identified and how you addressed it?** | *Be prepared with 2-3 concrete examples, e.g.:* "We identified that a single-point-of-failure in our data ingestion pipeline could halt reprocessing for all AD teams. We implemented redundant ingestion paths and automated failover, reducing potential downtime from hours to minutes." |
    | 6.1.3 | **How do you identify opportunities?** | "Through retrospectives, customer feedback sessions, technology radar reviews, and benchmarking against industry best practices. Opportunities are captured in our backlog and prioritized in OKR planning." |

    ```mermaid
    graph LR
        subgraph "Risk Management Process"
            A["Identify Risks<br/>(Context Analysis,<br/>Retrospectives,<br/>Incident Reviews)"] --> B["Assess<br/>(Likelihood × Impact<br/>5×5 Matrix)"]
            B --> C["Plan Mitigation<br/>(Assign Owner,<br/>Define Actions)"]
            C --> D["Implement<br/>Controls"]
            D --> E["Monitor &<br/>Review<br/>(Quarterly)"]
            E -->|"New risks or<br/>changed context"| A
        end
        style A fill:#D94A4A,color:#fff
        style B fill:#E8A838,color:#fff
        style C fill:#4A90D9,color:#fff
        style D fill:#50C878,color:#fff
        style E fill:#7B68EE,color:#fff
    ```

    ### 6.2 Quality Objectives

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 6.2.1 | **What are your quality objectives?** | "Our quality objectives are aligned with our OKRs and include: (1) Tool availability ≥ 99.5%, (2) Mean time to resolve critical bugs < 4h, (3) Customer satisfaction (NPS) ≥ 40, (4) Zero data integrity incidents in reprocessing pipelines, (5) 100% of releases pass automated regression suite." |
    | 6.2.2 | **How do you measure progress toward these objectives?** | "Each objective has a defined KPI, measurement method, frequency, and owner. We track them on our Grafana dashboards and review them monthly in team leads meeting and quarterly in management review." |
    | 6.2.3 | **Are quality objectives consistent with the quality policy?** | "Yes — our policy commits to reliability, security, and data-driven improvement. Each objective directly maps to one of these commitments. We maintain a traceability matrix." *Reference:* [Quality Objectives](../planning/quality-objectives.md) |

    ### 6.3 Planning of Changes

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 6.3.1 | **How do you plan changes to the QMS?** | "Changes to the QMS are managed through our change management process. Proposed changes are documented, impact-assessed, approved by the QMR and unit lead, communicated to affected parties, and tracked to completion. We use RFC (Request for Change) tickets in Jira." |

    ---

    ## Clause 7: Support

    ### 7.1 Resources

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 7.1.1 | **How do you determine and provide the resources needed?** | "Resource planning happens during quarterly OKR planning. We assess staffing needs, cloud infrastructure capacity, tooling licenses, and training budgets. Resource gaps are escalated through management review." |
    | 7.1.2 | **How do you manage your infrastructure (development environments, cloud resources)?** | "We use Infrastructure-as-Code (Terraform/SST) for all cloud resources. Environments are version-controlled. We have separate dev, staging, and production environments with defined promotion criteria." |
    | 7.1.3 | **How do you ensure the monitoring and measuring resources are adequate?** | "Our test infrastructure is calibrated through regular validation. CI/CD pipelines include automated checks. Performance benchmarks are baselined and tracked. SLA monitoring uses industry-standard observability stacks (Prometheus, Grafana, PagerDuty)." |

    ### 7.2 Competence

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 7.2.1 | **How do you determine required competencies?** | "Each role has a competency profile defining required technical skills (e.g., Python, cloud architecture, data engineering), domain knowledge (AD/ADAS), and soft skills. These are documented in our competency matrix." *Reference:* [Competency Matrix](../support/competency-matrix.md) |
    | 7.2.2 | **How do you ensure people are competent?** | "Through structured onboarding (30-60-90 day plan), regular 1:1s with skill assessments, annual development plans, internal tech talks, conference attendance, and mandatory training for critical processes." |
    | 7.2.3 | **How do you maintain records of competence?** | "Training records are maintained in our HR system (SuccessFactors). Technical certifications are tracked in our team wiki. Onboarding completion is signed off by team leads." |

    ### 7.3 Awareness

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 7.3.1 | **How do you ensure people are aware of the quality policy and their contribution to QMS effectiveness?** | "Through onboarding, quarterly all-hands where quality metrics are presented, sprint retrospectives, and the quality policy being visible on our Confluence landing page. Team members understand that the quality of our tools directly impacts the safety validation of autonomous vehicles." |

    ### 7.4 Communication

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 7.4.1 | **How do you determine internal and external communications related to the QMS?** | "We have a defined communication matrix covering what is communicated, when, to whom, and how. Internal: daily standups, sprint reviews, retrospectives, management reviews. External: release notes, SLA reports, incident notifications to consuming teams." *Reference:* [Communication Matrix](../support/communication-matrix.md) |

    ### 7.5 Documented Information

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 7.5.1 | **How do you control documented information required by the QMS?** | "All QMS documents are maintained in Confluence with version control, approval workflows, and access controls. Code and configuration are in Git (GitHub/GitLab) with branch protection and code review requirements. We distinguish between controlled documents (policies, procedures) and records (evidence of activities)." |
    | 7.5.2 | **How do you ensure documents are current and available?** | "Confluence spaces have designated owners who review content quarterly. Outdated pages are flagged by an automated staleness check. Git repositories use branch protection to prevent unauthorized changes. We have a document retention policy." |
    | 7.5.3 | **How do you protect documented information?** | "Access is controlled through AD group policies. Sensitive data is classified and handled per our information classification scheme. Backups are automated. We comply with organizational information security policies." |

    ```mermaid
    graph TD
        subgraph "Document Control Process"
            A["Create / Update<br/>Document"] --> B{"Review &<br/>Approve"}
            B -->|Approved| C["Publish to<br/>Confluence / Git"]
            B -->|Rejected| A
            C --> D["Notify Affected<br/>Parties"]
            D --> E["Document in Use"]
            E --> F{"Periodic<br/>Review Due?"}
            F -->|Yes| A
            F -->|No| E
            E --> G{"Obsolete?"}
            G -->|Yes| H["Archive with<br/>Retention Label"]
            G -->|No| E
        end
        style A fill:#4A90D9,color:#fff
        style B fill:#E8A838,color:#fff
        style C fill:#50C878,color:#fff
        style D fill:#7B68EE,color:#fff
        style H fill:#888,color:#fff
    ```

    ---

    ## Clause 8: Operation

    ### 8.1 Operational Planning and Control

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.1.1 | **How do you plan and control your operational processes?** | "We use Agile/Scrum with 2-week sprints. Epics trace to OKRs. Each sprint has defined goals, acceptance criteria, and a definition of done. We maintain architecture decision records (ADRs) for significant technical decisions. Release trains are planned quarterly." |
    | 8.1.2 | **How do you manage outsourced processes?** | "We manage cloud service providers (AWS/Azure) through SLAs and regular service reviews. Third-party tool vendors are evaluated per our supplier management process. Open-source components are tracked and assessed for vulnerabilities." |

    ### 8.2 Requirements for Products and Services

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.2.1 | **How do you determine customer requirements for your tools?** | "Requirements are gathered through: (1) direct engagement with AD/ADAS teams in refinement sessions, (2) feature requests through our internal portal / Jira, (3) SLA negotiations for platform services, (4) regulatory/compliance requirements flowing from ASPICE/ISO 26262 context, (5) technical constraints from the AD platform architecture." |
    | 8.2.2 | **How do you review requirements before committing to deliver?** | "Every feature goes through a refinement process where we verify completeness, feasibility, and testability. Acceptance criteria are defined before work begins. Large features require an architecture review. We confirm we can meet SLAs before onboarding new platform consumers." |
    | 8.2.3 | **How do you handle changes to requirements?** | "Changes are managed through our Jira workflow. Scope changes during a sprint are flagged by the Scrum Master. Significant changes require re-refinement and impact assessment. All changes are tracked and traceable." |

    ### 8.3 Design and Development

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.3.1 | **How do you plan design and development activities?** | "Design and development follows our SDLC process: Requirements → Architecture Design (ADRs) → Implementation (feature branches) → Code Review → Testing → Staging → Production. Each stage has defined entry/exit criteria." |
    | 8.3.2 | **What are the inputs to your design process?** | "Functional requirements (user stories), non-functional requirements (performance, scalability, security), interface specifications, applicable standards (ISO 26262 tooling requirements, ASPICE), lessons learned from previous releases, and technical constraints." |
    | 8.3.3 | **How do you control design and development?** | "Through code reviews (minimum 2 approvers), automated CI/CD pipelines (lint, test, security scan), architecture reviews for significant changes, and sprint demos for stakeholder validation." |
    | 8.3.4 | **What are the outputs of your design process?** | "Deployed tools/services meeting defined acceptance criteria, API documentation, user guides, architecture documentation, test reports, and release notes." |
    | 8.3.5 | **How do you verify and validate your designs?** | "Verification: automated unit tests, integration tests, E2E tests, static analysis, security scanning. Validation: user acceptance testing with AD/ADAS engineers, beta deployments, A/B testing for UX changes, and SLA compliance monitoring post-release." |
    | 8.3.6 | **How do you manage design changes?** | "All changes go through Git pull requests with mandatory reviews. Breaking changes follow our deprecation policy (minimum 2 sprint notice). Database schema changes require migration scripts and rollback plans." |

    ```mermaid
    graph LR
        subgraph "Software Development Lifecycle"
            A["Requirements<br/>(User Stories,<br/>Acceptance Criteria)"] --> B["Architecture<br/>& Design<br/>(ADRs)"]
            B --> C["Implementation<br/>(Feature Branch,<br/>Pair Programming)"]
            C --> D["Code Review<br/>(≥2 Approvers,<br/>Static Analysis)"]
            D --> E["Automated Testing<br/>(Unit, Integration,<br/>E2E, Security)"]
            E --> F["Staging<br/>Deployment<br/>(Smoke Tests)"]
            F --> G["Production<br/>Release<br/>(Canary/Blue-Green)"]
            G --> H["Monitoring &<br/>Observability<br/>(SLA Tracking)"]
        end
        H -->|"Feedback &<br/>Incidents"| A
        style A fill:#4A90D9,color:#fff
        style B fill:#4A90D9,color:#fff
        style C fill:#50C878,color:#fff
        style D fill:#50C878,color:#fff
        style E fill:#7B68EE,color:#fff
        style F fill:#E8A838,color:#fff
        style G fill:#D94A4A,color:#fff
        style H fill:#888,color:#fff
    ```

    ### 8.4 Control of Externally Provided Processes, Products, and Services

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.4.1 | **How do you evaluate and select external providers?** | "Cloud providers are selected per corporate procurement. For additional tools/libraries, we evaluate based on: security posture, license compatibility, community health, performance benchmarks, and corporate InfoSec approval. We maintain an approved vendor/tool list." |
    | 8.4.2 | **How do you ensure externally provided products/services meet requirements?** | "SLAs define performance expectations. We monitor cloud service health dashboards. Open-source dependencies are scanned for vulnerabilities (Snyk/Dependabot). Vendor performance is reviewed quarterly." *Reference:* [Supplier Evaluation](../operations/supplier-evaluation.md) |

    ### 8.5 Production and Service Provision

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.5.1 | **How do you control production/service provision?** | "Our tools are deployed via automated CI/CD pipelines with: Infrastructure-as-Code, immutable deployments, automated rollback capabilities, feature flags for controlled rollouts, and 24/7 monitoring with alerting." |
    | 8.5.2 | **How do you ensure traceability?** | "Every deployment is traceable to: Git commit → PR → Jira ticket → requirement. We maintain audit logs for all data pipeline operations. Data lineage is tracked for reprocessing workflows." |
    | 8.5.3 | **How do you handle customer property (data)?** | "Driving data from fleet vehicles is treated as sensitive asset. We follow organizational data classification. Access is role-based (RBAC). Data retention follows legal requirements. We do not modify source data — reprocessing creates new derived datasets with full lineage." |
    | 8.5.4 | **How do you preserve outputs?** | "Artifacts are stored in versioned registries (Docker images, Python packages). Data is stored in redundant, backed-up storage (S3 with versioning). Configuration is version-controlled in Git." |

    ### 8.7 Control of Nonconforming Outputs

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 8.7.1 | **How do you handle nonconforming outputs?** | "Bugs are categorized by severity (Critical/High/Medium/Low). Critical bugs trigger an immediate incident response with rollback. All nonconformities are tracked in Jira. Root cause analysis is performed for Critical/High issues. Fixes require the same review/test process as new features." |
    | 8.7.2 | **Can you show me an example of how you handled a nonconformity?** | *Be prepared with 2-3 examples of bugs/incidents, what happened, how you contained it, root cause, and corrective action taken.* |

    ---

    ## Clause 9: Performance Evaluation

    ### 9.1 Monitoring, Measurement, Analysis, and Evaluation

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 9.1.1 | **What do you monitor and measure?** | "Tool availability (uptime), response times, error rates, deployment frequency, lead time for changes, mean time to recovery (MTTR), test coverage, customer satisfaction (NPS), SLA compliance, and defect rates." |
    | 9.1.2 | **How do you evaluate QMS performance?** | "Through KPI dashboards (Grafana), monthly metrics reviews, quarterly management reviews, and annual internal audits. We use statistical analysis on trends, not just point-in-time values." |
    | 9.1.3 | **How do you measure customer satisfaction?** | "Quarterly NPS surveys to AD/ADAS teams, feature request tracking (volume and completion rate), support ticket analysis (response time, resolution time), and direct feedback in sprint reviews and user forums." |

    ```mermaid
    graph TB
        subgraph "Performance Measurement Framework"
            direction TB
            KPI["KPIs & Quality Objectives"]
            KPI --> M1["Tool Availability<br/>Target: ≥ 99.5%"]
            KPI --> M2["MTTR Critical Bugs<br/>Target: < 4 hours"]
            KPI --> M3["Customer NPS<br/>Target: ≥ 40"]
            KPI --> M4["Deployment Frequency<br/>Target: Daily"]
            KPI --> M5["Test Coverage<br/>Target: ≥ 80%"]
            KPI --> M6["Data Integrity<br/>Target: Zero incidents"]
        end
        subgraph "Review Cadence"
            R1["Daily: Dashboards & Alerts"]
            R2["Sprint: Retrospective Metrics"]
            R3["Monthly: Team Leads Review"]
            R4["Quarterly: Management Review"]
            R5["Annual: Internal Audit"]
        end
        M1 & M2 & M3 & M4 & M5 & M6 --> R1
        R1 --> R2 --> R3 --> R4 --> R5
        style KPI fill:#4A90D9,color:#fff
        style M1 fill:#50C878,color:#fff
        style M2 fill:#50C878,color:#fff
        style M3 fill:#50C878,color:#fff
        style M4 fill:#50C878,color:#fff
        style M5 fill:#50C878,color:#fff
        style M6 fill:#50C878,color:#fff
    ```

    ### 9.2 Internal Audit

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 9.2.1 | **Do you conduct internal audits?** | "Yes. We have an annual internal audit program. Audits are conducted by trained internal auditors who are independent of the area being audited. Results are documented and reported in management review." *Reference:* [Internal Audit Program](../performance/internal-audit-program.md) |
    | 9.2.2 | **How do you select auditors and ensure objectivity?** | "Auditors are trained in ISO 9001 auditing. They do not audit their own work. We rotate auditors and may use auditors from other organizational units to ensure independence." |
    | 9.2.3 | **Can you show me internal audit records?** | *Have recent internal audit reports, findings, and corrective action records ready.* |

    ### 9.3 Management Review

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 9.3.1 | **How often do you conduct management reviews?** | "Quarterly, with a comprehensive annual review. Ad-hoc reviews are triggered by significant events (major incidents, organizational changes)." |
    | 9.3.2 | **What topics are covered in management review?** | "Status of actions from previous reviews, changes in context/interested parties, QMS performance (KPIs), audit results, customer feedback, nonconformities and corrective actions, risk register updates, resource adequacy, and improvement opportunities." |
    | 9.3.3 | **What are the outputs of management reviews?** | "Decisions on improvement actions, resource allocation changes, QMS scope adjustments, updated quality objectives, and action items with owners and deadlines. All are documented in meeting minutes." *Reference:* [Management Review Template](../performance/management-review.md) |

    ---

    ## Clause 10: Improvement

    ### 10.1 General

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 10.1.1 | **How does your organization pursue continual improvement?** | "Improvement is embedded in our Agile way of working: sprint retrospectives identify improvements bi-weekly. We track improvement actions in Jira. DORA metrics help us measure engineering effectiveness. We conduct blameless post-mortems for incidents. Innovation time (hack days) drives technical improvement." |

    ### 10.2 Nonconformity and Corrective Action

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 10.2.1 | **How do you handle nonconformities?** | "When a nonconformity is identified (audit finding, customer complaint, incident), we: (1) contain the immediate impact, (2) investigate root cause (5-Why, Fishbone), (3) implement corrective action, (4) verify effectiveness, (5) update risk register if needed, (6) share lessons learned." |
    | 10.2.2 | **Can you show me your corrective action records?** | *Have 3-5 recent CAPA records ready showing the full cycle from identification to effectiveness verification.* *Reference:* [CAPA Log](../improvement/capa-log.md) |
    | 10.2.3 | **How do you verify that corrective actions are effective?** | "Each CAPA has a defined effectiveness check — typically a follow-up measurement at 30/60/90 days. The QMR reviews open CAPAs monthly. Recurring issues trigger process changes, not just fixes." |

    ```mermaid
    graph LR
        subgraph "CAPA Process"
            A["Nonconformity<br/>Detected"] --> B["Immediate<br/>Containment"]
            B --> C["Root Cause<br/>Analysis<br/>(5-Why / Fishbone)"]
            C --> D["Define Corrective<br/>Action"]
            D --> E["Implement<br/>Action"]
            E --> F["Verify<br/>Effectiveness<br/>(30/60/90 days)"]
            F -->|Effective| G["Close &<br/>Lessons Learned"]
            F -->|Not Effective| C
        end
        style A fill:#D94A4A,color:#fff
        style B fill:#E8A838,color:#fff
        style C fill:#4A90D9,color:#fff
        style D fill:#4A90D9,color:#fff
        style E fill:#50C878,color:#fff
        style F fill:#7B68EE,color:#fff
        style G fill:#50C878,color:#fff
    ```

    ### 10.3 Continual Improvement

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | 10.3.1 | **Can you show me evidence of continual improvement?** | "Yes — we can demonstrate: (1) Trend data showing improving KPIs over time, (2) Retrospective action items that led to process changes, (3) Reduced incident frequency quarter-over-quarter, (4) Increased deployment frequency and reduced lead time, (5) Improved NPS scores, (6) Lessons learned incorporated into standards." |

    ---

    ## Cross-Cutting Topics

    ### Automotive Context (ASPICE / ISO 26262 Interplay)

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | CC.1 | **How does your QMS relate to automotive standards like ASPICE or ISO 26262?** | "While we are not directly ASPICE-assessed, our tools support ASPICE-compliant development processes. Our simulation and reprocessing tools must meet ISO 26262 Tool Confidence Level (TCL) requirements when used in safety-relevant validation. We document tool qualification evidence per ISO 26262 Part 8, Clause 11." |
    | CC.2 | **How do you ensure your tools don't introduce errors in safety-critical validation?** | "Through rigorous testing (including fault injection), data integrity checks at every pipeline stage, checksums for data at rest and in transit, and tool validation reports that our customers use for their safety cases." |

    ### Information Security & Data Protection

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | CC.3 | **How do you handle information security?** | "We follow corporate InfoSec policies. Access control is role-based. Secrets management uses vault solutions. All data in transit is encrypted (TLS 1.3). Data at rest is encrypted. We conduct regular security assessments and penetration tests." |
    | CC.4 | **How do you handle personal data in driving recordings?** | "Driving data may contain personal data (faces, license plates). We have documented data processing agreements. Anonymization/pseudonymization is applied where required. We comply with GDPR and organizational data protection policies." |

    ### Change Management

    | # | Typical Auditor Question | How to Answer |
    |---|--------------------------|---------------|
    | CC.5 | **How do you manage changes to your tools and infrastructure?** | "All changes follow our change management process: RFC in Jira → Impact assessment → Approval (based on change category) → Implementation with rollback plan → Post-implementation review. Emergency changes have an expedited path with retrospective approval." |

    ```mermaid
    graph TD
        subgraph "Change Management Flow"
            A["Change Request<br/>(RFC in Jira)"] --> B{"Change<br/>Category?"}
            B -->|Standard| C["Pre-Approved<br/>Procedure"]
            B -->|Normal| D["Impact Assessment<br/>& Review Board"]
            B -->|Emergency| E["Expedited<br/>Implementation"]
            C --> F["Implementation<br/>via CI/CD"]
            D --> F
            E --> F
            F --> G["Post-Implementation<br/>Review"]
            G --> H{"Successful?"}
            H -->|Yes| I["Close RFC"]
            H -->|No| J["Rollback &<br/>Investigate"]
            J --> A
            E --> K["Retrospective<br/>Approval"]
        end
        style A fill:#4A90D9,color:#fff
        style B fill:#E8A838,color:#fff
        style C fill:#50C878,color:#fff
        style D fill:#7B68EE,color:#fff
        style E fill:#D94A4A,color:#fff
        style F fill:#50C878,color:#fff
        style I fill:#50C878,color:#fff
        style J fill:#D94A4A,color:#fff
    ```

    ---

    ## Quick Reference: Documents to Have Ready for the Audit

    | Document | Reference | Status |
    |----------|-----------|--------|
    | Context Analysis (SWOT) | [REF-01](../qms-framework/context-analysis.md) | ☐ Ready |
    | Stakeholder Register | [REF-02](../qms-framework/stakeholder-register.md) | ☐ Ready |
    | QMS Scope Statement | [REF-03](../qms-framework/qms-scope.md) | ☐ Ready |
    | Quality Policy | [REF-04](../qms-framework/quality-policy.md) | ☐ Ready |
    | RACI Matrix | [REF-05](../qms-framework/raci-matrix.md) | ☐ Ready |
    | Risk Register | [REF-06](../planning/risk-register.md) | ☐ Ready |
    | Quality Objectives | [REF-07](../planning/quality-objectives.md) | ☐ Ready |
    | Competency Matrix | [REF-08](../support/competency-matrix.md) | ☐ Ready |
    | Communication Matrix | [REF-09](../support/communication-matrix.md) | ☐ Ready |
    | Supplier Evaluation | [REF-10](../operations/supplier-evaluation.md) | ☐ Ready |
    | Internal Audit Program | [REF-11](../performance/internal-audit-program.md) | ☐ Ready |
    | Management Review Template | [REF-12](../performance/management-review.md) | ☐ Ready |
    | CAPA Log | [REF-13](../improvement/capa-log.md) | ☐ Ready |
    | QMS Process Map | [QMS Process Map](process-map.md) | ☐ Ready |
    | Audit Preparation Checklist | [Checklist](preparation-checklist.md) | ☐ Ready |

    ---

    ## Auditor Psychology — Tips for the Day

    1. **Be honest.** If something isn't in place, say so and explain what you're doing about it. Never fabricate evidence.
    2. **Show, don't tell.** Have systems open — Jira, Confluence, Grafana, Git. Show live evidence.
    3. **Stay in scope.** Answer what's asked. Don't volunteer problems or tangents.
    4. **Use the STAR method:** Situation → Task → Action → Result for examples.
    5. **One spokesperson per topic.** Avoid contradicting each other. Agree beforehand who answers what.
    6. **"We are on a journey."** Auditors respect honest improvement trajectories more than fake perfection.

    ---

    *Document Version: 1.0 | Created: 2026-02-06 | Next Review: Before Audit Date*
    *Owner: QMS Representative, DDD Unit*
