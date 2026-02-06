# REF-05: RACI Matrix

## DDD Unit — QMS Roles and Responsibilities

**Document Owner:** QMR
**Last Review:** YYYY-MM-DD
**Next Review:** YYYY-MM-DD

---

## Legend

| Letter | Meaning | Description |
|--------|---------|-------------|
| **R** | Responsible | Does the work |
| **A** | Accountable | Ultimately answerable (one per activity) |
| **C** | Consulted | Provides input before decision |
| **I** | Informed | Notified after decision |

---

## 1. QMS Management Activities

| Activity | Unit Lead | QMR | Team Lead | Scrum Master | Product Owner | Developer | DevOps |
|----------|:---------:|:---:|:---------:|:------------:|:-------------:|:---------:|:------:|
| Quality policy approval | **A** | R | I | I | I | I | I |
| Management review | **A** | R | C | I | C | I | I |
| QMS scope definition | **A** | R | C | | C | | |
| Internal audit planning | C | **A**/R | C | | | | |
| Internal audit execution | I | **A** | R | | | | |
| Risk register maintenance | **A** | R | C | | C | | |
| Quality objectives setting | **A** | R | C | | C | | |
| CAPA management | I | **A**/R | R | | | R | |
| Document control | I | **A**/R | C | | | | |
| Continual improvement | **A** | R | R | R | R | R | R |

## 2. Core Process Activities

| Activity | Unit Lead | QMR | Team Lead | Scrum Master | Product Owner | Developer | DevOps | QA |
|----------|:---------:|:---:|:---------:|:------------:|:-------------:|:---------:|:------:|:--:|
| Stakeholder identification | C | I | C | | **A**/R | | | |
| Requirements engineering | I | | C | C | **A**/R | C | | |
| Architecture & design | I | | **A** | | C | R | C | C |
| Sprint planning | | | C | **A**/R | R | R | | |
| Development (coding) | | | C | | | **A**/R | | |
| Code review | | | R | | | **A**/R | | |
| Testing & validation | | I | C | | C | R | | **A**/R |
| Release & deployment | I | I | **A** | | I | C | R | C |
| Incident management | I | I | **A** | | I | R | R | |
| SLA monitoring | I | C | **A** | | I | | R | |

## 3. Support Process Activities

| Activity | Unit Lead | QMR | Team Lead | HR | DevOps | Developer |
|----------|:---------:|:---:|:---------:|:--:|:------:|:---------:|
| Competence management | **A** | I | R | C | | |
| Training planning | C | I | **A**/R | C | | |
| Onboarding new members | I | | **A**/R | R | | C |
| Infrastructure management | I | | C | | **A**/R | |
| Supplier evaluation | **A** | C | R | | C | |
| Communication management | **A** | R | C | | | |

---

## 4. Key Role Definitions

### Unit Lead
- Overall accountability for QMS effectiveness
- Approves quality policy and objectives
- Chairs management review
- Allocates resources for quality activities

### Quality Management Representative (QMR)
- Day-to-day QMS coordination
- Manages document control system
- Plans and coordinates internal audits
- Tracks CAPAs and improvement actions
- Reports QMS performance to management

### Team Lead
- Responsible for team-level quality practices
- Ensures competence of team members
- Owns team's operational processes

### Scrum Master
- Facilitates Agile ceremonies
- Drives retrospective improvement actions
- Removes impediments to quality

### Product Owner
- Defines and prioritizes requirements
- Represents customer voice
- Accepts/rejects deliverables

### Quality Champion (per team)
- Promotes quality awareness within the team
- First point of contact for QMS questions
- Supports QMR with audit preparation

---

## 5. Review Log

| Date | Reviewer | Changes Made |
|------|----------|-------------|
| YYYY-MM-DD | [Name] | Initial creation |

---

*ISO 9001:2015 Reference: Clause 5.3*
