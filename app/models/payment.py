from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class Payment:
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
    
    @classmethod
    def create(cls, name: str, email: str) -> 'Payment':
        now = datetime.utcnow()
        return cls(
            id=str(uuid.uuid4()),
            name=name,
            email=email,
            created_at=now,
            updated_at=now
        )
    
    def update_name(self, name: str) -> None:
        self.name = name
        self.updated_at = datetime.utcnow()
# auto-commit: 1778737079678