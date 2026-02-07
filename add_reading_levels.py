#!/usr/bin/env python3
"""Transform all ISO 9001 docs to include three reading levels via content tabs.

Uses pymdownx.tabbed (already configured) with content.tabs.link for cross-page sync.
Tab selection persists across pages within each language.
"""

import os

DOCS = '/Users/Q284340/Agentic/iso-9001/docs'

def indent_block(text, spaces=4):
    """Indent all non-empty lines by given number of spaces."""
    prefix = ' ' * spaces
    lines = text.split('\n')
    result = []
    for line in lines:
        if line.strip():
            result.append(prefix + line)
        else:
            result.append('')
    return '\n'.join(result)


def transform_file(filepath, quick, essential, tab_labels):
    """Add three-level tabs to a markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    lines = content.split('\n')

    # Find title line (first # heading)
    title_line = ''
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title_line = line
            body_start = i + 1
            break

    body = '\n'.join(lines[body_start:]).strip()

    q_label, e_label, f_label = tab_labels
    new_content = (
        f'{title_line}\n\n'
        f'=== ":material-lightning-bolt: {q_label}"\n\n'
        f'{indent_block(quick.strip())}\n\n'
        f'=== ":material-book-open-variant: {e_label}"\n\n'
        f'{indent_block(essential.strip())}\n\n'
        f'=== ":material-book-open-page-variant: {f_label}"\n\n'
        f'{indent_block(body)}\n'
    )

    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f'  OK  {os.path.relpath(filepath, DOCS)}')


# ---------------------------------------------------------------------------
# TAB LABELS
# ---------------------------------------------------------------------------
EN = ('Quick (~1h)', 'Essential (~3h)', 'Full')
DE = ('Schnell (~1 Std.)', 'Wesentlich (~3 Std.)', u'Vollst\u00e4ndig')

# ---------------------------------------------------------------------------
# CONTENT DEFINITIONS — ENGLISH
# ---------------------------------------------------------------------------
PAGES = []

# ===== index.md =====
PAGES.append({
    'en': 'index.md',
    'de': 'index.de.md',
    'en_quick': """
!!! warning "Audit: **March 6, 2026** — 4 weeks to prepare"

## Three Things You Need to Know

1. **What we do:** We're the DDD unit — we build tools for AD/ADAS data engineering, simulation, and reprocessing
2. **What they'll ask:** Auditors check that processes **exist**, are **followed**, are **measured**, and are **improved**
3. **What you need:** Know your role in the QMS, the quality policy, and your team's KPIs

## Start Here

| Priority | Document | Reading Time |
|:--------:|----------|:------------:|
| 1 | [Audit Catalogue](getting-started/audit-catalogue.md) — What auditors will ask | ~10 min |
| 2 | [Preparation Checklist](getting-started/preparation-checklist.md) — Timeline & tasks | ~5 min |
| 3 | [Quality Policy](qms-framework/quality-policy.md) — Know this by heart | ~3 min |
| 4 | [Process Map](getting-started/process-map.md) — How we work | ~3 min |

!!! tip "Navigation Tip"
    Use the **Quick** tab on every page for a fast overview. Your tab selection carries across all pages automatically.
""",
    'en_essential': """
!!! warning "Audit: **March 6, 2026** — 4 weeks to prepare"

## DDD Unit — Data Driven Development | AD/ADAS Tooling

We develop and maintain tooling for data engineering, storage, simulation, and reprocessing used by software engineers working on Autonomous Driving (AD) and Advanced Driver Assistance Systems (ADAS).

---

## Documentation Structure

```mermaid
graph LR
    A[Audit Catalogue] --> B[Process Map]
    B --> C[Reference Documents]
    C --> D[Preparation Checklist]
    D --> E[Audit Ready!]
    style A fill:#4A90D9,color:#fff
    style B fill:#7B68EE,color:#fff
    style C fill:#E8A838,color:#fff
    style D fill:#27AE60,color:#fff
    style E fill:#27AE60,color:#fff
```

### :rocket: Getting Started

- **[Audit Catalogue](getting-started/audit-catalogue.md)** — 70+ typical auditor questions with suggested answers
- **[Process Map](getting-started/process-map.md)** — Complete QMS process landscape
- **[Preparation Checklist](getting-started/preparation-checklist.md)** — Phased 4-week timeline with tasks

### Reference Documents

| Clauses | Documents |
|---------|-----------|
| **4-5** QMS Framework | [Context Analysis](qms-framework/context-analysis.md) \\| [Stakeholder Register](qms-framework/stakeholder-register.md) \\| [QMS Scope](qms-framework/qms-scope.md) \\| [Quality Policy](qms-framework/quality-policy.md) \\| [RACI Matrix](qms-framework/raci-matrix.md) |
| **6** Planning | [Risk Register](planning/risk-register.md) \\| [Quality Objectives](planning/quality-objectives.md) |
| **7** Support | [Competency Matrix](support/competency-matrix.md) \\| [Communication Matrix](support/communication-matrix.md) |
| **8** Operations | [Supplier Evaluation](operations/supplier-evaluation.md) |
| **9** Performance | [Internal Audit Program](performance/internal-audit-program.md) \\| [Management Review](performance/management-review.md) |
| **10** Improvement | [CAPA Log](improvement/capa-log.md) |

## ISO 9001:2015 PDCA Cycle

```mermaid
graph TB
    subgraph "Plan"
        C4["Clause 4 — Context"]
        C5["Clause 5 — Leadership"]
        C6["Clause 6 — Planning"]
    end
    subgraph "Do"
        C7["Clause 7 — Support"]
        C8["Clause 8 — Operation"]
    end
    subgraph "Check"
        C9["Clause 9 — Performance Evaluation"]
    end
    subgraph "Act"
        C10["Clause 10 — Improvement"]
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

## What Auditors Look For

!!! success "Key Principles"
    - **Evidence over documentation** — Show real records of what you do
    - **Consistency** — Processes are followed the same way each time
    - **Measurement** — You track performance with meaningful metrics
    - **Improvement** — You use data to drive changes
    - **Awareness** — Team understands quality objectives and their role
""",
    'de_quick': """
!!! warning "Audit: **6. M\\u00e4rz 2026** — 4 Wochen Vorbereitung"

## Drei Dinge, die Sie wissen m\\u00fcssen

1. **Was wir tun:** Wir sind die DDD-Abteilung — wir bauen Werkzeuge f\\u00fcr AD/ADAS Datenengineering, Simulation und Reprocessing
2. **Was gefragt wird:** Auditoren pr\\u00fcfen, ob Prozesse **existieren**, **befolgt** werden, **gemessen** werden und **verbessert** werden
3. **Was Sie brauchen:** Kennen Sie Ihre Rolle im QMS, die Qualit\\u00e4tspolitik und die KPIs Ihres Teams

## Starten Sie hier

| Priorit\\u00e4t | Dokument | Lesezeit |
|:--------:|----------|:--------:|
| 1 | [Auditkatalog](getting-started/audit-catalogue.md) — Was Auditoren fragen | ~10 Min. |
| 2 | [Vorbereitungs-Checkliste](getting-started/preparation-checklist.md) — Zeitplan & Aufgaben | ~5 Min. |
| 3 | [Qualit\\u00e4tspolitik](qms-framework/quality-policy.md) — Auswendig kennen | ~3 Min. |
| 4 | [Prozesslandkarte](getting-started/process-map.md) — Wie wir arbeiten | ~3 Min. |

!!! tip "Navigationstipp"
    Nutzen Sie den **Schnell**-Tab auf jeder Seite f\\u00fcr einen schnellen \\u00dcberblick. Ihre Tab-Auswahl wird automatisch auf alle Seiten \\u00fcbertragen.
""",
    'de_essential': """
!!! warning "Audit: **6. M\\u00e4rz 2026** — 4 Wochen Vorbereitung"

## DDD-Abteilung — Data Driven Development | AD/ADAS Tooling

Wir entwickeln und betreiben Werkzeuge f\\u00fcr Datenengineering, Datenspeicherung, Simulation und Reprocessing f\\u00fcr Softwareentwickler im Bereich Autonomes Fahren (AD) und Fahrerassistenzsysteme (ADAS).

---

## Dokumentationsstruktur

```mermaid
graph LR
    A[Auditkatalog] --> B[Prozesslandkarte]
    B --> C[Referenzdokumente]
    C --> D[Checkliste]
    D --> E[Audit-bereit!]
    style A fill:#4A90D9,color:#fff
    style B fill:#7B68EE,color:#fff
    style C fill:#E8A838,color:#fff
    style D fill:#27AE60,color:#fff
    style E fill:#27AE60,color:#fff
```

### :rocket: Erste Schritte

- **[Auditkatalog](getting-started/audit-catalogue.md)** — 70+ typische Auditorfragen mit Antwortvorschl\\u00e4gen
- **[Prozesslandkarte](getting-started/process-map.md)** — Vollst\\u00e4ndige QMS-Prozesslandschaft
- **[Vorbereitungs-Checkliste](getting-started/preparation-checklist.md)** — 4-Wochen-Zeitplan mit Aufgaben

### Referenzdokumente

| Abschnitte | Dokumente |
|------------|-----------|
| **4-5** QMS-Rahmenwerk | [Kontextanalyse](qms-framework/context-analysis.md) \\| [Stakeholder-Register](qms-framework/stakeholder-register.md) \\| [QMS-Geltungsbereich](qms-framework/qms-scope.md) \\| [Qualit\\u00e4tspolitik](qms-framework/quality-policy.md) \\| [RACI-Matrix](qms-framework/raci-matrix.md) |
| **6** Planung | [Risikoregister](planning/risk-register.md) \\| [Qualit\\u00e4tsziele](planning/quality-objectives.md) |
| **7** Unterst\\u00fctzung | [Kompetenzmatrix](support/competency-matrix.md) \\| [Kommunikationsmatrix](support/communication-matrix.md) |
| **8** Betrieb | [Lieferantenbewertung](operations/supplier-evaluation.md) |
| **9** Leistungsbewertung | [Internes Auditprogramm](performance/internal-audit-program.md) \\| [Managementbewertung](performance/management-review.md) |
| **10** Verbesserung | [CAPA-Protokoll](improvement/capa-log.md) |

## Was Auditoren suchen

!!! success "Kernprinzipien"
    - **Nachweise statt Dokumentation** — Zeigen Sie echte Aufzeichnungen
    - **Konsistenz** — Prozesse werden jedes Mal gleich befolgt
    - **Messung** — Aussagekr\\u00e4ftige Metriken werden verfolgt
    - **Verbesserung** — Datengetriebene Ver\\u00e4nderungen
    - **Bewusstsein** — Team kennt Qualit\\u00e4tsziele und eigene Rolle
""",
})

# ===== preparation-checklist.md =====
PAGES.append({
    'en': 'getting-started/preparation-checklist.md',
    'de': 'getting-started/preparation-checklist.de.md',
    'en_quick': """
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
""",
    'en_essential': """
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
""",
    'de_quick': """
## DDD-Einheit — ISO 9001:2015 Zertifizierungsaudit

**Auditdatum:** 06.03.2026 | **Koordinator:** QMR — _[Name]_

---

## Zeitplan

```mermaid
gantt
    title 4-Wochen-Vorbereitung
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Wochen 1-2
    Dokumente & Nachweise        :a1, 2026-02-07, 14d

    section Wochen 2-3
    Teamvorbereitung             :b1, 2026-02-14, 14d

    section Woche 4
    Voraudit & Bereitschaft      :c1, 2026-02-28, 5d
    AUDITTAG                     :milestone, 2026-03-06, 0d
```

---

## Wichtigste Dokumente

| Nr. | Dokument | Referenz | Bereit? |
|-----|----------|----------|:-------:|
| 1 | Kontextanalyse (SWOT) | [REF-01](../qms-framework/context-analysis.md) | ☐ |
| 2 | QMS-Geltungsbereich | [REF-03](../qms-framework/qms-scope.md) | ☐ |
| 3 | Qualit\\u00e4tspolitik | [REF-04](../qms-framework/quality-policy.md) | ☐ |
| 4 | RACI-Matrix | [REF-05](../qms-framework/raci-matrix.md) | ☐ |
| 5 | Risikoregister | [REF-06](../planning/risk-register.md) | ☐ |
| 6 | Qualit\\u00e4tsziele | [REF-07](../planning/quality-objectives.md) | ☐ |
| 7 | Internes Auditprogramm | [REF-11](../performance/internal-audit-program.md) | ☐ |
| 8 | Managementbewertung | [REF-12](../performance/management-review.md) | ☐ |
| 9 | CAPA-Protokoll | [REF-13](../improvement/capa-log.md) | ☐ |

---

## Rollen am Audittag

| Rolle | Person | Fokus |
|-------|--------|-------|
| **Begleiter/Lotse** | _[Name]_ | Logistik, Zeiteinhaltung |
| **Abschnitt 4-5** | _[Unit Lead]_ | Kontext, F\\u00fchrung, Politik |
| **Abschnitt 6** | _[QMR]_ | Risiken, Ziele, Planung |
| **Abschnitt 7-8** | _[Tech Lead / PO]_ | Ressourcen, Betrieb, Entwicklung |
| **Abschnitt 9-10** | _[QMR]_ | Messung, Audit, Verbesserung |
| **Systemdemo** | _[DevOps]_ | Jira, Confluence, CI/CD, Grafana |
| **Protokollf\\u00fchrer** | _[Name]_ | Erfasst alle Auditorfragen |

---

## Audittag — Auf einen Blick

**Vormittag:** Auditor begr\\u00fc\\u00dfen &#8594; 10-Min-\\u00dcbersicht &#8594; Zeitplan best\\u00e4tigen &#8594; WLAN-Zugang

**W\\u00e4hrend:** Auditor begleiten &#8594; alles notieren &#8594; kurze, nachweisbasierte Antworten &#8594; Systeme f\\u00fcr Demo bereit

**Nachmittag:** Abschlussbesprechung &#8594; zuh\\u00f6ren, nicht streiten &#8594; danken &#8594; interne Nachbesprechung &#8594; CAPAs erstellen
""",
    'de_essential': """
## DDD-Einheit — ISO 9001:2015 Zertifizierungsaudit

**Auditdatum:** 06.03.2026
**Zertifizierungsstelle:** _[Name]_
**Leitender Auditor:** _[Name]_
**Interner Koordinator:** QMR — _[Name]_

---

## Zeitplan

```mermaid
gantt
    title Zeitplan Auditvorbereitung (4 Wochen)
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Dokumentation
    Alle REF-Dokumente fertigstellen     :a1, 2026-02-07, 10d
    Dokumente pr\\u00fcfen & genehmigen        :a2, after a1, 5d

    section Nachweissammlung
    Prozessnachweise sammeln              :b1, 2026-02-07, 12d
    Nachweisordner organisieren           :b2, after b1, 5d

    section Personalvorbereitung
    Team in QMS-Bewusstsein schulen       :c1, 2026-02-10, 7d
    Probeaudit-Interviews                 :c2, after c1, 7d

    section Abschlussvorbereitung
    Internes Voraudit                     :d1, 2026-02-24, 3d
    Feststellungen & Bereitschaft         :d2, after d1, 7d
    AUDITTAG                              :milestone, 2026-03-06, 0d
