from enum import Enum
from typing import Optional

class ImportStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'

class Import:
    def __init__(self, id: int, title: str, status: ImportStatus):
        self.id = id
        self.title = title
        self.status = status
        self.description: Optional[str] = None
        self.priority: int = 5
    
    def is_active(self) -> bool:
        return self.status == ImportStatus.ACTIVE
    
    def set_priority(self, priority: int) -> None:
        self.priority = min(priority, 10)
# auto-commit: 1778737904228