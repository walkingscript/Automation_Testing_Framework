from time import sleep

import pytest

from apps.steam import Steam
from framework.web.browser import WebBrowser


class TestSteamShop:

    def setup_method(self):
        self.browser = WebBrowser()
        self.browser.maximize()
        self.browser.navigate('https://store.steampowered.com/')
        self.steam = Steam(self.browser)

    def teardown_method(self):
        self.browser.quit()

    @pytest.mark.demo_test
    def test_steam(self):
        self.steam.main_page.categories_btn.move_to_element()
        self.steam.main_page.select_category('Симулятор гонок')
        game_labels = self.steam.category_page.game_names.find_all()
        names = [gl.text for gl in game_labels]

        # just for test purposes
        scroll_pos = 0
        step = 250
        while scroll_pos < 1300:
            self.steam.category_page.scroll_down(step)
            scroll_pos += step
            sleep(2)

        self.steam.category_page.scroll_up()
        sleep(2)

        assert 'Forza Horizon 5' in names, 'Incredible! Forza is not on top!'