```

---

## Phase 1: Dokumentation (Wochen 1-2 \\u00b7 7.-20. Feb.)

| Nr. | Dokument | Referenz | Verantwortlich | Status |
|-----|----------|----------|----------------|:------:|
| 1 | Kontextanalyse (SWOT/PESTLE) | [REF-01](../qms-framework/context-analysis.md) | Unit Lead | ☐ |
| 2 | Stakeholder-Register | [REF-02](../qms-framework/stakeholder-register.md) | PO / QMR | ☐ |
| 3 | QMS-Geltungsbereich | [REF-03](../qms-framework/qms-scope.md) | QMR | ☐ |
| 4 | Qualit\\u00e4tspolitik | [REF-04](../qms-framework/quality-policy.md) | Unit Lead | ☐ |
| 5 | RACI-Matrix | [REF-05](../qms-framework/raci-matrix.md) | QMR | ☐ |
| 6 | Risikoregister | [REF-06](../planning/risk-register.md) | QMR | ☐ |
| 7 | Qualit\\u00e4tsziele | [REF-07](../planning/quality-objectives.md) | QMR | ☐ |
| 8 | Kompetenzmatrix | [REF-08](../support/competency-matrix.md) | Team Leads | ☐ |
| 9 | Kommunikationsmatrix | [REF-09](../support/communication-matrix.md) | QMR | ☐ |
| 10 | Lieferantenbewertung | [REF-10](../operations/supplier-evaluation.md) | Tech Lead | ☐ |
| 11 | Internes Auditprogramm | [REF-11](../performance/internal-audit-program.md) | QMR | ☐ |
| 12 | Managementbewertung | [REF-12](../performance/management-review.md) | QMR | ☐ |
| 13 | CAPA-Protokoll | [REF-13](../improvement/capa-log.md) | QMR | ☐ |
| 14 | QMS-Prozesslandkarte | [Prozesslandkarte](process-map.md) | QMR | ☐ |

---

## Phase 2: Nachweissammlung (Wochen 1-2 \\u00b7 7.-20. Feb.)

| ISO-Abschnitt | Erforderliche Nachweise | Quelle | ☐ |
|:-------------:|-------------------------|--------|:-:|
| **4.1-4.2** | Kontextbewertungsprotokolle, Stakeholder-Feedback | Confluence | ☐ |
| **5.1-5.3** | Managementengagement, Qualit\\u00e4tspolitik angezeigt, RACI | E-Mail, Confluence | ☐ |
| **6.1-6.2** | Risikoregister-Reviews, Qualit\\u00e4tsziel-Messungen (4 Quartale) | REF-06, Grafana | ☐ |
| **7.1-7.5** | Schulungsnachweise, Ressourcenplanung, Dokumentenlenkung | SuccessFactors, Jira, Git | ☐ |
| **8.1-8.7** | Sprint-Aufzeichnungen, ADRs, PR-Verlauf, Testergebnisse | Jira, GitHub, CI/CD | ☐ |
| **9.1-9.3** | KPI-Dashboards, Auditberichte, Managementbewertung | Grafana, REF-11, REF-12 | ☐ |
| **10.2-10.3** | CAPA-Aufzeichnungen (3-5 Zyklen), Retrospektiven | REF-13, Jira | ☐ |

---

## Phase 3: Personalvorbereitung (Wochen 2-3 \\u00b7 14.-27. Feb.)

| Nr. | Aufgabe | Zielgruppe | Methode |
|-----|---------|------------|---------|
| 1 | ISO 9001-Grundlagen & QMS-\\u00dcberblick | Alle | Workshop (1 Std.) |
| 2 | Qualit\\u00e4tspolitik — kennen & erkl\\u00e4ren | Alle | All-Hands + Quiz |
| 3 | Qualit\\u00e4tsziele — eigene KPIs kennen | Alle | Teambesprechung |
| 4 | Umgang mit Auditorfragen | Sprecher | Workshop (1 Std.) |

---

## Rollenzuweisung am Audittag

| Rolle | Person | Verantwortung |
|-------|--------|---------------|
| **Begleiter/Lotse** | _[Name]_ | Begleitet Auditor, Logistik |
| **Sprecher Abschnitt 4-5** | _[Unit Lead]_ | Kontext, F\\u00fchrung, Politik |
| **Sprecher Abschnitt 6** | _[QMR]_ | Risiken, Ziele, Planung |
| **Sprecher Abschnitt 7-8** | _[Tech Lead / PO]_ | Ressourcen, Betrieb, Entwicklung |
| **Sprecher Abschnitt 9-10** | _[QMR]_ | Messung, Audit, Verbesserung |
| **Systemdemo** | _[DevOps]_ | Jira, Confluence, CI/CD, Grafana |
| **Protokollf\\u00fchrer** | _[Name]_ | Erfasst alle Fragen |

---

## Phase 4: Abschluss (Woche 4 \\u00b7 28. Feb.-5. M\\u00e4r.)

| Nr. | Aufgabe | Verantwortlich |
|-----|---------|----------------|
| 1 | Internes Voraudit | QMR |
| 2 | Voraudit-Feststellungen bearbeiten | Verantwortliche |
| 3 | Dokumente auf Aktualit\\u00e4t pr\\u00fcfen | QMR |
| 4 | KPI-Dashboards aktualisieren | DevOps |
| 5 | Konferenzraum vorbereiten | Begleiter |
| 6 | Alle Sprecher einweisen | QMR |
| 7 | Er\\u00f6ffnungspr\\u00e4sentation vorbereiten (10 Min.) | Unit Lead |

---

## Checkliste Audittag

### Vormittag
- [ ] Auditor begr\\u00fc\\u00dfen, Vorstellungsrunde
- [ ] 10-min \\u00dcbersicht durch Unit Lead
- [ ] Auditplan best\\u00e4tigen
- [ ] WLAN-Zugang, Raumlogistik

### W\\u00e4hrend des Audits
- [ ] Auditor begleiten
- [ ] Alle Fragen protokollieren
- [ ] Antworten kurz und nachweisbasiert
- [ ] Systeme f\\u00fcr Vorf\\u00fchrung bereithalten

### Nachmittag
- [ ] Abschlussbesprechung (alle Sprecher)
- [ ] Feststellungen anh\\u00f6ren — nicht widersprechen
- [ ] Auditor danken
- [ ] Sofortige interne Nachbesprechung
- [ ] CAPA-Eintr\\u00e4ge f\\u00fcr Feststellungen erstellen
""",
})

# ===== audit-catalogue.md =====
PAGES.append({
    'en': 'getting-started/audit-catalogue.md',
    'de': 'getting-started/audit-catalogue.de.md',
    'en_quick': """
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
""",
    'en_essential': """
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
""",
    'de_quick': """
> **Geltungsbereich:** DDD-Einheit — Werkzeuge f\\u00fcr AD/ADAS Datenengineering, Speicherung, Simulation und Reprocessing.

## ISO 9001 auf einen Blick (PDCA)

```mermaid
graph LR
    subgraph "Plan"
        C4["4 - Kontext"]
        C5["5 - F\\u00fchrung"]
        C6["6 - Planung"]
    end
    subgraph "Do"
        C7["7 - Unterst\\u00fctzung"]
        C8["8 - Betrieb"]
    end
    subgraph "Check"
        C9["9 - Bewertung"]
    end
    subgraph "Act"
        C10["10 - Verbesserung"]
    end
    C4 --> C5 --> C6 --> C7 --> C8 --> C9 --> C10
    C10 -->|Kontinuierliche Verbesserung| C4
    style C4 fill:#4A90D9,color:#fff
    style C5 fill:#4A90D9,color:#fff
    style C6 fill:#4A90D9,color:#fff
    style C7 fill:#7B68EE,color:#fff
    style C8 fill:#7B68EE,color:#fff
    style C9 fill:#E8A838,color:#fff
    style C10 fill:#D94A4A,color:#fff
