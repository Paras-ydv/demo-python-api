from typing import List

class DemoService:
    def filter_items(self, items: List[str], prefix: str) -> List[str]:
        return [i for i in items if i.startswith(prefix)]

    def count_matches(self, items: List[str], pattern: str) -> int:
        return sum(1 for i in items if pattern in i)
    # auto-commit: 1777399764984
