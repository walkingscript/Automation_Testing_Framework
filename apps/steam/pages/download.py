from framework.core.default_page import DefaultPage
from framework.core.web_elements import Button, Link


class DownloadPage(DefaultPage):
    
    def __init__(self, browser):
        super(DownloadPage, self).__init__(browser)

        self.install_now_btn = Button('//*[@id="about_greeting"]//*[contains(@class, "about_install")]', self.browser)

        self.download_link = Link(
            '//*[@id="about_greeting"]//*[contains(@class, "about_install")]//*[@class="about_install_steam_link"]',
            self.browser
        )
