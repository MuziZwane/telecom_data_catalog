"""Framework-neutral route handlers for catalog operations."""

from __future__ import annotations

from typing import Any

CatalogRecord = dict[str, Any]


def search_datasets(catalog: list[CatalogRecord], query: str) -> list[CatalogRecord]:
    """Return datasets whose name or description contains the query."""
    normalized_query = query.casefold()
    return [
        dataset
        for dataset in catalog
        if normalized_query in dataset.get("name", "").casefold()
        or normalized_query in dataset.get("description", "").casefold()
    ]


def get_dataset(catalog: list[CatalogRecord], dataset_name: str) -> CatalogRecord | None:
    """Return a dataset by name."""
    return next((dataset for dataset in catalog if dataset.get("name") == dataset_name), None)


def get_lineage(dataset: CatalogRecord) -> list[dict[str, Any]]:
    """Return lineage edges for a dataset."""
    return dataset.get("lineage", [])


def get_quality(dataset: CatalogRecord) -> dict[str, Any]:
    """Return quality metrics for a dataset."""
    return dataset.get("quality", {})


def get_freshness(dataset: CatalogRecord) -> str | None:
    """Return the dataset freshness timestamp."""
    return dataset.get("freshness")