```

---

## Wichtigste Fragen je Abschnitt

| Nr. | Wahrscheinliche Auditorfrage | Kernpunkte f\\u00fcr Ihre Antwort |
|-----|------------------------------|----------------------------------|
| **4.1** | Was macht Ihre Abteilung? | DDD: Datenengineering-, Simulations- und Reprocessing-Tools f\\u00fcr AD/ADAS-Ingenieure |
| **4.3** | Was ist der Geltungsbereich Ihres QMS? | Entwurf, Entwicklung, Bereitstellung & Wartung von Daten-/Simulationswerkzeugen. Physische Produkte ausgeschlossen. |
| **5.2** | K\\u00f6nnen Sie mir Ihre Qualit\\u00e4tspolitik zeigen? | Ausgedruckt bereithalten! Zuverl\\u00e4ssig, skalierbar, sicher; kontinuierliche Verbesserung; datengetrieben |
| **6.1** | Wie identifizieren und managen Sie Risiken? | Risikoregister, 5x5-Matrix, quartalsweise \\u00dcberpr\\u00fcfung, jedes Risiko hat Verantwortlichen. 2-3 Beispiele nennen |
| **6.2** | Was sind Ihre Qualit\\u00e4tsziele? | Verf\\u00fcgbarkeit >= 99,5%, MTTR < 4h, NPS >= 40, null Datenintegrit\\u00e4tsvorf\\u00e4lle |
| **7.2** | Wie stellen Sie Kompetenz sicher? | Kompetenzmatrix, strukturierte Einarbeitung (30-60-90), Schulungspl\\u00e4ne |
| **8.3** | Wie steuern Sie Design & Entwicklung? | SDLC: Anforderungen -> ADRs -> Implementierung -> Code Review (2 Pr\\u00fcfer) -> Test -> Staging -> Prod |
| **9.2** | F\\u00fchren Sie interne Audits durch? | Ja, Jahresprogramm, geschulte unabh\\u00e4ngige Auditoren, Ergebnisse in Managementbewertung |
| **10.2** | Wie behandeln Sie Nichtkonformit\\u00e4ten? | Eindämmen -> Ursache (5-Why) -> Korrektur -> Wirksamkeit pr\\u00fcfen (30/60/90 Tage) |

---

## Auditor-Tipps

1. **Ehrlich sein.** Niemals Nachweise erfinden
2. **Zeigen statt erz\\u00e4hlen.** Jira, Confluence, Grafana, Git offen haben
3. **Beim Thema bleiben.** Nur beantworten, was gefragt wird
4. **STAR-Methode:** Situation -> Aufgabe -> Aktion -> Resultat
5. **Ein Sprecher pro Thema.** Vorher abstimmen
""",
    'de_essential': """
> **Geltungsbereich:** DDD-Einheit — Werkzeuge f\\u00fcr AD/ADAS Datenengineering, Speicherung, Simulation und Reprocessing.

---

## Abschnitt 4: Kontext der Organisation

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 4.1.1 | **Was macht Ihre Abteilung?** | DDD-Einheit: Werkzeuge f\\u00fcr Datenengineering, Simulation, Reprocessing f\\u00fcr AD/ADAS-Ingenieure |
| 4.1.2 | **Welche Themen beeinflussen Ihr QMS?** | Extern: AD-Regulierung, Cloud-Kosten. Intern: schnelles Wachstum, technische Schulden. Ref: [Kontextanalyse](../qms-framework/context-analysis.md) |
| 4.2.1 | **Wer sind Ihre interessierten Parteien?** | AD/ADAS-Ingenieure, Management, Regulierungsbeh\\u00f6rden, Cloud-Anbieter, InfoSec. Ref: [Stakeholder-Register](../qms-framework/stakeholder-register.md) |
| 4.3.1 | **Was ist der QMS-Geltungsbereich?** | Entwurf, Entwicklung, Bereitstellung von Daten-/Simulationswerkzeugen. Ref: [QMS-Geltungsbereich](../qms-framework/qms-scope.md) |

## Abschnitt 5: F\\u00fchrung

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 5.1.1 | **Wie zeigt das Management Engagement?** | Quartalsweise Managementbewertung, Qualit\\u00e4tspolitik-Freigabe, Qualit\\u00e4tsbudget |
| 5.2.1 | **K\\u00f6nnen Sie Ihre Qualit\\u00e4tspolitik zeigen?** | Ausgedruckt! Ref: [Qualit\\u00e4tspolitik](../qms-framework/quality-policy.md) |
| 5.3.1 | **Wer ist f\\u00fcr das QMS verantwortlich?** | QMR [Name], berichtet an Unit Lead. Ref: [RACI-Matrix](../qms-framework/raci-matrix.md) |

## Abschnitt 6: Planung

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 6.1.1 | **Wie managen Sie Risiken?** | Risikoregister, 5x5-Matrix, quartalsweise Review, Verantwortlicher + Ma\\u00dfnahmen. Ref: [Risikoregister](../planning/risk-register.md) |
| 6.2.1 | **Was sind Ihre Qualit\\u00e4tsziele?** | Verf\\u00fcgbarkeit >= 99,5%, MTTR < 4h, NPS >= 40, null Datenintegrit\\u00e4tsvorf\\u00e4lle. Ref: [Qualit\\u00e4tsziele](../planning/quality-objectives.md) |

## Abschnitt 7: Unterst\\u00fctzung

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 7.2.1 | **Wie stellen Sie Kompetenz sicher?** | Kompetenzmatrix, Einarbeitung (30-60-90), Jahrespl\\u00e4ne. Ref: [Kompetenzmatrix](../support/competency-matrix.md) |
| 7.4.1 | **Wie managen Sie Kommunikation?** | Kommunikationsmatrix: was, wann, an wen, wie. Ref: [Kommunikationsmatrix](../support/communication-matrix.md) |
| 7.5.1 | **Wie lenken Sie Dokumente?** | Confluence + Versionskontrolle; Git + Branch Protection; Aufbewahrungsrichtlinie |

## Abschnitt 8: Betrieb

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 8.3.1 | **Wie planen Sie Design & Entwicklung?** | SDLC: Anforderungen -> ADRs -> Implementierung -> Code Review -> Test -> Staging -> Produktion |
| 8.4.1 | **Wie bewerten Sie Lieferanten?** | Bewertungsmatrix, kategoriebasierte Reviews. Ref: [Lieferantenbewertung](../operations/supplier-evaluation.md) |
| 8.7.1 | **Wie behandeln Sie fehlerhafte Ergebnisse?** | Bug-Klassifizierung, sofortige Reaktion bei Kritisch, Nachverfolgung in Jira |

## Abschnitt 9: Leistungsbewertung

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 9.1.1 | **Was messen Sie?** | Verf\\u00fcgbarkeit, Reaktionszeiten, Fehlerraten, Deploy-Frequenz, NPS, Testabdeckung |
| 9.2.1 | **F\\u00fchren Sie interne Audits durch?** | Ja, Jahresprogramm, unabh\\u00e4ngige geschulte Auditoren. Ref: [Internes Auditprogramm](../performance/internal-audit-program.md) |
| 9.3.1 | **Wie oft ist Managementbewertung?** | Quartalsweise + j\\u00e4hrlich umfassend. Ref: [Managementbewertung](../performance/management-review.md) |

## Abschnitt 10: Verbesserung

| Nr. | Typische Auditorfrage | Antworthinweise |
|-----|----------------------|-----------------|
| 10.2.1 | **Wie behandeln Sie Nichtkonformit\\u00e4ten?** | Eind\\u00e4mmen -> Ursache (5-Why) -> Korrektur -> Wirksamkeit pr\\u00fcfen -> Lessons Learned. Ref: [CAPA-Protokoll](../improvement/capa-log.md) |

---

## Auditor-Tipps

1. **Ehrlich sein.** Niemals Nachweise erfinden
2. **Zeigen statt erz\\u00e4hlen.** Systeme offen haben
3. **Beim Thema bleiben.** Nur beantworten, was gefragt wird
4. **STAR-Methode:** Situation -> Aufgabe -> Aktion -> Resultat
5. **Ein Sprecher pro Thema**
6. **\\"Wir sind auf dem Weg.\\"** Auditoren respektieren ehrliche Verbesserung
""",
})

# ===== process-map.md =====
PAGES.append({
    'en': 'getting-started/process-map.md',
    'de': 'getting-started/process-map.de.md',
    'en_quick': """
## Process Landscape Overview

Our QMS processes are organized into three tiers: **Management**, **Core**, and **Support**.

```mermaid
graph TB
    subgraph "MANAGEMENT PROCESSES"
        direction LR
        M1["Strategic Planning"] --- M2["Management Review"] --- M3["Continual Improvement"] --- M4["Risk Management"]
    end
    subgraph "CORE PROCESSES (Value Chain)"
        direction LR
        C1["Need ID"] --> C2["Requirements"] --> C3["Design"] --> C4["Development"] --> C5["V&V"] --> C6["Release"] --> C7["Operations"]
        C7 -->|Feedback| C1
    end
    subgraph "SUPPORT PROCESSES"
        direction LR
        S1["People"] --- S2["Infrastructure"] --- S3["Doc Control"] --- S4["Suppliers"] --- S5["Audit"] --- S6["Monitoring"]
    end
    M1 & M2 & M3 & M4 -.->|Govern| C1
    S1 & S2 & S3 & S4 & S5 & S6 -.->|Enable| C4
    style M1 fill:#1a5276,color:#fff
    style M2 fill:#1a5276,color:#fff
    style M3 fill:#1a5276,color:#fff
    style M4 fill:#1a5276,color:#fff
    style C1 fill:#196f3d,color:#fff
    style C2 fill:#196f3d,color:#fff
    style C3 fill:#196f3d,color:#fff
    style C4 fill:#196f3d,color:#fff
    style C5 fill:#196f3d,color:#fff
    style C6 fill:#196f3d,color:#fff
    style C7 fill:#196f3d,color:#fff
    style S1 fill:#7d3c98,color:#fff
    style S2 fill:#7d3c98,color:#fff
    style S3 fill:#7d3c98,color:#fff
    style S4 fill:#7d3c98,color:#fff
    style S5 fill:#7d3c98,color:#fff
    style S6 fill:#7d3c98,color:#fff
```

---

## Process Ownership

| Process | Owner | ISO 9001 Clause |
|---------|-------|-----------------|
| Strategic Planning | Unit Lead | 5.1, 6.2 |
| Management Review | Unit Lead + QMR | 9.3 |
| Risk Management | QMR | 6.1 |
| Requirements | Product Owner | 8.2, 8.3 |
| Development (Scrum) | Scrum Master + Team | 8.3, 8.5 |
| Verification & Validation | QA Lead | 8.3, 8.7 |
| Release & Deployment | DevOps Lead | 8.5 |
| Operations & Support | SRE/Ops Lead | 8.5, 9.1 |
| Internal Audit | QMR | 9.2 |
""",
    'en_essential': """
## Process Landscape Overview

```mermaid
graph TB
    subgraph "MANAGEMENT PROCESSES"
        direction LR
        M1["Strategic Planning<br/>& OKR Setting"]
        M2["Management<br/>Review"]
        M3["Continual<br/>Improvement"]
        M4["Risk & Opportunity<br/>Management"]
        M1 --- M2 --- M3 --- M4
    end
    subgraph "CORE PROCESSES (Value Chain)"
        direction LR
        C1["Stakeholder Need<br/>Identification"] --> C2["Requirements<br/>Engineering"]
        C2 --> C3["Architecture<br/>& Design"]
        C3 --> C4["Agile Development<br/>(Scrum)"]
        C4 --> C5["Verification<br/>& Validation"]
        C5 --> C6["Release &<br/>Deployment"]
        C6 --> C7["Operations &<br/>Support"]
        C7 -->|Feedback Loop| C1
    end
    subgraph "SUPPORT PROCESSES"
        direction LR
        S1["People &<br/>Competence"]
        S2["Infrastructure<br/>& Cloud"]
        S3["Document &<br/>Config Control"]
        S4["Supplier &<br/>Vendor Mgmt"]
        S5["Internal<br/>Audit"]
        S6["Monitoring &<br/>Measurement"]
        S1 --- S2 --- S3 --- S4 --- S5 --- S6
    end
    M1 & M2 & M3 & M4 -.->|Govern & Direct| C1
    S1 & S2 & S3 & S4 & S5 & S6 -.->|Enable| C4
    style M1 fill:#1a5276,color:#fff
    style M2 fill:#1a5276,color:#fff
    style M3 fill:#1a5276,color:#fff
    style M4 fill:#1a5276,color:#fff
    style C1 fill:#196f3d,color:#fff
    style C2 fill:#196f3d,color:#fff
    style C3 fill:#196f3d,color:#fff
    style C4 fill:#196f3d,color:#fff
    style C5 fill:#196f3d,color:#fff
    style C6 fill:#196f3d,color:#fff
    style C7 fill:#196f3d,color:#fff
    style S1 fill:#7d3c98,color:#fff
    style S2 fill:#7d3c98,color:#fff
    style S3 fill:#7d3c98,color:#fff
    style S4 fill:#7d3c98,color:#fff
    style S5 fill:#7d3c98,color:#fff
    style S6 fill:#7d3c98,color:#fff
```

---

## Core Process Details

| Process | Owner | Inputs | Key Outputs | KPIs | Clause |
|---------|-------|--------|-------------|------|:------:|
| Stakeholder Needs | PO | Feedback, surveys | Backlog, roadmap | Request response time | 4.2, 8.2 |
| Requirements | PO + Tech Lead | Backlog, constraints | User stories, specs | Rejection rate | 8.2, 8.3 |
| Architecture & Design | Tech Lead | Requirements, NFRs | ADRs, API specs | ADR coverage | 8.3 |
| Development (Scrum) | SM + Team | Sprint backlog | Tested code, PRs | Velocity, review time | 8.3, 8.5 |
| Verification & Validation | QA | Code, criteria | Test reports, coverage | Coverage >= 80% | 8.3, 8.7 |
| Release & Deployment | DevOps | Tested artifacts | Production release | Deploy freq, failure rate | 8.5 |
| Operations & Support | SRE | Production systems | Incident reports, SLAs | Uptime >= 99.5%, MTTR | 8.5, 9.1 |

### Sprint Cycle

```mermaid
graph LR
    subgraph "Sprint Cycle (2 weeks)"
        A["Sprint<br/>Planning"] --> B["Daily<br/>Standup"]
        B --> C["Development<br/>& Code Review"]
        C --> D["Continuous<br/>Integration"]
        D --> E["Sprint<br/>Review / Demo"]
        E --> F["Sprint<br/>Retrospective"]
        F -->|Next Sprint| A
    end
    style A fill:#1a5276,color:#fff
    style B fill:#2471a3,color:#fff
    style C fill:#2e86c1,color:#fff
    style D fill:#3498db,color:#fff
    style E fill:#196f3d,color:#fff
    style F fill:#e67e22,color:#fff
```

---

## Process Ownership Summary

| Process | Owner | ISO 9001 Clause |
|---------|-------|:---------------:|
| Strategic Planning | Unit Lead | 5.1, 6.2 |
| Management Review | Unit Lead + QMR | 9.3 |
| Risk Management | QMR | 6.1 |
| Continual Improvement | QMR | 10.1, 10.3 |
| Need Identification | Product Owner | 4.2, 8.2 |
| Requirements Eng. | PO + Tech Lead | 8.2, 8.3 |
| Architecture & Design | Tech Lead | 8.3 |
| Development | SM + Team | 8.3, 8.5 |
| V&V | QA Lead | 8.3, 8.7 |
| Release & Deployment | DevOps Lead | 8.5 |
| Operations | SRE/Ops Lead | 8.5, 9.1 |
| People & Competence | Team Leads | 7.1, 7.2 |
| Document Control | QMR | 7.5 |
| Supplier Management | Tech Lead | 8.4 |
| Internal Audit | QMR | 9.2 |
""",
    'de_quick': """
## Prozesslandschaft

Unsere QMS-Prozesse sind in drei Ebenen gegliedert: **Management**, **Kern** und **Unterst\\u00fctzung**.

```mermaid
graph TB
    subgraph "MANAGEMENTPROZESSE"
        direction LR
        M1["Strategische Planung"] --- M2["Managementbewertung"] --- M3["Verbesserung"] --- M4["Risikomanagement"]
    end
    subgraph "KERNPROZESSE (Wertsch\\u00f6pfung)"
        direction LR
        C1["Bedarf"] --> C2["Anforderungen"] --> C3["Design"] --> C4["Entwicklung"] --> C5["V&V"] --> C6["Release"] --> C7["Betrieb"]
        C7 -->|Feedback| C1
    end
    subgraph "UNTERST\\u00dcTZUNGSPROZESSE"
        direction LR
        S1["Personal"] --- S2["Infrastruktur"] --- S3["Dok.-Lenkung"] --- S4["Lieferanten"] --- S5["Audit"] --- S6["\\u00dcberwachung"]
    end
    M1 & M2 & M3 & M4 -.->|Steuern| C1
    S1 & S2 & S3 & S4 & S5 & S6 -.->|Erm\\u00f6glichen| C4
    style M1 fill:#1a5276,color:#fff
    style M2 fill:#1a5276,color:#fff
    style M3 fill:#1a5276,color:#fff
    style M4 fill:#1a5276,color:#fff
    style C1 fill:#196f3d,color:#fff
    style C2 fill:#196f3d,color:#fff
    style C3 fill:#196f3d,color:#fff
    style C4 fill:#196f3d,color:#fff
    style C5 fill:#196f3d,color:#fff
    style C6 fill:#196f3d,color:#fff
    style C7 fill:#196f3d,color:#fff
    style S1 fill:#7d3c98,color:#fff
    style S2 fill:#7d3c98,color:#fff
    style S3 fill:#7d3c98,color:#fff
    style S4 fill:#7d3c98,color:#fff
    style S5 fill:#7d3c98,color:#fff
    style S6 fill:#7d3c98,color:#fff
