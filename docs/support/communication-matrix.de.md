# REF-09: Kommunikationsmatrix

## DDD-Einheit — Data Driven Development | AD/ADAS Tooling

**Dokumentenverantwortlicher:** Qualitätsmanagementbeauftragter (QMB)
**Letzte Überprüfung:** TT.MM.JJJJ
**Nächste Überprüfung:** TT.MM.JJJJ

---

## 1. Zweck

Definiert die internen und externen Kommunikationsanforderungen für das QMS, wie von ISO 9001:2015 Abschnitt 7.4 gefordert.

---

## 2. Interne Kommunikation

| Was | Zweck | Wann | Von | An | Wie | Aufzeichnungen |
|------|---------|------|------|-----|-----|---------|
| Daily Standup | Teamarbeit synchronisieren, Hindernisse aufdecken | Täglich (15 Min.) | Teammitglieder | Team | MS Teams / persönlich | Jira-Board-Aktualisierungen |
| Sprint Planning | Sprint-Umfang und -Ziele vereinbaren | Alle 2 Wochen | PO + SM | Team | Meeting | Sprint-Backlog in Jira |
| Sprint Review / Demo | Abgeschlossene Arbeit den Stakeholdern vorführen | Alle 2 Wochen | Team | Stakeholder | Meeting + Aufzeichnung | Demo-Notizen, Jira-Aktualisierungen |
| Sprint-Retrospektive | Verbesserungen identifizieren | Alle 2 Wochen | SM | Team | Meeting (Miro/FunRetro) | Retro-Maßnahmen in Jira |
| Teamleiter-Sync | Teamübergreifende Abstimmung, KPI-Überprüfung | Wöchentlich | Teamleiter | Abteilungsleiter | Meeting | Besprechungsprotokoll |
| All-Hands | Abteilungsupdates, Strategie, Qualitätskennzahlen | Monatlich | Abteilungsleiter | Alle Teammitglieder | Meeting + Präsentation | Präsentationsunterlagen |
| Qualitätspolitik- & Ziele-Update | Bewusstsein und Abstimmung | Vierteljährlich | QMB | Alle Teammitglieder | All-Hands / E-Mail | Präsentation, Bestätigung |
| Managementbewertung | QMS-Leistungsüberprüfung | Vierteljährlich | QMB + Abteilungsleiter | Managementteam | Formelles Meeting | Protokoll der Managementbewertung |
| Interne Auditergebnisse | Feststellungen und Maßnahmen teilen | Nach jedem Audit | QMB | Auditierte Teams + Management | Bericht + Meeting | Auditbericht |
| Störungsmeldung | Warnung bei Produktionsstörungen | Nach Bedarf (sofort) | Bereitschaftsingenieur | Team + Management | PagerDuty + Slack/Teams | Störungsticket |
| Post-Mortem / Lessons Learned | Erkenntnisse aus Störungen teilen | Innerhalb von 5 Tagen nach Störung | Störungsverantwortlicher | Alle relevanten Beteiligten | Meeting + Dokument | Post-Mortem-Bericht |
| Onboarding | QMS, Prozesse, Werkzeuge vorstellen | Erste Woche des neuen Mitarbeiters | Teamleiter + QMB | Neues Teammitglied | Onboarding-Checkliste | Unterschriebene Bestätigung |

---

## 3. Externe Kommunikation (an andere BMW Group-Einheiten)

| Was | Zweck | Wann | Von | An | Wie | Aufzeichnungen |
|------|---------|------|------|-----|-----|---------|
| Release Notes | Kunden über Änderungen informieren | Jedes Release | DevOps / PO | AD/ADAS-Teams (Kunden) | Confluence + E-Mail | Release-Notes-Seite |
| SLA-Berichte | Über Serviceleistung berichten | Monatlich | SRE-Team | Plattformnutzer | Dashboard + E-Mail | SLA-Bericht |
| Dienststörungsmeldung | Kunden über Ausfälle benachrichtigen | Nach Bedarf (sofort) | Bereitschaftsingenieur | Betroffene Kunden | Slack/Teams-Kanal + E-Mail | Störungsticket |
| Roadmap-Vorstellung | Abstimmung zu kommenden Funktionen | Vierteljährlich | PO | Kunden-Stakeholder | Präsentation | Roadmap-Dokument |
| Kundenfeedback-Erhebung | Zufriedenheitsdaten sammeln | Vierteljährlich | PO | AD/ADAS-Teams | Umfrage (NPS) | Umfrageergebnisse |
| Sicherheitsvorfall-Bericht | Verpflichtende Meldung | Nach Bedarf | Sicherheitsbeauftragter | InfoSec-Team, Datenschutzbeauftragter | Formeller Bericht | Vorfallakte |
| Auditergebnisse (an BMW QM) | Über QMS-Status berichten | Jährlich | QMB | BMW Group QM | Formeller Bericht | Auditzusammenfassung |

---

## 4. Kommunikationskanäle

| Kanal | Anwendungsfall | Zielgruppe | Aufbewahrung |
|---------|----------|----------|-----------|
| **MS Teams / Slack** | Tägliche Kommunikation, kurze Fragen | Teamintern | Gemäß Aufbewahrungsrichtlinie |
| **Confluence** | Dokumentation, Verfahren, Richtlinien, Release Notes | Team + Kunden | Unbegrenzt (versioniert) |
| **Jira** | Arbeitsverfolgung, Störungen, CAPAs | Teamintern | Unbegrenzt |
| **E-Mail** | Formelle Kommunikation, Genehmigungen, externe Benachrichtigungen | Nach Bedarf | Gemäß Aufbewahrungsrichtlinie |
| **PagerDuty** | Störungsalarmierung | Bereitschaftsteam | 12 Monate |
| **Grafana Dashboards** | KPI-Sichtbarkeit | Team + Management | Metrik-Aufbewahrungszeitraum |
| **All-Hands-Meetings** | Abteilungsweite Ankündigungen | Alle Teammitglieder | Präsentationen archiviert |

---

## 5. Überprüfungsprotokoll

| Datum | Prüfer | Vorgenommene Änderungen |
|------|----------|-------------|
| TT.MM.JJJJ | [Name] | Erstmalige Erstellung |

---

*ISO 9001:2015 Referenz: Abschnitt 7.4*
