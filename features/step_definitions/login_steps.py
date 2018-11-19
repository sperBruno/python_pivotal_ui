from robot.api.deco import keyword
from robot.api import logger


def i_navigate_to_pivotal_page():
    logger.info("Navigating to Pivotal webpage")


def i_click_on_login_button():
    logger.info("Navigating to Pivotal webpage")


@keyword("I set '${user_name}' as user")
def i_set_user(user_name):
    logger.info("Inserting to user textbox: {}".format(user_name))


@keyword("I set password '${user_password}'")
def i_set_password(user_password):
    logger.info("Inserting to password textbox: {}".format(user_password))


def i_click_on_login():
    logger.info("Clicking on login button")

def dashboard_is_displayed():
    logger.info("Pivotal Dashboard is displayed")