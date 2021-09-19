from framework.core.default_page import DefaultPage
from framework.core.web_elements import Label


class GamePage(DefaultPage):

    def __init__(self, browser):
        super(GamePage, self).__init__(browser)

        self.discount_rate = Label(
            '//*[@id="game_area_purchase"]//*[@class="game_area_purchase_game_wrapper"]//*[(@class="discount_pct")]',
            self.browser
        )
        self.discount_initial_price = Label(
            '//*[@id="game_area_purchase"]//*[@class="game_area_purchase_game_wrapper"]//*[(@class='
            '"discount_prices")]//*[@class="discount_original_price"]',
            self.browser
        )
        self.discount_final_price = Label(
            '//*[@id="game_area_purchase"]//*[@class="game_area_purchase_game_wrapper"]//*[(@class='
            '"discount_prices")]//*[@class="discount_final_price"]',
            self.browser
        )

        # multiple elements section
        self.game_names = Label('//*[@class="apphub_AppName"]', self.browser)
