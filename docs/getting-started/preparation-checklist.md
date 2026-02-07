# Audit Preparation Checklist

=== ":material-lightning-bolt: Quick (~1h)"

    ## DDD Unit — ISO 9001:2015 Certification Audit

    **Audit Date:** 2026-03-06 | **Coordinator:** QMR — _[Name]_

    ---

    ## Timeline

    ```mermaid
    gantt
        title 4-Week Preparation Sprint
        dateFormat YYYY-MM-DD
        axisFormat %b %d

        section Weeks 1-2
        Documents & evidence         :a1, 2026-02-07, 14d

        section Weeks 2-3
        Team preparation             :b1, 2026-02-14, 14d

        section Week 4
        Pre-audit & final readiness  :c1, 2026-02-28, 5d
        AUDIT DAY                    :milestone, 2026-03-06, 0d
    ```

    ---

    ## Key Documents

    | # | Document | Reference | Ready? |
    |---|----------|-----------|:------:|
    | 1 | Context Analysis (SWOT) | [REF-01](../qms-framework/context-analysis.md) | ☐ |
    | 2 | QMS Scope Statement | [REF-03](../qms-framework/qms-scope.md) | ☐ |
    | 3 | Quality Policy | [REF-04](../qms-framework/quality-policy.md) | ☐ |
    | 4 | RACI Matrix | [REF-05](../qms-framework/raci-matrix.md) | ☐ |
    | 5 | Risk Register | [REF-06](../planning/risk-register.md) | ☐ |
    | 6 | Quality Objectives | [REF-07](../planning/quality-objectives.md) | ☐ |
    | 7 | Internal Audit Program | [REF-11](../performance/internal-audit-program.md) | ☐ |
    | 8 | Management Review | [REF-12](../performance/management-review.md) | ☐ |
    | 9 | CAPA Log | [REF-13](../improvement/capa-log.md) | ☐ |

    ---

    ## Audit Day Roles

    | Role | Person | Focus |
    |------|--------|-------|
    | **Escort / Guide** | _[Name]_ | Logistics, time-keeping |
    | **Clauses 4-5** | _[Unit Lead]_ | Context, leadership, policy |
    | **Clause 6** | _[QMR]_ | Risk, objectives, planning |
    | **Clauses 7-8** | _[Tech Lead / PO]_ | Resources, operations, development |
    | **Clauses 9-10** | _[QMR]_ | Measurement, audit, improvement |
    | **System Demo** | _[DevOps]_ | Jira, Confluence, CI/CD, Grafana |
    | **Note Taker** | _[Name]_ | Records all auditor questions |

    ---

    ## Audit Day — At a Glance

    **Morning:** Welcome auditor &#8594; 10-min unit overview &#8594; confirm schedule &#8594; WiFi access

    **During:** Escort auditor &#8594; note all questions &#8594; answers concise & evidence-based &#8594; systems ready for demo

    **Afternoon:** Attend closing &#8594; listen, don't argue &#8594; thank auditor &#8594; internal debrief &#8594; create CAPAs

