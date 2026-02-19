from pydantic import BaseModel

class SensorResponse(BaseModel):
    state: str
    severity: str
    last_seen_sec: float
    description: str