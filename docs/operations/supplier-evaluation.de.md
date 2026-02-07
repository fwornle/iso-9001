# REF-10: Lieferanten- / Anbieterbewertung

=== ":material-lightning-bolt: Schnell (~1 Std.)"

    **ISO 9001 Abschnitt 8.4** | **Verantwortlich:** Tech Lead + Beschaffung

    ## Lieferantenkategorien

    | Kategorie | Beispiele | Bewertung |
    |-----------|----------|-----------|
    | **A — Strategisch** | AWS, Azure, große SaaS | Vollbewertung + jährliches Review |
    | **B — Wichtig** | Drittanbieter-Tools, Beratung | Standardbewertung + periodisches Review |
    | **C — Standard** | Büro-Tools, Open Source | Vereinfachte Bewertung |

    ## Genehmigungsschwellen

    - **>= 4,0:** Genehmigt
    - **3,0-3,9:** Bedingt genehmigt
    - **< 3,0:** Nicht genehmigt

=== ":material-book-open-variant: Wesentlich (~3 Std.)"

    **ISO 9001 Abschnitt 8.4** | **Verantwortlich:** Tech Lead + Beschaffung

    ## Bewertungskriterien

    | Kriterium | Gewichtung |
    |-----------|:----------:|
    | Technische Fähigkeit | 25% |
    | Zuverlässigkeit & SLA | 20% |
    | Sicherheit (ISO 27001, SOC2) | 20% |
    | Kosteneffizienz | 15% |
    | Support & Reaktionsfähigkeit | 10% |
    | Compliance (Lizenz, DSGVO) | 10% |

    ## Überwachung

    | Kategorie | Methode | Frequenz |
    |-----------|---------|----------|
    | A — Strategisch | SLA-Review, Sicherheits-Tracking | Monatlich + jährlich |
    | B — Wichtig | SLA-Check, Bug-/Feature-Tracking | Quartalsweise |
    | C — Standard | Vulnerability-Scanning, Lizenzcheck | Automatisiert |

