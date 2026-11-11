from typing import Dict, Any, Optional
from datetime import datetime

class ProductService:
    def __init__(self):
        self._cache: Dict[str, Any] = {}
    
    def get(self, key: str) -> Optional[Any]:
        return self._cache.get(key)
    
    def has(self, key: str) -> bool:
        """True when the key is stored, even if its value is None."""
        return key in self._cache

    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value
    
    def delete(self, key: str) -> bool:
        if key in self._cache:
            del self._cache[key]
            return True
        return False
    
    def clear(self) -> None:
        self._cache.clear()
# auto-commit: 1778730631136