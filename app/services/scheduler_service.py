import requests
from typing import Dict, Any

class SchedulerService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def fetch(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
# auto-commit: 1778712282045