from datetime import datetime, timezone
from fastapi import HTTPException
from src.models.error import ErrorResponse

def sensor_not_found(sensor_id: str):
    return HTTPException(
        status_code=404,
        detail={
            "error": "SENSOR_NOT_FOUND",
            "message": f"Sensor {sensor_id} does not exist",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )