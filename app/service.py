from collections import Counter
from typing import List

class DemoService:
    def count_frequency(self, items: List[str]) -> dict:
        return dict(Counter(items))

    def most_common(self, items: List[str], n: int = 1) -> List[tuple]:
        return Counter(items).most_common(n)
    # auto-commit: 1777399766643
