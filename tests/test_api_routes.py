from src.api import get_dataset, get_freshness, get_lineage, get_quality, search_datasets


CATALOG = [
    {
        "name": "sample_subscribers",
        "description": "Subscriber account status and revenue data.",
        "freshness": "2026-06-15T00:00:00+00:00",
        "quality": {"completeness": 1.0},
        "lineage": [{"upstream": "billing", "downstream": "sample_subscribers"}],
    }
]


def test_search_datasets_matches_name_and_description():
    assert search_datasets(CATALOG, "subscriber") == CATALOG
    assert search_datasets(CATALOG, "revenue") == CATALOG
    assert search_datasets(CATALOG, "network") == []


def test_dataset_lookup_and_metadata_helpers():
    dataset = get_dataset(CATALOG, "sample_subscribers")

    assert dataset is not None
    assert get_freshness(dataset) == "2026-06-15T00:00:00+00:00"
    assert get_quality(dataset) == {"completeness": 1.0}
    assert get_lineage(dataset) == [{"upstream": "billing", "downstream": "sample_subscribers"}]
    assert get_dataset(CATALOG, "missing") is None