```

---

## Prozessverantwortung

| Prozess | Verantwortlich | ISO-Abschnitt |
|---------|----------------|:-------------:|
| Strategische Planung | Unit Lead | 5.1, 6.2 |
| Managementbewertung | Unit Lead + QMR | 9.3 |
| Risikomanagement | QMR | 6.1 |
| Anforderungen | Product Owner | 8.2, 8.3 |
| Entwicklung (Scrum) | Scrum Master + Team | 8.3, 8.5 |
| V&V | QA Lead | 8.3, 8.7 |
| Release & Deployment | DevOps Lead | 8.5 |
| Betrieb & Support | SRE/Ops Lead | 8.5, 9.1 |
| Internes Audit | QMR | 9.2 |
""",
    'de_essential': """
## Prozesslandschaft

```mermaid
graph TB
    subgraph "MANAGEMENTPROZESSE"
        direction LR
        M1["Strategische<br/>Planung & OKRs"] --- M2["Management-<br/>bewertung"] --- M3["Kontinuierliche<br/>Verbesserung"] --- M4["Risiko-<br/>management"]
    end
    subgraph "KERNPROZESSE (Wertsch\\u00f6pfungskette)"
        direction LR
        C1["Bedarfs-<br/>ermittlung"] --> C2["Anforderungs-<br/>engineering"]
        C2 --> C3["Architektur<br/>& Design"]
        C3 --> C4["Agile Entwicklung<br/>(Scrum)"]
        C4 --> C5["Verifizierung<br/>& Validierung"]
        C5 --> C6["Release &<br/>Deployment"]
        C6 --> C7["Betrieb &<br/>Support"]
        C7 -->|Feedback| C1
    end
    subgraph "UNTERST\\u00dcTZUNGSPROZESSE"
        direction LR
        S1["Personal &<br/>Kompetenz"] --- S2["Infrastruktur<br/>& Cloud"] --- S3["Dokumenten-<br/>lenkung"] --- S4["Lieferanten-<br/>mgmt"] --- S5["Internes<br/>Audit"] --- S6["\\u00dcberwachung"]
    end
    M1 & M2 & M3 & M4 -.->|Steuern & Lenken| C1
    S1 & S2 & S3 & S4 & S5 & S6 -.->|Erm\\u00f6glichen| C4
    style M1 fill:#1a5276,color:#fff
    style M2 fill:#1a5276,color:#fff
    style M3 fill:#1a5276,color:#fff
    style M4 fill:#1a5276,color:#fff
    style C1 fill:#196f3d,color:#fff
    style C2 fill:#196f3d,color:#fff
    style C3 fill:#196f3d,color:#fff
    style C4 fill:#196f3d,color:#fff
    style C5 fill:#196f3d,color:#fff
    style C6 fill:#196f3d,color:#fff
    style C7 fill:#196f3d,color:#fff
    style S1 fill:#7d3c98,color:#fff
    style S2 fill:#7d3c98,color:#fff
    style S3 fill:#7d3c98,color:#fff
    style S4 fill:#7d3c98,color:#fff
    style S5 fill:#7d3c98,color:#fff
    style S6 fill:#7d3c98,color:#fff
```

---

## Kernprozesse im Detail

| Prozess | Verantwortlich | Eingaben | Ergebnisse | KPIs | Abschnitt |
|---------|----------------|----------|------------|------|:---------:|
| Bedarfsermittlung | PO | Feedback, Umfragen | Backlog, Roadmap | Reaktionszeit | 4.2, 8.2 |
| Anforderungen | PO + Tech Lead | Backlog | User Stories, Specs | Ablehnungsrate | 8.2, 8.3 |
| Architektur & Design | Tech Lead | Anforderungen | ADRs, API-Specs | ADR-Abdeckung | 8.3 |
| Entwicklung (Scrum) | SM + Team | Sprint Backlog | Getesteter Code | Velocity | 8.3, 8.5 |
| V&V | QA | Code, Kriterien | Testberichte | Abdeckung >= 80% | 8.3, 8.7 |
| Release | DevOps | Getestete Artefakte | Produktionsrelease | Deploy-Frequenz | 8.5 |
| Betrieb | SRE | Produktivsysteme | Incident Reports | Verf\\u00fcgbarkeit >= 99,5% | 8.5, 9.1 |

---

## Prozessverantwortung

| Prozess | Verantwortlich | ISO-Abschnitt |
|---------|----------------|:-------------:|
| Strategische Planung | Unit Lead | 5.1, 6.2 |
| Managementbewertung | Unit Lead + QMR | 9.3 |
| Risikomanagement | QMR | 6.1 |
| Anforderungen | Product Owner | 8.2, 8.3 |
| Entwicklung | SM + Team | 8.3, 8.5 |
| V&V | QA Lead | 8.3, 8.7 |
| Release & Deployment | DevOps Lead | 8.5 |
| Betrieb | SRE/Ops Lead | 8.5, 9.1 |
| Dokumentenlenkung | QMR | 7.5 |
| Lieferantenmanagement | Tech Lead | 8.4 |
| Internes Audit | QMR | 9.2 |
""",
})

# ===== Reference Documents =====
# For reference docs, Quick is a brief summary, Essential is key content

# --- context-analysis.md ---
PAGES.append({
    'en': 'qms-framework/context-analysis.md',
    'de': 'qms-framework/context-analysis.de.md',
    'en_quick': """
**ISO 9001 Clause 4.1** | **Owner:** Unit Lead

## Key Takeaways

- **Strengths:** Deep AD/ADAS expertise, strong DevOps culture, cloud-native architecture
- **Weaknesses:** Rapid growth causing knowledge silos, technical debt, limited formal QMS docs
- **Opportunities:** Growing AD market, data-driven development trend, cloud innovation
- **Threats:** Evolving regulations (EU AI Act), cloud cost inflation, talent competition

> If asked: "We conduct quarterly context reviews as part of management review. External issues tracked via regulatory watch; internal issues surface through retrospectives and team health checks."
""",
    'en_essential': """
**ISO 9001 Clause 4.1** | **Owner:** Unit Lead

## SWOT Analysis

### Strengths

| # | Strength | Impact on QMS |
|---|----------|---------------|
| S1 | Deep AD/ADAS data pipeline expertise | High-quality, fit-for-purpose tooling |
| S2 | Strong Agile/DevOps culture with CI/CD | Rapid, reliable delivery |
| S3 | Direct access to real-world driving data | Realistic validation and testing |
| S4 | Cloud-native architecture (IaC) | Reproducibility, auditability, scalability |
| S5 | Embedded in BMW Group ecosystem | Access to shared platforms and standards |

### Weaknesses

| # | Weakness | Mitigation |
|---|----------|------------|
| W1 | Rapid growth causing knowledge silos | Structured onboarding, documentation, pairing |
| W2 | Technical debt in legacy components | Dedicated tech debt sprints, refactoring OKRs |
| W3 | Limited formal QMS documentation | This initiative — establishing QMS docs |
| W4 | Key person dependencies | Cross-training, runbooks |

### Opportunities

| # | Opportunity | Potential Benefit |
|---|-------------|-------------------|
| O1 | Growing AD/ADAS market | Increased demand for our tooling |
| O2 | Industry shift to data-driven development | Strategic enabler positioning |
| O3 | Cloud provider innovation | Better performance, lower costs |

### Threats

| # | Threat | Mitigation |
|---|--------|------------|
| T1 | Evolving regulations (EU AI Act, UN R157) | Regulatory watch, proactive compliance |
| T2 | Cloud cost inflation | FinOps practices, cost optimization |
| T3 | Cybersecurity threats | Security hardening, pen testing |
| T4 | Talent competition in AD/ML space | Competitive compensation, learning culture |

> Monitoring: quarterly context reviews in management review cycle.
""",
    'de_quick': """
**ISO 9001 Abschnitt 4.1** | **Verantwortlich:** Unit Lead

## Kernergebnisse

- **St\\u00e4rken:** Tiefe AD/ADAS-Expertise, starke DevOps-Kultur, Cloud-native Architektur
- **Schw\\u00e4chen:** Schnelles Wachstum verursacht Wissenssilos, technische Schulden, wenig formale QMS-Doku
- **Chancen:** Wachsender AD-Markt, datengetriebene Entwicklung, Cloud-Innovation
- **Risiken:** Evolvierende Regulierung (EU AI Act), Cloud-Kosten, Talentwettbewerb

> Antworthinweis: \\"Wir f\\u00fchren quartalsweise Kontextbewertungen im Rahmen der Managementbewertung durch.\\"
""",
    'de_essential': """
**ISO 9001 Abschnitt 4.1** | **Verantwortlich:** Unit Lead

## SWOT-Analyse

### St\\u00e4rken

| Nr. | St\\u00e4rke | Auswirkung auf QMS |
|-----|----------|-------------------|
| S1 | Tiefe AD/ADAS-Datenpipeline-Expertise | Hochwertige, zweckm\\u00e4\\u00dfige Werkzeuge |
| S2 | Starke Agile/DevOps-Kultur mit CI/CD | Schnelle, zuverl\\u00e4ssige Lieferung |
| S3 | Direkter Zugang zu realen Fahrdaten | Realistische Validierung und Tests |
| S4 | Cloud-native Architektur (IaC) | Reproduzierbarkeit, Auditierbarkeit |

### Schw\\u00e4chen

| Nr. | Schw\\u00e4che | Gegenma\\u00dfnahme |
|-----|----------|----------------|
| W1 | Schnelles Wachstum, Wissenssilos | Strukturierte Einarbeitung, Dokumentation |
| W2 | Technische Schulden | Dedizierte Tech-Debt-Sprints |
| W3 | Begrenzte formale QMS-Dokumentation | Diese Initiative |

### Chancen

| Nr. | Chance | Nutzen |
|-----|--------|--------|
| O1 | Wachsender AD/ADAS-Markt | Steigende Nachfrage nach unseren Werkzeugen |
| O2 | Branchentrend datengetriebene Entwicklung | Strategische Positionierung |

### Risiken

| Nr. | Risiko | Gegenma\\u00dfnahme |
|-----|--------|----------------|
| T1 | Regulierung (EU AI Act) | Regulierungsmonitoring |
| T2 | Cloud-Kostenanstieg | FinOps-Praktiken |
| T3 | Cybersicherheitsbedrohungen | Security-H\\u00e4rtung |
| T4 | Talentwettbewerb | Attraktive Arbeitsbedingungen |
""",
})

# --- stakeholder-register.md ---
PAGES.append({
    'en': 'qms-framework/stakeholder-register.md',
    'de': 'qms-framework/stakeholder-register.de.md',
    'en_quick': """
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
""",
    'en_essential': """
**ISO 9001 Clause 4.2** | **Owner:** PO / QMR

## Stakeholder Register

| # | Stakeholder | Needs & Expectations | How We Address | Priority |
|---|-------------|---------------------|----------------|:--------:|
| 1 | AD/ADAS SW Engineers | Reliable, fast tools; responsive support | SLAs, user docs, feedback sessions | High |
| 2 | AD Function Owners | Compliant validation tools (ISO 26262) | Tool qualification evidence | High |
| 3 | Unit Management | Quality delivery, strategic alignment | OKRs, KPI dashboards | High |
| 4 | BMW Group Management | AD program success, cost efficiency | Strategic roadmap alignment | High |
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
    BMW Group Mgmt: [0.5, 0.95]
    InfoSec Team: [0.6, 0.7]
    Cloud Providers: [0.4, 0.3]
```
""",
    'de_quick': """
**ISO 9001 Abschnitt 4.2** | **Verantwortlich:** PO / QMR

## Wichtigste Stakeholder

| Stakeholder | Bed\\u00fcrfnisse | Wie wir darauf eingehen |
|-------------|------------|------------------------|
| **AD/ADAS-Ingenieure** | Zuverl\\u00e4ssige, schnelle Werkzeuge | SLAs, Dokumentation, Support |
| **AD-Funktionsverantwortliche** | Konforme Validierungswerkzeuge | Werkzeugqualifizierungsnachweise |
| **Unit-Management** | Effiziente Lieferung | OKRs, KPI-Dashboards |
| **InfoSec-Team** | Einhaltung der Sicherheitsrichtlinien | Sicherheitsbewertungen |
| **Datenschutzbeauftragter** | DSGVO-Konformit\\u00e4t | DSFAs, Anonymisierung |
""",
    'de_essential': """
**ISO 9001 Abschnitt 4.2** | **Verantwortlich:** PO / QMR

## Stakeholder-Register

