import json
from pathlib import Path


def load_records(filepath: str = "students_records.json") -> list[dict]:
    path = Path(filepath)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError) as e:
        print(f"Warning: Could not load '{filepath}' ({e}). Starting with an empty list.")
        return []


def save_records(records: list[dict], filepath: str = "students_records.json") -> None:
    path = Path(filepath)
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)
        print(f"Records saved to '{filepath}'.")
    except OSError as e:
        print(f"Error saving to '{filepath}': {e}")