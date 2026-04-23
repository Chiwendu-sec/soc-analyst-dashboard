import json
from datetime import datetime

def save_json_report(target, results):
    report = {
        "target": target,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": results
    }

    filename = f"scan_report_{target.replace('.', '_')}.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    return filename