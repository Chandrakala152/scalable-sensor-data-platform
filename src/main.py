from src.sensor import Sensor
from src.storage import FileStorage
from src.logger import setup_logger
import logging
import time

def main():
    logger= setup_logger()
    logger.info("Sensor system started")

    sensors = [
        Sensor("TEMP_001", "temperature", "C"),
        Sensor("HUM_001", "humidity", "%"),
        Sensor("PRESS_001", "pressure", "hPa")
    ]

    storage = FileStorage()

    try:
        while True:
            for sensor in sensors:
                reading = sensor.generate_reading() 
                logger.info(f"Generated reading: {reading}")
                storage.save(reading)

            time.sleep(1)

    except KeyboardInterrupt:
        logger.warning("Sensor system stopped by user")

    except Exception as e:
        logger.error(f"System crashed: {e}")

if __name__ == "__main__":
    main()

