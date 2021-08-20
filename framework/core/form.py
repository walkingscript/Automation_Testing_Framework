from selenium.common.exceptions import NoAlertPresentException

from framework.utils.logger import logger
from framework.browser.webdriver import WebDriver


class BaseForm:

    def __init__(self):
        self._web_driver = WebDriver.get_driver()

    def is_opened(self, locator_type: str, locator: str):
        """Returns True if indicated element presented on the page."""
        return self.is_element_presented(locator_type, locator)

    def is_element_presented(self, locator_type: str, locator: str):
        """Returns True if element found on the page."""
        elements = self._web_driver.find_elements(locator_type, locator)
        return True if elements else False

    def is_alert_presented(self):
        """Returns True if alert presented"""
        try:
            self._web_driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def accept_alert(self):
        """Will accept alert if it is exists"""
        return self._web_driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Cancel for presented alert"""
        return self._web_driver.switch_to.alert.dismiss()

    def print_to_alert(self, text):
        """If alert supports input, method will have typed text"""
        self._web_driver.switch_to.alert.send_keys(text)

    @property
    def alert_text(self):
        """If alert is presented, command will have returned it text"""
        return self._web_driver.switch_to.alert.text

    def switch_to_frame(self, frame):
        """Switch to frame from default content"""
        self._web_driver.switch_to.frame(frame.get_web_element())

    def switch_to_default_content(self):
        """Switch to default content from frame"""
        self._web_driver.switch_to.default_content()

    def execute_javascript(self, script: str):
        self._web_driver.execute_script(script)

    def scroll_down(self, offset=0):
        """Scroll the page down."""
        if offset:
            self.execute_javascript(f'''window.scrollTo(0, {offset});''')
        else:
            # scroll to end of page
            self.execute_javascript('''window.scrollTo(0, document.body.scrollHeight);''')

    def scroll_up(self, offset=0):
        """Scroll the page up."""
        if offset:
            self.execute_javascript(f'''window.scrollTo(0, document.documentElement.scrollHeight - {abs(offset)});''')
        else:
            # scroll to top of the page
            self.execute_javascript('''window.scrollTo(0, 0);''')
