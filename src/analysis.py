import json
from collections import defaultdict

DATA_FILE= "data/sensor_data.json"

def load_records():
    records=[]

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                records.append(json.loads(line))

    return records

def group_by_sensor(records):
    grouped= defaultdict(list)

    for record in records:
        grouped[record["sensor_id"]].append(record["value"])

    return grouped

def calculate_stats(grouped_data):
    stats= {}

    for sensor_id, values in grouped_data.items():
        stats[sensor_id]= {
            "count": len(values),
            "max": max(values),
            "min": min(values),
            "average": round(sum(values) / len(values), 2)
        }

    return stats

def main():
    records= load_records()
    grouped= group_by_sensor(records)
    stats= calculate_stats(grouped)

    for sensor_id, data in stats.items():
        print(sensor_id, "➡", data)

if __name__ == "__main__":
    main()

