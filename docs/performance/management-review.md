# REF-12: Management Review Template

=== ":material-lightning-bolt: Quick (~1h)"

    **ISO 9001 Clause 9.3** | **Owner:** QMR | **Chair:** Unit Lead

    ## Management Review — Required Inputs

    1. Status of actions from previous reviews
    2. Changes in external/internal issues
    3. QMS performance: customer satisfaction, quality objectives, process performance, nonconformities/CAPAs, audit results
    4. Adequacy of resources
    5. Risk and opportunity review
    6. Improvement opportunities

    ## Required Outputs

    - Decisions on improvement actions
    - Resource allocation changes
    - QMS scope adjustments (if any)
    - Updated quality objectives
    - Action items with owners and deadlines

    > **Frequency:** Quarterly + annual comprehensive review. Ad-hoc for significant events.

=== ":material-book-open-variant: Essential (~3h)"

    **ISO 9001 Clause 9.3** | **Owner:** QMR | **Chair:** Unit Lead | **Frequency:** Quarterly

    ## Agenda — Required Inputs (Clause 9.3.2)

    ### 1. Previous Actions

    | Action # | Description | Owner | Due | Status |
    |:--------:|-------------|-------|:---:|:------:|
    | MR-_[#]_ | _[Action]_ | _[Name]_ | _[Date]_ | ☐/✅ |

    ### 2. Changes in Context

    | Issue | Change | Impact on QMS | Action |
    |-------|--------|---------------|--------|
    | _[Issue]_ | _[Change]_ | _[Impact]_ | _[Action]_ |

    ### 3. QMS Performance

    #### Quality Objectives

    | Objective | Previous | Current | Target | Status |
    |-----------|:--------:|:-------:|:------:|:------:|
    | QO-1: Availability | _[%]_ | _[%]_ | >= 99.5% | &#x1F7E2;&#x1F7E1;&#x1F534; |
    | QO-2: MTTR | _[h]_ | _[h]_ | < 4h | &#x1F7E2;&#x1F7E1;&#x1F534; |
    | QO-3: NPS | _[#]_ | _[#]_ | >= 40 | &#x1F7E2;&#x1F7E1;&#x1F534; |
    | QO-4: Data Integrity | _[#]_ | _[#]_ | 0 | &#x1F7E2;&#x1F7E1;&#x1F534; |

    #### Audit Results & CAPAs

    | Audit/CAPA | Status | Key Findings |
    |------------|:------:|-------------|
    | _[Ref]_ | _[Status]_ | _[Summary]_ |

    ### 4. Resources & Risks

    | Area | Status | Gap | Action |
    |------|:------:|-----|--------|
    | Staffing | _[Status]_ | _[Gap]_ | _[Action]_ |
    | Infrastructure | _[Status]_ | _[Gap]_ | _[Action]_ |

    ## Outputs (Clause 9.3.3)

    | # | Decision/Action | Owner | Due Date |
    |---|----------------|-------|:--------:|
    | D-_[#]_ | _[Decision]_ | _[Name]_ | _[Date]_ |

=== ":material-book-open-page-variant: Full"

    ## DDD Unit — Data Driven Development | AD/ADAS Tooling

    **Document Owner:** QMR
    **Meeting Chair:** Unit Lead

    ---

    ## Management Review Meeting Record

    | Attribute | Detail |
    |-----------|--------|
    | **Date** | YYYY-MM-DD |
    | **Time** | HH:MM – HH:MM |
    | **Location** | _[Room / Teams link]_ |
    | **Attendees** | _[Names and roles]_ |
    | **Absent** | _[Names]_ |
    | **Minutes by** | _[Name]_ |

    ---

    ## Agenda / Required Inputs (ISO 9001:2015, Clause 9.3.2)

    ### 1. Status of Actions from Previous Management Reviews

    | Action # | Description | Owner | Due Date | Status | Comments |
    |:--------:|-------------|-------|:--------:|:------:|----------|
    | MR-_[#]_ | _[Action]_ | _[Name]_ | _[Date]_ | ☐ Open / ✅ Closed | |
    | | | | | | |

    ### 2. Changes in External and Internal Issues

    | Issue | Type | Change Description | Impact on QMS | Action Required |
    |-------|------|-------------------|---------------|-----------------|
    | _[Issue]_ | Internal / External | _[What changed]_ | _[Impact]_ | _[Action]_ |
    | | | | | |

    **Reference:** [REF-01 Context Analysis](../qms-framework/context-analysis.md)

    ### 3. QMS Performance and Effectiveness

    #### 3a. Customer Satisfaction

    | Metric | Previous Period | Current Period | Target | Trend | Action |
    |--------|:--------------:|:--------------:|:------:|:-----:|--------|
    | NPS Score | _[#]_ | _[#]_ | ≥ 40 | ↑↓→ | |
    | Support ticket resolution time | _[hours]_ | _[hours]_ | _[target]_ | ↑↓→ | |
    | Feature request completion rate | _[%]_ | _[%]_ | _[target]_ | ↑↓→ | |

    #### 3b. Quality Objectives Performance

    | Objective | KPI | Previous | Current | Target | Status |
    |-----------|-----|:--------:|:-------:|:------:|:------:|
    | QO-1: Availability | Uptime % | _[%]_ | _[%]_ | ≥ 99.5% | 🟢🟡🔴 |
    | QO-2: MTTR | Hours | _[h]_ | _[h]_ | < 4h | 🟢🟡🔴 |
    | QO-3: NPS | Score | _[#]_ | _[#]_ | ≥ 40 | 🟢🟡🔴 |
    | QO-4: Data Integrity | Incidents | _[#]_ | _[#]_ | 0 | 🟢🟡🔴 |
    | QO-5: Release Quality | Pass rate | _[%]_ | _[%]_ | 100% | 🟢🟡🔴 |
    | QO-6: Test Coverage | Coverage % | _[%]_ | _[%]_ | ≥ 80% | 🟢🟡🔴 |
    | QO-7: Training | Completion % | _[%]_ | _[%]_ | ≥ 90% | 🟢🟡🔴 |

    **Reference:** [REF-07 Quality Objectives](../planning/quality-objectives.md)

    #### 3c. Process Performance

    | Process | Key Metric | Previous | Current | Trend | Issue / Action |
    |---------|-----------|:--------:|:-------:|:-----:|---------------|
    | Development | Sprint velocity | _[pts]_ | _[pts]_ | ↑↓→ | |
    | Deployment | Deploy frequency | _[/week]_ | _[/week]_ | ↑↓→ | |
    | Deployment | Failure rate | _[%]_ | _[%]_ | ↑↓→ | |
    | Operations | MTTR | _[h]_ | _[h]_ | ↑↓→ | |
    | Operations | Incident count | _[#]_ | _[#]_ | ↑↓→ | |

    #### 3d. Nonconformities and Corrective Actions

    | CAPA # | Description | Root Cause | Action Taken | Status | Effective? |
    |:------:|-------------|------------|-------------|:------:|:----------:|
    | CA-_[#]_ | _[Description]_ | _[Root cause]_ | _[Action]_ | ☐ Open / ✅ Closed | ☐ Yes / ☐ No |

    **Reference:** [REF-13 CAPA Log](../improvement/capa-log.md)

    #### 3e. Internal Audit Results

    | Audit # | Scope | Date | Major NCs | Minor NCs | Observations | Status |
    |:-------:|-------|:----:|:---------:|:---------:|:------------:|:------:|
    | A-_[#]_ | _[Clauses]_ | _[Date]_ | _[#]_ | _[#]_ | _[#]_ | _[Status]_ |

    **Reference:** [REF-11 Internal Audit Program](internal-audit-program.md)

    ### 4. Adequacy of Resources

    | Resource Area | Current Status | Gap Identified | Action Required |
    |--------------|:-------------:|:--------------:|-----------------|
    | Staffing | _[Status]_ | _[Gap]_ | _[Action]_ |
    | Cloud infrastructure | _[Status]_ | _[Gap]_ | _[Action]_ |
    | Tooling / licenses | _[Status]_ | _[Gap]_ | _[Action]_ |
    | Training budget | _[Status]_ | _[Gap]_ | _[Action]_ |

    ### 5. Risk and Opportunity Review

    | Top Risks (by score) | Score | Mitigation Status | Change Since Last Review |
    |----------------------|:-----:|:-----------------:|:------------------------:|
    | _[Risk from REF-06]_ | _[#]_ | _[Status]_ | ↑↓→ |
    | | | | |

    **Reference:** [REF-06 Risk Register](../planning/risk-register.md)

    ### 6. Opportunities for Improvement

    | # | Improvement Proposal | Source | Expected Benefit | Decision |
    |---|---------------------|--------|------------------|----------|
    | 1 | _[Proposal]_ | _[Retro/Audit/Feedback]_ | _[Benefit]_ | ☐ Approve / ☐ Defer / ☐ Reject |
    | | | | | |

    ---

    ## Outputs / Decisions (ISO 9001:2015, Clause 9.3.3)

    ### Decisions Made

    | # | Decision | Owner | Due Date |
    |---|----------|-------|:--------:|
    | D-_[#]_ | _[Decision]_ | _[Name]_ | _[Date]_ |
    | | | | |

    ### Action Items

    | # | Action | Owner | Due Date | Priority |
    |---|--------|-------|:--------:|:--------:|
    | MR-_[#]_ | _[Action]_ | _[Name]_ | _[Date]_ | High/Med/Low |
    | | | | | |

    ### Resource Allocations

    | Resource | Allocation Decision | Amount/Detail |
    |----------|-------------------|---------------|
    | _[Resource]_ | _[Decision]_ | _[Detail]_ |

    ### Changes to QMS

    | Change | Reason | Effective Date |
    |--------|--------|:--------------:|
    | _[Change]_ | _[Reason]_ | _[Date]_ |

    ---

    ## Next Management Review

    | Date | Focus Areas |
    |------|------------|
    | _[Date]_ | _[Special focus areas for next review]_ |

    ---

    **Minutes approved by:**

    _________________________
    [Unit Lead Name] — Date: YYYY-MM-DD

    ---

    *ISO 9001:2015 Reference: Clause 9.3*
