from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class HealthSummary(BaseModel):
    ACTIVE: int
    STALE: int
    DEAD: int

class SensorHealth(BaseModel):
    state: str
    severity: str
    last_seen_sec: float
    description: str

class SystemHealthReport(BaseModel):
    generated_at: datetime
    overall_state: str
    summary: HealthSummary
    sensors: Dict[str, SensorHealth]