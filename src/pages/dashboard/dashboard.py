from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from core.web_driver.driver_manager import DriverManager
from pages.base.base_page import BasePage

PROFILE_DROPDOWN_BUTTON = "div[data-aid='ProfileDropdown'] > button"


class Dashboard(BasePage):
    def __int__(self):
        BasePage.__init__(self)

    def is_dashboard_displayed(self):
        try:
            DriverManager.get_instance().get_web_driver_wait().until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, PROFILE_DROPDOWN_BUTTON)))
            return True
        except:
            return False

    def get_user_name(self):
        user_dropdown = self.web_driver.find_element_by_css_selector("div[data-aid='ProfileDropdown'] > button")
        return user_dropdown.text