| Nr. | Stakeholder | Bed\\u00fcrfnisse | Wie wir darauf eingehen | Priorit\\u00e4t |
|-----|-------------|------------|------------------------|:---------:|
| 1 | AD/ADAS-Ingenieure | Zuverl\\u00e4ssige Werkzeuge, reaktionsf\\u00e4higer Support | SLAs, Doku, Feedback-Sitzungen | Hoch |
| 2 | AD-Funktionsverantwortliche | Konforme Validierung (ISO 26262) | Werkzeugqualifizierung | Hoch |
| 3 | Unit-Management | Qualit\\u00e4tslieferung, strategische Ausrichtung | OKRs, KPI-Dashboards | Hoch |
| 4 | BMW-Konzernmanagement | AD-Programmerfolg, Kosteneffizienz | Strategische Roadmap | Hoch |
| 5 | InfoSec-Team | Sicherheitsrichtlinien-Konformit\\u00e4t | Sicherheitsbewertungen | Hoch |
| 6 | Datenschutzbeauftragter | DSGVO-Konformit\\u00e4t | DSFAs, Anonymisierung | Hoch |
| 7 | Cloud-Anbieter | Vorhersehbarer Verbrauch | Service-Reviews | Mittel |
| 8 | Neue Teammitglieder | Klare Einarbeitung | 30-60-90-Tage-Plan | Mittel |
""",
})

# --- qms-scope.md ---
PAGES.append({
    'en': 'qms-framework/qms-scope.md',
    'de': 'qms-framework/qms-scope.de.md',
    'en_quick': """
**ISO 9001 Clause 4.3** | **Owner:** QMR

## Scope Statement

> Design, development, deployment, operation, and maintenance of **data engineering tools**, **simulation environments**, **data storage solutions**, **reprocessing pipelines**, and **CI/CD toolchains** for AD/ADAS software validation.

## Exclusions

| Excluded | Justification |
|----------|---------------|
| Physical goods production (8.5.1) | Software tools and cloud services only |
| Post-delivery for physical products (8.5.5) | Digital services; operations & support covers post-delivery |
| Metrological traceability (7.1.5.2) | No physical measurements |
""",
    'en_essential': """
**ISO 9001 Clause 4.3** | **Owner:** QMR | **Approved by:** Unit Lead

## Scope Statement

> The QMS covers the **design, development, deployment, operation, and maintenance** of:
>
> - Data engineering tools for driving data ingestion, processing, and transformation
> - Data storage solutions for large-scale driving datasets (petabyte-scale)
> - Simulation environments (Simulation-as-a-Service) for AD/ADAS validation
> - Reprocessing pipelines for large-scale batch processing
> - CI/CD toolchains and developer productivity tools
> - Data cataloguing and discovery platforms

**Customers:** AD/ADAS software engineers and function owners within BMW Group.

## Products and Services In Scope

| # | Product / Service | Description |
|---|-------------------|-------------|
| 1 | Data Ingestion Platform | Collecting and processing driving data from vehicle fleet |
| 2 | Data Lake / Storage | Scalable storage with metadata cataloguing |
| 3 | Simulation-as-a-Service | Cloud-based simulation for AD/ADAS validation |
| 4 | Reprocessing Pipeline | Large-scale batch reprocessing of recorded data |
| 5 | Developer Toolchain | CI/CD, build tools, productivity tools |
| 6 | Data Catalogue | Discovery and metadata management |

## Exclusions

| Clause | Excluded | Justification |
|--------|----------|---------------|
| 8.5.1 (partial) | Physical goods production | Software and cloud services only |
| 8.5.5 (partial) | Post-delivery for physical products | Digital; post-delivery covered by ops |
| 7.1.5.2 | Metrological traceability | No physical measurements |

## Applicable Standards

| Standard | Relevance |
|----------|-----------|
| ISO 9001:2015 | Primary QMS standard |
| ISO 26262 Part 8 | Tool qualification for safety validation |
| ASPICE | Development process alignment |
| GDPR / BDSG | Personal data in driving recordings |
| ISO 21434 | Automotive cybersecurity |
""",
    'de_quick': """
**ISO 9001 Abschnitt 4.3** | **Verantwortlich:** QMR

## Geltungsbereich

> Entwurf, Entwicklung, Bereitstellung, Betrieb und Wartung von **Datenengineering-Werkzeugen**, **Simulationsumgebungen**, **Datenspeicherl\\u00f6sungen**, **Reprocessing-Pipelines** und **CI/CD-Toolchains** f\\u00fcr die AD/ADAS-Softwarevalidierung.

## Ausschl\\u00fcsse

| Ausgeschlossen | Begr\\u00fcndung |
|----------------|---------------|
| Physische Produktion (8.5.1) | Nur Software und Cloud-Dienste |
| Nachlieferung physischer Produkte (8.5.5) | Digitale Dienste |
| Metrologische R\\u00fcckverfolgbarkeit (7.1.5.2) | Keine physischen Messungen |
""",
    'de_essential': """
**ISO 9001 Abschnitt 4.3** | **Verantwortlich:** QMR | **Genehmigt durch:** Unit Lead

## Geltungsbereich

> Das QMS umfasst **Entwurf, Entwicklung, Bereitstellung, Betrieb und Wartung** von:
>
> - Datenengineering-Werkzeuge f\\u00fcr Fahrdaten-Ingestion und -Verarbeitung
> - Datenspeicherl\\u00f6sungen im Petabyte-Ma\\u00dfstab
> - Simulationsumgebungen (Simulation-as-a-Service)
> - Reprocessing-Pipelines f\\u00fcr Batch-Verarbeitung
> - CI/CD-Toolchains und Entwicklerproduktivit\\u00e4tswerkzeuge
> - Datenkatalog- und Discovery-Plattformen

## Produkte und Dienste

| Nr. | Produkt/Dienst | Beschreibung |
|-----|----------------|--------------|
| 1 | Daten-Ingestion-Plattform | Sammlung und Verarbeitung von Fahrdaten |
| 2 | Data Lake/Speicherplattform | Skalierbare Speicherung mit Metadaten |
| 3 | Simulation-as-a-Service | Cloud-basierte AD/ADAS-Simulation |
| 4 | Reprocessing-Pipeline | Gro\\u00dffl\\u00e4chige Batch-Verarbeitung |
| 5 | Entwickler-Toolchain | CI/CD, Build-Tools |
| 6 | Datenkatalog | Metadatenmanagement |

## Ausschl\\u00fcsse

| Abschnitt | Ausgeschlossen | Begr\\u00fcndung |
|-----------|----------------|---------------|
| 8.5.1 | Physische Produktion | Nur Software und Cloud-Dienste |
| 8.5.5 | Nachlieferung physischer Produkte | Digital; Betrieb deckt Nachlieferung ab |
| 7.1.5.2 | Metrologische R\\u00fcckverfolgbarkeit | Keine physischen Messungen |
""",
})

# --- quality-policy.md ---
PAGES.append({
    'en': 'qms-framework/quality-policy.md',
    'de': 'qms-framework/quality-policy.de.md',
    'en_quick': """
**ISO 9001 Clause 5.2** | **Approved by:** Unit Lead

## Quality Policy — Know This by Heart

We commit to providing **reliable, scalable, and secure tooling** for AD/ADAS engineers.

**Our 7 Commitments:**

1. **Customer Focus** — tools that meet evolving needs
2. **Reliability & Data Integrity** — high availability, zero data corruption
3. **Compliance** — ISO 9001, ISO 26262, GDPR, BMW policies
4. **Data-Driven Decisions** — metrics and evidence guide us
5. **Continual Improvement** — retrospectives, measurement, learning
6. **Security & Privacy** — protect driving data and infrastructure
7. **People & Competence** — invest in team growth

> Display: Confluence landing page, team area, onboarding materials, management review agenda.
""",
    'en_essential': """
**ISO 9001 Clause 5.2** | **Approved by:** Unit Lead — [Name, Date]

## Quality Policy Statement

The Data Driven Development (DDD) unit is committed to providing **reliable, scalable, and secure tooling** that enables our Autonomous Driving and ADAS engineers to validate and develop driving functions with confidence.

### We commit to:

1. **Customer Focus** — Delivering tools that meet the evolving needs of our AD/ADAS engineering teams, measured through regular feedback and satisfaction tracking.

2. **Reliability & Data Integrity** — Ensuring our data pipelines, simulation environments, and reprocessing infrastructure operate with high availability and zero tolerance for data corruption.

3. **Compliance** — Meeting all applicable requirements including ISO 9001, ISO 26262 tool qualification, GDPR, cybersecurity standards, and BMW Group policies.

4. **Data-Driven Decision Making** — Using metrics, monitoring, and evidence to guide our decisions.

5. **Continual Improvement** — Systematically improving our processes, tools, and competencies through retrospectives, measurement, and learning from incidents.

6. **Security & Privacy** — Protecting the integrity, confidentiality, and availability of driving data and our infrastructure.

7. **People & Competence** — Investing in the growth and well-being of our team members.

### This policy is:
- Communicated to all team members and available to interested parties
- Reviewed annually for continuing suitability
- The framework for setting and reviewing quality objectives

> **Display locations:** Confluence landing page, team area, onboarding materials, management review agenda.
""",
    'de_quick': """
**ISO 9001 Abschnitt 5.2** | **Genehmigt durch:** Unit Lead

## Qualit\\u00e4tspolitik — Auswendig kennen

Wir verpflichten uns zu **zuverl\\u00e4ssigen, skalierbaren und sicheren Werkzeugen** f\\u00fcr AD/ADAS-Ingenieure.

**Unsere 7 Verpflichtungen:**

1. **Kundenfokus** — Werkzeuge, die Bed\\u00fcrfnisse erf\\u00fcllen
2. **Zuverl\\u00e4ssigkeit & Datenintegrit\\u00e4t** — Hohe Verf\\u00fcgbarkeit, null Datenkorruption
3. **Compliance** — ISO 9001, ISO 26262, DSGVO, BMW-Richtlinien
4. **Datengetriebene Entscheidungen** — Metriken und Nachweise leiten uns
5. **Kontinuierliche Verbesserung** — Retrospektiven, Messung, Lernen
6. **Sicherheit & Datenschutz** — Fahrdaten und Infrastruktur sch\\u00fctzen
7. **Menschen & Kompetenz** — In Teamwachstum investieren
""",
    'de_essential': """
**ISO 9001 Abschnitt 5.2** | **Genehmigt durch:** Unit Lead — [Name, Datum]

## Qualit\\u00e4tspolitik

Die DDD-Abteilung verpflichtet sich zur Bereitstellung **zuverl\\u00e4ssiger, skalierbarer und sicherer Werkzeuge**, die unseren AD/ADAS-Ingenieuren die Validierung und Entwicklung von Fahrfunktionen mit Zuversicht erm\\u00f6glichen.

### Wir verpflichten uns zu:

1. **Kundenfokus** — Werkzeuge, die den sich entwickelnden Bed\\u00fcrfnissen unserer Teams entsprechen
2. **Zuverl\\u00e4ssigkeit & Datenintegrit\\u00e4t** — Hohe Verf\\u00fcgbarkeit und null Toleranz f\\u00fcr Datenkorruption
3. **Compliance** — ISO 9001, ISO 26262, DSGVO, Cybersicherheit, BMW-Richtlinien
4. **Datengetriebene Entscheidungen** — Metriken und Nachweise leiten unsere Entscheidungen
5. **Kontinuierliche Verbesserung** — Systematische Verbesserung durch Retrospektiven und Lernen
6. **Sicherheit & Datenschutz** — Schutz von Fahrdaten und Infrastruktur
7. **Menschen & Kompetenz** — Investition in Wachstum und Wohlbefinden des Teams

### Diese Politik wird:
- Allen Teammitgliedern kommuniziert
- J\\u00e4hrlich auf Eignung \\u00fcberpr\\u00fcft
- Als Rahmen f\\u00fcr Qualit\\u00e4tsziele genutzt
""",
})

# --- raci-matrix.md ---
PAGES.append({
    'en': 'qms-framework/raci-matrix.md',
    'de': 'qms-framework/raci-matrix.de.md',
    'en_quick': """
**ISO 9001 Clause 5.3** | **Owner:** QMR

**R** = Responsible (does work) | **A** = Accountable (one per activity) | **C** = Consulted | **I** = Informed

## Key Roles

| Role | QMS Responsibility |
|------|-------------------|
| **Unit Lead** | Overall QMS accountability, approves policy & objectives, chairs management review |
| **QMR** | Day-to-day QMS coordination, document control, audit planning, CAPA tracking |
| **Team Lead** | Team-level quality practices, competence management |
| **Scrum Master** | Agile ceremonies, retrospective improvements |
| **Product Owner** | Requirements, customer voice, acceptance |
| **Quality Champion** | Per-team QMS awareness, supports QMR |
""",
    'en_essential': """
**ISO 9001 Clause 5.3** | **Owner:** QMR

**R** = Responsible | **A** = Accountable | **C** = Consulted | **I** = Informed

## QMS Management Activities

| Activity | Unit Lead | QMR | Team Lead | PO | Developer |
|----------|:---------:|:---:|:---------:|:--:|:---------:|
| Quality policy approval | **A** | R | I | I | I |
| Management review | **A** | R | C | C | I |
| Internal audit planning | C | **A**/R | C | | |
| Risk register maintenance | **A** | R | C | C | |
| Quality objectives | **A** | R | C | C | |
| CAPA management | I | **A**/R | R | | R |
| Document control | I | **A**/R | C | | |

## Core Process Activities

| Activity | Unit Lead | Team Lead | SM | PO | Developer | QA |
|----------|:---------:|:---------:|:--:|:--:|:---------:|:--:|
| Requirements engineering | I | C | C | **A**/R | C | |
| Architecture & design | I | **A** | | C | R | C |
| Development | | C | | | **A**/R | |
| Testing & validation | | C | | C | R | **A**/R |
| Release & deployment | I | **A** | | I | C | C |

