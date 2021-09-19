import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By as LocatorType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select as BaseSelect
from selenium.webdriver.support.ui import WebDriverWait

from framework import config
from .errors import MethodDoesNotSupportThisLocator

logger = logging.getLogger(__name__)


class WebElement:

    def __init__(self, locator, browser, description=None, wait_timeout=0.0):
        logger.info("Creating element %s with locator=%s description=%s",
                    self.__class__.__name__, locator, description)
        self.browser = browser
        self.description = description
        self.element_obj = None

        if isinstance(locator, str):
            if '/' in locator:
                self.locator = (LocatorType.XPATH, locator)
            else:
                self.locator = (LocatorType.ID, locator)
        else:
            self.locator = locator

        if not wait_timeout:
            self.wait_timeout = float(config.DEFAULT_WAIT_TIMEOUT)
        else:
            self.wait_timeout = wait_timeout

        self._driver = self.browser.driver
        self.wait = WebDriverWait(self._driver, self.wait_timeout)

    def find(self):
        logger.info('Searching for element with locator: %s', self.locator)
        self.wait.until(ec.presence_of_element_located(self.locator))
        return self._driver.find_element(*self.locator)

    def find_all(self):

        if self.locator[0] != LocatorType.XPATH:
            raise MethodDoesNotSupportThisLocator(self.locator[0])

        logger.info('Searching multiple elements with locator: %s', self.locator)

        result_list = []
        items = self.wait.until(ec.presence_of_all_elements_located(self.locator))
        for i, item in enumerate(items, 1):
            result_list.append(
                self.__class__(
                    (LocatorType.XPATH, f'({self.locator[1]})[{i}]'),
                    self.browser,
                    self.description,
                    self.wait_timeout
                )
            )
        return result_list

    @property
    def web_element(self):
        if not self.element_obj:
            self.element_obj = self.find()
        self.highlight_element()
        return self.element_obj

    @property
    def text(self):
        return self.web_element.text

    @property
    def exists(self):
        logger.info('Checking existence of element with locator: %s', self.locator)
        return True if self._driver.find_elements(*self.locator) else False

    def click(self):
        logger.info('Click to element with locator: %s', self.locator)
        element = self.web_element
        self.wait_to_be_clickable()
        action = ActionChains(self._driver)
        action.move_to_element(element).click(on_element=element).perform()

    def double_click(self):
        logger.info('Double click to element with locator: %s', self.locator)
        element = self.web_element
        self.wait_to_be_clickable()
        action = ActionChains(self._driver)
        action.move_to_element(element).double_click(on_element=element).perform()

    @property
    def visible(self):
        logger.info('Checking visibility of element with locator: %s', self.locator)
        return self.web_element.is_displayed()

    def get(self, attr_name):
        logger.info('Getting attr_name="%s" for element with locator: %s', attr_name, self.locator)
        return self.web_element.get_attribute(attr_name)

    def wait_to_be_clickable(self):
        logger.info('Wait element to be clickable with locator: %s', self.locator)
        self.wait.until(ec.element_to_be_clickable(self.locator))

    def wait_until_not_visible(self):
        logger.info('Wait appearing of element with locator: %s', self.locator)
        self.wait.until(ec.visibility_of_element_located(self.locator))

    def wait_disappear(self):
        logger.info('Wait disappearing of element with locator: %s', self.locator)
        self.wait.until(ec.invisibility_of_element_located(self.locator))

    def highlight_element(self):
        self._driver.execute_script(
            f'''
                item = document.evaluate('{self.locator[1]}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE)
                if (item.singleNodeValue) {{
                    item.singleNodeValue.style.border = "3px solid red"
                }}
            '''
        )

    def move_to_element(self):
        logger.info('Moving to element with locator: %s', self.locator)
        element = self.web_element
        action = ActionChains(self._driver)
        action.move_to_element_with_offset(element, 5, 5).perform()

    def scroll_to_element(self):
        logger.info('Scrolling to element with locator: %s', self.locator)
        self._driver.execute_script(
            f'''
            item = document.evaluate('{self.locator[1]}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            item.singleNodeValue.scrollIntoView();
            '''
        )


class EditBox(WebElement):

    def send_keys(self, keys):
        logger.info('Sending keys="%s" to element with locator: %s', keys, self.locator)
        keys = keys.replace('\n', '')
        self.web_element.send_keys(keys)

    def set_text(self, text):
        logger.info('Calling method "set_text"')
        self.clear()
        self.send_keys(text)

    def clear(self):
        logger.info('Clearing text from EditBox with locator: %s', self.locator)
        self.web_element.clear()

    def select_text(self):
        logger.info('Selecting text in EditBox with locator: %s', self.locator)
        element = self.web_element
        element.send_keys(Keys.LEFT_CONTROL, Keys.HOME)
        element.send_keys(Keys.LEFT_CONTROL, Keys.SHIFT, Keys.END)


class Select(WebElement):

    def select_item_by_value(self, value):
        logger.info('Selecting item for element with locator: %s', self.locator)
        select = BaseSelect(self.web_element)
        select.select_by_value(value)


class Button(WebElement):
    pass


class CheckBox(WebElement):
    pass


class Label(WebElement):
    pass


class Link(WebElement):
    pass


__all__ = ["WebElement", "Button", "Label", "EditBox", "CheckBox", "Link", "Select"]
