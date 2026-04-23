import json
from datetime import datetime

HISTORY_FILE = "scan_history.json"

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_history(target, results):
    history = load_history()

    history.append({
        "target": target,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": results
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)