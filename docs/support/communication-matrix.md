# REF-09: Communication Matrix

=== ":material-lightning-bolt: Quick (~1h)"

    **ISO 9001 Clause 7.4** | **Owner:** QMR

    ## Key Communication Channels

    | What | When | From/To | How |
    |------|------|---------|-----|
    | Daily Standup | Daily | Team | MS Teams |
    | Sprint Review | Bi-weekly | Team to stakeholders | Meeting |
    | Sprint Retrospective | Bi-weekly | Team | Miro/FunRetro |
    | All-Hands (incl. quality metrics) | Monthly | Unit Lead to all | Meeting |
    | Management Review | Quarterly | QMR + management | Formal meeting |
    | Release Notes | Per release | DevOps to customers | Confluence + email |
    | Incident Notification | Immediate | On-call to team | PagerDuty + Slack |

=== ":material-book-open-variant: Essential (~3h)"

    **ISO 9001 Clause 7.4** | **Owner:** QMR

    ## Internal Communication

    | What | Purpose | When | From | To | How |
    |------|---------|------|------|----|-----|
    | Daily Standup | Sync team, surface blockers | Daily (15 min) | Team | Team | MS Teams |
    | Sprint Planning | Agree scope & goals | Bi-weekly | PO + SM | Team | Meeting |
    | Sprint Review/Demo | Show completed work | Bi-weekly | Team | Stakeholders | Meeting |
    | Sprint Retrospective | Identify improvements | Bi-weekly | SM | Team | Miro/FunRetro |
    | Team Leads Sync | Cross-team alignment | Weekly | Leads | Unit Lead | Meeting |
    | All-Hands | Unit updates, quality metrics | Monthly | Unit Lead | All | Meeting |
    | Management Review | QMS performance review | Quarterly | QMR | Management | Formal meeting |
    | Incident Notification | Production incident alert | Immediate | On-call | Team + mgmt | PagerDuty + Slack |
    | Post-Mortem | Lessons learned | Within 5 days | Incident lead | All relevant | Meeting + doc |

    ## External Communication

    | What | When | From | To | How |
    |------|------|------|----|-----|
    | Release Notes | Each release | DevOps/PO | Customers | Confluence + email |
    | SLA Reports | Monthly | SRE | Consumers | Dashboard + email |
    | Incident Notification | Immediate | On-call | Customers | Slack + email |
    | Roadmap Sharing | Quarterly | PO | Customer stakeholders | Presentation |
    | NPS Survey | Quarterly | PO | AD/ADAS teams | Survey |

=== ":material-book-open-page-variant: Full"

    ## DDD Unit — Data Driven Development | AD/ADAS Tooling

    **Document Owner:** QMR
    **Last Review:** YYYY-MM-DD
    **Next Review:** YYYY-MM-DD

    ---

    ## 1. Purpose

    Defines internal and external communication requirements for the QMS, as required by ISO 9001:2015 Clause 7.4.

    ---

    ## 2. Internal Communication

    | What | Purpose | When | From | To | How | Records |
    |------|---------|------|------|-----|-----|---------|
    | Daily Standup | Synchronize team work, surface blockers | Daily (15 min) | Team members | Team | MS Teams / in-person | Jira board updates |
    | Sprint Planning | Agree sprint scope and goals | Every 2 weeks | PO + SM | Team | Meeting | Sprint backlog in Jira |
    | Sprint Review / Demo | Demonstrate completed work to stakeholders | Every 2 weeks | Team | Stakeholders | Meeting + recording | Demo notes, Jira updates |
    | Sprint Retrospective | Identify improvements | Every 2 weeks | SM | Team | Meeting (Miro/FunRetro) | Retro action items in Jira |
    | Team Leads Sync | Cross-team alignment, KPI review | Weekly | Team Leads | Unit Lead | Meeting | Meeting minutes |
    | All-Hands | Unit updates, strategy, quality metrics | Monthly | Unit Lead | All team members | Meeting + slides | Presentation deck |
    | Quality Policy & Objectives Update | Awareness and alignment | Quarterly | QMR | All team members | All-Hands / email | Presentation, acknowledgement |
    | Management Review | QMS performance review | Quarterly | QMR + Unit Lead | Management team | Formal meeting | Management review minutes |
    | Internal Audit Results | Share findings and actions | After each audit | QMR | Audited teams + management | Report + meeting | Audit report |
    | Incident Notification | Alert on production incidents | As needed (immediate) | On-call engineer | Team + management | PagerDuty + Slack/Teams | Incident ticket |
    | Post-Mortem / Lessons Learned | Share learning from incidents | Within 5 days of incident | Incident lead | All relevant parties | Meeting + document | Post-mortem report |
    | Onboarding | Introduce QMS, processes, tools | First week of new hire | Team Lead + QMR | New team member | Onboarding checklist | Signed completion |

    ---

    ## 3. External Communication (to other organizational units)

    | What | Purpose | When | From | To | How | Records |
    |------|---------|------|------|-----|-----|---------|
    | Release Notes | Inform customers of changes | Each release | DevOps / PO | AD/ADAS teams (customers) | Confluence + email | Release notes page |
    | SLA Reports | Report on service performance | Monthly | SRE team | Platform consumers | Dashboard + email | SLA report |
    | Service Incident Notification | Alert customers on outages | As needed (immediate) | On-call engineer | Affected customers | Slack/Teams channel + email | Incident ticket |
    | Roadmap Sharing | Align on upcoming features | Quarterly | PO | Customer stakeholders | Presentation | Roadmap document |
    | Customer Feedback Collection | Gather satisfaction data | Quarterly | PO | AD/ADAS teams | Survey (NPS) | Survey results |
    | Security Incident Report | Mandatory reporting | As needed | Security officer | InfoSec team, DPO | Formal report | Incident record |
    | Audit Results (to Corporate QM) | Report on QMS status | Annually | QMR | Corporate QM | Formal report | Audit summary |

    ---

    ## 4. Communication Channels

    | Channel | Use Case | Audience | Retention |
    |---------|----------|----------|-----------|
    | **MS Teams / Slack** | Day-to-day communication, quick questions | Team internal | Per retention policy |
    | **Confluence** | Documentation, procedures, policies, release notes | Team + customers | Indefinite (versioned) |
    | **Jira** | Work tracking, incidents, CAPAs | Team internal | Indefinite |
    | **Email** | Formal communication, approvals, external notifications | As needed | Per retention policy |
    | **PagerDuty** | Incident alerting | On-call team | 12 months |
    | **Grafana Dashboards** | KPI visibility | Team + management | Metric retention period |
    | **All-Hands Meetings** | Unit-wide announcements | All team members | Slides archived |

    ---

    ## 5. Review Log

    | Date | Reviewer | Changes Made |
    |------|----------|-------------|
    | YYYY-MM-DD | [Name] | Initial creation |

    ---

    *ISO 9001:2015 Reference: Clause 7.4*
