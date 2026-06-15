from src.metadata_collector import scan_csv


def test_scan_csv_returns_schema_row_count_and_freshness():
    metadata = scan_csv("examples/sample_subscribers.csv")

    assert metadata["name"] == "sample_subscribers"
    assert metadata["row_count"] == 3
    assert metadata["format"] == "csv"
    assert metadata["freshness"]
    assert metadata["columns"] == [
        {"name": "subscriber_id", "type": "integer"},
        {"name": "account_id", "type": "integer"},
        {"name": "status", "type": "string"},
        {"name": "activation_date", "type": "date"},
        {"name": "monthly_revenue", "type": "number"},
    ]
