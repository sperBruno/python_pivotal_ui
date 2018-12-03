from robot.api.deco import keyword
from robot.api import logger
from pages.pivotal_page import PivotalPage
from robot.libraries.BuiltIn import BuiltIn

pivotal = PivotalPage()
login_page = None
dashboard_page = None


def i_navigate_to_pivotal_page():
    logger.info("Navigating to Pivotal webpage")
    pivotal.go_to_pivotal_page()


def i_click_on_login_button():
    logger.info("Navigating to Pivotal webpage")
    login_page = pivotal.click_login_btn()


@keyword("I set '${user_name}' as user")
def i_set_user(user_name):
    logger.info("Inserting to user textbox: {}".format(user_name))
    login_page.set_user(user_name)


@keyword("I set password '${user_password}'")
def i_set_password(user_password):
    logger.info("Inserting to password textbox: {}".format(user_password))
    login_page.set_password(user_password)


def i_click_on_login_button_on_login_page():
    logger.info("Clicking on login button")
    dashboard_page = login_page.click_login()


def dashboard_is_displayed():
    logger.info("Pivotal Dashboard is displayed")
    BuiltIn().should_be_true(dashboard_page.is_displayed(), "Dashboard Page is not displayed")
