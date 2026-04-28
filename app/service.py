from typing import Dict, Any

class DemoService:
    def __init__(self):
        self.cache: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self.cache[key] = value

    def get(self, key: str) -> Any:
        return self.cache.get(key)
    # auto-commit: 1777399717408
