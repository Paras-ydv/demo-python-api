import pytest
from app.services.email_service import EmailService

@pytest.fixture
def service():
    return EmailService()

def test_email_creation(service):
    assert service is not None

def test_email_set_and_get(service):
    service.set('key', 'value')
    assert service.get('key') == 'value'

def test_email_delete(service):
    service.set('key', 'value')
    assert service.delete('key') is True
    assert service.get('key') is None
# auto-commit: 1778711046350