import base64

class DemoService:
    def encode(self, text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    def decode(self, encoded: str) -> str:
        return base64.b64decode(encoded.encode()).decode()
    # auto-commit: 1777399746115
