import json

class DemoService:
    def serialize(self, data: dict) -> str:
        return json.dumps(data)

    def deserialize(self, text: str) -> dict:
        return json.loads(text)
    # auto-commit: 1777399743073
