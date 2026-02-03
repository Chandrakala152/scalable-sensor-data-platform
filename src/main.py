from src.sensor import Sensor
from src.storage import FileStorage
from datetime import datetime
from src.logger import setup_logger, alert_sensor
from src.config_loader import load_sensors_config
import logging
import time
from src.time_analysis import detect_stale_sensors

setup_logger()

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
            sensor_status = detect_stale_sensors(storage.get_latest_readings())
            for sensor_id, status_info in sensor_status.items():
                alert_sensor(sensor_id, status_info)

            time.sleep(5)

    except KeyboardInterrupt:
        logger.warning("Sensor system stopped by user")

    except Exception as e:
        logger.error(f"System crashed: {e}")

if __name__ == "__main__":
    main()


