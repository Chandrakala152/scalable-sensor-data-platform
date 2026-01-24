import os
import json
import logging

class FileStorage:
    def __init__(self, filename="sensor_data.json"):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.filepath = os.path.join(self.data_dir, filename)

    def save(self, reading):
        try:
            with open(self.filepath, "a", encoding="utf-8") as f:
              json.dump(reading, f)
              f.write("\n")
            logging.info(f"Saved reading from {reading['sensor_id']}")
        except Exception as e:
            logging.error(f"Failed to save reading: {e}")