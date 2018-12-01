from core.web_driver.driver_manager import DriverManager


class BasePage:



    def __init__(self):
        self.webDriver = DriverManager.get_instance().get_web_driver()
        self.webDriverWait = DriverManager.get_instance().get_web_driver_wait()
        PageFactory.initElements(webDriver, this);
