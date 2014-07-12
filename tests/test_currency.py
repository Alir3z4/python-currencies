from unittest import TestCase
from currencies import Currency


class TestCurrency(TestCase):
    def test_get_money_currency(self):
        currency = Currency('USD')

        self.assertIsInstance(currency.get_money_currency(), str)
        self.assertEqual(currency.get_money_currency(), 'USD')
