from robot.api import logger
from pages.login_page import LoginPage


class PivotalPage:
    def __init__(self):
        pass

    def click_login_btn(self):
        logger.info("PivotalPage::click login btn")
        return LoginPage()

    def go_to_pivotal_page(self):
        logger.info("PivotalPage::go to pivotal page")

