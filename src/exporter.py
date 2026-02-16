import json
import csv
import logging
import os

def export_json_to_csv(
        json_path="data/sensor_data.json",
        csv_path="data/sensor_data.csv"
):
    if not os.path.exists(json_path):
        logging.error("JSON Data file not found")
        return
    
    with open(json_path,"r", encoding="utf-8") as json_file:
        records= [json.loads(line) for line in json_file if line.strip()]
        
    if not records:
        logging.warning("No records found to export")
        return
    
    fieldnames=records[0].keys()

    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    logging.info(f"Exported {len(records)} records to CSV")

def export_health_report(sensor_status, output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)

    json_path = os.path.join(output_dir, "sensor_health.json")
    csv_path = os.path.join(output_dir, "sensor_health.csv")

    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(sensor_status, jf, indent=2, default=str)

    with open(csv_path, "w", encoding="utf-8") as cf:
        writer = csv.writer(cf)
        writer.writerow([
            "sensor_id",
            "state",
            "severity",
            "last_seen_sec",
            "description"
        ])

        for sensor_id, info in sensor_status.items():
            writer.writerow([
                sensor_id,
                info["state"],
                info["severity"],
                info["last_seen_sec"],
                info["description"]
            ])

        logging.info("Exported Sensor Health Report")