## Key Role Definitions

| Role | Key Responsibilities |
|------|---------------------|
| **Unit Lead** | Overall QMS accountability, policy approval, resource allocation |
| **QMR** | Day-to-day QMS, document control, audit coordination, CAPA tracking |
| **Team Lead** | Team quality practices, competence management |
| **Scrum Master** | Agile ceremonies, retrospective improvements |
| **Product Owner** | Requirements, customer voice, deliverable acceptance |
| **Quality Champion** | Per-team QMS awareness, first contact for QMS questions |
""",
    'de_quick': """
**ISO 9001 Abschnitt 5.3** | **Verantwortlich:** QMR

**R** = Responsible (f\\u00fchrt aus) | **A** = Accountable (eine Person) | **C** = Consulted | **I** = Informed

## Schl\\u00fcsselrollen

| Rolle | QMS-Verantwortung |
|-------|-------------------|
| **Unit Lead** | Gesamtverantwortung QMS, genehmigt Politik & Ziele |
| **QMR** | T\\u00e4gliche QMS-Koordination, Dokumentenlenkung, Auditplanung |
| **Team Lead** | Qualit\\u00e4tspraktiken im Team, Kompetenzmanagement |
| **Scrum Master** | Agile Zeremonien, Retrospektiven |
| **Product Owner** | Anforderungen, Kundenstimme |
| **Quality Champion** | QMS-Bewusstsein im Team, unterst\\u00fctzt QMR |
""",
    'de_essential': """
**ISO 9001 Abschnitt 5.3** | **Verantwortlich:** QMR

**R** = Responsible | **A** = Accountable | **C** = Consulted | **I** = Informed

## QMS-Management-Aktivit\\u00e4ten

| Aktivit\\u00e4t | Unit Lead | QMR | Team Lead | PO |
|-------------|:---------:|:---:|:---------:|:--:|
| Qualit\\u00e4tspolitik-Genehmigung | **A** | R | I | I |
| Managementbewertung | **A** | R | C | C |
| Internes Auditprogramm | C | **A**/R | C | |
| Risikoregister | **A** | R | C | C |
| CAPA-Management | I | **A**/R | R | |

## Kernprozess-Aktivit\\u00e4ten

| Aktivit\\u00e4t | Team Lead | SM | PO | Entwickler | QA |
|-------------|:---------:|:--:|:--:|:---------:|:--:|
| Anforderungen | C | C | **A**/R | C | |
| Architektur & Design | **A** | | C | R | C |
| Entwicklung | C | | | **A**/R | |
| Test & Validierung | C | | C | R | **A**/R |
| Release | **A** | | I | C | C |

## Schl\\u00fcsselrollen

| Rolle | Verantwortung |
|-------|---------------|
| **Unit Lead** | Gesamtverantwortung QMS, Politikgenehmigung, Ressourcen |
| **QMR** | T\\u00e4gliches QMS, Dokumentenlenkung, Auditkoordination |
| **Team Lead** | Team-Qualit\\u00e4t, Kompetenzmanagement |
| **Product Owner** | Anforderungen, Kundenstimme |
| **Quality Champion** | QMS-Bewusstsein im Team |
""",
})

# --- risk-register.md ---
PAGES.append({
    'en': 'planning/risk-register.md',
    'de': 'planning/risk-register.de.md',
    'en_quick': """
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
""",
    'en_essential': """
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
""",
    'de_quick': """
**ISO 9001 Abschnitt 6.1** | **Verantwortlich:** QMR | **\\u00dcberpr\\u00fcfung:** Quartalsweise

## Risikobewertung: 5x5-Matrix

| Bewertung | Stufe | Ma\\u00dfnahme |
|:---------:|:-----:|------------|
| 1-4 | Niedrig | Akzeptieren und \\u00fcberwachen |
| 5-9 | Mittel | Mindern |
| 10-15 | Hoch | Aktive Minderung erforderlich |
| 16-25 | Kritisch | Sofortma\\u00dfnahme, eskalieren |

## Top-Risiken

| ID | Risiko | Bewertung | Stufe | Gegenma\\u00dfnahme |
|----|--------|:---------:|:-----:|----------------|
| R-001 | Single Point of Failure Daten-Ingestion | 15 | Hoch | Redundante Pfade, automatisches Failover |
| R-002 | Schl\\u00fcsselpersonenabh\\u00e4ngigkeit Simulation | 16 | Kritisch | Cross-Training, Runbooks |
| R-004 | Datenleck bei Fahrdatenspeicherung | 10 | Hoch | Verschl\\u00fcsselung, RBAC, Pen-Tests |
| R-005 | Regulierungs\\u00e4nderung | 12 | Hoch | Regulierungsmonitoring |
""",
    'de_essential': """
**ISO 9001 Abschnitt 6.1** | **Verantwortlich:** QMR | **\\u00dcberpr\\u00fcfung:** Quartalsweise

## Risikoregister

| ID | Risiko | W | A | Bew. | Stufe | Verantwortlich | Gegenma\\u00dfnahme | Status |
|----|--------|:-:|:-:|:----:|:-----:|----------------|----------------|--------|
| R-001 | Single Point of Failure Daten-Ingestion | 3 | 5 | 15 | Hoch | _[Name]_ | Redundante Pfade, Failover | In Arbeit |
| R-002 | Schl\\u00fcsselpersonenabh\\u00e4ngigkeit | 4 | 4 | 16 | Kritisch | _[Name]_ | Cross-Training, Runbooks | In Arbeit |
| R-003 | Cloud-Kosten\\u00fcberschreitung | 3 | 3 | 9 | Mittel | _[Name]_ | FinOps, Kostenalarme | \\u00dcberwachung |
| R-004 | Datenleck Fahrdaten | 2 | 5 | 10 | Hoch | _[Name]_ | Verschl\\u00fcsselung, RBAC | In Arbeit |
| R-005 | Regulierungs\\u00e4nderung | 3 | 4 | 12 | Hoch | _[Name]_ | Monitoring, modularer Ansatz | \\u00dcberwachung |
| R-006 | OSS-Lieferkettenrisiko | 3 | 4 | 12 | Hoch | _[Name]_ | Dependency-Scanning, SBOM | In Arbeit |
| R-007 | Cloud-Regionausfall | 2 | 5 | 10 | Hoch | _[Name]_ | Multi-AZ, DR-Plan | Umgesetzt |
| R-008 | Talentabwanderung | 4 | 3 | 12 | Hoch | _[Name]_ | Verg\\u00fctung, Lernbudget | Laufend |

## Chancenregister

| ID | Chance | Bew. | Verantwortlich | Status |
|----|--------|:----:|----------------|--------|
| O-001 | Neue GPU-Instanzen f\\u00fcr Simulation | 16 | _[Name]_ | Evaluierung |
| O-002 | SimaaS f\\u00fcr Partner-OEMs | 10 | _[Name]_ | Vorgeschlagen |
""",
})

# --- quality-objectives.md ---
PAGES.append({
    'en': 'planning/quality-objectives.md',
    'de': 'planning/quality-objectives.de.md',
    'en_quick': """
**ISO 9001 Clause 6.2** | **Owner:** QMR

## Quality Objectives at a Glance

| # | Objective | KPI | Target |
|---|-----------|-----|:------:|
| QO-1 | Tool Availability | Uptime | >= 99.5% |
| QO-2 | Incident Response | MTTR (Critical) | < 4 hours |
| QO-3 | Customer Satisfaction | NPS | >= 40 |
| QO-4 | Data Integrity | Integrity incidents | 0 per quarter |
| QO-5 | Release Quality | CI/CD pass rate | 100% |
| QO-6 | Test Coverage | Code coverage | >= 80% |
| QO-7 | Competence Development | Training completion | >= 90% |

> All objectives are SMART, derived from Quality Policy, tracked in Grafana, reviewed monthly + quarterly.
""",
    'en_essential': """
**ISO 9001 Clause 6.2** | **Owner:** QMR | **Approved by:** Unit Lead

## Quality Objectives

| # | Objective | KPI | Target | Measurement | Frequency | Owner |
|---|-----------|-----|:------:|-------------|-----------|-------|
| QO-1 | Tool Availability | Uptime | >= 99.5% | Prometheus/Grafana | Continuous | DevOps/SRE Lead |
| QO-2 | Incident Response | MTTR (P1) | < 4 hours | Jira/PagerDuty | Per incident | Team Lead |
| QO-3 | Customer Satisfaction | NPS | >= 40 | Quarterly survey | Quarterly | PO |
| QO-4 | Data Integrity | Incidents | 0/quarter | Incident tracking | Continuous | Data Eng Lead |
| QO-5 | Release Quality | Pass rate | 100% | CI/CD metrics | Per release | DevOps Lead |
| QO-6 | Test Coverage | Code coverage | >= 80% | Coverage tools | Per PR | Team Leads |
| QO-7 | Competence Dev | Training done | >= 90% | HR system | Annual | Team Leads |

```mermaid
graph LR
    subgraph "Quality Policy"
        P1["Customer Focus"]
        P2["Reliability"]
        P5["Improvement"]
        P7["People"]
    end
    subgraph "Objectives"
        QO1["QO-1: Availability >= 99.5%"]
        QO2["QO-2: MTTR < 4h"]
        QO3["QO-3: NPS >= 40"]
        QO4["QO-4: 0 data incidents"]
        QO5["QO-5: 100% release pass"]
        QO6["QO-6: Coverage >= 80%"]
        QO7["QO-7: Training >= 90%"]
    end
    P1 --> QO3
    P2 --> QO1 & QO2 & QO4
    P5 --> QO5 & QO6
    P7 --> QO7
    style P1 fill:#1a5276,color:#fff
    style P2 fill:#1a5276,color:#fff
    style P5 fill:#1a5276,color:#fff
    style P7 fill:#1a5276,color:#fff
```

## Quarterly Tracking

| Objective | Q1 | Q2 | Q3 | Q4 | Trend |
|-----------|:--:|:--:|:--:|:--:|:-----:|
| QO-1 | _[Fill]_ | | | | |
| QO-2 | _[Fill]_ | | | | |
| QO-3 | _[Fill]_ | | | | |
| QO-4 | _[Fill]_ | | | | |
| QO-5 | _[Fill]_ | | | | |
| QO-6 | _[Fill]_ | | | | |
| QO-7 | _[Fill]_ | | | | |
""",
    'de_quick': """
**ISO 9001 Abschnitt 6.2** | **Verantwortlich:** QMR

## Qualit\\u00e4tsziele auf einen Blick

| Nr. | Ziel | KPI | Zielwert |
|-----|------|-----|:--------:|
| QO-1 | Werkzeugverf\\u00fcgbarkeit | Verf\\u00fcgbarkeit | >= 99,5% |
| QO-2 | Reaktionszeit bei St\\u00f6rungen | MTTR (Kritisch) | < 4 Stunden |
| QO-3 | Kundenzufriedenheit | NPS | >= 40 |
| QO-4 | Datenintegrit\\u00e4t | Integrit\\u00e4tsvorf\\u00e4lle | 0 pro Quartal |
| QO-5 | Release-Qualit\\u00e4t | CI/CD-Passrate | 100% |
| QO-6 | Testabdeckung | Code-Abdeckung | >= 80% |
| QO-7 | Kompetenzentwicklung | Schulungsabschluss | >= 90% |
""",
    'de_essential': """
**ISO 9001 Abschnitt 6.2** | **Verantwortlich:** QMR

## Qualit\\u00e4tsziele

| Nr. | Ziel | KPI | Zielwert | Messung | Frequenz | Verantwortlich |
|-----|------|-----|:--------:|---------|----------|----------------|
| QO-1 | Verf\\u00fcgbarkeit | Uptime | >= 99,5% | Grafana | Kontinuierlich | DevOps/SRE Lead |
| QO-2 | Reaktionszeit | MTTR (P1) | < 4 Std. | Jira/PagerDuty | Pro Vorfall | Team Lead |
| QO-3 | Kundenzufriedenheit | NPS | >= 40 | Quartalsbefragung | Quartalsweise | PO |
| QO-4 | Datenintegrit\\u00e4t | Vorf\\u00e4lle | 0/Quartal | Vorfalltracking | Kontinuierlich | Data Eng Lead |
| QO-5 | Release-Qualit\\u00e4t | Passrate | 100% | CI/CD-Metriken | Pro Release | DevOps Lead |
| QO-6 | Testabdeckung | Abdeckung | >= 80% | Coverage-Tools | Pro PR | Team Leads |
| QO-7 | Kompetenz | Schulung | >= 90% | HR-System | J\\u00e4hrlich | Team Leads |

## Quartals-Tracking

| Ziel | Q1 | Q2 | Q3 | Q4 | Trend |
|------|:--:|:--:|:--:|:--:|:-----:|
| QO-1 bis QO-7 | _[Ausf\\u00fcllen]_ | | | | |
""",
})

# --- competency-matrix.md ---
PAGES.append({
    'en': 'support/competency-matrix.md',
    'de': 'support/competency-matrix.de.md',
    'en_quick': """
**ISO 9001 Clause 7.2** | **Owner:** Team Leads + HR

## Competency Scale

| Level | Description |
|:-----:|-------------|
| 0 | No knowledge |
| 1 | Awareness — understands concepts |
| 2 | Basic — can perform with guidance |
| 3 | Proficient — performs independently |
| 4 | Expert — can teach others |

## Key Training Requirements

