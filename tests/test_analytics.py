import unittest
from app.models.analytics import Analytics

class TestAnalytics(unittest.TestCase):
    def test_creation(self):
        obj = Analytics.create('test', 'test@example.com')
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.name, 'test')
    
    def test_update(self):
        obj = Analytics.create('test', 'test@example.com')
        obj.update_name('updated')
        self.assertEqual(obj.name, 'updated')
# auto-commit: 1778454126366