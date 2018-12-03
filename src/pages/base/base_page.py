from core.web_driver.driver_manager import DriverManager


class BasePage:

    def __init__(self):
        self.web_driver = DriverManager.get_instance().get_web_driver().init_driver()
        self.web_driver_wait = DriverManager.get_instance().get_web_driver_wait()
        # PageFactory.initElements(self.web_driver, self)
