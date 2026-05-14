import asyncio
from typing import List

class CacheService:
    def __init__(self):
        self.items: List[str] = []
    
    async def add(self, item: str) -> None:
        await asyncio.sleep(0.01)
        self.items.append(item)
    
    async def get_all(self) -> List[str]:
        return self.items.copy()
    
    async def remove(self, item: str) -> bool:
        if item in self.items:
            self.items.remove(item)
            return True
        return False
# auto-commit: 1778737564341