import logging
import os

logger = logging.getLogger("sensor_monitor")

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler()
        ]   
    )
    return logger

def alert_sensor(sensor_id, status_info):
    state = status_info["state"]
    severity = status_info["severity"]
    last_seen = status_info["last_seen_sec"]
    
    if state == "ACTIVE":
        logger.info(f"[OK] {sensor_id} active | last seen {last_seen}s ago")

    elif state == "STALE":
        logger.warning(f"[STALE] {sensor_id} | severity = {severity} | last seen {last_seen}s ago")

    elif state == "DEAD":
        logger.error(f"[DEAD] {sensor_id} | severity = {severity} | last seen {last_seen}s ago")