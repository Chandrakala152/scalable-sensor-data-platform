import time

def simulate_sensor_stream(sensor, interval=1):
    while True:
        reading=sensor.generate_reading()
        print(reading)  
        time.sleep(interval)