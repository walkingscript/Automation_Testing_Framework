from framework.core.default_page import DefaultPage
from framework.core.web_elements import Button, Label


class CategoryPage(DefaultPage):

    def __init__(self, browser):
        super(CategoryPage, self).__init__(browser)

        self.top_sales_tab = Button('//div[@id="tab_select_TopSellers"]', self.browser)
        self.game_names = Label('//div[@id="NewReleasesRows"]/a//div[@class="tab_item_name"]', self.browser)
