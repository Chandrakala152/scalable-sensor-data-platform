import os
import json
import logging
from validator import validate_reading 

class FileStorage:
    def __init__(self, filename="sensor_data.json"):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.filepath = os.path.join(self.data_dir, filename)

    def save(self, reading):
        if not validate_reading(reading):
            logging.error("Invalid reading skipped")
            return
        
        try:
            with open(self.filepath, "a", encoding="utf-8") as f:
              json.dump(reading, f)
              f.write("\n")
            logging.info(f"Saved reading from {reading['sensor_id']}")
        except Exception as e:
            logging.error(f"Failed to save reading: {e}")

    def get_latest_readings(self):
        readings = []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    readings.append(json.loads(line))
        except Exception as e:
            logging.error(f"Failed to read readings: {e}")

        return readings