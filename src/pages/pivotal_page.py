from robot.api import logger

from pages.base.base_page import BasePage
from pages.singin.login_page import LoginPage
from utils.property_handler import PropertyHandler


class PivotalPage(BasePage):

    @FindBy
    singin_btn = None
    def __init__(self):
        pass

    def click_login_btn(self):
        logger.info("PivotalPage::click login btn")
        CommonActions.click_button()
        return LoginPage()

    def go_to_pivotal_page(self):
        logger.info("PivotalPage::go to pivotal page")
        self.web_driver.get(PropertyHandler.get_instance().get_base_url())

