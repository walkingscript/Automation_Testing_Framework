import logging

import requests

from .wrappers import request

logger = logging.getLogger(__name__)


@request('GET')
def get(*args, **kwargs):
    return requests.get(*args, **kwargs)


@request('POST')
def post(*args, **kwargs):
    return requests.post(*args, **kwargs)


@request('PUT')
def put(*args, **kwargs):
    return requests.put(*args, **kwargs)


@request('DELETE')
def delete(*args, **kwargs):
    return requests.delete(*args, **kwargs)


def basic_auth(url, username, password):
    logger.info('Running GET request with basic authorization. Params: url=%s, username=%s, password=%s',
                url, username, password)
    url = url.replace('//', f'//{username}:{password}@', 1)
    response = requests.get(url)
    logger.info('Result: %s (%s)', response.reason, response.status_code)
    return response
