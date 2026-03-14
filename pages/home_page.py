from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    """
    Locators for elements on Home Page
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()