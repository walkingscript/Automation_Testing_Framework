from pyautogui import click
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select as BaseSelect
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

import framework.utils.logger
from framework.core.types import By, Locator
from framework.settings.config import config
from framework.utils.logger import logger, info
from framework.browser.webdriver import WebDriver
from framework.core.errors import MethodDoesNotSupportThisLocator


class WebElement:

    def __init__(self, locator_type, locator, description: str = '', wait_timeout=0):
        framework.utils.logger.info(f"Creating element %s with name=%s and locator=%s" % (self.__class__.__name__, description, locator))
        self._web_driver = WebDriver.get_driver()
        self._default_wait = WebDriverWait(self._web_driver, float(config.element_search_timeout))
        self.no_wait = wait_timeout
        self.name = description
        self.locator = Locator(locator_type, locator)
        self.element = None
        self.find()

    def find(self):
        """Default search for an element."""
        framework.utils.logger.info(f"{self.__class__.__name__}.find Searching of '{self.name}' by locator {self.locator}")
        if self.element is None:
            self.research()

    def research(self):
        """Forced search for an element."""
        if self.no_wait:
            self.element = self._web_driver.find_element(*self.locator)
        else:
            self.element = self._default_wait.until(ec.presence_of_element_located(self.locator))

    @info("Searching of multiple elements.")
    def find_all(self):
        if self.locator.type != By.XPATH:
            raise MethodDoesNotSupportThisLocator(self.locator.type)
        result_list = []
        items = self._default_wait.until(ec.presence_of_all_elements_located((By.XPATH, self.locator.value)))
        for i, item in enumerate(items, 1):
            result_list.append(
                self.__class__(f'{self.__class__.__name__} {i}', By.XPATH, f'({self.locator.value})[{i}]')
            )
        return result_list

    @info('Checking for an element presence.')
    def is_presented(self):
        return True if self._web_driver.find_elements(*self.locator) else False

    @info('Clicking to the element')
    def click(self):
        self.research()
        self.element.click()

    def safe_click(self, hold_seconds=0, x_offset=1, y_offset=1):
        framework.utils.logger.info(f"{self.__class__.__name__}.click to '{self.name}'")
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).pause(hold_seconds)\
                .click(on_element=element).perform()
        else:
            raise AttributeError('ELEMENT NOT FOUND')

    def double_click(self, hold_seconds=0, x_offset=1, y_offset=1):
        framework.utils.logger.info(f"{self.__class__.__name__}.double_click to '{self.name}'")
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).pause(hold_seconds)\
                .double_click(on_element=element).perform()
        else:
            raise AttributeError('ELEMENT NOT FOUND')

    def is_visible(self):
        framework.utils.logger.info(f"{self.__class__.__name__}.is_visible Check for '{self.name}'")
        return self.element.is_displayed()

    def get_attribute(self, attr_name):
        framework.utils.logger.info(f"{self.__class__.__name__}.get_attribute '{attr_name}' from '{self.name}'")
        return self.element.get_attribute(attr_name)

    def get_text(self):
        framework.utils.logger.info(f"{self.__class__.__name__}.get_text from '{self.name}'")
        return self.element.text

    def wait_to_be_clickable(self):
        """Wait until the element will be ready for click."""
        framework.utils.logger.info(f"{self.__class__.__name__}.wait_to_be_clickable for '{self.name}'")
        element = self._default_wait.until(ec.element_to_be_clickable(self.locator))
        return element

    def wait_until_not_visible(self):
        framework.utils.logger.info(f"{self.__class__.__name__}.wait_until_not_visible for '{self.name}'")
        element = self._default_wait.until(ec.visibility_of_element_located(self.locator))
        return element

    def wait_for_invisible(self):
        framework.utils.logger.info(f"{self.__class__.__name__}.wait_for_invisible for '{self.name}'")
        element = self._default_wait.until(ec.invisibility_of_element_located(self.locator))
        return element

    def is_clickable(self):
        """ Check is element ready for click or not. """
        framework.utils.logger.info(f"{self.__class__.__name__}.is_clickable '{self.name}'")
        element = self.wait_to_be_clickable()
        return element is not None

    def move_to_element(self):
        action = ActionChains(self._web_driver)
        action.move_to_element_with_offset(self.element, 5, 5).perform()


class Button(WebElement):
    pass


class Label(WebElement):
    pass


class TextBox(WebElement):

    def send_keys(self, keys):
        framework.utils.logger.info(f"{self.__class__.__name__}.send_keys to '{self.name}'")
        self.research()
        keys = keys.replace('\n', '\ue007')
        self.element.send_keys(keys)

    def set_text(self, text):
        self.clear()
        self.send_keys(text)

    def clear(self):
        self.research()
        self.element.clear()

    def select_text(self):
        self.element.send_keys(Keys.LEFT_CONTROL, Keys.HOME)
        self.element.send_keys(Keys.LEFT_CONTROL, Keys.SHIFT, Keys.END)


class CheckBox(WebElement):
    pass


class Frame(WebElement):

    def get_web_element(self):
        """Returns WebElement object"""
        return self.element


class Link(WebElement):

    def get_link(self):
        self.research()
        return self.element.get_attribute('href')


class Select(WebElement):

    def select_by_value(self, value):
        framework.utils.logger.info(f"{self.__class__.__name__}.select_by_value for '{self.name}'")
        self.research()
        select = BaseSelect(self.element)
        select.select_by_value(value)


class Block(WebElement):
    pass


__all__ = [Button, Label, TextBox, CheckBox, Frame, Link, Select]
