# REF-12: Vorlage Managementbewertung

## DDD-Einheit — Data Driven Development | AD/ADAS Tooling

**Dokumentenverantwortlicher:** Qualitätsmanagementbeauftragter (QMB)
**Sitzungsleitung:** Abteilungsleiter

---

## Protokoll der Managementbewertung

| Attribut | Detail |
|-----------|--------|
| **Datum** | TT.MM.JJJJ |
| **Uhrzeit** | HH:MM – HH:MM |
| **Ort** | _[Raum / Teams-Link]_ |
| **Teilnehmer** | _[Namen und Rollen]_ |
| **Abwesend** | _[Namen]_ |
| **Protokollführung** | _[Name]_ |

---

## Tagesordnung / Erforderliche Eingaben (ISO 9001:2015, Abschnitt 9.3.2)

### 1. Status der Maßnahmen aus vorherigen Managementbewertungen

| Maßnahme-Nr. | Beschreibung | Verantwortlich | Fälligkeitsdatum | Status | Kommentare |
|:--------:|-------------|-------|:--------:|:------:|----------|
| MR-_[#]_ | _[Maßnahme]_ | _[Name]_ | _[Datum]_ | ☐ Offen / ✅ Geschlossen | |
| | | | | | |

### 2. Änderungen bei externen und internen Themen

| Thema | Typ | Änderungsbeschreibung | Auswirkung auf QMS | Erforderliche Maßnahme |
|-------|------|-------------------|---------------|-----------------|
| _[Thema]_ | Intern / Extern | _[Was hat sich geändert]_ | _[Auswirkung]_ | _[Maßnahme]_ |
| | | | | |

**Referenz:** [REF-01 Kontextanalyse](../qms-framework/context-analysis.md)

### 3. QMS-Leistung und -Wirksamkeit

#### 3a. Kundenzufriedenheit

| Kennzahl | Vorheriger Zeitraum | Aktueller Zeitraum | Ziel | Trend | Maßnahme |
|--------|:--------------:|:--------------:|:------:|:-----:|--------|
| NPS-Wert | _[#]_ | _[#]_ | ≥ 40 | ↑↓→ | |
| Lösungszeit für Support-Tickets | _[Stunden]_ | _[Stunden]_ | _[Ziel]_ | ↑↓→ | |
| Umsetzungsrate von Feature-Anfragen | _[%]_ | _[%]_ | _[Ziel]_ | ↑↓→ | |

#### 3b. Leistung der Qualitätsziele

| Ziel | KPI | Vorher | Aktuell | Ziel | Status |
|-----------|-----|:--------:|:-------:|:------:|:------:|
| QO-1: Verfügbarkeit | Uptime % | _[%]_ | _[%]_ | ≥ 99,5% | 🟢🟡🔴 |
| QO-2: MTTR | Stunden | _[h]_ | _[h]_ | < 4h | 🟢🟡🔴 |
| QO-3: NPS | Wert | _[#]_ | _[#]_ | ≥ 40 | 🟢🟡🔴 |
| QO-4: Datenintegrität | Vorfälle | _[#]_ | _[#]_ | 0 | 🟢🟡🔴 |
| QO-5: Release-Qualität | Erfolgsrate | _[%]_ | _[%]_ | 100% | 🟢🟡🔴 |
| QO-6: Testabdeckung | Abdeckung % | _[%]_ | _[%]_ | ≥ 80% | 🟢🟡🔴 |
| QO-7: Schulung | Abschlussrate % | _[%]_ | _[%]_ | ≥ 90% | 🟢🟡🔴 |

**Referenz:** [REF-07 Qualitätsziele](../planning/quality-objectives.md)

#### 3c. Prozessleistung

| Prozess | Schlüsselkennzahl | Vorher | Aktuell | Trend | Problem / Maßnahme |
|---------|-----------|:--------:|:-------:|:-----:|---------------|
| Entwicklung | Sprint-Velocity | _[Pkt.]_ | _[Pkt.]_ | ↑↓→ | |
| Deployment | Deploy-Häufigkeit | _[/Woche]_ | _[/Woche]_ | ↑↓→ | |
| Deployment | Fehlerrate | _[%]_ | _[%]_ | ↑↓→ | |
| Betrieb | MTTR | _[h]_ | _[h]_ | ↑↓→ | |
| Betrieb | Anzahl Störungen | _[#]_ | _[#]_ | ↑↓→ | |

#### 3d. Nichtkonformitäten und Korrekturmaßnahmen

| CAPA-Nr. | Beschreibung | Grundursache | Ergriffene Maßnahme | Status | Wirksam? |
|:------:|-------------|------------|-------------|:------:|:----------:|
| CA-_[#]_ | _[Beschreibung]_ | _[Grundursache]_ | _[Maßnahme]_ | ☐ Offen / ✅ Geschlossen | ☐ Ja / ☐ Nein |

**Referenz:** [REF-13 CAPA-Protokoll](../improvement/capa-log.md)

#### 3e. Interne Auditergebnisse

| Audit-Nr. | Umfang | Datum | Schwere NK | Leichte NK | Beobachtungen | Status |
|:-------:|-------|:----:|:---------:|:---------:|:------------:|:------:|
| A-_[#]_ | _[Abschnitte]_ | _[Datum]_ | _[#]_ | _[#]_ | _[#]_ | _[Status]_ |

**Referenz:** [REF-11 Internes Auditprogramm](internal-audit-program.md)

### 4. Angemessenheit der Ressourcen

| Ressourcenbereich | Aktueller Status | Identifizierte Lücke | Erforderliche Maßnahme |
|--------------|:-------------:|:--------------:|-----------------|
| Personal | _[Status]_ | _[Lücke]_ | _[Maßnahme]_ |
| Cloud-Infrastruktur | _[Status]_ | _[Lücke]_ | _[Maßnahme]_ |
| Werkzeuge / Lizenzen | _[Status]_ | _[Lücke]_ | _[Maßnahme]_ |
| Schulungsbudget | _[Status]_ | _[Lücke]_ | _[Maßnahme]_ |

### 5. Überprüfung von Risiken und Chancen

| Top-Risiken (nach Bewertung) | Bewertung | Mitigationsstatus | Änderung seit letzter Überprüfung |
|----------------------|:-----:|:-----------------:|:------------------------:|
| _[Risiko aus REF-06]_ | _[#]_ | _[Status]_ | ↑↓→ |
| | | | |

**Referenz:** [REF-06 Risikoregister](../planning/risk-register.md)

### 6. Verbesserungsmöglichkeiten

| # | Verbesserungsvorschlag | Quelle | Erwarteter Nutzen | Entscheidung |
|---|---------------------|--------|------------------|----------|
| 1 | _[Vorschlag]_ | _[Retro/Audit/Feedback]_ | _[Nutzen]_ | ☐ Genehmigt / ☐ Zurückgestellt / ☐ Abgelehnt |
| | | | | |

---

## Ergebnisse / Entscheidungen (ISO 9001:2015, Abschnitt 9.3.3)

### Getroffene Entscheidungen

| # | Entscheidung | Verantwortlich | Fälligkeitsdatum |
|---|----------|-------|:--------:|
| D-_[#]_ | _[Entscheidung]_ | _[Name]_ | _[Datum]_ |
| | | | |

### Maßnahmen

| # | Maßnahme | Verantwortlich | Fälligkeitsdatum | Priorität |
|---|--------|-------|:--------:|:--------:|
| MR-_[#]_ | _[Maßnahme]_ | _[Name]_ | _[Datum]_ | Hoch/Mittel/Niedrig |
| | | | | |

### Ressourcenzuweisungen

| Ressource | Zuweisungsentscheidung | Betrag/Detail |
|----------|-------------------|---------------|
| _[Ressource]_ | _[Entscheidung]_ | _[Detail]_ |

### Änderungen am QMS

| Änderung | Grund | Wirksamkeitsdatum |
|--------|--------|:--------------:|
| _[Änderung]_ | _[Grund]_ | _[Datum]_ |

---

## Nächste Managementbewertung

| Datum | Schwerpunktbereiche |
|------|------------|
| _[Datum]_ | _[Besondere Schwerpunktbereiche für die nächste Bewertung]_ |

---

**Protokoll genehmigt durch:**

_________________________
[Name des Abteilungsleiters] — Datum: TT.MM.JJJJ

---

*ISO 9001:2015 Referenz: Abschnitt 9.3*
