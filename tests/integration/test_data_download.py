from pathlib import Path

import pandas as pd

DATASET_PATH = Path("data/raw/default_of_credit_card_clients.csv")


def test_downloaded_dataset_contract() -> None:
    assert DATASET_PATH.exists()

    data = pd.read_csv(DATASET_PATH)

    assert data.shape == (30_000, 24)
    assert list(data.columns) == [
        "X1",
        "X2",
        "X3",
        "X4",
        "X5",
        "X6",
        "X7",
        "X8",
        "X9",
        "X10",
        "X11",
        "X12",
        "X13",
        "X14",
        "X15",
        "X16",
        "X17",
        "X18",
        "X19",
        "X20",
        "X21",
        "X22",
        "X23",
        "Y",
    ]

    assert data["Y"].value_counts().sort_index().to_dict() == {
        0: 23_364,
        1: 6_636,
    }
