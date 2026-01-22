from src.sensor import Sensor
from src.storage import FileStorage
import time

def main():
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
                print("📡", reading)
                storage.save(reading)

            time.sleep(1)

    except KeyboardInterrupt:
        print("🛑 Stopped")

if __name__ == "__main__":
    main()

