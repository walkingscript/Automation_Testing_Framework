# TODO: does that module is really needed?

import json
import requests

from framework.utils.logger import logger


class Request:

    @staticmethod
    def get(*args, **kwargs):
        logger.info('Performing of GET request with params: args=%s kwargs=%s', (args, kwargs))
        response = requests.get(*args, **kwargs)
        logger.info(f'Checking that data in JSON format')
        return response

    @staticmethod
    def post(*args, **kwargs):
        logger.info('Performing of POST request with params: args=%s kwargs=%s', (args, kwargs))
        response = requests.post(*args, **kwargs)
        return response

    @staticmethod
    def put(*args, **kwargs):
        logger.info('Performing of PUT request with params: args=%s kwargs=%s', (args, kwargs))
        response = requests.put(*args, **kwargs)
        return response

    @staticmethod
    def delete(*args, **kwargs):
        logger.info('Performing of DELETE request with params: args=%s kwargs=%s', (args, kwargs))
        response = requests.delete(*args, **kwargs)
        return response

    @staticmethod
    def basic_auth(url, username, password) -> str:
        logger.info('Performing basic authorization request with params: %s', ((url, username, password),))
        url = url.replace('//', f'//{username}:{password}@', 1)
        data = requests.post(url)
        return data.json()

    @staticmethod
    def is_response_in_json_format(response: requests.Response):
        logger.info('Checking that response data is in JSON format')
        try:
            response.json()
        except json.JSONDecodeError:
            return False
        return True
