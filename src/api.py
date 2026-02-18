from fastapi import FastAPI, HTTPException
from src.storage import FileStorage
from src.analysis import AnalysisEngine
from src.time_analysis import classify_sensor
from datetime import datetime, timezone

app = FastAPI(title="Sensor Monitoring API")

storage = FileStorage()
analysis_engine = AnalysisEngine(storage)

@app.get("/health")
def get_system_health():
    report = analysis_engine.generate_system_health_report()
    return report

@app.get("/health/summary")
def get_health_summary():
    report = analysis_engine.generate_system_health_report()
    return report["summary"]

@app.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: str):
    report = analysis_engine.generate_system_health_report()
    sensors = report["sensors"]

    if sensor_id not in sensors:
        raise HTTPException(status_code=404, detail="Sensor not found")
    
    return sensors[sensor_id]

@app.get("/export/health")
def export_health():
    return analysis_engine.generate_system_health_report()

@app.get("/")
def root():
    return {
        "message": "Sensor Health API is running",
        "docs": "/docs"
    }

