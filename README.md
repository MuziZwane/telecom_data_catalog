# Telecom Data Catalog

Telecom operators often manage data across many countries, brands, and technology stacks. Customer records, call detail records, mobile money activity, recharge events, network metrics, billing data, and sales information may live in separate platforms with different naming conventions, ownership models, freshness expectations, and quality standards. This fragmentation makes it difficult for analysts, engineers, product teams, and governance teams to find trusted datasets, understand their meaning, trace their lineage, and determine whether they are safe to use.

The Telecom Data Catalog provides a centralized metadata layer for discovering, documenting, governing, and monitoring telecom datasets across markets. It helps teams standardize dataset knowledge while still supporting country-specific systems, business rules, and ownership structures.

## Core Features

- **Dataset discovery**: Search and browse datasets across telecom domains, countries, platforms, and data layers.
- **Business glossary**: Define common telecom terms, KPIs, acronyms, and business concepts so teams share a consistent vocabulary.
- **Ownership tracking**: Record data owners, technical stewards, business contacts, support teams, and escalation paths.
- **Column dictionary**: Document column names, data types, descriptions, sensitivity classifications, and business rules.
- **Data lineage**: Show how datasets move from source systems through bronze, silver, and gold layers to downstream consumers.
- **Freshness and quality indicators**: Surface last update times, expected refresh schedules, validation results, completeness checks, and anomaly signals.
- **Dataset certification**: Mark datasets as certified, experimental, deprecated, or under review to guide trusted usage.

## Example Telecom Domains

The catalog can organize metadata for domains such as:

- `cdr`
- `customer`
- `recharge`
- `airtime`
- `momo`
- `sales`
- `network`
- `billing`

## High-Level Architecture

```text
+----------------+      +-----------------------------+
| Source Systems | ---> | Bronze / Silver / Gold Data |
+----------------+      +-----------------------------+
        |                            |
        v                            v
+------------------+       +---------------------+
| Metadata Scanner | ----> | Metadata Repository |
+------------------+       +---------------------+
                                  |
                                  v
                           +--------------+
                           |   REST API   |
                           +--------------+
                                  |
                                  v
                           +--------------+
                           | Catalog UI   |
                           +--------------+
```

### Architecture Components

- **Source systems**: Operational systems, data warehouses, lakehouses, streaming platforms, CRM systems, billing platforms, mobile money systems, and network platforms.
- **Bronze/Silver/Gold layers**: Data lake or warehouse layers that represent raw ingestion, cleaned and conformed data, and curated business-ready datasets.
- **Metadata scanner**: Automated process that extracts schema, ownership, freshness, quality, lineage, and classification metadata from data platforms and pipelines.
- **Metadata repository**: Central store for dataset definitions, column dictionaries, glossary terms, lineage graphs, quality results, freshness metrics, and certification status.
- **REST API**: Programmatic interface for searching metadata, retrieving dataset details, and integrating with other tools.
- **Catalog UI**: User-facing application for exploring datasets, glossary terms, lineage, quality, freshness, and ownership information.

## Example API Endpoints

| Endpoint | Purpose |
| --- | --- |
| `/search` | Search datasets, columns, glossary terms, owners, and domains. |
| `/dataset/{id}` | Retrieve metadata for a specific dataset, including ownership, certification, columns, and descriptions. |
| `/lineage/{dataset_id}` | Retrieve upstream and downstream lineage for a dataset. |
| `/quality/{dataset_id}` | Retrieve quality checks, validation status, and recent quality trends. |
| `/freshness/{dataset_id}` | Retrieve freshness status, last update time, expected schedule, and delay indicators. |

## Intended Users

- Data analysts looking for trusted telecom datasets.
- Data engineers documenting pipelines and dependencies.
- Business teams aligning on KPI definitions and domain terminology.
- Governance teams tracking ownership, certification, quality, and sensitive data.
- Platform teams exposing metadata through APIs and catalog interfaces.

## Outcome

By centralizing telecom metadata, the project reduces duplicated discovery work, improves trust in shared datasets, clarifies ownership, and gives teams a consistent way to understand data across countries and domains.
