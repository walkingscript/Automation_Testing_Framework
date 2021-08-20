import functools
import time


def clock(func):
    """Calculates time elapsed by function call"""

    @functools.wraps
    def clocked(*args, **kwargs):
        t0 = time.monotonic()
        result = func(*args, **kwargs)
        elapsed = time.monotonic() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('{%0.8fs} %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked
