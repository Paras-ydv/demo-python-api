from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()

class ProductRequest(BaseModel):
    name: str
    value: str

class ProductResponse(BaseModel):
    success: bool
    message: str

@router.post('/product')
async def handle_product(request: ProductRequest) -> ProductResponse:
    return ProductResponse(
        success=True,
        message=f"Processed: {request.name}"
    )
# auto-commit: 1778741324440