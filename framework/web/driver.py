from logging import getLogger

from .driver_factory import WebDriverCreator

logger = getLogger(__name__)


class WebDriver:
    __drivers = {}

    @classmethod
    def get_driver(cls, browser_identifier):
        if not (driver := cls.__drivers.get(browser_identifier, None)):
            logger.info('Creating new web driver for browser with id=%s', browser_identifier)
            driver = WebDriverCreator.create_driver()
            cls.__drivers[browser_identifier] = driver
        return driver

    @classmethod
    def destroy(cls, browser_identifier):
        logger.info('Destroying WebDriver for web browser with id=%s', browser_identifier)
        del cls.__drivers[browser_identifier]
