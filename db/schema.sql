CREATE TABLE datasets (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    source TEXT NOT NULL,
    format TEXT NOT NULL,
    owner TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dataset_fields (
    id INTEGER PRIMARY KEY,
    dataset_id INTEGER NOT NULL REFERENCES datasets(id),
    name TEXT NOT NULL,
    data_type TEXT NOT NULL,
    description TEXT,
    nullable INTEGER DEFAULT 1,
    ordinal_position INTEGER
);

CREATE TABLE lineage_edges (
    id INTEGER PRIMARY KEY,
    upstream_dataset_id INTEGER NOT NULL REFERENCES datasets(id),
    downstream_dataset_id INTEGER NOT NULL REFERENCES datasets(id),
    transformation TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE quality_metrics (
    id INTEGER PRIMARY KEY,
    dataset_id INTEGER NOT NULL REFERENCES datasets(id),
    metric_name TEXT NOT NULL,
    metric_value REAL NOT NULL,
    measured_at TEXT NOT NULL
);

CREATE TABLE freshness_observations (
    id INTEGER PRIMARY KEY,
    dataset_id INTEGER NOT NULL REFERENCES datasets(id),
    observed_at TEXT NOT NULL,
    source_updated_at TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE glossary_terms (
    id INTEGER PRIMARY KEY,
    term TEXT NOT NULL UNIQUE,
    definition TEXT NOT NULL,
    steward TEXT,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
