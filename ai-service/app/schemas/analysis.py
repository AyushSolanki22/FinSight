from pydantic import BaseModel, Field
from typing import Optional

class AnalysisRequest(BaseModel):
    company: str = Field(min_length=1, max_length=200)
    question: str = Field(min_length=1, max_length=5000)
    years: Optional[int] = Field(default=5, ge=1, le=20)

class AnalysisResponse(BaseModel):
    status: str
    company: str
    question: str
    message: str
