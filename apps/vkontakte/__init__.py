from framework.core.default_page import DefaultPage
from .pages.login_page import LoginPage
from .panels.menu import Menu
from .panels.my_page import Wall


class VKontakte(DefaultPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.menu = Menu(self.browser)
        self.login_page = LoginPage(self.browser)
        self.wall = Wall(self.browser)
