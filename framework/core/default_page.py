import logging
import typing

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver

from .web_elements import WebElement

logger = logging.getLogger(__name__)


class DefaultPage:

    def __init__(self, browser):
        logger.info('Initialization of %s', self.__class__.__name__)
        self.browser = browser
        self._driver: WebDriver = self.browser.driver

    def wait_page_opened(self, locator: typing.Collection):
        """Returns True if indicated element presented on the page."""
        logger.info('Waiting while page will be opened')
        element = WebElement(locator, self.browser, 'Some Unique Element On The WebPage')
        element.wait_until_not_visible()

    def is_alert_presented(self):
        """Returns True if alert presented, False otherwise."""
        logger.info('Checking alert is presented')
        try:
            self._driver.switch_to.alert
        except NoAlertPresentException:
            return False
        else:
            self.switch_to_default_content()
        return True

    def accept_alert(self):
        """Accepts alert if it is exists"""
        logger.info('Accepting alert window')
        return self._driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Cancel for presented alert"""
        logger.info('Dismissing alert window')
        return self._driver.switch_to.alert.dismiss()

    def print_to_alert(self, text):
        """If alert supports input, method will have typed text"""
        logger.info('Printing text="%s" to alert', text)
        self._driver.switch_to.alert.send_keys(text)

    @property
    def alert_text(self):
        """Returns alert text if alert is presented."""
        logger.info('Getting alert text')
        return self._driver.switch_to.alert.text

    def switch_to_frame(self, frame):
        """Switch to frame from default content"""
        logger.info('Switching to frame')
        self._driver.switch_to.frame(frame.get_web_element())

    def switch_to_default_content(self):
        """Switch to default content from frame"""
        logger.info('Switching to default content')
        self._driver.switch_to.default_content()

    def scroll_down(self, offset=0):
        """Scroll the page down."""
        logger.info('Scrolling down')
        if offset:
            self._driver.execute_script(f'window.scrollBy(0, {offset});')
        else:
            # scroll to end of page
            self._driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """Scroll the page up."""
        logger.info('Scrolling up')
        if offset:
            self._driver.execute_script(
                f'window.scrollBy(0, -{offset});'
            )
        else:
            # scroll to top of the page
            self._driver.execute_script('window.scrollBy(0, -document.body.scrollHeight);')


__all__ = ['DefaultPage']
