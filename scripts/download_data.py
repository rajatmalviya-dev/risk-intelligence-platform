from pathlib import Path

from ucimlrepo import fetch_ucirepo

DATASET_ID = 350
OUTPUT_DIR = Path("data/raw")
OUTPUT_FILE = OUTPUT_DIR / "default_of_credit_card_clients.csv"


def main() -> None:
    dataset = fetch_ucirepo(id=DATASET_ID)

    data = dataset.data.features.copy()
    target = dataset.data.targets.copy()

    data[target.columns[0]] = target.iloc[:, 0]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT_FILE, index=False)

    print(f"Dataset: {dataset.metadata.name}")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
