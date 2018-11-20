from selenium import webdriver

from core.web_driver.idriver import IDriver


class FireFox(IDriver):

    def init_driver(self):
        return webdriver.Firefox(executable_path="../../../drivers/geckodriver")