=== ":material-book-open-page-variant: Vollständig"

    ## DDD-Einheit — Data Driven Development | AD/ADAS Tooling

    **Dokumentenverantwortlicher:** Tech Lead + Beschaffung
    **Letzte Überprüfung:** TT.MM.JJJJ
    **Nächste Überprüfung:** TT.MM.JJJJ

    ---

    ## 1. Zweck

    Definiert den Prozess zur Bewertung, Auswahl und Überwachung externer Anbieter von Produkten und Dienstleistungen, wie von ISO 9001:2015 Abschnitt 8.4 gefordert.

    ---

    ## 2. Lieferantenkategorien

    | Kategorie | Beispiele | Risikostufe | Bewertungstiefe |
    |----------|----------|:----------:|-----------------|
    | **A — Strategisch** | Cloud-Anbieter (AWS, Azure), große SaaS-Plattformen | Hoch | Vollständige Bewertung + jährliche Überprüfung |
    | **B — Wichtig** | Drittanbieter-Tools, kostenpflichtige Bibliotheken, Beratungsdienstleistungen | Mittel | Standardbewertung + regelmäßige Überprüfung |
    | **C — Standard** | Bürowerkzeuge, Standarddienstleistungen, Open-Source-Bibliotheken | Niedrig | Vereinfachte Bewertung |

    ---

    ## 3. Bewertungskriterien

    ### 3.1 Erstbewertung — Scorecard

    | Kriterium | Gewichtung | Bewertung (1-5) | Gewichtete Bewertung |
    |-----------|:------:|:-----------:|:--------------:|
    | **Technische Leistungsfähigkeit** — Erfüllt funktionale Anforderungen | 25% | _[1-5]_ | |
    | **Zuverlässigkeit & Verfügbarkeit** — SLA-Zusagen, Leistungsbilanz | 20% | _[1-5]_ | |
    | **Sicherheitsniveau** — Zertifizierungen (ISO 27001, SOC2), Schwachstellenmanagement | 20% | _[1-5]_ | |
    | **Kosteneffizienz** — Gesamtbetriebskosten | 15% | _[1-5]_ | |
    | **Support & Reaktionsfähigkeit** — SLA für Support, Dokumentationsqualität | 10% | _[1-5]_ | |
    | **Compliance** — Lizenzkompatibilität, regulatorische Compliance, GDPR | 10% | _[1-5]_ | |
    | **Gesamt** | **100%** | | **_[Gesamt]_** |

    **Freigabeschwellenwerte:**
    - ≥ 4,0: Freigegeben
    - 3,0 – 3,9: Bedingt freigegeben (mit dokumentierten Gegenmaßnahmen)
    - < 3,0: Abgelehnt

    ### 3.2 Zusätzliche Kriterien für Open-Source-Komponenten

    | Kriterium | Bewertung |
    |-----------|-----------|
    | Lizenzkompatibilität (MIT, Apache 2.0, etc.) | ☐ Kompatibel |
    | Community-Gesundheit (Aktivität, Maintainer, Issues) | ☐ Aktiv |
    | Historie von Sicherheitslücken | ☐ Akzeptabel |
    | Unternehmens-InfoSec-Freigabe | ☐ Freigegeben |
    | SBOM-Einbindung | ☐ Enthalten |

    ---

    ## 4. Freigegebenes Lieferantenverzeichnis

    | # | Lieferant | Kategorie | Produkt/Dienstleistung | Bewertungsergebnis | Freigabedatum | Nächste Überprüfung | Status |
    |---|----------|:--------:|-----------------|:----------------:|:-------------:|:-----------:|:------:|
    | 1 | AWS | A | Cloud-Infrastruktur | _[Ergebnis]_ | TT.MM.JJJJ | TT.MM.JJJJ | ✅ Freigegeben |
    | 2 | _[Anbieter]_ | B | _[Dienstleistung]_ | _[Ergebnis]_ | TT.MM.JJJJ | TT.MM.JJJJ | ✅ Freigegeben |
    | 3 | _[Anbieter]_ | C | _[Werkzeug]_ | _[Ergebnis]_ | TT.MM.JJJJ | TT.MM.JJJJ | ✅ Freigegeben |
    | | _[Weitere hinzufügen]_ | | | | | | |

    ---

    ## 5. Laufende Überwachung

    ### 5.1 Überwachungsmethoden nach Kategorie

    | Kategorie | Überwachungsmethode | Häufigkeit |
    |----------|------------------|-----------|
    | **A — Strategisch** | SLA-Leistungsüberprüfung, Service-Health-Dashboards, Sicherheitshinweis-Tracking, jährliche Geschäftsüberprüfung | Monatliche Kennzahlen, Jährliche Überprüfung |
    | **B — Wichtig** | SLA-Compliance-Prüfung, Feature-/Bug-Tracking, Sicherheitshinweise | Vierteljährlich |
    | **C — Standard** | Schwachstellenscanning von Abhängigkeiten, Lizenz-Compliance-Prüfung | Automatisiert (kontinuierlich) |

    ### 5.2 Lieferantenleistungsverfolgung

    | Lieferant | Zeitraum | SLA-Einhaltung | Störungen | Sicherheitsprobleme | Supportqualität | Gesamtbewertung | Maßnahme |
    |----------|--------|:--------------:|:---------:|:---------------:|:---------------:|:--------------:|--------|
    | _[Name]_ | Q_/JJJJ | _[%]_ | _[#]_ | _[#]_ | _[1-5]_ | _[1-5]_ | _[Maßnahme bei Bedarf]_ |

    ---

    ## 6. Lieferantenproblem-Eskalation

    ```mermaid
    graph TD
        A["Problem erkannt<br/>(Leistung, Sicherheit, SLA)"] --> B{"Schweregrad?"}
        B -->|Niedrig| C["Im Tracking erfassen<br/>Bei nächster Überprüfung besprechen"]
        B -->|Mittel| D["An Tech Lead eskalieren<br/>Korrekturmaßnahme anfordern"]
        B -->|Hoch/Kritisch| E["An Abteilungsleiter eskalieren<br/>Vertrags-SLA einfordern<br/>Alternativen bewerten"]
        D --> F["Bis zur Lösung verfolgen"]
        E --> G{"Gelöst?"}
        G -->|Ja| F
        G -->|Nein| H["Lieferantenwechsel<br/>in Betracht ziehen"]
    ```

    ---

    ## 7. Überprüfungsprotokoll

    | Datum | Prüfer | Vorgenommene Änderungen |
    |------|----------|-------------|
    | TT.MM.JJJJ | [Name] | Erstmalige Erstellung |

    ---

    *ISO 9001:2015 Referenz: Abschnitt 8.4*
