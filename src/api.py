from fastapi import FastAPI, HTTPException, APIRouter
from src.storage import FileStorage
from src.analysis import AnalysisEngine
from src.time_analysis import classify_sensor
from datetime import datetime, timezone

app = FastAPI(title="Sensor Monitoring API")

api_v1 = APIRouter(prefix="/api/v1")

storage = FileStorage()
analysis_engine = AnalysisEngine(storage)

@api_v1.get("/health")
def get_system_health():
    report = analysis_engine.generate_system_health_report()
    return report

@api_v1.get("/health/summary")
def get_health_summary():
    report = analysis_engine.generate_system_health_report()
    return report["summary"]

@api_v1.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: str):
    report = analysis_engine.generate_system_health_report()
    sensors = report["sensors"]

    if sensor_id not in sensors:
        raise HTTPException(status_code=404, detail="Sensor not found")
    
    return sensors[sensor_id]

@api_v1.get("/export/health")
def export_health():
    return analysis_engine.generate_system_health_report()

@api_v1.get("/")
def root():
    return {
        "message": "Sensor Health API is running",
        "docs": "/docs"
    }

app.include_router(api_v1)
