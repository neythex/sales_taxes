from unittest import TestCase

from sales_taxes.Receipt import Receipt
from sales_taxes.ShoppingCart import ShoppingCart
from sales_taxes.product.Product import Product


class TestShoppingCart(TestCase):
    def setUp(self):
        self.test_shopping_cart = ShoppingCart()
        self.test_products = []
        self.test_receipt: Receipt

    def test_add_to_cart(self):
        self.test_shopping_cart.add_to_cart("1 book at 12.49")
        self.assertIsInstance(self.test_products[0], Product, "Should be instance of Product")
        self.assertEqual(len(self.test_products), 1, "List should have 1 object")

        self.test_shopping_cart.add_to_cart(" ")
        self.assertEqual(len(self.test_products), 1)

    def test_get_receipt(self):
        self.test_receipt = self.test_shopping_cart.get_receipt()
        self.assertIsInstance(self.test_receipt, Receipt, "Should be instance of Receipt")
