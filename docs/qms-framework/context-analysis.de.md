# REF-01: Kontextanalyse (SWOT)

=== ":material-lightning-bolt: Schnell (~1 Std.)"

    **ISO 9001 Abschnitt 4.1** | **Verantwortlich:** Unit Lead

    ## Kernergebnisse

    - **Stärken:** Tiefe AD/ADAS-Expertise, starke DevOps-Kultur, Cloud-native Architektur
    - **Schwächen:** Schnelles Wachstum verursacht Wissenssilos, technische Schulden, wenig formale QMS-Doku
    - **Chancen:** Wachsender AD-Markt, datengetriebene Entwicklung, Cloud-Innovation
    - **Risiken:** Evolvierende Regulierung (EU AI Act), Cloud-Kosten, Talentwettbewerb

    > Antworthinweis: \"Wir führen quartalsweise Kontextbewertungen im Rahmen der Managementbewertung durch.\"

=== ":material-book-open-variant: Wesentlich (~3 Std.)"

    **ISO 9001 Abschnitt 4.1** | **Verantwortlich:** Unit Lead

    ## SWOT-Analyse

    ### Stärken

    | Nr. | Stärke | Auswirkung auf QMS |
    |-----|----------|-------------------|
    | S1 | Tiefe AD/ADAS-Datenpipeline-Expertise | Hochwertige, zweckmäßige Werkzeuge |
    | S2 | Starke Agile/DevOps-Kultur mit CI/CD | Schnelle, zuverlässige Lieferung |
    | S3 | Direkter Zugang zu realen Fahrdaten | Realistische Validierung und Tests |
    | S4 | Cloud-native Architektur (IaC) | Reproduzierbarkeit, Auditierbarkeit |

    ### Schwächen

    | Nr. | Schwäche | Gegenmaßnahme |
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

    | Nr. | Risiko | Gegenmaßnahme |
    |-----|--------|----------------|
    | T1 | Regulierung (EU AI Act) | Regulierungsmonitoring |
    | T2 | Cloud-Kostenanstieg | FinOps-Praktiken |
    | T3 | Cybersicherheitsbedrohungen | Security-Härtung |
    | T4 | Talentwettbewerb | Attraktive Arbeitsbedingungen |

