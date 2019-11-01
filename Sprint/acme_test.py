#!/usr/bin/env python

import unittest
from acme import AcmeProduct
from acme_report import generate_products, ADJ, NOUN


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = AcmeProduct('Toy')
        self.assertEqual(prod.price, 10)

    def test_default_values(self):
        prod = AcmeProduct('Toy')
        self.assertEqual(AcmeProduct('Toy').__dict__, prod.__dict__)

    def test_default_explode(self):
        prod = AcmeProduct('Toy', 20, 5, .2)
        self.assertEqual(prod.explode(), 'fizzle')

    def test_default_steal(self):
        prod = AcmeProduct('Toy', 20, 5, .2)
        self.assertEqual(prod.stealability(), 'Very stealable')


if __name__ == '__main__':
    unittest.main()