| Training | Audience | Frequency |
|----------|----------|-----------|
| ISO 9001 QMS Awareness | All | Annual + onboarding |
| Quality Policy & Objectives | All | Annual |
| Security Awareness | All | Annual (mandatory) |
| Data Protection (GDPR) | All | Annual (mandatory) |
| Internal Auditor Training | Selected staff | As needed |

> Evidence: training records in SuccessFactors, certifications in team wiki, onboarding sign-off by team leads.
""",
    'en_essential': """
**ISO 9001 Clause 7.2** | **Owner:** Team Leads + HR

## Competency Scale

| Level | Description | Indicator |
|:-----:|-------------|-----------|
| 0 | No knowledge | No exposure |
| 1 | Awareness | Understands concepts |
| 2 | Basic | Performs with guidance |
| 3 | Proficient | Performs independently |
| 4 | Expert | Can teach others |

## Key Technical Competencies (Required Level)

| Competency | Data Eng | Backend | DevOps | QA | Tech Lead | PO |
|------------|:--------:|:-------:|:------:|:--:|:---------:|:--:|
| Python / Data Processing | 4 | 3 | 2 | 3 | 3 | 1 |
| Cloud Architecture | 3 | 2 | 4 | 2 | 3 | 1 |
| CI/CD Pipelines | 2 | 3 | 4 | 3 | 3 | 1 |
| Testing & QA | 2 | 3 | 2 | 4 | 3 | 1 |
| Security Practices | 2 | 2 | 3 | 2 | 3 | 1 |

## Process & Soft Skills (Minimum)

| Competency | All Roles | Team Lead | QMR |
|------------|:---------:|:---------:|:---:|
| Agile/Scrum | 2 | 3 | 2 |
| ISO 9001 Awareness | 1 | 2 | 4 |
| Risk Management | 1 | 3 | 4 |

## Training Plan

| Training | Audience | Format | Frequency |
|----------|----------|--------|-----------|
| ISO 9001 QMS Awareness | All | Workshop | Annual + onboarding |
| ISO 26262 Tool Qualification | QA, Tech Leads | External course | As needed |
| Cloud Certification | DevOps, Data Eng | Online + exam | Yearly cohort |
| Security Awareness | All | E-learning | Annual (mandatory) |
| Data Protection (GDPR) | All | E-learning | Annual (mandatory) |
| Internal Auditor Training | Selected | 2-day course | As needed |

## Evidence of Competence

- Education: degree certificates (HR system)
- Training: completion certificates (SuccessFactors)
- Experience: project assignments (HR system)
- Skills: annual 1:1 review records
- Certifications: tracked in team wiki
""",
    'de_quick': """
**ISO 9001 Abschnitt 7.2** | **Verantwortlich:** Team Leads + HR

## Kompetenzskala

| Stufe | Beschreibung |
|:-----:|-------------|
| 0 | Keine Kenntnisse |
| 1 | Bewusstsein — versteht Konzepte |
| 2 | Grundkenntnisse — kann mit Anleitung |
| 3 | Kompetent — eigenst\\u00e4ndig |
| 4 | Experte — kann andere schulen |

## Wichtigste Schulungen

| Schulung | Zielgruppe | Frequenz |
|----------|------------|----------|
| ISO 9001 QMS-Bewusstsein | Alle | J\\u00e4hrlich + Einarbeitung |
| Sicherheitsbewusstsein | Alle | J\\u00e4hrlich (Pflicht) |
| Datenschutz (DSGVO) | Alle | J\\u00e4hrlich (Pflicht) |
| Interner Auditor | Ausgew\\u00e4hlte | Nach Bedarf |
""",
    'de_essential': """
**ISO 9001 Abschnitt 7.2** | **Verantwortlich:** Team Leads + HR

## Technische Kernkompetenzen (Erforderliche Stufe)

| Kompetenz | Data Eng | Backend | DevOps | QA | Tech Lead |
|-----------|:--------:|:-------:|:------:|:--:|:---------:|
| Python / Datenverarbeitung | 4 | 3 | 2 | 3 | 3 |
| Cloud-Architektur | 3 | 2 | 4 | 2 | 3 |
| CI/CD-Pipelines | 2 | 3 | 4 | 3 | 3 |
| Testing & QA | 2 | 3 | 2 | 4 | 3 |

## Schulungsplan

| Schulung | Zielgruppe | Format | Frequenz |
|----------|------------|--------|----------|
| ISO 9001 QMS-Bewusstsein | Alle | Workshop | J\\u00e4hrlich + Einarbeitung |
| ISO 26262 Werkzeugqualifizierung | QA, Tech Leads | Extern | Nach Bedarf |
| Cloud-Zertifizierung | DevOps, Data Eng | Online | J\\u00e4hrlich |
| Sicherheitsbewusstsein | Alle | E-Learning | J\\u00e4hrlich (Pflicht) |
| Datenschutz (DSGVO) | Alle | E-Learning | J\\u00e4hrlich (Pflicht) |

## Kompetenznachweise
- Ausbildung: Zeugnisse (HR-System)
- Schulungen: Zertifikate (SuccessFactors)
- Erfahrung: Projektzuweisungen
- Bewertung: J\\u00e4hrliche 1:1-Gespr\\u00e4che
""",
})

# --- communication-matrix.md ---
PAGES.append({
    'en': 'support/communication-matrix.md',
    'de': 'support/communication-matrix.de.md',
    'en_quick': """
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
""",
    'en_essential': """
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
""",
    'de_quick': """
**ISO 9001 Abschnitt 7.4** | **Verantwortlich:** QMR

## Wichtigste Kommunikationskan\\u00e4le

| Was | Wann | Von/An | Wie |
|-----|------|--------|-----|
| Daily Standup | T\\u00e4glich | Team | MS Teams |
| Sprint Review | Alle 2 Wochen | Team an Stakeholder | Besprechung |
| Sprint Retrospektive | Alle 2 Wochen | Team | Miro |
| All-Hands (inkl. Qualit\\u00e4tsmetriken) | Monatlich | Unit Lead an alle | Besprechung |
| Managementbewertung | Quartalsweise | QMR + Management | Formale Sitzung |
| Release Notes | Pro Release | DevOps an Kunden | Confluence + E-Mail |
| St\\u00f6rungsmeldung | Sofort | Bereitschaft an Team | PagerDuty + Slack |
""",
    'de_essential': """
**ISO 9001 Abschnitt 7.4** | **Verantwortlich:** QMR

## Interne Kommunikation

| Was | Zweck | Wann | Von | An | Wie |
|-----|-------|------|-----|-----|-----|
| Daily Standup | Synchronisation, Blocker | T\\u00e4glich (15 Min.) | Team | Team | MS Teams |
| Sprint Planning | Umfang & Ziele | Alle 2 Wochen | PO + SM | Team | Besprechung |
| Sprint Review | Ergebnisse zeigen | Alle 2 Wochen | Team | Stakeholder | Besprechung |
| Retrospektive | Verbesserungen | Alle 2 Wochen | SM | Team | Miro |
| Team-Leads-Sync | \\u00dcbergreifende Abstimmung | W\\u00f6chentlich | Leads | Unit Lead | Besprechung |
| All-Hands | Updates, Qualit\\u00e4tsmetriken | Monatlich | Unit Lead | Alle | Besprechung |
| Managementbewertung | QMS-Leistung | Quartalsweise | QMR | Management | Formale Sitzung |

## Externe Kommunikation

| Was | Wann | Von | An | Wie |
|-----|------|-----|-----|-----|
| Release Notes | Pro Release | DevOps/PO | Kunden | Confluence |
| SLA-Berichte | Monatlich | SRE | Nutzer | Dashboard |
| St\\u00f6rungsmeldung | Sofort | Bereitschaft | Kunden | Slack + E-Mail |
| Roadmap | Quartalsweise | PO | Stakeholder | Pr\\u00e4sentation |
""",
})

# --- supplier-evaluation.md ---
PAGES.append({
    'en': 'operations/supplier-evaluation.md',
    'de': 'operations/supplier-evaluation.de.md',
    'en_quick': """
**ISO 9001 Clause 8.4** | **Owner:** Tech Lead + Procurement

## Supplier Categories

| Category | Examples | Evaluation |
|----------|----------|------------|
| **A — Strategic** | AWS, Azure, major SaaS | Full evaluation + annual review |
| **B — Important** | Third-party tools, consulting | Standard evaluation + periodic review |
| **C — Standard** | Office tools, open-source | Simplified assessment |

## Approval Thresholds

- **>= 4.0:** Approved
- **3.0-3.9:** Conditionally approved (with mitigations)
- **< 3.0:** Not approved

## Evaluation Criteria

Technical capability (25%), reliability/SLA (20%), security posture (20%), cost (15%), support (10%), compliance (10%)
""",
    'en_essential': """
**ISO 9001 Clause 8.4** | **Owner:** Tech Lead + Procurement

## Supplier Categories

| Category | Examples | Risk | Evaluation |
|----------|----------|:----:|------------|
| **A — Strategic** | Cloud providers (AWS, Azure) | High | Full evaluation + annual review |
| **B — Important** | Third-party tools, consulting | Medium | Standard evaluation + periodic review |
| **C — Standard** | Office tools, open-source | Low | Simplified assessment |

## Evaluation Scorecard

| Criterion | Weight |
|-----------|:------:|
| Technical capability | 25% |
| Reliability & availability (SLA) | 20% |
| Security posture (ISO 27001, SOC2) | 20% |
| Cost effectiveness | 15% |
| Support & responsiveness | 10% |
| Compliance (license, GDPR) | 10% |

**Thresholds:** >= 4.0 Approved | 3.0-3.9 Conditional | < 3.0 Not approved

## Monitoring

| Category | Method | Frequency |
|----------|--------|-----------|
| A — Strategic | SLA review, security tracking, annual business review | Monthly + Annual |
| B — Important | SLA check, bug/feature tracking | Quarterly |
| C — Standard | Vulnerability scanning, license check | Automated |

```mermaid
graph TD
    A["Issue Identified"] --> B{"Severity?"}
    B -->|Low| C["Log, discuss at next review"]
    B -->|Medium| D["Escalate to Tech Lead"]
    B -->|High| E["Escalate to Unit Lead, evaluate alternatives"]
    style A fill:#c0392b,color:#fff
    style C fill:#196f3d,color:#fff
    style E fill:#e67e22,color:#fff
```
""",
    'de_quick': """
**ISO 9001 Abschnitt 8.4** | **Verantwortlich:** Tech Lead + Beschaffung

## Lieferantenkategorien

| Kategorie | Beispiele | Bewertung |
|-----------|----------|-----------|
| **A — Strategisch** | AWS, Azure, gro\\u00dfe SaaS | Vollbewertung + j\\u00e4hrliches Review |
| **B — Wichtig** | Drittanbieter-Tools, Beratung | Standardbewertung + periodisches Review |
| **C — Standard** | B\\u00fcro-Tools, Open Source | Vereinfachte Bewertung |

## Genehmigungsschwellen

- **>= 4,0:** Genehmigt
- **3,0-3,9:** Bedingt genehmigt
- **< 3,0:** Nicht genehmigt
""",
    'de_essential': """
**ISO 9001 Abschnitt 8.4** | **Verantwortlich:** Tech Lead + Beschaffung

## Bewertungskriterien

| Kriterium | Gewichtung |
|-----------|:----------:|
| Technische F\\u00e4higkeit | 25% |
| Zuverl\\u00e4ssigkeit & SLA | 20% |
| Sicherheit (ISO 27001, SOC2) | 20% |
| Kosteneffizienz | 15% |
| Support & Reaktionsf\\u00e4higkeit | 10% |
| Compliance (Lizenz, DSGVO) | 10% |

## \\u00dcberwachung

| Kategorie | Methode | Frequenz |
|-----------|---------|----------|
| A — Strategisch | SLA-Review, Sicherheits-Tracking | Monatlich + j\\u00e4hrlich |
| B — Wichtig | SLA-Check, Bug-/Feature-Tracking | Quartalsweise |
| C — Standard | Vulnerability-Scanning, Lizenzcheck | Automatisiert |
""",
})

# --- internal-audit-program.md ---
PAGES.append({
    'en': 'performance/internal-audit-program.md',
    'de': 'performance/internal-audit-program.de.md',
    'en_quick': """
**ISO 9001 Clause 9.2** | **Owner:** QMR

## Audit Cycle

Full QMS coverage over 12 months. High-risk areas audited more frequently.

## Annual Schedule

| Audit | Clauses | Focus |
|:-----:|:-------:|-------|
| A-01 | 4.1-4.4 | Context, scope, processes |
| A-02 | 5.1-5.3 | Leadership, policy, roles |
| A-03 | 6.1-6.3 | Risk, objectives, change |
| A-04 | 7.1-7.5 | Resources, competence, docs |
| A-05 | 8.1-8.7 | Operations, design, suppliers |
| A-06 | 9.1-9.3 | Monitoring, audit, mgmt review |
| A-07 | 10.1-10.3 | Improvement, CAPA |

## Finding Classification

| Type | Response |
|------|----------|
| **Major NC** | CAPA within 30 days, root cause required |
| **Minor NC** | CAPA within 60 days |
| **Observation** | Recommended action |
| **Opportunity** | Optional, tracked |
""",
    'en_essential': """
**ISO 9001 Clause 9.2** | **Owner:** QMR | **Approved by:** Unit Lead

## Objectives

- Verify conformance to ISO 9001:2015
- Verify conformance to own QMS requirements
- Assess QMS effectiveness
- Identify improvement opportunities

## Annual Schedule

