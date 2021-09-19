from framework.core.default_page import DefaultPage
from framework.core.web_elements import Link


class Menu(DefaultPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.my_page = '//li[@id="l_pr"]//span[contains(@class, "left_label") and contains(@class, "inl_bl")]'

    def navigate(self, menu_item):
        Link(menu_item, self.browser).click()
