from framework.core.default_page import DefaultPage
from framework.core.web_elements import Button, Link, Label, WebElement


class PostBlock(DefaultPage):

    def __init__(self, browser, post_id, user_id):
        super().__init__(browser)

        self.post_id = post_id
        self.user_id = user_id

        # inherited locators
        self.post_xpath = f'//div[@id="post{user_id}_{post_id}"]'
        self.post_content_xpath = f'{self.post_xpath}//div[@id="wpt{user_id}_{post_id}"]'

        # web elements
        self.post_block = WebElement(self.post_content_xpath, self.browser, f'Post {post_id}')
        self.post_text = Label(f'{self.post_content_xpath}//div[contains(@class, "wall_post_text")]',
                               self.browser, description='Post Text')
        self.like_btn = Button(f'{self.post_xpath}//div[contains(@class, "PostButtonReactions__icon")]',
                               self.browser, 'Post Like Button')
        self.show_more_comments_link = Link(f'{self.post_xpath}//a[contains(@class, "replies_next")]',
                                            self.browser, description='Show more comments link')
        self.comments_btn = Button(
            f'{self.post_xpath}//div[contains(@class, "PostBottomAction") and contains(@class, "comment")]',
            self.browser,
            description='Comments Button'
        )

    def wait_disappear(self):
        content = WebElement(self.post_content_xpath, self.browser, 'Post content block')
        content.wait_disappear()

    @property
    def text(self):
        return self.post_text.text

    def like(self):
        self.like_btn.click()

    def show_more_comments(self):
        self.show_more_comments_link.click()
