import random
from datetime import datetime
import time

class Sensor:
    def __init__(self, sensor_id, sensor_type, unit, location=None):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.unit = unit

    def generate_reading(self):
        if self.sensor_type == "temperature":
            value = round(random.uniform(20, 40), 2)
        elif self.sensor_type == "pressure":
            value = round(random.uniform(90000, 110000), 2)
        elif self.sensor_type == "humidity":
            value = round(random.uniform(30, 70), 2)
        else:
            value = None

        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "value": value,
            "unit": self.unit,
            "timestamp": time.time()
        }
