import functools

import logging
from json import JSONDecodeError

logger = logging.getLogger(__name__)


def request(name):
    def inner(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info('Running %s request with params: args=%s kwargs=%s', name, args, kwargs)
            response = func(*args, *kwargs)
            logger.info('Result: %s (%s)', response.reason, response.status_code)
            try:
                logger.info('Response JSON: %s', response.json())
            except JSONDecodeError:
                logger.info("Response is not in JSON format")
            return response

        return wrapper

    return inner
