import functools
import time
from logging import getLogger


def log_method(method):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        logger_ = getLogger(method.__module__)
        logger_.info('Started method %s.%s(args=%s, kwargs=%s)',
                     method.__name__, args, kwargs)
        time_start = time.monotonic()
        result = method(*args, **kwargs)
        time_end = time.monotonic()
        delta = time_end - time_start
        logger_.info(
            'Finished method %s(args=%s, kwargs=%s); Execution time: %.3f s; Result: %s',
            method.__name__, args, kwargs, delta, result
        )
        return result

    return inner
