from unittest import TestCase
from currencies import Currency, get_version, __VERSION__
from currencies.exceptions import CurrencyDoesNotExist


class TestCurrency(TestCase):
    def test_get_version(self):
        version = get_version()

        self.assertIsInstance(version, str)
        self.assertEqual(len(version.split('.')), len(__VERSION__))

    def test_get_money_currency(self):
        currency = Currency('USD')

        self.assertIsInstance(currency.get_money_currency(), str)
        self.assertEqual(currency.get_money_currency(), 'USD')

    def test_set_money_currency(self):
        currency = Currency('USD')

        self.assertEqual(currency.get_money_currency(), 'USD')
        self.assertEqual(currency.get_money_format(13), '$13')

        currency.set_money_currency('AED')

        self.assertEqual(currency.get_money_currency(), 'AED')
        self.assertEqual(currency.get_money_format(13), 'Dhs. 13')

    def test_get_currency_formats(self):
        currency_formats = Currency.get_currency_formats()

        self.assertIsNotNone(currency_formats)
        self.assertIsInstance(currency_formats, list)
        self.assertGreater(len(currency_formats), 0)

    def test_get_money_format(self):
        currency = Currency('USD')

        self.assertEqual(currency.get_money_format(13), '$13')
        self.assertEqual(currency.get_money_format(13.99), '$13.99')
        self.assertEqual(
            currency.get_money_format('13,2313,33'),
            '$13,2313,33'
        )

    def test_get_money_with_currency_format(self):
        currency = Currency('USD')

        self.assertEqual(currency.get_money_with_currency_format(13.99), '$13.99 USD')
        self.assertEqual(
            currency.get_money_with_currency_format('13,2313,33'),
            '$13,2313,33 USD'
        )

    def test_does_not_exist_currency(self):
        self.assertRaises(
            CurrencyDoesNotExist,
            Currency,
            money_currency='BingoMingo'
        )
