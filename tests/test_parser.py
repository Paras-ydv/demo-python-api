import unittest
from app.models.parser import Parser

class TestParser(unittest.TestCase):
    def test_creation(self):
        obj = Parser.create('test', 'test@example.com')
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.name, 'test')
    
    def test_update(self):
        obj = Parser.create('test', 'test@example.com')
        obj.update_name('updated')
        self.assertEqual(obj.name, 'updated')
# auto-commit: 1778732623159