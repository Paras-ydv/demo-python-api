import pytest
from app.services.auth_service import AuthService

@pytest.fixture
def service():
    return AuthService()

def test_auth_creation(service):
    assert service is not None

def test_auth_set_and_get(service):
    service.set('key', 'value')
    assert service.get('key') == 'value'

def test_auth_delete(service):
    service.set('key', 'value')
    assert service.delete('key') is True
    assert service.get('key') is None
# auto-commit: 1778737566197