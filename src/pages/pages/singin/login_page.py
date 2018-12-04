from robot.api import logger
from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage
from pages.dashboard.dashboard import Dashboard
from utils.common_actions import CommonActions


class LoginPage(BasePage):

    def __int__(self):
        BasePage.__init__(self)

    def set_user(self, user_name):
        logger.info("LoginPage:: set user {}".format(user_name))
        # CommonActions.set_input_field(self.web_driver.find_element_by_id("credentials_username"), user_name)
        # CommonActions.set_input_field((By.ID, "credentials_username"), user_name)
        user_txt = self.web_driver.find_element_by_id("credentials_username")
        user_txt.clear()
        user_txt.click()
        user_txt.send_keys(user_name)

    def set_password(self, user_password):
        logger.info("LoginPage:: set user {}".format(user_password))
        # CommonActions.set_input_field(self.web_driver.find_element_by_id("credentials_password"), user_password)
        # CommonActions.set_input_field((By.ID, "credentials_password"), user_password)
        password_txt = self.web_driver.find_element_by_id("credentials_password")
        password_txt.clear()
        password_txt.click()
        password_txt.send_keys(user_password)

    def click_login(self):
        logger.info("LoginPage::click login button")
        # CommonActions.click_button(self.web_driver.find_element_by_class_name("app_signin_action_button"))
        CommonActions.click_button((By.CLASS_NAME, "app_signin_action_button"))
        # next_btn = driver.find_element_by_class_name("app_signin_action_button")
        # next_btn.click()
        # return Dashboard()

    def login_as(self, user, password):
        self.set_user(user)
        self.click_login()
        self.set_password(password)
        self.click_login()
        return Dashboard()
