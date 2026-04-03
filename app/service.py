import random
from typing import List

class DemoService:
    def __init__(self):
        self.items: List[str] = []

    def add(self, item: str) -> None:
        self.items.append(item)

    def get_all(self) -> List[str]:
        return self.items
    # auto-commit: 1775199930022
