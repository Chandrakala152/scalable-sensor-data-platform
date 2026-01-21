import os

class FileStorage:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        self.filepath = os.path.join(data_dir, "sensor_data.txt")
        print("📂 Writing to:", self.filepath)

    def save(self, reading):
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(
                f"{reading['timestamp']},"
                f"{reading['sensor_id']},"
                f"{reading['sensor_type']},"
                f"{reading['value']},"
                f"{reading['unit']}\n"
            )

