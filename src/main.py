from sensor import Sensor
from storage import FileStorage
from datetime import datetime, timezone
from logger import setup_logger, alert_sensor
from config_loader import load_sensors_config
import logging
import time
from time_analysis import detect_stale_sensors, latest_reading_per_sensor
from analysis import AnalysisEngine

logging.basicConfig(level=logging.INFO)
setup_logger()

timestamp = datetime.now(timezone.utc).isoformat()

def main():
    logger= setup_logger()
    logger.info("Sensor system started")

    sensors_config = load_sensors_config()

    sensors = [
        Sensor(
            cfg["sensor_id"], 
            cfg["sensor_type"],
            cfg["unit"],
        )
        for cfg in sensors_config
    ]

    storage = FileStorage()

    try:
        while True:
            for sensor in sensors:
                reading = sensor.generate_reading() 
                reading["timestamp"] = datetime.utcnow().isoformat()
                logger.info(f"Generated reading: {reading}")
                storage.save(reading)
                records = storage.get_latest_readings()
                latest_records = latest_reading_per_sensor(records)
            sensor_status = detect_stale_sensors(
                latest_records,
                threshold_seconds=5
            )
            for sensor_id, status_info in sensor_status.items():
                alert_sensor(sensor_id, status_info)

            time.sleep(5)

    except KeyboardInterrupt:
        logger.warning("Sensor system stopped by user")

    except Exception as e:
        logger.error(f"System crashed: {e}")

if __name__ == "__main__":
    main()


