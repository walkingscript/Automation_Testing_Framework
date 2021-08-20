from collections import namedtuple

from selenium.webdriver.common.by import By


Locator = namedtuple('Locator', ('type', 'value'))
NamedLocator = namedtuple('Locator', ('description', 'type', 'value'))
