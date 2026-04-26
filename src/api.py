from fastapi import FastAPI, HTTPException, APIRouter, Path, Query
from src.storage import FileStorage
from src.analysis import AnalysisEngine
from src.time_analysis import classify_sensor
from datetime import datetime, timezone
from src.models.health import SystemHealthReport, HealthSummary
from src.models.sensor import SensorResponse
from src.errors import sensor_not_found
from src.logger import logger
from src.schemas import SensorResponse, HealthResponse

app = FastAPI(title="Sensor Monitoring API")

api_v1 = APIRouter(prefix="/api/v1")

storage = FileStorage()
analysis_engine = AnalysisEngine(storage)

@api_v1.get("/health", response_model=HealthResponse)
def get_system_health():
    report = analysis_engine.generate_health_report()
    return report

@api_v1.get("/health/summary", response_model=HealthSummary)
def get_health_summary():
    report = analysis_engine.generate_health_report()
    return report["summary"]

@api_v1.get("/sensors/{sensor_id}", response_model=SensorResponse)
def get_sensor(sensor_id: str = Path(..., min_length=2, max_length=20)):
    logger.info(f"Fetching sensor: {sensor_id}")
    report = analysis_engine.generate_health_report()
    sensors = report["sensors"]

    for sensor in sensors:
        if sensor["sensor_id"] == sensor_id:
            return{
                "sensor_id": sensor["sensor_id"],
                "state": sensor["state"],
                "stats": {
                    "average": sensor["average"],
                    "min": sensor["min"],
                    "max": sensor["max"],
                    "stale": sensor["stale"]
                }
            }   
    logger.warning(f"Sensor not found: {sensor_id}")
    sensor_not_found(sensor_id)

@api_v1.get("/export/health", response_model=SystemHealthReport)
def export_health():
    return analysis_engine.generate_health_report()

@api_v1.get("/")
def root():
    return {
        "message": "Sensor Health API is running",
        "docs": "/docs"
    }

app.include_router(api_v1)


