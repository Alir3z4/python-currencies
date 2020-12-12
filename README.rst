==================
Python Currencies
==================

Display money format and its filthy currencies, for all money lovers out there.

.. image:: https://github.com/Alir3z4/python-currencies/workflows/Python%20Currencies%20Package/badge.svg
   :alt: Build Status
   :target: https://github.com/Alir3z4/python-currencies/actions


.. image:: https://codecov.io/gh/Alir3z4/python-currencies/branch/master/graph/badge.svg?token=Ag25YMSuEX
   :target: https://codecov.io/gh/Alir3z4/python-currencies




Installation
------------
``currencies`` is available on PyPi

http://pypi.python.org/pypi/currencies

So easily install it by ``pip``

::

    $ pip install currencies

Or by ``easy_install``

::

    $ easy_install currencies

Another way is by cloning ``currencies``'s `git repo <https://github.com/Alir3z4/python-currencies>`_

::

    $ git clone git://github.com/Alir3z4/python-currencies.git

Then install it by running:
::

    $ python setup.py install


Usage
-----

Displaying money format:

>>> from currencies import Currency
>>>
>>> currency = Currency('USD')
>>> currency.get_money_format(13)
>>> '$13'
>>> currency.get_money_format(13.99)
>>> '$13.99'
>>> currency.get_money_format('13,2313,33')
>>> '$13,2313,33'
>>>
>>> # Displaying with currency as well
>>>
>>> currency.get_money_with_currency_format(13)
>>> '$13 USD'
>>> currency.get_money_with_currency_format(13.99)
>>> '$13.99 USD'
>>> currency.get_money_with_currency_format('13,2313,33')
>>> '$13,2313,33 USD'



Tests
-----

``currencies`` is well tested, to run the test suite:

::

    $ PYTHONPATH=$PYTHONPATH:. python setup.py test


Available currencies
---------------------

* AED
* AFN
* ALL
* AMD
* ANG
* AOA
* ARS
* AUD
* AWG
* AZN
* BAM
* BBD
* BDT
* BGN
* BHD
* BND
* BOB
* BRL
* BSD
* BTN
* BWP
* BYR
* BZD
* CAD
* CHF
* CLP
* CNY
* COP
* CRC
* CZK
* DKK
* DOP
* DZD
* EGP
* ETB
* EUR
* FJD
* GBP
* GEL
* GHS
* GMD
* GTQ
* GYD
* HKD
* HNL
* HRK
* HUF
* IDR
* ILS
* INR
* ISK
* JEP
* JMD
* JOD
* JPY
* KES
* KGS
* KHR
* KRW
* KWD
* KYD
* KZT
* LBP
* LKR
* LTL
* LVL
* MAD
* MDL
* MGA
* MKD
* MMK
* MNT
* MOP
* MUR
* MVR
* MXN
* MYR
* MZN
* NAD
* NGN
* NIO
* NOK
* NPR
* NZD
* OMR
* PEN
* PGK
* PHP
* PKR
* PLN
* PYG
* QAR
* RON
* RSD
* RUB
* RWF
* SAR
* SCR
* SEK
* SGD
* STD
* SYP
* THB
* TND
* TRY
* TTD
* TWD
* TZS
* UAH
* UGX
* USD
* UYU
* VEF
* VND
* VUV
* WST
* XAF
* XBT
* XCD
* XOF
* XPF
* ZAR
* ZMW


----

========== ======
Source      https://github.com/Alir3z4/python-currencies
Website     http://alir3z4.github.com/python-currencies
Issues      https://github.com/Alir3z4/python-currencies/issues
PyPi        http://pypi.python.org/pypi/currencies
Author      Alireza Savand
License     GNU GPL 3
========== ======
