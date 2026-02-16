from datetime import datetime, timedelta
from src.time_analysis import classify_sensor, detect_stale_sensors

def test_classify_sensor_active():
    now = datetime.utcnow()
    status = classify_sensor(
        last_seen = now,
        now = now,
        stale_treshold = 10,
        dead_treshold = 30
    )
    assert status["status"] == "ACTIVE"

def test_classify_sensor_stale():
    now = datetime.utcnow()
    last_seen = now - timedelta(seconds=15)
    status = classify_sensor(
        last_seen = last_seen,
        now = now,
        stale_treshold = 10,
        dead_treshold = 30
    )
    assert status["status"] == "STALE"

def test_classify_sensor_dead():
    now = datetime.utcnow()
    last_seen = now - timedelta(seconds=40)
    status = classify_sensor(
        last_seen = last_seen,
        now = now,
        stale_treshold = 10,
        dead_treshold = 30
    )
    assert status["status"] == "DEAD"

def test_detect_stale_sensors():
    now = datetime.utcnow()
    records = {
        "S1": now,
        "S2": now - timedelta(seconds=20),
        "S3": now - timedelta(seconds=50)
    }

    results = detect_stale_sensors(
        records,
        now = now,
        stale_treshold=10,
        dead_treshold=30
    )
    assert results["S1"]["status"] == "ACTIVE"  
    assert results["S2"]["status"] == "STALE"
    assert results["S3"]["status"] == "DEAD"