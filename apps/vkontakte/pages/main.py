from framework.core.default_page import DefaultPage
from ..panels.menu import Menu


class MainPage(DefaultPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.menu = Menu(browser)
