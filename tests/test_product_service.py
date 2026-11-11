import unittest
from app.services.product_service import ProductService


class TestProductService(unittest.TestCase):
    def test_has_stored_key(self):
        svc = ProductService()
        svc.set("a", 1)
        self.assertTrue(svc.has("a"))

    def test_has_none_value(self):
        svc = ProductService()
        svc.set("a", None)
        self.assertTrue(svc.has("a"))

    def test_has_missing_key(self):
        self.assertFalse(ProductService().has("missing"))
