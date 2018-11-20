from selenium import webdriver

from core.web_driver.idriver import IDriver


class Chrome(IDriver):

    def init_driver(self):
        #TODO: create util to get path to drivers
        return webdriver.Chrome(executable_path="../../../drivers/chromedriver")

