from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "tasks.json"

def save_tasks(tasks: list[dict]) -> None:
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks() -> list[dict]:
    try:
        with open(DATA_FILE, "r") as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        return []