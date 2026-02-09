import logging

def validate_reading(reading):
    required_fields=[
        "sensor_id",
        "sensor_type",
        "value",
        "unit",
        "timestamp"
    ]

    for field in required_fields:
        if field not in reading:
            logging.error(f"Missing required field: {field}")
            return False
        if not isinstance(reading["sensor_id"], (int, str)):
            logging.error("sensor_id must be int or string")
            return False
        if not isinstance(reading["value"], (int, float)):
            logging.error("value must be numeric")
            return False
        if reading["sensor_type"] == "temperature":
            if not (-50 <= reading["value"] <= 150):
                logging.error("Temperature value out of range (-50 to -150)")
                return False
            if reading["sensor_type"] == "humidity":
                if not (0 <= reading["value"] <= 100):
                    logging.error("Humidity value out of range (0 to 100)")
                    return False
        return True    
            