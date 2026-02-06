# REF-03: QMS Scope Statement

## DDD Unit — Data Driven Development | AD/ADAS Tooling

**Document Owner:** QMR
**Approved by:** Unit Lead
**Last Review:** YYYY-MM-DD
**Next Review:** YYYY-MM-DD

---

## 1. Scope of the Quality Management System

### 1.1 Scope Statement

> The Quality Management System of the Data Driven Development (DDD) unit covers the **design, development, deployment, operation, and maintenance** of:
>
> - **Data engineering tools** for ingesting, processing, and transforming driving data from fleet vehicles and simulation environments
> - **Data storage solutions** for large-scale driving datasets (petabyte-scale)
> - **Simulation environments** (Simulation-as-a-Service) for AD/ADAS function validation
> - **Reprocessing pipelines** for large-scale batch processing of driving data against updated perception/planning algorithms
> - **CI/CD toolchains** and developer productivity tools supporting AD/ADAS software development
> - **Data cataloguing and discovery** platforms enabling data-driven development workflows
>
> These products and services are provided to internal customers: software engineers and function owners working on Autonomous Driving (AD) and Advanced Driver Assistance Systems (ADAS) within BMW Group.

### 1.2 Organizational Boundaries

| Attribute | Detail |
|-----------|--------|
| **Organization** | BMW Group |
| **Division** | [Your Division] |
| **Department** | [Your Department] |
| **Unit** | Data Driven Development (DDD) |
| **Locations** | [Primary office location(s)], Remote work |
| **Headcount** | [Number] |

### 1.3 Products and Services In Scope

| # | Product / Service | Description |
|---|-------------------|-------------|
| 1 | Data Ingestion Platform | Tools for collecting and processing driving data from vehicle fleet |
| 2 | Data Lake / Storage Platform | Scalable storage for driving datasets with metadata cataloguing |
| 3 | Simulation-as-a-Service | Cloud-based simulation environment for AD/ADAS validation |
| 4 | Reprocessing Pipeline | Large-scale batch reprocessing of recorded driving data |
| 5 | Developer Toolchain | CI/CD, build tools, and developer productivity tools |
| 6 | Data Catalogue | Discovery and metadata management for driving datasets |
| 7 | *[Add additional services]* | |

---

## 2. Exclusions

| ISO 9001 Clause | Excluded Requirement | Justification |
|-----------------|---------------------|---------------|
| 8.5.1 (partial) | Production of physical goods | We develop software tools and cloud services only; no physical manufacturing |
| 8.5.5 (partial) | Post-delivery activities for physical products | Not applicable — our services are digital; post-delivery is covered by operations & support |
| 7.1.5.2 | Measurement traceability to international standards | Not applicable — we do not perform physical measurements requiring metrological traceability |

> **Note:** All other clauses of ISO 9001:2015 are applicable and addressed within our QMS.

---

## 3. Applicable Standards and Regulations

| Standard / Regulation | Relevance |
|----------------------|-----------|
| ISO 9001:2015 | Primary QMS standard |
| ISO 26262 (Part 8, Clause 11) | Tool qualification for safety-related validation |
| ASPICE | Development process alignment for automotive SW |
| GDPR / BDSG | Personal data in driving recordings |
| ISO 21434 | Cybersecurity in automotive development |
| BMW Group InfoSec Policies | Internal information security requirements |
| EU AI Act | Potential applicability to AI-based tooling |

---

## 4. Review Log

| Date | Reviewer | Changes Made |
|------|----------|-------------|
| YYYY-MM-DD | [Name] | Initial creation |

---

*ISO 9001:2015 Reference: Clause 4.3*
