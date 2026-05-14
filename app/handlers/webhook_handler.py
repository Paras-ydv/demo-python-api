from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()

class WebhookRequest(BaseModel):
    name: str
    value: str

class WebhookResponse(BaseModel):
    success: bool
    message: str

@router.post('/webhook')
async def handle_webhook(request: WebhookRequest) -> WebhookResponse:
    return WebhookResponse(
        success=True,
        message=f"Processed: {request.name}"
    )
# auto-commit: 1778731796908