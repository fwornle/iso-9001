# REF-03: QMS-Geltungsbereich

## DDD Unit — Data Driven Development | AD/ADAS Tooling

**Dokumentenverantwortlicher:** QMB
**Genehmigt durch:** Unit Lead
**Letzte Überprüfung:** TT.MM.JJJJ
**Nächste Überprüfung:** TT.MM.JJJJ

---

## 1. Geltungsbereich des Qualitätsmanagementsystems

### 1.1 Geltungsbereichserklärung

> Das Qualitätsmanagementsystem der Data Driven Development (DDD) Einheit umfasst die **Konzeption, Entwicklung, Bereitstellung, den Betrieb und die Wartung** von:
>
> - **Datenverarbeitungs-Tools** zur Aufnahme, Verarbeitung und Transformation von Fahrdaten aus Flottenfahrzeugen und Simulationsumgebungen
> - **Datenspeicherlösungen** für umfangreiche Fahrdatensätze (Petabyte-Maßstab)
> - **Simulationsumgebungen** (Simulation-as-a-Service) zur Validierung von AD/ADAS-Funktionen
> - **Reprocessing-Pipelines** zur großmaßstäblichen Stapelverarbeitung von Fahrdaten gegen aktualisierte Wahrnehmungs-/Planungsalgorithmen
> - **CI/CD-Toolchains** und Entwicklerproduktivitäts-Tools zur Unterstützung der AD/ADAS-Softwareentwicklung
> - **Datenkatalogisierungs- und Discovery-Plattformen** zur Ermöglichung datengetriebener Entwicklungsworkflows
>
> Diese Produkte und Dienstleistungen werden internen Kunden bereitgestellt: Softwareingenieuren und Funktionsverantwortlichen, die im Bereich Autonomes Fahren (AD) und Fahrerassistenzsysteme (ADAS) innerhalb der BMW Group arbeiten.

### 1.2 Organisatorische Grenzen

| Merkmal | Detail |
|---------|--------|
| **Organisation** | BMW Group |
| **Division** | _[Ausfüllen]_ |
| **Abteilung** | _[Ausfüllen]_ |
| **Einheit** | Data Driven Development (DDD) |
| **Standorte** | _[Primärer Bürostandort(e)]_, Remote-Arbeit |
| **Mitarbeiterzahl** | _[Ausfüllen]_ |

### 1.3 Produkte und Dienstleistungen im Geltungsbereich

| # | Produkt / Dienstleistung | Beschreibung |
|---|--------------------------|-------------|
| 1 | Datenaufnahme-Plattform | Tools zur Erfassung und Verarbeitung von Fahrdaten aus der Fahrzeugflotte |
| 2 | Data Lake / Speicherplattform | Skalierbare Speicherung von Fahrdatensätzen mit Metadatenkatalogisierung |
| 3 | Simulation-as-a-Service | Cloud-basierte Simulationsumgebung zur AD/ADAS-Validierung |
| 4 | Reprocessing-Pipeline | Großmaßstäbliche Stapelverarbeitung aufgezeichneter Fahrdaten |
| 5 | Entwickler-Toolchain | CI/CD, Build-Tools und Entwicklerproduktivitäts-Tools |
| 6 | Datenkatalog | Discovery und Metadatenmanagement für Fahrdatensätze |
| 7 | *_[Weitere Dienstleistungen ergänzen]_* | |

---

## 2. Ausschlüsse

| ISO 9001 Abschnitt | Ausgeschlossene Anforderung | Begründung |
|---------------------|----------------------------|------------|
| 8.5.1 (teilweise) | Herstellung physischer Güter | Wir entwickeln Software-Tools und Cloud-Services; keine physische Fertigung |
| 8.5.5 (teilweise) | Tätigkeiten nach der Lieferung für physische Produkte | Nicht zutreffend — unsere Dienstleistungen sind digital; Nachlieferung wird durch Betrieb & Support abgedeckt |
| 7.1.5.2 | Rückführbarkeit von Messungen auf internationale Normen | Nicht zutreffend — wir führen keine physischen Messungen durch, die metrologische Rückführbarkeit erfordern |

> **Hinweis:** Alle anderen Abschnitte der ISO 9001:2015 sind anwendbar und werden in unserem QMS behandelt.

---

## 3. Anwendbare Normen und Vorschriften

| Norm / Vorschrift | Relevanz |
|-------------------|----------|
| ISO 9001:2015 | Primäre QMS-Norm |
| ISO 26262 (Teil 8, Abschnitt 11) | Tool-Qualifizierung für sicherheitsrelevante Validierung |
| ASPICE | Abstimmung der Entwicklungsprozesse für Automobil-SW |
| GDPR / BDSG | Personenbezogene Daten in Fahraufzeichnungen |
| ISO 21434 | Cybersicherheit in der Automobilentwicklung |
| BMW Group InfoSec-Richtlinien | Interne Anforderungen an die Informationssicherheit |
| EU AI Act | Potenzielle Anwendbarkeit auf KI-basiertes Tooling |

---

## 4. Überprüfungsprotokoll

| Datum | Prüfer | Vorgenommene Änderungen |
|-------|--------|-------------------------|
| TT.MM.JJJJ | _[Name]_ | Erstmalige Erstellung |

---

*ISO 9001:2015 Referenz: Abschnitt 4.3*
