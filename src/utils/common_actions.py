from robot.api import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from core.web_driver.driver_manager import DriverManager
from selenium.webdriver.support import expected_conditions


class CommonActions:

    def __init__(self):
        pass

    @staticmethod
    def set_input_field(web_element, content):
        """
             * This method set text content to a web element.
             *
             * @param webElement Is web element.
             * @param content    Is the content that will be set to the web element.
             */
        """
        DriverManager.get_instance().get_web_driver_wait().until(
            expected_conditions.element_to_be_clickable(web_element))
        element = DriverManager.get_instance().get_web_driver().find_element(web_element[0], web_element[1])
        element.clear()
        element.sendKeys(content)

    @staticmethod
    def click_button(web_element):
        """
      * This method perform a click action in a web element.
      * example (By.LINK_TEXT, "Sign in")
      * @param webElement Is the web element that will be pressed.
       """
        DriverManager.get_instance().get_web_driver_wait().until(
            expected_conditions.element_to_be_clickable(web_element))
        DriverManager.get_instance().get_web_driver().find_element(web_element[0], web_element[1]).click()

    @staticmethod
    def is_visible(web_element):
        """
        * This method verifies if a web element is visible.
        *
        * @param webElement is the web element.
        * @return true if web element is visible or false if it isn't visible.
       """
        try:
            return web_element.isDisplayed()
        except NoSuchElementException as e:
            logger.error("Element doesn't exists")
            logger.info(e)
            return False

    @staticmethod
    def get_text_content(web_element):
        """
        * This method return the text content of a WebElement.
        *
        * @param webElement is the WebElement to extract the text.
        * @return the text content of the WebElement.
        """
        DriverManager.get_instance().getWebDriverWait().until(expected_conditions.visibility_of(web_element))
        return web_element.getText()

    @staticmethod
    def get_page_title():
        """
        * This method get title of current page.
        *
        * @return title of the current page.
        """
        return DriverManager.get_instance().getWebDriver().getTitle()

    @staticmethod
    def press_enter_key(web_element):
        """
        * This method press enter key to web element.
        *
        * @param webElement is the WebElement.
        """
        web_element.sendKeys(Keys.ENTER)

    @staticmethod
    def get_error_message():
        """
        * This method return the text of message de error.
        *
        * @return the text of message error.
        """
        web_element = DriverManager.get_instance().get_web_driver_wait().until(
            expected_conditions.visibility_of_element_located(By.CSS_SELECTOR("div[data-aid='AlertDialog']")))
        return web_element.getText()

    @staticmethod
    def close_driver_session():
        DriverManager.get_instance().web_driver.quit()
