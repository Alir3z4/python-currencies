#!/usr/bin/env python
# coding: utf-8

__VERSION__ = (0000, 0, 0)


def get_version():
    """
    :rtype: basestring
    """
    return ".".join(str(v) for v in __VERSION__)


class Currency(object):
    currency = None
