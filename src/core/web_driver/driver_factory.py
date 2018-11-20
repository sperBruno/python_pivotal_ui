from selenium.common.exceptions import WebDriverException
from core.web_driver.browser_enum import BrowserEnum
from core.web_driver.chrome import Chrome
from core.web_driver.firefox import FireFox

BROWSER_NOT_FOUND_MSG = "Browser not found."


class DriverFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_driver(browser):
        BrowserEnum.valueOf(browser.u())
        if BrowserEnum.CHROME.name is browser.upper():
            return Chrome()
        elif BrowserEnum.FIREFOX.name is browser.upper():
            return FireFox()
        elif BrowserEnum.EXPLORER.name is browser.upper():
            raise NotImplemented()
        else:
            raise WebDriverException(BROWSER_NOT_FOUND_MSG)
