import random
from datetime import datetime

class Sensor:
    def __init__(self, sensor_id, sensor_type, unit):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.unit = unit

    def generate_reading(self):
        value = round(random.uniform(10, 100), 2)
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "value": value,
            "unit": self.unit,
            "timestamp": datetime.utcnow().isoformat()
        }
