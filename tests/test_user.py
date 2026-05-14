import pytest
from app.services.user_service import UserService

@pytest.fixture
def service():
    return UserService()

def test_user_creation(service):
    assert service is not None

def test_user_set_and_get(service):
    service.set('key', 'value')
    assert service.get('key') == 'value'

def test_user_delete(service):
    service.set('key', 'value')
    assert service.delete('key') is True
    assert service.get('key') is None
# auto-commit: 1778737568036