from datetime import time
from selenium.webdriver.support.wait import WebDriverWait
from core.web_driver.driver_factory import DriverFactory
from utils.property_handler import PropertyHandler

IMPLICIT_TIME_WAIT = PropertyHandler.get_instance().get_implicit_time_wait()
EXPLICIT_TIME_WAIT = PropertyHandler.get_instance().get_explicit_time_wait()


class DriverManager:
    instance = None

    def __init__(self):
        self.driverType = PropertyHandler.get_instance().get_browser().upper()
        print self.driverType
        self.web_driver_wait = None
        self.web_driver = DriverFactory.get_driver(self.driverType).init_driver()
        self.restore_previous_time_wait()

    @staticmethod
    def get_instance():
        if DriverManager.instance is None:
            DriverManager.instance = DriverManager()
        return DriverManager.instance

    def get_web_driver(self):
        return self.web_driver

    def get_web_driver_wait(self):
        return self.web_driver_wait

    def set_implicit_time_wait(self, implicit_time_wait):
        self.web_driver.implicitly_wait(implicit_time_wait)

    def set_explicit_time_wait(self, explicit_time_wait):
        self.web_driver_wait = WebDriverWait(self.web_driver, explicit_time_wait)

    def update_time_wait(self, time_wait):
        self.set_implicit_time_wait(time_wait)
        self.set_explicit_time_wait(time_wait)

    def restore_previous_time_wait(self):
        self.set_implicit_time_wait(IMPLICIT_TIME_WAIT)
        self.set_explicit_time_wait(EXPLICIT_TIME_WAIT)