=== ":material-book-open-page-variant: Vollständig"

    ## DDD Unit — Data Driven Development | AD/ADAS Tooling

    **Dokumentenverantwortlicher:** Unit Lead
    **Letzte Überprüfung:** TT.MM.JJJJ
    **Nächste Überprüfung:** TT.MM.JJJJ
    **Genehmigt durch:** _[Name]_

    ---

    ## 1. Zweck

    Dieses Dokument erfasst die internen und externen Themen, die die Fähigkeit der DDD-Einheit beeinflussen, die beabsichtigten Ergebnisse des QMS zu erreichen, wie von ISO 9001:2015 Abschnitt 4.1 gefordert.

    ---

    ## 2. SWOT-Analyse

    ### Stärken (Intern, Positiv)

    | # | Stärke | Auswirkung auf das QMS |
    |---|--------|------------------------|
    | S1 | Tiefgehende Fachkompetenz in AD/ADAS-Datenpipelines | Ermöglicht hochwertiges, zweckgerechtes Tooling |
    | S2 | Starke Agile/DevOps-Kultur mit CI/CD-Reife | Unterstützt schnelle, zuverlässige Bereitstellung und Änderungsmanagement |
    | S3 | Direkter Zugang zu realen Fahrdaten (Flotte) | Ermöglicht realistische Validierung und Prüfung unserer Tools |
    | S4 | Cloud-native Architektur (Infrastructure-as-Code) | Unterstützt Reproduzierbarkeit, Auditierbarkeit, Skalierbarkeit |
    | S5 | Eingebettet in das Ökosystem der Mutterorganisation | Zugang zu gemeinsamen Plattformen, Standards und Unterstützungsfunktionen |
    | S6 | *_[Ausfüllen]_* | |

    ### Schwächen (Intern, Negativ)

    | # | Schwäche | Auswirkung auf das QMS | Gegenmaßnahme |
    |---|----------|------------------------|----------------|
    | W1 | Schnelles Teamwachstum → Wissenssilos | Risiko inkonsistenter Praktiken | Strukturiertes Onboarding, Dokumentation, Pair Programming |
    | W2 | Technische Schulden in Legacy-Komponenten | Beeinträchtigt Zuverlässigkeit und Wartbarkeit | Dedizierte Tech-Debt-Sprints, Refactoring-OKRs |
    | W3 | Bisher begrenzte formale QMS-Dokumentation | Lücke bei der Auditbereitschaft | Diese Initiative — Aufbau der QMS-Dokumentation |
    | W4 | Abhängigkeit von Schlüsselpersonen für kritische Systeme | Bus-Faktor-Risiko | Cross-Training, Dokumentation, Runbooks |
    | W5 | *_[Ausfüllen]_* | | |

    ### Chancen (Extern, Positiv)

    | # | Chance | Potenzieller Nutzen |
    |---|--------|---------------------|
    | O1 | Wachsender AD/ADAS-Markt und regulatorischer Druck zur Validierung | Steigende Nachfrage nach unseren Tooling-Dienstleistungen |
    | O2 | Branchenweite Verlagerung zur datengetriebenen Entwicklung | Positioniert unsere Einheit als strategischen Enabler |
    | O3 | Innovationen der Cloud-Anbieter (GPU-Instanzen, Managed-ML-Services) | Kann die Tool-Leistung verbessern und Kosten senken |
    | O4 | Wachstum des Open-Source-Ökosystems im AD-Bereich (ROS2, OpenAD Kit) | Nutzung von Community-Tools, Reduzierung des Entwicklungsaufwands |
    | O5 | *_[Ausfüllen]_* | |

    ### Risiken (Extern, Negativ → Bedrohungen)

    | # | Risiko | Potenzielle Auswirkung | Gegenmaßnahme |
    |---|--------|------------------------|----------------|
    | T1 | Sich entwickelnde regulatorische Landschaft (EU AI Act, UN R157) | Kann Tool-Requalifizierung erfordern | Regulatorische Beobachtung, proaktive Compliance |
    | T2 | Steigende Cloud-Kosten | Budgetdruck | FinOps-Praktiken, Kostenoptimierung |
    | T3 | Cybersicherheitsbedrohungen für Dateninfrastruktur | Risiko für Datenintegrität/-verfügbarkeit | Sicherheitshärtung, Penetrationstests |
    | T4 | Wettbewerb um Talente im AD/ML-Bereich | Schwierigkeiten, qualifizierte Ingenieure zu halten | Wettbewerbsfähige Vergütung, interessante Arbeit, Lernkultur |
    | T5 | Änderungen der Sensortechnologie erfordern Pipeline-Neugestaltung | Überarbeitung der Datenaufnahme/-verarbeitung | Modulare Architektur, Abstraktionsschichten |
    | T6 | *_[Ausfüllen]_* | | |

    ---

    ## 3. PESTLE-Analyse (Externe Faktoren)

    | Faktor | Kernthemen | Relevanz |
    |--------|-----------|----------|
    | **Politisch** | Staatliche AD-Regulierung, EU-Gesetzgebung | Beeinflusst Validierungsanforderungen |
    | **Wirtschaftlich** | Cloud-Kosten, Halbleiterpreise, OEM-Budgetzyklen | Beeinflusst Ressourcenverfügbarkeit |
    | **Sozial** | Öffentliches Vertrauen in autonomes Fahren, Erwartungen der Belegschaft | Beeinflusst Nachfrage und Talentgewinnung |
    | **Technologisch** | Neue Sensortypen, KI/ML-Fortschritte, Rechenleistungsentwicklung | Beeinflusst Tool-Anforderungen |
    | **Rechtlich** | GDPR, Produkthaftung für AD, Schutz geistigen Eigentums | Beeinflusst Datenverarbeitung und Tool-Qualifizierung |
    | **Umwelt** | Nachhaltigkeitsziele, energieeffizientes Computing | Beeinflusst Infrastrukturentscheidungen |

    ---

    ## 4. Überprüfungsprotokoll

    | Datum | Prüfer | Vorgenommene Änderungen |
    |-------|--------|-------------------------|
    | TT.MM.JJJJ | _[Name]_ | Erstmalige Erstellung |
    | | | |

    ---

    *ISO 9001:2015 Referenz: Abschnitt 4.1*
