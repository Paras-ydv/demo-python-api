from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()

class MetricsRequest(BaseModel):
    name: str
    value: str

class MetricsResponse(BaseModel):
    success: bool
    message: str

@router.post('/metrics')
async def handle_metrics(request: MetricsRequest) -> MetricsResponse:
    return MetricsResponse(
        success=True,
        message=f"Processed: {request.name}"
    )
# auto-commit: 1778737902177