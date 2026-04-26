from pydantic import BaseModel
from typing import Literal, List
from datetime import datetime

class SensorResponse(BaseModel):
    state: Literal["ACTIVE", "STALE", "DEAD"]
    stats: dict

class ErrorDetail(BaseModel):
    error: str
    message: str
    timestamp: datetime

class ErrorResponse(BaseModel):
    detail: ErrorDetail

class HealthSummary(BaseModel):
    ACTIVE: int
    STALE: int
    DEAD: int

class SensorStats(BaseModel):
    sensor_id:str
    average:float
    min:float
    max:float
    stale:bool

class HealthResponse(BaseModel):
    generated_at:datetime
    overall_state:str
    summary: HealthSummary
    sensors: List[SensorStats]