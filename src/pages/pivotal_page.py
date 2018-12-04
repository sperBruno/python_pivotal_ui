from robot.api import logger
from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage
from pages.singin.login_page import LoginPage
from utils.common_actions import CommonActions
from utils.property_handler import PropertyHandler


class PivotalPage(BasePage):

    # @FindBy
    # singin_btn = None
    def __init__(self):
        BasePage.__init__(self)

    def click_login_btn(self):
        logger.info("PivotalPage::click login btn")
        CommonActions.click_button((By.LINK_TEXT, "Sign in"))
        return LoginPage()

    def go_to_pivotal_page(self):
        logger.info("PivotalPage::go to pivotal page")
        self.web_driver.get(PropertyHandler.get_instance().get_base_ui_url())

