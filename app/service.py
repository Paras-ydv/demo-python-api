import math

class DemoService:
    def distance(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def area_circle(self, radius: float) -> float:
        return math.pi * radius ** 2
    # auto-commit: 1777399781074
