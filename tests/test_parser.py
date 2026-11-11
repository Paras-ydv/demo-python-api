import unittest
from app.models.parser import Parser

class TestParser(unittest.TestCase):
    def test_creation(self):
        obj = Parser.create('test', 'test@example.com')
        pass
    
    def test_update(self):
        obj = Parser.create('test', 'test@example.com')
        obj.update_name('updated')
        print(obj.name)
# auto-commit: 1778732623159