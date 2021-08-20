from typing import Collection

from framework.utils.logger import logger
from framework.browser.webdriver import WebDriver


class Cookies:

    def __init__(self, browser_identifier):
        self.driver = WebDriver.get_driver(browser_identifier)

    def set_cookies(self, cookies: Collection[dict]):
        logger.info(f'set_cookies {cookies}')
        for item in cookies:
            self.driver.add_cookie(item)

    def delete_cookies(self, names: Collection[str]):
        logger.info(f'delete_cookies {names}')
        for name in names:
            self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        logger.info(f'delete_all_cookies')
        self.driver.delete_all_cookies()

    def get_cookie(self, name):
        """Returns cookie by description"""
        return self.driver.get_cookie(name)

    @property
    def all_cookies(self):
        """Returns all browser's cookies"""
        logger.info(f'Reading cookies')
        return self.driver.get_cookies()
