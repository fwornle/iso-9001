# REF-08: Kompetenzmatrix

## DDD-Einheit — Data Driven Development | AD/ADAS Tooling

**Dokumentenverantwortlicher:** Teamleiter + Personalabteilung
**Letzte Überprüfung:** TT.MM.JJJJ
**Nächste Überprüfung:** TT.MM.JJJJ

---

## 1. Zweck

Definiert die erforderlichen Kompetenzen für jede Rolle in der DDD-Einheit und verfolgt die aktuellen Kompetenzniveaus, um Schulungsbedarfe zu ermitteln, wie von ISO 9001:2015 Abschnitt 7.2 gefordert.

---

## 2. Kompetenzskala

| Stufe | Beschreibung | Indikator |
|-------|-------------|-----------|
| 0 | Keine Kenntnisse | Kein Kontakt mit dem Thema |
| 1 | Grundkenntnisse | Versteht Konzepte, kann nicht selbstständig ausführen |
| 2 | Basiskenntnisse | Kann mit Anleitung/Unterstützung ausführen |
| 3 | Anwender | Kann selbstständig ausführen |
| 4 | Experte | Kann andere schulen, treibt Verbesserungen im Bereich voran |

---

## 3. Rollenbezogene Kompetenzanforderungen

### 3.1 Technische Kompetenzen

| Kompetenz | Data Engineer | Backend Dev | DevOps/SRE | QA Engineer | Tech Lead | Product Owner |
|-----------|:------------:|:-----------:|:----------:|:-----------:|:---------:|:------------:|
| Python / Datenverarbeitung | 4 | 3 | 2 | 3 | 3 | 1 |
| Cloud-Architektur (AWS/Azure) | 3 | 2 | 4 | 2 | 3 | 1 |
| Infrastructure-as-Code (Terraform/SST) | 2 | 1 | 4 | 1 | 3 | 0 |
| CI/CD Pipelines | 2 | 3 | 4 | 3 | 3 | 1 |
| Containerisierung (Docker/K8s) | 2 | 3 | 4 | 2 | 3 | 0 |
| Datenbanksysteme | 3 | 3 | 2 | 2 | 3 | 1 |
| Datenpipeline (Spark/Airflow) | 4 | 2 | 1 | 2 | 3 | 1 |
| API-Design & -Entwicklung | 2 | 4 | 2 | 3 | 3 | 1 |
| Testen & Qualitätssicherung | 2 | 3 | 2 | 4 | 3 | 1 |
| Sicherheitspraktiken | 2 | 2 | 3 | 2 | 3 | 1 |
| Monitoring & Observability | 2 | 2 | 4 | 2 | 3 | 1 |

### 3.2 Fachkompetenzen

| Kompetenz | Data Engineer | Backend Dev | DevOps/SRE | QA Engineer | Tech Lead | Product Owner |
|-----------|:------------:|:-----------:|:----------:|:-----------:|:---------:|:------------:|
| AD/ADAS-Domänenwissen | 3 | 2 | 1 | 2 | 3 | 3 |
| Fahrdatenformate (MDF, rosbag) | 4 | 2 | 1 | 2 | 3 | 2 |
| Simulationskonzepte | 3 | 2 | 1 | 3 | 3 | 3 |
| ISO 26262 Tool-Qualifizierung | 2 | 1 | 1 | 3 | 3 | 2 |
| ASPICE-Grundlagen | 1 | 1 | 1 | 2 | 2 | 2 |
| Datenschutz (GDPR) | 2 | 2 | 2 | 2 | 3 | 3 |

### 3.3 Prozess- & Sozialkompetenzen

| Kompetenz | Alle Rollen (Minimum) | Teamleiter | Scrum Master | QMB |
|-----------|:-------------------:|:---------:|:------------:|:---:|
| Agile/Scrum | 2 | 3 | 4 | 2 |
| ISO 9001 QMS-Bewusstsein | 1 | 2 | 2 | 4 |
| Risikomanagement | 1 | 3 | 2 | 4 |
| Kommunikation | 2 | 3 | 4 | 3 |
| Problemlösung | 2 | 3 | 3 | 3 |
| Dokumentation | 2 | 3 | 2 | 4 |

---

## 4. Individuelle Kompetenzverfolgung

> **Anleitung:** Erstellen Sie eine Zeile pro Teammitglied. Bewerten Sie die aktuellen Stufen anhand der Rollenanforderungen. Lücke = Erforderlich - Aktuell. Negativ oder null = keine Lücke. Positiv = Schulungsbedarf.

| Teammitglied | Rolle | Kompetenzbereich | Erforderliche Stufe | Aktuelle Stufe | Lücke | Maßnahmenplan | Zieldatum |
|-------------|------|----------------|:--------------:|:------------:|:---:|------------|-------------|
| _[Ausfüllen]_ | _[Ausfüllen]_ | _[Ausfüllen]_ | _[1-4]_ | _[0-4]_ | _[+/-]_ | _[Schulung/Mentoring/etc.]_ | _[Ausfüllen]_ |
| | | | | | | | |
| | | | | | | | |

---

## 5. Schulungsplan

| Schulungsthema | Zielgruppe | Anbieter | Format | Häufigkeit | Status |
|---------------|----------------|----------|--------|-----------|--------|
| ISO 9001 QMS-Bewusstsein | Alle Teammitglieder | Intern (QMB) | Workshop | Jährlich + Onboarding | ☐ Geplant |
| ISO 26262 Tool-Qualifizierung | QA, Tech Leads | Externe Schulung | Kurs | Nach Bedarf | ☐ Geplant |
| Cloud-Architektur-Zertifizierung | DevOps, Data Eng | AWS/Azure | Online + Prüfung | Jährliche Kohorte | ☐ Geplant |
| Agile/Scrum-Auffrischung | Alle | Scrum Master | Workshop | Jährlich | ☐ Geplant |
| Sicherheitsbewusstsein | Alle | InfoSec-Team | E-Learning | Jährlich (Pflicht) | ☐ Geplant |
| Datenschutz (GDPR) | Alle | Datenschutzbeauftragter | E-Learning | Jährlich (Pflicht) | ☐ Geplant |
| Interne Auditorenschulung | Ausgewählte Mitarbeiter | Extern | 2-Tages-Kurs | Nach Bedarf | ☐ Geplant |
| *[Weitere hinzufügen]* | | | | | |

---

## 6. Kompetenznachweise

Aufzeichnungen zu folgenden Punkten werden geführt:

- **Ausbildung:** Abschlusszeugnisse (HR-System)
- **Schulungen:** Abschlusszertifikate (SuccessFactors / Team-Wiki)
- **Erfahrung:** Projektzuordnungen, Berufserfahrung in Jahren (HR-System)
- **Kompetenzbewertung:** Jährliche Gesprächsprotokolle (Vorgesetztennotizen)
- **Zertifizierungen:** Berufszertifizierungen (Team-Wiki)

---

## 7. Überprüfungsprotokoll

| Datum | Prüfer | Vorgenommene Änderungen |
|------|----------|-------------|
| TT.MM.JJJJ | [Name] | Erstmalige Erstellung |

---

*ISO 9001:2015 Referenz: Abschnitt 7.2*
