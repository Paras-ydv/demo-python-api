import unittest
from app.models.validator import Validator

class TestValidator(unittest.TestCase):
    def test_creation(self):
        obj = Validator.create('test', 'test@example.com')
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.name, 'test')
    
    def test_update(self):
        obj = Validator.create('test', 'test@example.com')
        obj.update_name('updated')
        self.assertEqual(obj.name, 'updated')
# auto-commit: 1778586675551