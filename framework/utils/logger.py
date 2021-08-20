import functools

from framework.settings.config import config


# TODO: use logging.py here


def info(text):
    """Decorator for beautiful logging of methods in class."""

    def wrapper(method):

        @functools.wraps(method)
        def inner(self, *args, **kwargs):
            logger.info("%s.%s - %s", (self.__class__.__name__, method.__name__, text))
            result = method(self, *args, **kwargs)
            return result

        return inner

    return wrapper