=== ":material-book-open-variant: Essential (~3h)"

    ## DDD Unit — ISO 9001:2015 Certification Audit

    **Audit Date:** 2026-03-06
    **Auditing Body:** _[Name]_
    **Lead Auditor:** _[Name]_
    **Internal Coordinator:** QMR — _[Name]_

    ---

    ## Timeline

    ```mermaid
    gantt
        title Audit Preparation Timeline (4 Weeks)
        dateFormat YYYY-MM-DD
        axisFormat %b %d

        section Documentation
        Complete all REF documents          :a1, 2026-02-07, 10d
        Review & approve documents          :a2, after a1, 5d

        section Evidence Gathering
        Collect process evidence             :b1, 2026-02-07, 12d
        Organize evidence folder             :b2, after b1, 5d

        section People Preparation
        Train team on QMS awareness          :c1, 2026-02-10, 7d
        Conduct mock audit interviews        :c2, after c1, 7d

        section Final Preparation
        Internal pre-audit                   :d1, 2026-02-24, 3d
        Address findings & final review      :d2, after d1, 7d
        AUDIT DAY                            :milestone, 2026-03-06, 0d
    ```

    ---

    ## Phase 1: Documentation (Weeks 1-2 · Feb 7-20)

    ### All QMS Documents

    | # | Document | Reference | Owner | Status |
    |---|----------|-----------|-------|:------:|
    | 1 | Context Analysis (SWOT/PESTLE) | [REF-01](../qms-framework/context-analysis.md) | Unit Lead | ☐ |
    | 2 | Stakeholder Register | [REF-02](../qms-framework/stakeholder-register.md) | PO / QMR | ☐ |
    | 3 | QMS Scope Statement | [REF-03](../qms-framework/qms-scope.md) | QMR | ☐ |
    | 4 | Quality Policy | [REF-04](../qms-framework/quality-policy.md) | Unit Lead | ☐ |
    | 5 | RACI Matrix | [REF-05](../qms-framework/raci-matrix.md) | QMR | ☐ |
    | 6 | Risk Register | [REF-06](../planning/risk-register.md) | QMR | ☐ |
    | 7 | Quality Objectives | [REF-07](../planning/quality-objectives.md) | QMR | ☐ |
    | 8 | Competency Matrix | [REF-08](../support/competency-matrix.md) | Team Leads | ☐ |
    | 9 | Communication Matrix | [REF-09](../support/communication-matrix.md) | QMR | ☐ |
    | 10 | Supplier Evaluation | [REF-10](../operations/supplier-evaluation.md) | Tech Lead | ☐ |
    | 11 | Internal Audit Program | [REF-11](../performance/internal-audit-program.md) | QMR | ☐ |
    | 12 | Management Review Template | [REF-12](../performance/management-review.md) | QMR | ☐ |
    | 13 | CAPA Log | [REF-13](../improvement/capa-log.md) | QMR | ☐ |
    | 14 | QMS Process Map | [QMS Process Map](process-map.md) | QMR | ☐ |

    ---

    ## Phase 2: Evidence Collection (Weeks 1-2 · Feb 7-20)

    | ISO Clause | Evidence Required | Source | ☐ |
    |:----------:|-------------------|--------|:-:|
    | **4.1-4.2** | Context review minutes, stakeholder feedback | Confluence | ☐ |
    | **5.1-5.3** | Management commitment, policy displayed, org chart, RACI | Email, Confluence | ☐ |
    | **6.1-6.2** | Risk register reviews, quality objective measurements (4 quarters) | REF-06, Grafana | ☐ |
    | **7.1-7.5** | Training records, resource plans, communication records, document version history | SuccessFactors, Jira, Git | ☐ |
    | **8.1-8.7** | Sprint records, user stories, ADRs, PR history, test results, deployment records | Jira, GitHub, CI/CD | ☐ |
    | **9.1-9.3** | KPI dashboards, internal audit reports, management review minutes | Grafana, REF-11, REF-12 | ☐ |
    | **10.2-10.3** | CAPA records (3-5 complete cycles), retrospective actions | REF-13, Jira | ☐ |

    ---

    ## Phase 3: People Preparation (Weeks 2-3 · Feb 14-27)

    ### Team Training

    | # | Task | Audience | Method |
    |---|------|----------|--------|
    | 1 | ISO 9001 basics & QMS overview | All | Workshop (1h) |
    | 2 | Quality policy — know & explain | All | All-hands + quiz |
    | 3 | Quality objectives — know your KPIs | All | Team meeting |
    | 4 | "What's your role in the QMS?" | All | 1:1 with team lead |
    | 5 | How to handle auditor questions | Spokespersons | Workshop (1h) |

    ### Mock Audit Interviews

    | # | Role | Clause Focus | Interviewer |
    |---|------|:------------:|-------------|
    | 1 | Unit Lead | 5.1, 5.2, 9.3 | QMR |
    | 2 | QMR | 4.3, 7.5, 9.2, 10.2 | External |
    | 3 | Product Owner | 4.2, 8.2 | QMR |
    | 4 | Tech Lead | 8.3, 8.4 | QMR |
    | 5 | Developer | 7.2, 8.3, 8.5 | Team Lead |

    ---

    ## Audit Day Roles

    | Role | Person | Responsibility |
    |------|--------|---------------|
    | **Escort / Guide** | _[Name]_ | Accompanies auditor, logistics, time-keeping |
    | **Clause 4-5 Spokesperson** | _[Unit Lead]_ | Context, leadership, policy |
    | **Clause 6 Spokesperson** | _[QMR]_ | Risk, objectives, planning |
    | **Clause 7 Spokesperson** | _[Team Lead / QMR]_ | Resources, competence, documents |
    | **Clause 8 Spokesperson** | _[Tech Lead / PO]_ | Operations, design, development |
    | **Clause 9-10 Spokesperson** | _[QMR]_ | Measurement, audit, improvement |
    | **System Demo** | _[DevOps Engineer]_ | Shows Jira, Confluence, CI/CD, Grafana |
    | **Note Taker** | _[Name]_ | Records all auditor questions and comments |

    ---

    ## Phase 4: Final Readiness (Week 4 · Feb 28-Mar 5)

    | # | Task | Owner |
    |---|------|-------|
    | 1 | Internal pre-audit (mini-audit of all clauses) | QMR |
    | 2 | Address all pre-audit findings | Respective owners |
    | 3 | Verify all documents are current | QMR |
    | 4 | Ensure KPI dashboards are up-to-date | DevOps |
    | 5 | Prepare conference room | Escort |
    | 6 | Test system access for demos | Demo person |
    | 7 | Brief all spokespersons — final run-through | QMR |
    | 8 | Prepare 10-min opening presentation | Unit Lead |

    ---

    ## Audit Day Checklist

    ### Morning
    - [ ] Welcome auditor, introductions
    - [ ] Unit Lead presents 10-min overview
    - [ ] Confirm audit plan and schedule
    - [ ] Provide WiFi access, room logistics

    ### During
    - [ ] Escort auditor between sessions
    - [ ] Note taker records all questions
    - [ ] Keep answers concise and evidence-based
    - [ ] Have systems open for demonstrations

    ### Afternoon
    - [ ] Attend closing meeting (all spokespersons)
    - [ ] Listen to findings — don't argue
    - [ ] Thank the auditor
    - [ ] Internal debrief immediately after
    - [ ] Create CAPA entries for any findings

