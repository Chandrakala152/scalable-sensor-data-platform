from src.sensor import Sensor
from src.storage import FileStorage
from datetime import datetime, timezone
from src.logger import setup_logger, alert_sensor
from src.config_loader import load_sensors_config
import logging
import time
from src.time_analysis import detect_stale_sensors, latest_reading_per_sensor
from src.analysis import AnalysisEngine, generate_health_report
from src.exporter import export_health_report, export_system_health_report

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
            health_report = generate_health_report(sensor_status)
            logger.info(f"System Health : {health_report["overall_state"]}")
            export_health_report(sensor_status)
            export_system_health_report(health_report)
            print("\n=== SENSOR HEALTH REPORT ===")
            for sensor_id, info in sensor_status.items():
                print(
                    f"{sensor_id} | "
                    f"state: {info['state']} | "
                    f"severity: {info['severity']} | "
                    f"last seen: {int(info['last_seen_sec'])} sec ago | "
                )
            print("============================\n")

            for sensor_id, info in sensor_status.items():
                if info["severity"] == "ERROR":
                    logger.error(f"{sensor_id} DEAD: {info['description']}")
                elif info["severity"] == "WARNING":
                    logger.warning(f"{sensor_id} STALE: {info['description']}")
                else:
                    logger.info(f"{sensor_id} ACTIVE")
                    
            for sensor_id, status_info in sensor_status.items():
                alert_sensor(sensor_id, status_info)

            time.sleep(5)

    except KeyboardInterrupt:
        logger.warning("Sensor system stopped by user")

    except Exception as e:
        logger.error(f"System crashed: {e}")

if __name__ == "__main__":
    main()


