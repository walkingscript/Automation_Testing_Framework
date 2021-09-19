from logging import getLogger

import allure
import vk_api

from apps.vkontakte import VKontakte
from framework import config
from framework.web.browser import WebBrowser

logger = getLogger(__name__)


class TestVkontakte:

    def setup_method(self):
        self.browser = WebBrowser()
        self.browser.maximize()
        self.browser.navigate(config.VK_URL)
        self.vkontakte = VKontakte(self.browser)

        self.session = vk_api.VkApi(token=config.VK_API_TOKEN, api_version=config.VK_API_VERSION)
        self.vk_api = self.session.get_api()

    def teardown_method(self):
        self.browser.quit()

    @allure.feature('API')
    @allure.story('Adding and removing wall post')
    @allure.severity('normal')
    def test_vk(self):
        logger.info('[UI] Authorization')
        self.vkontakte.login_page.log_in()

        logger.info('[UI] Transition to "My page"')
        self.vkontakte.menu.navigate(self.vkontakte.menu.my_page)

        logger.info('[API] Adding record to the wall')

        message = "Hello, Everybody!"
        post_id = self.vk_api.wall.post(message=message)['post_id']

        logger.info('[UI] Checking the record have appeared on the page')
        user_id = self.vk_api.users.get()[0]['id']
        logger.info('User ID = %s', user_id)

        logger.info('[UI] Updating page through transition to "my page"')
        self.vkontakte.menu.navigate(self.vkontakte.menu.my_page)

        post = self.vkontakte.wall.find_post(post_id, user_id)
        assert post, 'Post not found!'
        post_text = post.text
        assert post_text == message, "Text did not matched with expected!"

        self.vk_api.wall.delete(post_id=post_id)
