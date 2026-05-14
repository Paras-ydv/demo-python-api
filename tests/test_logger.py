import pytest
from app.services.logger_service import LoggerService

@pytest.fixture
def service():
    return LoggerService()

def test_logger_creation(service):
    assert service is not None

def test_logger_set_and_get(service):
    service.set('key', 'value')
    assert service.get('key') == 'value'

def test_logger_delete(service):
    service.set('key', 'value')
    assert service.delete('key') is True
    assert service.get('key') is None
# auto-commit: 1778732127110