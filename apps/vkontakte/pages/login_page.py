from framework import config
from framework.core.default_page import DefaultPage
from framework.core.web_elements import EditBox, Button


class LoginPage(DefaultPage):

    def __init__(self, browser):
        super().__init__(browser)

        self.login_eb = EditBox('//input[@id="index_email"]', self.browser, 'Email or Phone number')
        self.password_eb = EditBox('//input[@id="index_pass"]', self.browser, 'Password')
        self.login_btn = Button('//button[@id="index_login_button"]', self.browser, 'Entrance Button')

    def log_in(self):
        self.login_eb.set_text(config.VK_LOGIN)
        self.password_eb.set_text(config.VK_PASSWORD)
        self.login_btn.click()
