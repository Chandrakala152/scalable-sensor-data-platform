from models.sensor import Sensor
from simulator.generator import simulate_sensor_stream

if __name__ == "__main__":
    temperature_sensor= Sensor(
        sensor_id="TEMP_001",
        sensor_type="temperature",
        unit="C"
    )

simulate_sensor_stream(temperature_sensor)