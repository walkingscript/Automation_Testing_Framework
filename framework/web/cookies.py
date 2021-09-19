from logging import getLogger
from typing import Collection

from .driver import WebDriver

logger = getLogger(__name__)


class Cookies:

    def __init__(self, browser_identifier):
        self.driver = WebDriver.get_driver(browser_identifier)

    def set_cookies(self, cookies: Collection[dict]):
        logger.info('Setting cookies %s', cookies)
        for item in cookies:
            self.driver.add_cookie(item)

    def delete_cookies(self, names: Collection[str]):
        logger.info('Removing cookies %s', names)
        for name in names:
            self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        logger.info('Removing all cookies')
        self.driver.delete_all_cookies()

    def get_cookie(self, name):
        """Returns cookie by description"""
        logger.info('Getting cookie %s', name)
        return self.driver.get_cookie(name)

    @property
    def all_cookies(self):
        """Returns all browser's cookies"""
        logger.info('Reading all cookies')
        return self.driver.get_cookies()
