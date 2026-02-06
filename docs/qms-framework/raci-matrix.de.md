# REF-05: RACI-Matrix

## DDD Unit — QMS-Rollen und Verantwortlichkeiten

**Dokumentenverantwortlicher:** QMB
**Letzte Überprüfung:** TT.MM.JJJJ
**Nächste Überprüfung:** TT.MM.JJJJ

---

## Legende

| Buchstabe | Bedeutung | Beschreibung |
|-----------|-----------|-------------|
| **R** | Responsible (Durchführung) | Führt die Arbeit aus |
| **A** | Accountable (Verantwortlich) | Letztverantwortlich (einer pro Aktivität) |
| **C** | Consulted (Konsultiert) | Gibt Input vor der Entscheidung |
| **I** | Informed (Informiert) | Wird nach der Entscheidung benachrichtigt |

---

## 1. QMS-Managementaktivitäten

| Aktivität | Unit Lead | QMB | Team Lead | Scrum Master | Product Owner | Entwickler | DevOps |
|-----------|:---------:|:---:|:---------:|:------------:|:-------------:|:----------:|:------:|
| Genehmigung der Qualitätspolitik | **A** | R | I | I | I | I | I |
| Management Review | **A** | R | C | I | C | I | I |
| Definition des QMS-Geltungsbereichs | **A** | R | C | | C | | |
| Planung interner Audits | C | **A**/R | C | | | | |
| Durchführung interner Audits | I | **A** | R | | | | |
| Pflege des Risikoregisters | **A** | R | C | | C | | |
| Festlegung der Qualitätsziele | **A** | R | C | | C | | |
| CAPA-Management | I | **A**/R | R | | | R | |
| Dokumentenlenkung | I | **A**/R | C | | | | |
| Kontinuierliche Verbesserung | **A** | R | R | R | R | R | R |

## 2. Kernprozessaktivitäten

| Aktivität | Unit Lead | QMB | Team Lead | Scrum Master | Product Owner | Entwickler | DevOps | QA |
|-----------|:---------:|:---:|:---------:|:------------:|:-------------:|:----------:|:------:|:--:|
| Identifikation der Interessenparteien | C | I | C | | **A**/R | | | |
| Anforderungsmanagement | I | | C | C | **A**/R | C | | |
| Architektur & Design | I | | **A** | | C | R | C | C |
| Sprint-Planung | | | C | **A**/R | R | R | | |
| Entwicklung (Programmierung) | | | C | | | **A**/R | | |
| Code Review | | | R | | | **A**/R | | |
| Test & Validierung | | I | C | | C | R | | **A**/R |
| Release & Deployment | I | I | **A** | | I | C | R | C |
| Störungsmanagement | I | I | **A** | | I | R | R | |
| SLA-Überwachung | I | C | **A** | | I | | R | |

## 3. Unterstützungsprozessaktivitäten

| Aktivität | Unit Lead | QMB | Team Lead | HR | DevOps | Entwickler |
|-----------|:---------:|:---:|:---------:|:--:|:------:|:----------:|
| Kompetenzmanagement | **A** | I | R | C | | |
| Schulungsplanung | C | I | **A**/R | C | | |
| Onboarding neuer Mitglieder | I | | **A**/R | R | | C |
| Infrastrukturmanagement | I | | C | | **A**/R | |
| Lieferantenbewertung | **A** | C | R | | C | |
| Kommunikationsmanagement | **A** | R | C | | | |

---

## 4. Wichtige Rollendefinitionen

### Unit Lead
- Gesamtverantwortung für die Wirksamkeit des QMS
- Genehmigt Qualitätspolitik und -ziele
- Leitet das Management Review
- Stellt Ressourcen für Qualitätsaktivitäten bereit

### Qualitätsmanagementbeauftragter (QMB)
- Tägliche QMS-Koordination
- Verwaltet das Dokumentenlenkungssystem
- Plant und koordiniert interne Audits
- Verfolgt CAPAs und Verbesserungsmaßnahmen
- Berichtet über die QMS-Leistung an das Management

### Team Lead
- Verantwortlich für die Qualitätspraktiken auf Teamebene
- Stellt die Kompetenz der Teammitglieder sicher
- Verantwortet die operativen Prozesse des Teams

### Scrum Master
- Moderiert Agile-Zeremonien
- Treibt Verbesserungsmaßnahmen aus Retrospektiven voran
- Beseitigt Hindernisse für Qualität

### Product Owner
- Definiert und priorisiert Anforderungen
- Vertritt die Stimme des Kunden
- Akzeptiert/lehnt Lieferergebnisse ab

### Quality Champion (pro Team)
- Fördert das Qualitätsbewusstsein innerhalb des Teams
- Erster Ansprechpartner für QMS-Fragen
- Unterstützt den QMB bei der Auditvorbereitung

---

## 5. Überprüfungsprotokoll

| Datum | Prüfer | Vorgenommene Änderungen |
|-------|--------|-------------------------|
| TT.MM.JJJJ | _[Name]_ | Erstmalige Erstellung |

---

*ISO 9001:2015 Referenz: Abschnitt 5.3*
