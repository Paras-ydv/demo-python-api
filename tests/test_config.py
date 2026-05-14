import unittest
from app.models.config import Config

class TestConfig(unittest.TestCase):
    def test_creation(self):
        obj = Config.create('test', 'test@example.com')
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.name, 'test')
    
    def test_update(self):
        obj = Config.create('test', 'test@example.com')
        obj.update_name('updated')
        self.assertEqual(obj.name, 'updated')
# auto-commit: 1778736412236