from datetime import datetime
from typing import Any

def get_timestamp() -> int:
    return int(datetime.utcnow().timestamp())

def format_duration(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}h {minutes}m {secs}s"

def truncate_string(s: str, max_len: int) -> str:
    return s if len(s) <= max_len else s[:max_len] + '...'
# auto-commit: 1778730930960