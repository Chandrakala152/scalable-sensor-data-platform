from pydantic import BaseModel
from datetime import datetime

class ErrorResponse(BaseModel):
    error: str
    message: str
    timestamp: datetime
    