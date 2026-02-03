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