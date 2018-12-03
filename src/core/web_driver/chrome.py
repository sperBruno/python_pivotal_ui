from selenium import webdriver

from core.web_driver.idriver import IDriver


class Chrome(IDriver):



    def init_driver(self):
        return webdriver.Chrome(executable_path="../../../drivers/chromedriver")