| Audit # | Clauses | Processes Audited | Lead Auditor | Status |
|:-------:|:-------:|-------------------|:------------:|:------:|
| A-01 | 4.1-4.4 | Context, scope, processes | _[Name]_ | ☐ |
| A-02 | 5.1-5.3 | Leadership, policy, roles | _[Name]_ | ☐ |
| A-03 | 6.1-6.3 | Risk, objectives, change | _[Name]_ | ☐ |
| A-04 | 7.1-7.4 | Resources, competence, communication | _[Name]_ | ☐ |
| A-05 | 7.5 | Document control | _[Name]_ | ☐ |
| A-06 | 8.1-8.3 | Operations, requirements, design | _[Name]_ | ☐ |
| A-07 | 8.4-8.7 | Suppliers, service provision, NC outputs | _[Name]_ | ☐ |
| A-08 | 9.1-9.3 | Monitoring, internal audit, mgmt review | _[Name]_ | ☐ |
| A-09 | 10.1-10.3 | Improvement, CAPA | _[Name]_ | ☐ |

## Audit Process

```mermaid
graph LR
    A["Annual Plan"] --> B["Prepare"]
    B --> C["Opening Meeting"]
    C --> D["Conduct Audit"]
    D --> E["Closing Meeting"]
    E --> F["Audit Report"]
    F --> G["Corrective Actions"]
    G --> H["Follow-up"]
    H --> I["Management Review"]
    style A fill:#1a5276,color:#fff
    style D fill:#196f3d,color:#fff
    style F fill:#e67e22,color:#fff
    style G fill:#c0392b,color:#fff
```

## Finding Classification

| Classification | Description | Response |
|---------------|-------------|----------|
| **Major NC** | Absence or total breakdown of required process | CAPA within 30 days |
| **Minor NC** | Isolated lapse | CAPA within 60 days |
| **Observation** | Potential risk or concern | Recommended action |
| **Opportunity** | Enhancement suggestion | Optional |
| **Positive Practice** | Noteworthy good practice | Shared |

## Auditor Requirements

- ISO 9001 internal auditor training (min. 16 hours)
- Must not audit own work
- Min. 1 audit as observer before leading
""",
    'de_quick': """
**ISO 9001 Abschnitt 9.2** | **Verantwortlich:** QMR

## Audit-Zyklus

Vollst\\u00e4ndige QMS-Abdeckung \\u00fcber 12 Monate.

## Jahresplan

| Audit | Abschnitte | Fokus |
|:-----:|:----------:|-------|
| A-01 | 4.1-4.4 | Kontext, Geltungsbereich |
| A-02 | 5.1-5.3 | F\\u00fchrung, Politik, Rollen |
| A-03 | 6.1-6.3 | Risiken, Ziele, \\u00c4nderungen |
| A-04 | 7.1-7.5 | Ressourcen, Kompetenz, Dokumente |
| A-05 | 8.1-8.7 | Betrieb, Design, Lieferanten |
| A-06 | 9.1-9.3 | \\u00dcberwachung, Audit, Bewertung |
| A-07 | 10.1-10.3 | Verbesserung, CAPA |

## Feststellungsklassifizierung

| Typ | Reaktion |
|-----|----------|
| **Haupt-NK** | CAPA innerhalb 30 Tagen |
| **Neben-NK** | CAPA innerhalb 60 Tagen |
| **Beobachtung** | Empfohlene Ma\\u00dfnahme |
""",
    'de_essential': """
**ISO 9001 Abschnitt 9.2** | **Verantwortlich:** QMR

## Jahresplan

| Audit Nr. | Abschnitte | Gepr\\u00fcfte Prozesse | Auditor | Status |
|:---------:|:----------:|----------------------|:-------:|:------:|
| A-01 | 4.1-4.4 | Kontext, Geltungsbereich | _[Name]_ | ☐ |
| A-02 | 5.1-5.3 | F\\u00fchrung, Politik, Rollen | _[Name]_ | ☐ |
| A-03 | 6.1-6.3 | Risiken, Ziele, \\u00c4nderungsplanung | _[Name]_ | ☐ |
| A-04 | 7.1-7.4 | Ressourcen, Kompetenz, Kommunikation | _[Name]_ | ☐ |
| A-05 | 7.5 | Dokumentenlenkung | _[Name]_ | ☐ |
| A-06 | 8.1-8.3 | Betrieb, Anforderungen, Entwicklung | _[Name]_ | ☐ |
| A-07 | 8.4-8.7 | Lieferanten, Bereitstellung | _[Name]_ | ☐ |
| A-08 | 9.1-9.3 | \\u00dcberwachung, Audit, Bewertung | _[Name]_ | ☐ |
| A-09 | 10.1-10.3 | Verbesserung, CAPA | _[Name]_ | ☐ |

## Audit-Prozess

```mermaid
graph LR
    A["Jahresplan"] --> B["Vorbereitung"]
    B --> C["Er\\u00f6ffnung"]
    C --> D["Durchf\\u00fchrung"]
    D --> E["Abschluss"]
    E --> F["Auditbericht"]
    F --> G["Korrekturma\\u00dfnahmen"]
    G --> H["Nachverfolgung"]
    style A fill:#1a5276,color:#fff
    style D fill:#196f3d,color:#fff
    style F fill:#e67e22,color:#fff
```

## Feststellungsklassifizierung

| Klassifizierung | Beschreibung | Reaktion |
|----------------|-------------|----------|
| **Haupt-NK** | Fehlen oder Totalausfall eines Prozesses | CAPA 30 Tage |
| **Neben-NK** | Einzelfall | CAPA 60 Tage |
| **Beobachtung** | Potenzielles Risiko | Empfohlene Ma\\u00dfnahme |
| **Verbesserungsm\\u00f6glichkeit** | Vorschlag | Optional |
""",
})

# --- management-review.md ---
PAGES.append({
    'en': 'performance/management-review.md',
    'de': 'performance/management-review.de.md',
    'en_quick': """
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
""",
    'en_essential': """
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
""",
    'de_quick': """
**ISO 9001 Abschnitt 9.3** | **Verantwortlich:** QMR | **Vorsitz:** Unit Lead

## Managementbewertung — Erforderliche Eingaben

1. Status der Ma\\u00dfnahmen aus vorherigen Bewertungen
2. \\u00c4nderungen externer/interner Themen
3. QMS-Leistung: Kundenzufriedenheit, Qualit\\u00e4tsziele, Prozessleistung, NKs/CAPAs, Auditergebnisse
4. Angemessenheit der Ressourcen
5. Risiken- und Chancen-\\u00dcberpr\\u00fcfung
6. Verbesserungsm\\u00f6glichkeiten

## Erforderliche Ergebnisse

- Entscheidungen zu Verbesserungsma\\u00dfnahmen
- Ressourcenzuweisungs\\u00e4nderungen
- Aktualisierte Qualit\\u00e4tsziele
- Ma\\u00dfnahmen mit Verantwortlichen und Terminen

> **Frequenz:** Quartalsweise + j\\u00e4hrlich umfassend.
""",
    'de_essential': """
**ISO 9001 Abschnitt 9.3** | **Verantwortlich:** QMR | **Frequenz:** Quartalsweise

## Agenda — Erforderliche Eingaben (Abschnitt 9.3.2)

### 1. Vorherige Ma\\u00dfnahmen

| Nr. | Beschreibung | Verantwortlich | F\\u00e4llig | Status |
|:---:|-------------|----------------|:------:|:------:|
| MR-_[#]_ | _[Ma\\u00dfnahme]_ | _[Name]_ | _[Datum]_ | ☐/✅ |

### 2. Kontext\\u00e4nderungen

| Thema | \\u00c4nderung | Auswirkung | Ma\\u00dfnahme |
|-------|-----------|-----------|------------|
| _[Thema]_ | _[\\u00c4nderung]_ | _[Auswirkung]_ | _[Ma\\u00dfnahme]_ |

### 3. QMS-Leistung

| Ziel | Vorherig | Aktuell | Zielwert | Status |
|------|:--------:|:-------:|:--------:|:------:|
| QO-1: Verf\\u00fcgbarkeit | _[%]_ | _[%]_ | >= 99,5% | &#x1F7E2;&#x1F7E1;&#x1F534; |
| QO-2: MTTR | _[Std.]_ | _[Std.]_ | < 4 Std. | &#x1F7E2;&#x1F7E1;&#x1F534; |
| QO-3: NPS | _[#]_ | _[#]_ | >= 40 | &#x1F7E2;&#x1F7E1;&#x1F534; |

## Ergebnisse (Abschnitt 9.3.3)

| Nr. | Entscheidung/Ma\\u00dfnahme | Verantwortlich | F\\u00e4llig |
|-----|-------------------------|----------------|:------:|
| D-_[#]_ | _[Entscheidung]_ | _[Name]_ | _[Datum]_ |
""",
})

# --- capa-log.md ---
PAGES.append({
    'en': 'improvement/capa-log.md',
    'de': 'improvement/capa-log.de.md',
    'en_quick': """
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
""",
    'en_essential': """
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
""",
    'de_quick': """
**ISO 9001 Abschnitt 10.2** | **Verantwortlich:** QMR | **\\u00dcberpr\\u00fcfung:** Monatlich

## CAPA-Prozess

```mermaid
graph LR
    A["Nichtkonformit\\u00e4t"] --> B["Eind\\u00e4mmen"]
    B --> C["Ursache<br/>(5-Why)"]
    C --> D["Korrektur"]
    D --> E["Wirksamkeit<br/>pr\\u00fcfen"]
    E -->|OK| F["Schlie\\u00dfen"]
    E -->|Nicht OK| C
    style A fill:#c0392b,color:#fff
    style C fill:#e67e22,color:#fff
    style D fill:#2471a3,color:#fff
    style F fill:#196f3d,color:#fff
```

**Quellen:** Auditfeststellungen, Kundenbeschwerden, Vorf\\u00e4lle, Managementbewertung

## CAPA-Register (Vorlage)

| CAPA Nr. | Datum | Quelle | Beschreibung | Schwere | Ursache | Korrektur | Verantw. | F\\u00e4llig | Status |
|:--------:|:-----:|:------:|-------------|:-------:|---------|-----------|----------|:------:|:------:|
| CA-001 | | | | Krit./Haupt/Neben | | | | | ☐ |

> Wirksamkeitspr\\u00fcfung nach 30/60/90 Tagen.
""",
    'de_essential': """
**ISO 9001 Abschnitt 10.2** | **Verantwortlich:** QMR | **\\u00dcberpr\\u00fcfung:** Monatlich

## CAPA-Prozess

```mermaid
graph TD
    A["Nichtkonformit\\u00e4tsquelle"] --> B["Im CAPA-Register erfassen"]
    B --> C["Verantwortlichen zuweisen"]
    C --> D["Sofortige Eind\\u00e4mmung"]
    D --> E["Ursachenanalyse"]
    E --> F["Korrekturma\\u00dfnahme definieren"]
    F --> G["Ma\\u00dfnahme umsetzen"]
    G --> H["Wirksamkeit pr\\u00fcfen"]
    H -->|"Wirksam"| I["CAPA schlie\\u00dfen"]
    H -->|"Nicht wirksam"| E
    I --> J["Risikoregister & Lessons Learned"]
    style A fill:#c0392b,color:#fff
    style E fill:#e67e22,color:#fff
    style G fill:#2471a3,color:#fff
    style I fill:#196f3d,color:#fff
```

## Ursachenanalyse-Methoden

| Methode | Anwendung |
|---------|-----------|
| **5-Why** | Die meisten Nichtkonformit\\u00e4ten |
| **Fishbone (Ishikawa)** | Komplex, mehrere Ursachen |
| **Fehlerbaumanalyse** | Kritische/sicherheitsrelevante Themen |

## CAPA-Register

| Nr. | Datum | Quelle | Beschreibung | Schwere | Ursache | Eind\\u00e4mmung | Korrektur | Verantw. | F\\u00e4llig | Status |
|:---:|:-----:|:------:|-------------|:-------:|---------|------------|-----------|----------|:------:|:------:|
| CA-001 | | | | | | | | | | ☐ |

## Dashboard-Metriken

| Metrik | Aktuell | Vorherig | Trend |
|--------|:-------:|:--------:|:-----:|
| Offene CAPAs | _[#]_ | _[#]_ | \\u2191\\u2193\\u2192 |
| \\u00d8 Zeit bis Abschluss | _[Tage]_ | _[Tage]_ | \\u2191\\u2193\\u2192 |
| Wirksamkeitsrate | _[%]_ | _[%]_ | \\u2191\\u2193\\u2192 |
""",
})


# ---------------------------------------------------------------------------
# EXECUTION
# ---------------------------------------------------------------------------
def main():
    print("Adding three reading levels to all documentation pages...\n")
    success = 0
    errors = []

    for page in PAGES:
        # Process EN file
        en_path = os.path.join(DOCS, page['en'])
        if os.path.exists(en_path):
            try:
                transform_file(en_path, page['en_quick'], page['en_essential'], EN)
                success += 1
            except Exception as e:
                errors.append(f"EN {page['en']}: {e}")
        else:
            errors.append(f"EN {page['en']}: file not found")

        # Process DE file
        de_path = os.path.join(DOCS, page['de'])
        if os.path.exists(de_path):
            try:
                transform_file(de_path, page['de_quick'], page['de_essential'], DE)
                success += 1
            except Exception as e:
                errors.append(f"DE {page['de']}: {e}")
        else:
            errors.append(f"DE {page['de']}: file not found")

    print(f"\nDone: {success} files processed successfully.")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  ! {e}")


if __name__ == '__main__':
    main()
