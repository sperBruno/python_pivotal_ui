from robot.api import logger
from pages.pivotal_page import PivotalPage
from robot.libraries.BuiltIn import BuiltIn

pivotal = PivotalPage()
login_page = None
dashboard_page = None

logger.info("Navigating to Pivotal webpage")
pivotal.go_to_pivotal_page()

logger.info("Navigating to Pivotal webpage")
login_page = pivotal.click_login_btn()

logger.info("Inserting to user textbox: {}".format("pirateTest@mailinator.com"))
login_page.set_user("pirateTest@mailinator.com")
login_page.click_login()

logger.info("Inserting to password textbox: {}".format("pirateTest"))
login_page.set_password("pirateTest123")

dashboard_page = login_page.click_login()

logger.info("Pivotal Dashboard is displayed")
BuiltIn().should_be_true(dashboard_page.is_dashboard_displayed(), "Dashboard Page is not displayed")
