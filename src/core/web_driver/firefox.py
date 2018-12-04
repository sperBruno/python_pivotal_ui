from selenium import webdriver

from core.web_driver.idriver import IDriver
# from utils.env_utils import EnvironmentUtil


class FireFox(IDriver):

    def init_driver(self):
        # driver_path = "%s/%s" % (EnvironmentUtil.get_root_folder_path(), "drivers/geckodriver")
        # print driver_path
        # return webdriver.Firefox(executable_path=driver_path)
        return webdriver.Firefox()