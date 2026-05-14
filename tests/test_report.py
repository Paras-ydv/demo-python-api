import unittest
from app.models.report import Report

class TestReport(unittest.TestCase):
    def test_creation(self):
        obj = Report.create('test', 'test@example.com')
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.name, 'test')
    
    def test_update(self):
        obj = Report.create('test', 'test@example.com')
        obj.update_name('updated')
        self.assertEqual(obj.name, 'updated')
# auto-commit: 1778737413412