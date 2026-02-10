from datetime import datetime, timedelta, timezone
import json
from src.logger import alert_sensor


def load_records(file_path):
    records=[]
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                record["timestamp"] = datetime.fromisoformat(record["timestamp"])
                records.append(record)
    return records

def latest_reading_per_sensor(records):
    latest = {}

    for record in records:
        sensor_id = record["sensor_id"]

    if sensor_id not in latest:
        latest[sensor_id] = record
    else:
        if record["timestamp"] > latest[sensor_id]["timestamp"]:
            latest[sensor_id] = record

    return latest

def detect_stale_sensors(latest_records, threshold_seconds=5):
    now = datetime.now(timezone.utc)
    status = {}

    for sensor_id, record in latest_records.items():

        last_time = record["timestamp"]

        if isinstance(last_time, str):
            last_time = datetime.fromisoformat(last_time)

        if last_time.tzinfo is None:
            last_time = last_time.replace(tzinfo=timezone.utc)

        diff = (now - last_time).total_seconds()

        state, severity = classify_sensor(diff)

        status[sensor_id] = {
            "state": state,
            "severity": severity,
            "last_seen_sec": diff,
            "description": f"Last update {int(diff)} seconds ago"
        }

    return status

def classify_sensor(diff_seconds):
    if diff_seconds <= 5:
        return "ACTIVE", "INFO"
    elif diff_seconds <= 15:
        return "STALE", "WARNING"
    else:
        return "DEAD", "ERROR"

