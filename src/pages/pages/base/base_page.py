from core.web_driver.driver_manager import DriverManager
# from selenium.webdriver.support.ui import upport.PageFactory
# from selenium.common.support import .PageFactory
class BasePage:

    def __init__(self):
        self.web_driver = DriverManager.get_instance().get_web_driver()
        self.web_driver.maximize_window()

        self.web_driver_wait = DriverManager.get_instance().get_web_driver_wait()
        # PageFactory.initElements(self.web_driver, self)


    def close_driver_session(self):
        self.web_driver.quit()