#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are consistent."""
    def test_default_num_products(self):
        """Test default number of products is 30"""
        self.assertEqual(generate_products(30), 30)
    def test_legal_names(self):
        """Test the legal names of the acme products"""
        self.assertIN(products, products)


if __name__ == '__main__':
    unittest.main()