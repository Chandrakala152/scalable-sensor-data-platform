import json
import logging

def load_sensors_config(filepath="config/sensors.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            sensors = json.load(f)
        logging.info(f"Loaded {len(sensors)} sensors from config")
        return sensors
    
    except Exception as e:
        logging.critical(f"Failed to load sensors config: {e}")
        raise