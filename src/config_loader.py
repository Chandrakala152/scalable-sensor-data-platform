import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "sensors.json"

def load_sensors_config():
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            sensors = json.load(f)
            logging.info(f"Loaded {len(sensors)} sensors from config")
            return sensors
    
    except Exception as e:
        logging.critical(f"Failed to load sensors config: {e}")
        raise