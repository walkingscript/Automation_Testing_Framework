import os

from framework.utils.logger import logger
from framework.settings.config import config
from framework.browser.webdriver import WebDriver
from framework.browser.cookies import Cookies


class WebBrowser:
    """Defines basic browser functions."""

    def __init__(self):
        logger.info('Creating WebBrowser...')
        browser_identifier = id(self)
        self.driver = WebDriver.get_driver(browser_identifier)
        self.cookies = Cookies(browser_identifier)

    def navigate(self, url='', login=None, password=None):
        logger.info(f'Navigating to {url}...')
        if login and password:
            url = url.replace('//', f'//{login}:{password}@', 1)
        self.driver.get(url)

    def go_back(self):
        logger.info('Going back')
        self.driver.back()

    def refresh(self):
        logger.info('Refreshing page')
        self.driver.refresh()

    def screenshot(self, filename='screenshot.png'):
        screenshot_folder = config.screenshots_folder
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder, exist_ok=True)
        related_path = os.path.join(screenshot_folder, filename)
        logger.info(f"Saving screenshot as {related_path}")
        self.driver.save_screenshot(related_path)
        return related_path

    @property
    def current_url(self):
        return self.driver.current_url

    def maximize(self):
        logger.info(f'Maximizing browser window.')
        self.driver.maximize_window()

    def quit(self):
        logger.info(f'Closing browser.')
        self.driver.quit()
        WebDriver.destroy(id(self))
