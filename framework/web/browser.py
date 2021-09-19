import os
import uuid
from datetime import datetime
from logging import getLogger

from framework import config
from .cookies import Cookies
from .driver import WebDriver

logger = getLogger(__name__)


class WebBrowser:
    """Defines basic browser functions."""

    def __init__(self):
        self.browser_identifier = uuid.uuid4()
        logger.info('Creating web browser with id=%s', self.browser_identifier)
        self.driver = WebDriver.get_driver(self.browser_identifier)
        self.cookies = Cookies(self.browser_identifier)

    def navigate(self, url, login=None, password=None):
        logger.info('Navigating to url=%s, login=%s, password=%s', url, login, password)
        if login and password:
            url = url.replace('//', f'//{login}:{password}@', 1)
        self.driver.get(url)

    def go_back(self):
        logger.info('Going back to the previous page')
        self.driver.back()

    def refresh(self):
        logger.info('Refreshing the page')
        self.driver.refresh()

    def screenshot(self, filename=None):
        logger.info('Making screenshot')
        screenshot_folder = config.SCREENSHOTS_DIRECTORY

        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder, exist_ok=True)

        if filename is None:
            filename = f'screenshot_{datetime.now()}.jpg'

        related_path = os.path.join(screenshot_folder, filename)
        self.driver.save_screenshot(related_path)

        logger.info('Screenshot saved: %s', os.path.abspath(related_path))

        return related_path

    @property
    def current_url(self):
        logger.info('Calling "current_url" property')
        return self.driver.current_url

    def maximize(self):
        logger.info('Maximizing web browser window')
        self.driver.maximize_window()

    def quit(self):
        logger.info('Closing web browser with id=%s', self.browser_identifier)
        self.driver.quit()
        WebDriver.destroy(self.browser_identifier)


__all__ = ['WebBrowser']
