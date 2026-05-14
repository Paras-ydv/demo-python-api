from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()

class OrderRequest(BaseModel):
    name: str
    value: str

class OrderResponse(BaseModel):
    success: bool
    message: str

@router.post('/order')
async def handle_order(request: OrderRequest) -> OrderResponse:
    return OrderResponse(
        success=True,
        message=f"Processed: {request.name}"
    )
# auto-commit: 1778741350719