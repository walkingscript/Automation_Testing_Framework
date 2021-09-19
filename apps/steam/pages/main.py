from framework.core.default_page import DefaultPage
from framework.core.web_elements import Button, Label


class MainPage(DefaultPage):

    def __init__(self, browser):
        super(MainPage, self).__init__(browser)

        self.categories_btn = Button('//*[@id="genre_tab"]', self.browser)
        self.install_steam_btn = Button('//*[@id="global_action_menu"]//a[@class="header_installsteam_btn_content"]',
                                        self.browser)

        # dynamic xpath
        self._category_xpath = '//*[@id="genre_flyout"]//a[contains(text(), "{category_name}")]'

    def select_category(self, category_name):
        xpath = self._category_xpath.format(category_name=category_name)
        Button(xpath, self.browser).click()