=== ":material-book-open-page-variant: Full"

    ## DDD Unit — ISO 9001:2015 Certification Audit

    **Audit Date:** 2026-03-06
    **Auditing Body:** _[Name]_
    **Lead Auditor:** _[Name]_
    **Internal Coordinator:** QMR — _[Name]_

    ---

    ## Timeline

    ```mermaid
    gantt
        title Audit Preparation Timeline (4 Weeks)
        dateFormat YYYY-MM-DD
        axisFormat %b %d

        section Documentation
        Complete all REF documents          :a1, 2026-02-07, 10d
        Review & approve documents          :a2, after a1, 5d
        Dry run with documents              :a3, after a2, 3d

        section Evidence Gathering
        Collect process evidence             :b1, 2026-02-07, 12d
        Prepare example records              :b2, after b1, 5d
        Organize evidence folder             :b3, after b2, 2d

        section People Preparation
        Train team on QMS awareness          :c1, 2026-02-10, 7d
        Conduct mock audit interviews        :c2, after c1, 7d
        Assign audit day roles               :c3, after c2, 3d

        section Final Preparation
        Internal pre-audit                   :d1, 2026-02-24, 3d
        Address pre-audit findings           :d2, after d1, 5d
        Final readiness review               :d3, after d2, 2d
        AUDIT DAY                            :milestone, 2026-03-06, 0d
    ```

    ---

    ## Phase 1: Documentation Readiness (Weeks 1–2 · Feb 7–20)

    ### QMS Foundation Documents

    | # | Document | Reference | Owner | Status | Review Date | Approved |
    |---|----------|-----------|-------|:------:|:-----------:|:--------:|
    | 1 | Context Analysis (SWOT/PESTLE) | [REF-01](../qms-framework/context-analysis.md) | Unit Lead | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 2 | Stakeholder Register | [REF-02](../qms-framework/stakeholder-register.md) | PO / QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 3 | QMS Scope Statement | [REF-03](../qms-framework/qms-scope.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 4 | Quality Policy | [REF-04](../qms-framework/quality-policy.md) | Unit Lead | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 5 | RACI Matrix | [REF-05](../qms-framework/raci-matrix.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 6 | Risk Register | [REF-06](../planning/risk-register.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 7 | Quality Objectives | [REF-07](../planning/quality-objectives.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 8 | Competency Matrix | [REF-08](../support/competency-matrix.md) | Team Leads | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 9 | Communication Matrix | [REF-09](../support/communication-matrix.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 10 | Supplier Evaluation | [REF-10](../operations/supplier-evaluation.md) | Tech Lead | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 11 | Internal Audit Program | [REF-11](../performance/internal-audit-program.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 12 | Management Review Template | [REF-12](../performance/management-review.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 13 | CAPA Log | [REF-13](../improvement/capa-log.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |
    | 14 | QMS Process Map | [QMS Process Map](process-map.md) | QMR | ☐ Draft ☐ Review ☐ Final | | ☐ |

    ### Additional Documents Needed

    | # | Document | Description | Owner | Status |
    |---|----------|-------------|-------|:------:|
    | 15 | Document Control Procedure | How documents are created, reviewed, approved, and controlled | QMR | ☐ |
    | 16 | Change Management Procedure | RFC process, approval levels, rollback | DevOps Lead | ☐ |
    | 17 | Incident Management Procedure | Severity levels, response times, escalation, post-mortem | SRE Lead | ☐ |
    | 18 | Onboarding Procedure | 30-60-90 day plan, QMS awareness training | Team Leads | ☐ |
    | 19 | Data Protection Impact Assessment | GDPR compliance for driving data | DPO liaison | ☐ |
    | 20 | Tool Qualification Plan (ISO 26262) | TCL assessment for safety-relevant tools | QA Lead | ☐ |

    ---

    ## Phase 2: Evidence Collection (Weeks 1–2 · Feb 7–20)

    ### Process Evidence Checklist

    | ISO Clause | Evidence Required | Source | Collected |
    |:----------:|-------------------|--------|:---------:|
    | **4.1** | Context review meeting minutes | Confluence | ☐ |
    | **4.2** | Stakeholder feedback records (NPS, meeting notes) | Survey tool, Confluence | ☐ |
    | **5.1** | Management commitment evidence (budget approvals, review participation) | Email, Jira | ☐ |
    | **5.2** | Quality policy displayed and acknowledged | Confluence, onboarding records | ☐ |
    | **5.3** | Role definitions, org chart, RACI | Confluence, HR system | ☐ |
    | **6.1** | Risk register with evidence of reviews | REF-06, meeting minutes | ☐ |
    | **6.2** | Quality objective measurements (last 4 quarters) | Grafana exports, reports | ☐ |
    | **7.1** | Resource planning records, infrastructure documentation | Jira, Terraform repos | ☐ |
    | **7.2** | Training records, competency assessments | SuccessFactors, wiki | ☐ |
    | **7.3** | Quality awareness evidence (all-hands slides, onboarding) | Slides, checklists | ☐ |
    | **7.4** | Communication records (sprint reviews, release notes) | Confluence, email | ☐ |
    | **7.5** | Document control evidence (version history, approvals) | Confluence, Git | ☐ |
    | **8.1** | Sprint planning records, Definition of Done | Jira, Confluence | ☐ |
    | **8.2** | Requirements/user stories with acceptance criteria | Jira | ☐ |
    | **8.3** | Design documentation (ADRs, architecture docs) | Confluence, Git | ☐ |
    | **8.3** | Code review records (PR history) | GitHub/GitLab | ☐ |
    | **8.3** | Test results (CI/CD pipeline reports) | CI/CD tool | ☐ |
    | **8.4** | Supplier evaluations, SLA reviews | REF-10, meeting notes | ☐ |
    | **8.5** | Deployment records, release notes | CI/CD, Confluence | ☐ |
    | **8.5** | Monitoring dashboards (uptime, performance) | Grafana | ☐ |
    | **8.7** | Bug/incident records with resolution | Jira, PagerDuty | ☐ |
    | **9.1** | KPI dashboard screenshots/exports | Grafana | ☐ |
    | **9.2** | Internal audit reports and findings | REF-11 | ☐ |
    | **9.3** | Management review meeting minutes | REF-12 (completed) | ☐ |
    | **10.2** | CAPA records (at least 3-5 complete cycles) | REF-13 | ☐ |
    | **10.3** | Improvement evidence (retrospective actions, trend data) | Jira, Grafana | ☐ |

    ---

    ## Phase 3: People Preparation (Weeks 2–3 · Feb 14–27)

    ### Team Awareness Training

    | # | Task | Audience | Method | Status |
    |---|------|----------|--------|:------:|
    | 1 | ISO 9001 basics & our QMS overview | All team members | Workshop (1h) | ☐ |
    | 2 | Quality policy — know it, explain it | All team members | All-hands + quiz | ☐ |
    | 3 | Quality objectives — know your KPIs | All team members | Team meeting | ☐ |
    | 4 | "What's your role in the QMS?" | All team members | 1:1 with team lead | ☐ |
    | 5 | How to handle auditor questions | Interview candidates | Workshop (1h) | ☐ |

    ### Mock Audit Interviews

    | # | Interviewee Role | Clause Focus | Interviewer | Date | Score | Follow-up |
    |---|-----------------|:------------:|-------------|:----:|:-----:|-----------|
    | 1 | Unit Lead | 5.1, 5.2, 9.3 | QMR | | /10 | |
    | 2 | QMR | 4.3, 7.5, 9.2, 10.2 | External/cross-unit | | /10 | |
    | 3 | Product Owner | 4.2, 8.2 | QMR | | /10 | |
    | 4 | Tech Lead | 8.3, 8.4 | QMR | | /10 | |
    | 5 | Scrum Master | 8.1, 10.1 | QMR | | /10 | |
    | 6 | Developer | 7.2, 8.3, 8.5 | Team Lead | | /10 | |
    | 7 | DevOps Engineer | 7.1, 8.5 | Team Lead | | /10 | |
    | 8 | QA Engineer | 8.3, 8.7 | QMR | | /10 | |

    ### Audit Day Role Assignments

    | Role | Person | Responsibility |
    |------|--------|---------------|
    | **Escort / Guide** | _[Name]_ | Accompanies auditor, manages logistics, time-keeping |
    | **Clause 4-5 Spokesperson** | _[Unit Lead]_ | Answers on context, leadership, policy |
    | **Clause 6 Spokesperson** | _[QMR]_ | Answers on risk, objectives, planning |
    | **Clause 7 Spokesperson** | _[Team Lead / QMR]_ | Answers on resources, competence, documents |
    | **Clause 8 Spokesperson** | _[Tech Lead / PO]_ | Answers on operations, design, development |
    | **Clause 9-10 Spokesperson** | _[QMR]_ | Answers on measurement, audit, improvement |
    | **System Demo** | _[DevOps Engineer]_ | Shows Jira, Confluence, CI/CD, Grafana live |
    | **Note Taker** | _[Name]_ | Records all auditor questions and comments |

    ---

    ## Phase 4: Final Readiness (Week 4 · Feb 28–Mar 5)

    | # | Task | Owner | Status |
    |---|------|-------|:------:|
    | 1 | Conduct internal pre-audit (mini-audit of all clauses) | QMR + auditor | ☐ |
    | 2 | Address all findings from pre-audit | Respective owners | ☐ |
    | 3 | Verify all documents are current (no stale content) | QMR | ☐ |
    | 4 | Ensure all KPI dashboards are up-to-date | DevOps | ☐ |
    | 5 | Prepare conference room (projector, whiteboard, documents) | Escort | ☐ |
    | 6 | Print key documents (Quality Policy, Scope, Process Map) | QMR | ☐ |
    | 7 | Test system access (can show Jira, Confluence, Git, Grafana) | System Demo person | ☐ |
    | 8 | Brief all spokespersons — final run-through | QMR | ☐ |
    | 9 | Prepare opening presentation (unit overview, 10 min) | Unit Lead | ☐ |
    | 10 | Notify team of audit schedule and expectations | QMR | ☐ |

    ---

    ## Audit Day Checklist

    ### Morning — Opening

    - [ ] Welcome auditor, introductions
    - [ ] Unit Lead presents 10-min overview (who we are, what we do, QMS scope)
    - [ ] Confirm audit plan and schedule
    - [ ] Provide WiFi access, room logistics

    ### During — Interview Sessions

    - [ ] Escort auditor between sessions
    - [ ] Note taker records all questions and comments
    - [ ] If unsure about an answer: "Let me get you that information" (then actually get it)
    - [ ] Keep answers concise and evidence-based
    - [ ] Have systems open and ready for live demonstrations

    ### Afternoon — Closing

    - [ ] Attend closing meeting (all spokespersons)
    - [ ] Listen to findings — don't argue, ask for clarification if needed
    - [ ] Thank the auditor
    - [ ] Internal debrief immediately after — capture all observations
    - [ ] Create CAPA entries for any findings

    ---

    ## Post-Audit Actions

    | # | Task | Owner | Due Date | Status |
    |---|------|-------|:--------:|:------:|
    | 1 | Distribute audit report to management | QMR | +1 week | ☐ |
    | 2 | Create CAPA for each finding | QMR | +2 weeks | ☐ |
    | 3 | Root cause analysis for major findings | Finding owners | +3 weeks | ☐ |
    | 4 | Implement corrective actions | Finding owners | Per CAPA | ☐ |
    | 5 | Verify effectiveness of corrections | QMR | Per CAPA | ☐ |
    | 6 | Submit evidence to certification body (if required) | QMR | Per deadline | ☐ |
    | 7 | Lessons learned session | QMR + all | +4 weeks | ☐ |
    | 8 | Update QMS documents based on lessons learned | QMR | +6 weeks | ☐ |

    ---

    *Document Version: 1.0 | Created: 2026-02-06 | Owner: QMR, DDD Unit*
