__VERSION__ = (0000, 0, 0)


def get_version():
    """
    :rtype: basestring
    """
    return ".".join(str(v) for v in __VERSION__)
