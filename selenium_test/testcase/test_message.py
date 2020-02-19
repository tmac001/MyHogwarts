# @Time : 2020-02-15 18:07
from selenium_test.page.create_message_page import CreateMessagePage


class TestMessage:
    def setup(self):
        self.create_message = CreateMessagePage(reuse=True)

    def test_send_message(self):
        self.create_message.send_message()
