from selenium.common.exceptions import WebDriverException
from core.web_driver.browser_enum import Browser
from core.web_driver.chrome import Chrome
from core.web_driver.firefox import FireFox

BROWSER_NOT_FOUND_MSG = "Browser not found."


class DriverFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_driver(browser_type):
        if "CHROME" == browser_type.upper():
            return Chrome()
        elif "FIREFOX" == browser_type.upper():
            return FireFox()
        elif "EXPLORER" == browser_type.upper():
            raise NotImplemented()
        else:
            raise WebDriverException(BROWSER_NOT_FOUND_MSG)
