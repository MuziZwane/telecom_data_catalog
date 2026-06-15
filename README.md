# Telecom Data Catalog

Telecom Data Catalog is a baseline reference project for inventorying telecom data assets, documenting business meaning, and exposing searchable metadata through an API. It is designed for teams that need a shared view of datasets such as subscriber profiles, billing events, network usage, device activations, churn features, and customer care interactions.

## Goals

- Discover datasets and capture technical metadata such as schema, row counts, and freshness.
- Store catalog records, lineage relationships, data quality summaries, and glossary terms in a metadata database.
- Provide API endpoints for search, dataset lookup, lineage, quality, and freshness checks.
- Include examples and tests that make future implementation work easy to extend.

## Architecture Overview

The project is organized into four major layers:

1. **Metadata collector** scans source datasets and produces normalized metadata records.
2. **Metadata database** stores datasets, schema fields, lineage edges, quality metrics, and freshness observations.
3. **REST API** exposes catalog operations for applications, analysts, and governance workflows.
4. **Documentation and examples** define telecom terminology, architecture expectations, and sample metadata.

See [`docs/architecture.md`](docs/architecture.md) for component responsibilities and extension points.

## Project Structure

```text
telecom_data_catalog/
├── db/
│   └── schema.sql
├── docs/
│   ├── architecture.md
│   └── glossary.md
├── examples/
│   ├── sample_catalog_metadata.json
│   └── sample_subscribers.csv
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   └── metadata_collector/
│       ├── __init__.py
│       └── scanner.py
└── tests/
    ├── test_api_routes.py
    └── test_scanner.py
```

## Setup

This baseline uses only the Python standard library so it can run in a clean environment.

```bash
python -m pytest
```

Future iterations can add web framework, database, and data platform dependencies in a dedicated dependency file.

## Usage

Run the scanner against a CSV file to collect basic metadata:

```python
from src.metadata_collector import scan_csv

metadata = scan_csv("examples/sample_subscribers.csv", dataset_name="sample_subscribers")
print(metadata)
```

Use the API route helpers as framework-neutral handlers while the project is still in baseline form:

```python
from src.api import search_datasets

results = search_datasets([metadata], query="subscriber")
```

## Development Roadmap

- Add FastAPI or another REST framework for production HTTP endpoints.
- Add persistent database access using the schema in `db/schema.sql`.
- Add source connectors for warehouses, object storage, streaming topics, and BI tools.
- Add lineage extraction and data quality integrations.
- Add authentication, authorization, and governance workflows.
