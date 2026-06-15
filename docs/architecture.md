# Architecture

## Components

### Metadata Collector

The collector scans telecom datasets and records technical metadata:

- Dataset identity and source location.
- Field names and inferred data types.
- Row counts for tabular files.
- Freshness timestamps based on source modification time.

The initial implementation lives in `src/metadata_collector/scanner.py` and focuses on CSV files. Future connectors can target data warehouses, object stores, streaming platforms, and catalog APIs.

### Metadata Database

The metadata database stores catalog entities and relationships. The starter schema in `db/schema.sql` includes tables for datasets, fields, lineage, quality metrics, freshness observations, and glossary terms.

### REST API

The API layer provides operations for:

- Search across datasets and descriptions.
- Dataset lookup by identifier or name.
- Lineage retrieval.
- Quality metric retrieval.
- Freshness status retrieval.

The baseline route helpers in `src/api/routes.py` are framework-neutral so they can be tested without a web server and later wrapped by FastAPI, Flask, or another framework.

### Examples and Tests

The `examples/` directory provides small telecom-oriented sample data and metadata. The `tests/` directory validates scanner behavior and API helper logic.

## Data Flow

1. A collector scans source systems and emits dataset metadata.
2. Metadata is normalized into the catalog schema.
3. API handlers read catalog records and expose them to users and applications.
4. Analysts, engineers, and governance users search, inspect, and enrich catalog assets.

## Extension Points

- Add collector adapters for Snowflake, BigQuery, S3, Kafka, or operational databases.
- Add lineage extractors from orchestration systems and transformation tools.
- Add quality integrations for validation rules, profiling, and anomaly detection.
- Add glossary stewardship workflows for business definitions and ownership.
