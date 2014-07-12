#!/usr/bin/env python
# coding: utf-8
from currencies.config import MONEY_FORMATS
from currencies.exceptions import CurrencyDoesNotExist

__VERSION__ = (2014, 7, 13)


def get_version():
    """
    :rtype: basestring
    """
    return ".".join(str(v) for v in __VERSION__)


class Currency(object):
    money_currency = None
    money_formats = MONEY_FORMATS

    def __init__(self, money_currency):
        """
        :type money_currency: str
        """
        self.set_money_currency(money_currency)

    def set_money_currency(self, money_currency):
        """
        :type money_currency: str
        """
        if money_currency not in self.money_formats:
            raise CurrencyDoesNotExist

        self.money_currency = money_currency

    def get_money_currency(self):
        """
        :rtype: str
        """
        return self.money_currency

    @classmethod
    def get_currency_formats(cls):
        """
        :rtype: list
        """
        return cls.money_formats.keys()

    def get_money_format(self, amount):
        """
        :type amount: int or float or str

        Usage:
        >>> currency = Currency('USD')
        >>> currency.get_money_format(13)
        >>> '$13'
        >>> currency.get_money_format(13.99)
        >>> '$13.99'
        >>> currency.get_money_format('13,2313,33')
        >>> '$13,2313,33'

        :rtype: str
        """
        return self.money_formats[
            self.get_money_currency()
        ]['money_format'].format(amount=amount)

    def get_money_with_currency_format(self, amount):
        """
        :type amount: int or float or str

        Usage:
        >>> currency = Currency('USD')
        >>> currency.get_money_with_currency_format(13)
        >>> '$13 USD'
        >>> currency.get_money_with_currency_format(13.99)
        >>> '$13.99 USD'
        >>> currency.get_money_with_currency_format('13,2313,33')
        >>> '$13,2313,33 USD'

        :rtype: str
        """
        return self.money_formats[
            self.get_money_currency()
        ]['money_with_currency_format'].format(amount=amount)

