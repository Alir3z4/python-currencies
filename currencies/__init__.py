#!/usr/bin/env python
# coding: utf-8

__VERSION__ = (2014, 7, 12)


def get_version():
    """
    :rtype: basestring
    """
    return ".".join(str(v) for v in __VERSION__)


class Currency(object):
    money_currency = None
    money_formats = {
        "USD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} USD"
        },
        "EUR": {
            "money_format": "€{amount}",
            "money_with_currency_format": "€{amount} EUR"
        },
        "GBP": {
            "money_format": "£{amount}",
            "money_with_currency_format": "£{amount} GBP"
        },
        "CAD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} CAD"
        },
        "ALL": {
            "money_format": "Lek {amount}",
            "money_with_currency_format": "Lek {amount} ALL"
        },
        "DZD": {
            "money_format": "DA {amount}",
            "money_with_currency_format": "DA {amount} DZD"
        },
        "AOA": {
            "money_format": "Kz{amount}",
            "money_with_currency_format": "Kz{amount} AOA"
        },
        "ARS": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} ARS"
        },
        "AMD": {
            "money_format": "{amount} AMD",
            "money_with_currency_format": "{amount} AMD"
        },
        "AWG": {
            "money_format": "Afl{amount}",
            "money_with_currency_format": "Afl{amount} AWG"
        },
        "AUD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} AUD"
        },
        "BBD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} Bds"
        },
        "AZN": {
            "money_format": "m.{amount}",
            "money_with_currency_format": "m.{amount} AZN"
        },
        "BDT": {
            "money_format": "Tk {amount}",
            "money_with_currency_format": "Tk {amount} BDT"
        },
        "BSD": {
            "money_format": "BS${amount}",
            "money_with_currency_format": "BS${amount} BSD"
        },
        "BHD": {
            "money_format": "{amount} BD",
            "money_with_currency_format": "{amount} BHD"
        },
        "BYR": {
            "money_format": "Br {amount}",
            "money_with_currency_format": "Br {amount} BYR"
        },
        "BZD": {
            "money_format": "BZ${amount}",
            "money_with_currency_format": "BZ${amount} BZD"
        },
        "BTN": {
            "money_format": "Nu {amount}",
            "money_with_currency_format": "Nu {amount} BTN"
        },
        "BAM": {
            "money_format": "KM {amount}",
            "money_with_currency_format": "KM {amount} BAM"
        },
        "BRL": {
            "money_format": "R$ {amount}",
            "money_with_currency_format": "R$ {amount} BRL"
        },
        "BOB": {
            "money_format": "Bs{amount}",
            "money_with_currency_format": "Bs{amount} BOB"
        },
        "BWP": {
            "money_format": "P{amount}",
            "money_with_currency_format": "P{amount} BWP"
        },
        "BND": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} BND"
        },
        "BGN": {
            "money_format": "{amount} лв",
            "money_with_currency_format": "{amount} лв BGN"
        },
        "MMK": {
            "money_format": "K{amount}",
            "money_with_currency_format": "K{amount} MMK"
        },
        "KHR": {
            "money_format": "KHR{amount}",
            "money_with_currency_format": "KHR{amount}"
        },
        "KYD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} KYD"
        },
        "XAF": {
            "money_format": "FCFA{amount}",
            "money_with_currency_format": "FCFA{amount} XAF"
        },
        "CLP": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} CLP"
        },
        "CNY": {
            "money_format": "¥{amount}",
            "money_with_currency_format": "¥{amount} CNY"
        },
        "COP": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} COP"
        },
        "CRC": {
            "money_format": "₡ {amount}",
            "money_with_currency_format": "₡ {amount} CRC"
        },
        "HRK": {
            "money_format": "{amount} kn",
            "money_with_currency_format": "{amount} kn HRK"
        },
        "CZK": {
            "money_format": "{amount} Kč",
            "money_with_currency_format": "{amount} Kč"
        },
        "DKK": {
            "money_format": "{amount}",
            "money_with_currency_format": "kr.{amount}"
        },
        "DOP": {
            "money_format": "RD$ {amount}",
            "money_with_currency_format": "RD$ {amount}"
        },
        "XCD": {
            "money_format": "${amount}",
            "money_with_currency_format": "EC${amount}"
        },
        "EGP": {
            "money_format": "LE {amount}",
            "money_with_currency_format": "LE {amount} EGP"
        },
        "ETB": {
            "money_format": "Br{amount}",
            "money_with_currency_format": "Br{amount} ETB"
        },
        "XPF": {
            "money_format": "{amount} XPF",
            "money_with_currency_format": "{amount} XPF"
        },
        "FJD": {
            "money_format": "${amount}",
            "money_with_currency_format": "FJ${amount}"
        },
        "GMD": {
            "money_format": "D {amount}",
            "money_with_currency_format": "D {amount} GMD"
        },
        "GHS": {
            "money_format": "GH₵{amount}",
            "money_with_currency_format": "GH₵{amount}"
        },
        "GTQ": {
            "money_format": "Q{amount}",
            "money_with_currency_format": "{amount} GTQ"
        },
        "GYD": {
            "money_format": "G${amount}",
            "money_with_currency_format": "${amount} GYD"
        },
        "GEL": {
            "money_format": "{amount} GEL",
            "money_with_currency_format": "{amount} GEL"
        },
        "HNL": {
            "money_format": "L {amount}",
            "money_with_currency_format": "L {amount} HNL"
        },
        "HKD": {
            "money_format": "${amount}",
            "money_with_currency_format": "HK${amount}"
        },
        "HUF": {
            "money_format": "{amount}",
            "money_with_currency_format": "{amount} Ft"
        },
        "ISK": {
            "money_format": "{amount} kr",
            "money_with_currency_format": "{amount} kr ISK"
        },
        "INR": {
            "money_format": "Rs. {amount}",
            "money_with_currency_format": "Rs. {amount}"
        },
        "IDR": {
            "money_format": "{amount}",
            "money_with_currency_format": "Rp {amount}"
        },
        "ILS": {
            "money_format": "{amount} NIS",
            "money_with_currency_format": "{amount} NIS"
        },
        "JMD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} JMD"
        },
        "JPY": {
            "money_format": "¥{amount}",
            "money_with_currency_format": "¥{amount} JPY"
        },
        "JEP": {
            "money_format": "£{amount}",
            "money_with_currency_format": "£{amount} JEP"
        },
        "JOD": {
            "money_format": "{amount} JD",
            "money_with_currency_format": "{amount} JOD"
        },
        "KZT": {
            "money_format": "{amount} KZT",
            "money_with_currency_format": "{amount} KZT"
        },
        "KES": {
            "money_format": "KSh{amount}",
            "money_with_currency_format": "KSh{amount}"
        },
        "KWD": {
            "money_format": "{amount} KD",
            "money_with_currency_format": "{amount} KWD"
        },
        "KGS": {
            "money_format": "лв{amount}",
            "money_with_currency_format": "лв{amount}"
        },
        "LVL": {
            "money_format": "Ls {amount}",
            "money_with_currency_format": "Ls {amount} LVL"
        },
        "LBP": {
            "money_format": "L£{amount}",
            "money_with_currency_format": "L£{amount} LBP"
        },
        "LTL": {
            "money_format": "{amount} Lt",
            "money_with_currency_format": "{amount} Lt"
        },
        "MGA": {
            "money_format": "Ar {amount}",
            "money_with_currency_format": "Ar {amount} MGA"
        },
        "MKD": {
            "money_format": "ден {amount}",
            "money_with_currency_format": "ден {amount} MKD"
        },
        "MOP": {
            "money_format": "MOP${amount}",
            "money_with_currency_format": "MOP${amount}"
        },
        "MVR": {
            "money_format": "Rf{amount}",
            "money_with_currency_format": "Rf{amount} MRf"
        },
        "MXN": {
            "money_format": "$ {amount}",
            "money_with_currency_format": "$ {amount} MXN"
        },
        "MYR": {
            "money_format": "RM{amount} MYR",
            "money_with_currency_format": "RM{amount} MYR"
        },
        "MUR": {
            "money_format": "Rs {amount}",
            "money_with_currency_format": "Rs {amount} MUR"
        },
        "MDL": {
            "money_format": "{amount} MDL",
            "money_with_currency_format": "{amount} MDL"
        },
        "MAD": {
            "money_format": "{amount} dh",
            "money_with_currency_format": "Dh {amount} MAD"
        },
        "MNT": {
            "money_format": "{amount} ₮",
            "money_with_currency_format": "{amount} MNT"
        },
        "MZN": {
            "money_format": "{amount} Mt",
            "money_with_currency_format": "Mt {amount} MZN"
        },
        "NAD": {
            "money_format": "N${amount}",
            "money_with_currency_format": "N${amount} NAD"
        },
        "NPR": {
            "money_format": "Rs{amount}",
            "money_with_currency_format": "Rs{amount} NPR"
        },
        "ANG": {
            "money_format": "ƒ{amount}",
            "money_with_currency_format": "{amount} NAƒ"
        },
        "NZD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} NZD"
        },
        "NIO": {
            "money_format": "C${amount}",
            "money_with_currency_format": "C${amount} NIO"
        },
        "NGN": {
            "money_format": "₦{amount}",
            "money_with_currency_format": "₦{amount} NGN"
        },
        "NOK": {
            "money_format": "kr {amount}",
            "money_with_currency_format": "kr {amount} NOK"
        },
        "OMR": {
            "money_format": "{amount} OMR",
            "money_with_currency_format": "{amount} OMR"
        },
        "PKR": {
            "money_format": "Rs.{amount}",
            "money_with_currency_format": "Rs.{amount} PKR"
        },
        "PGK": {
            "money_format": "K {amount}",
            "money_with_currency_format": "K {amount} PGK"
        },
        "PYG": {
            "money_format": "Gs. {amount}",
            "money_with_currency_format": "Gs. {amount} PYG"
        },
        "PEN": {
            "money_format": "S/. {amount}",
            "money_with_currency_format": "S/. {amount} PEN"
        },
        "PHP": {
            "money_format": "₱{amount}",
            "money_with_currency_format": "₱{amount} PHP"
        },
        "PLN": {
            "money_format": "{amount} zl",
            "money_with_currency_format": "{amount} zl PLN"
        },
        "QAR": {
            "money_format": "QAR {amount}",
            "money_with_currency_format": "QAR {amount}"
        },
        "RON": {
            "money_format": "{amount} lei",
            "money_with_currency_format": "{amount} lei RON"
        },
        "RUB": {
            "money_format": "руб{amount}",
            "money_with_currency_format": "руб{amount} RUB"
        },
        "RWF": {
            "money_format": "{amount} RF",
            "money_with_currency_format": "{amount} RWF"
        },
        "WST": {
            "money_format": "WS$ {amount}",
            "money_with_currency_format": "WS$ {amount} WST"
        },
        "SAR": {
            "money_format": "{amount} SR",
            "money_with_currency_format": "{amount} SAR"
        },
        "STD": {
            "money_format": "Db {amount}",
            "money_with_currency_format": "Db {amount} STD"
        },
        "RSD": {
            "money_format": "{amount} RSD",
            "money_with_currency_format": "{amount} RSD"
        },
        "SCR": {
            "money_format": "Rs {amount}",
            "money_with_currency_format": "Rs {amount} SCR"
        },
        "SGD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} SGD"
        },
        "SYP": {
            "money_format": "S£{amount}",
            "money_with_currency_format": "S£{amount} SYP"
        },
        "ZAR": {
            "money_format": "R {amount}",
            "money_with_currency_format": "R {amount} ZAR"
        },
        "KRW": {
            "money_format": "₩{amount}",
            "money_with_currency_format": "₩{amount} KRW"
        },
        "LKR": {
            "money_format": "Rs {amount}",
            "money_with_currency_format": "Rs {amount} LKR"
        },
        "SEK": {
            "money_format": "{amount} kr",
            "money_with_currency_format": "{amount} kr SEK"
        },
        "CHF": {
            "money_format": "SFr. {amount}",
            "money_with_currency_format": "SFr. {amount} CHF"
        },
        "TWD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} TWD"
        },
        "THB": {
            "money_format": "{amount} ฿",
            "money_with_currency_format": "{amount} ฿ THB"
        },
        "TZS": {
            "money_format": "{amount} TZS",
            "money_with_currency_format": "{amount} TZS"
        },
        "TTD": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} TTD"
        },
        "TND": {
            "money_format": "{amount}",
            "money_with_currency_format": "{amount} DT"
        },
        "TRY": {
            "money_format": "{amount}TL",
            "money_with_currency_format": "{amount}TL"
        },
        "UGX": {
            "money_format": "Ush {amount}",
            "money_with_currency_format": "Ush {amount} UGX"
        },
        "UAH": {
            "money_format": "₴{amount}",
            "money_with_currency_format": "₴{amount} UAH"
        },
        "AED": {
            "money_format": "Dhs. {amount}",
            "money_with_currency_format": "Dhs. {amount} AED"
        },
        "UYU": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount} UYU"
        },
        "VUV": {
            "money_format": "${amount}",
            "money_with_currency_format": "${amount}VT"
        },
        "VEF": {
            "money_format": "Bs. {amount}",
            "money_with_currency_format": "Bs. {amount} VEF"
        },
        "VND": {
            "money_format": "{amount}₫",
            "money_with_currency_format": "{amount} VND"
        },
        "XBT": {
            "money_format": "{amount} BTC",
            "money_with_currency_format": "{amount} BTC"
        },
        "XOF": {
            "money_format": "CFA{amount}",
            "money_with_currency_format": "CFA{amount} XOF"
        },
        "ZMW": {
            "money_format": "K{amount}",
            "money_with_currency_format": "ZMW{amount}"
        }
    }

    def __init__(self, money_currency):
        """
        :type money_currency: str
        """
        self.set_money_currency(money_currency)

    def set_money_currency(self, money_currency):
        """
        :type money_currency: str
        """
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
        >>> '$12.99'
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
        >>> '$13 USD'
        >>> currency.get_money_with_currency_format(13.99)
        >>> '$13 USD'
        >>> currency.get_money_with_currency_format('13,2313,33')
        >>> '$13,2313,33 USD'

        :rtype: str
        """
        return self.money_formats[
            self.get_money_currency()
        ]['money_with_currency_format'].format(amount=amount)

