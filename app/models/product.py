from enum import Enum
from typing import Optional

class ProductStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'

class Product:
    def __init__(self, id: int, title: str, status: ProductStatus):
        self.id = id
        self.title = title
        self.status = status
        self.description: Optional[str] = None
        self.priority: int = 5
    
    def is_active(self) -> bool:
        return self.status == ProductStatus.ACTIVE
    
    def set_priority(self, priority: int) -> None:
        self.priority = min(priority, 10)
# auto-commit: 1778737077811