from framework.core.default_page import DefaultPage
from .pages.category import CategoryPage
from .pages.download import DownloadPage
from .pages.game import GamePage
from .pages.main import MainPage


class Steam(DefaultPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.main_page = MainPage(self.browser)
        self.game_page = GamePage(self.browser)
        self.download_page = DownloadPage(self.browser)
        self.category_page = CategoryPage(self.browser)
