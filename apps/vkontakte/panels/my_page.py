import typing

from apps.vkontakte.panels.wall_post import PostBlock
from framework.core.default_page import DefaultPage


class Wall(DefaultPage):

    post: typing.Union[PostBlock, None] = None

    def find_post(self, post_id, user_id):
        return PostBlock(self.browser, post_id, user_id)
