from src.sensor import Sensor
from src.storage import FileStorage
import time

def main():
    sensor = Sensor("TEMP_001", "temperature", "C")
    storage = FileStorage()

    try:
        while True:
            reading = sensor.read()
            print("📡", reading)
            storage.save(reading)
            time.sleep(1)

    except KeyboardInterrupt:
        print("🛑 Stopped")

if __name__ == "__main__":
    main()
