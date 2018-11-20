from robot.api import logger
from pages.dashboard.dashboard import Dashboard


class LoginPage:

    def __int__(self):
        pass

    def set_user(self, user_name):
        logger.info("LoginPage:: set user {}".format(user_name))

    def set_password(self, user_password):
        logger.info("LoginPage:: set user {}".format(user_password))

    def click_login(self):
        logger.info("LoginPage::click login button")
        return Dashboard()
