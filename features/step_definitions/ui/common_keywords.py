from core.web_driver.driver_manager import DriverManager


def close_driver_session():
    DriverManager.get_instance().get_web_driver().quit()