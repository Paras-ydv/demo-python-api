import hashlib

class DemoService:
    def hash_data(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def validate(self, data: str, expected: str) -> bool:
        return self.hash_data(data) == expected
    # auto-commit: 1777399740158
