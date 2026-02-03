import json
from collections import defaultdict

DATA_FILE= "data/sensor_data.json"

def load_records():
    records=[]

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                records.append(json.loads(line))

    return records

def group_by_sensor(records):
    grouped= defaultdict(list)

    for record in records:
        grouped[record["sensor_id"]].append(record["value"])

    return grouped

def calculate_stats(grouped_data):
    stats= {}

    for sensor_id, values in grouped_data.items():
        stats[sensor_id]= {
            "count": len(values),
            "max": max(values),
            "min": min(values),
            "average": round(sum(values) / len(values), 2)
        }

    return stats

def system_health_report(sensor_status):
    report = {
        "ACTIVE": 0,
        "STALE": 0,
        "DEAD": 0
    }

    for info in sensor_status.values():
        report[info["state"]] += 1

    return report

def generate_health_alerts(sensor_status):
    alerts = []

    for sensor_id, info in sensor_status.items():
        if info["severity"] in ("WARNING", "ERROR"):
            alert = {
                "sensor_id": sensor_id,
                "state": info["state"],
                "severity": info["severity"],
                "last_seen_seconds": info["last_seen"]
            }
            alerts.append(alert)

    return alerts
    
def main():
    records= load_records()
    grouped= group_by_sensor(records)
    stats= calculate_stats(grouped)

    for sensor_id, data in stats.items():
        print(sensor_id, "➡", data)

if __name__ == "__main__":
    main()

