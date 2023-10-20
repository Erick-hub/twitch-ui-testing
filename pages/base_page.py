from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_text(self, by_locator):
        """clear text field"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def get_attribute(self, by_locator, attribute) -> str:
        """Returns the title of the page"""
        element = self.get_single_element(by_locator)
        return element.get_attribute(attribute)

    def get_multiple_elements(self, by_locator):
        by, string = by_locator
        return self.driver.find_elements(by, string)

    def get_single_element(self, by_locator):
        by, string = by_locator
        return self.driver.find_element(by, string)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def execute_script(self, script, *argument):
        self.driver.execute_script(script, argument)
