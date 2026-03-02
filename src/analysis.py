import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from statistics import mean
import logging
import os

logger = logging.getLogger(__name__)

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

def filter_last_n_minutes(readings, minutes=5):
    cutoff_time = datetime.utcnow() - timedelta(minutes=minutes)
    return[
        r for r in readings
        if datetime.fromisoformat(r["timestamp"]) >= cutoff_time
    ]

def detect_trend(readings):
    if len(readings) < 2:
        return "STABLE"

    values = [r["value"] for r in readings]
    if values[-1] > values[0]:
        return "RISING"
    elif values[-1] < values[0]:
        return "FALLING"
    else:
        return "STABLE"
        
class AnalysisEngine:
    def __init__(self, storage):
        self.storage = storage

    def get_recent_readings(self, sensor_id, minutes=5):
        readings = self.storage.get_latest_readings()
        cutoff_time = datetime.utcnow() - timedelta(minutes=minutes)
        recent = [
            r for r in readings
            if datetime.fromisoformat(r["timestamp"]) >= cutoff_time
        ]
        logger.info(f"{len(recent)} recent readings found for {sensor_id}")
        return recent
    
    def compute_stats(self, readings):
        timestamps = [
            datetime.fromisoformat(r["timestamp"]) 
            for r in readings
        ]
        latest_ts = max(timestamps) 
        now = datetime.utcnow()
        stale = (now - latest_ts).total_seconds() > 5
        values = [r["value"] for r in readings]
        return {
            "average": sum(values)/ len(values),
            "min": min(values),
            "max": max(values),
            "stale": stale
        }
        
    
    def classify_risk(self, sensor_id):
        stats = self.compute_stats(sensor_id)
        if not stats:
            return {"sensor_id": sensor_id, "risk_level": "NO_DATA"}
        risk = "NORMAL"

        if stats.get("max",0) > 90:
            risk = "CRITICAL"
        elif stats.gets("average",0) > 75:
            risk = "WARNING"
        elif stats.get("trend") == "increasing" and stats.get("average", 0) > 70:
            risk = "WARNING"

        return {
            "sensor_id": sensor_id,
            "risk": risk,
            "stats": stats
        }
    
    def process_sensor(self, sensor_id):
        readings = self.storage.get_latest_readings()
        if not readings:
            return {
                "state": "DEAD",
                "stats": {}
            }
        stats = self.compute_stats(readings)
        print("DEBUG stats:", stats)
        if stats["stale"]:
            state = "STALE"
        else:
            state = "ACTIVE"
        return {
            "state": state,
            "stats": stats
        }
    

    def compute_sensor_status(self):
        sensor_status = {}
        sensors = self.storage.get_all_sensors()
        for sensor_id in sensors:
            result = self.process_sensor(sensor_id)
            sensor_status[sensor_id] = {
                "state": result["state"],
                "stats": result.get("stats", {})
            }
        return sensor_status

    def generate_health_report(self):
        sensor_status = self.compute_sensor_status()
        summary = {
            "ACTIVE": 0,
            "STALE": 0,
            "DEAD": 0
        }
        for _, info in sensor_status.items():
            state = info["state"]
            if state in summary:
                summary[state] += 1

        overall_state = "HEALTHY"
        if summary["DEAD"] > 0:
            overall_state = "CRITICAL"
        elif summary["STALE"] > 0:
            overall_state = "WARNING"

        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "overall_state": overall_state,
            "summary": summary,
            "sensors": sensor_status
        }

        return report
    
def main():
    records= load_records()
    grouped= group_by_sensor(records)
    stats= calculate_stats(grouped)

    for sensor_id, data in stats.items():
        print(sensor_id, "➡", data)

if __name__ == "__main__":
    main()

