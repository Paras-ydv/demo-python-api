import hashlib
import base64

def hash_string(input_str: str) -> str:
    return hashlib.sha256(input_str.encode()).hexdigest()

def encode_base64(data: bytes) -> str:
    return base64.b64encode(data).decode('utf-8')

def decode_base64(encoded: str) -> bytes:
    return base64.b64decode(encoded)
# auto-commit: 1778586642729