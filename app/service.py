import uuid

class DemoService:
    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def short_id(self) -> str:
        return str(uuid.uuid4())[:8]
    # auto-commit: 1777399737184
