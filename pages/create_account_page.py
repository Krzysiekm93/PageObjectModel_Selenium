from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from utils.custom_types import Gender


class Locators:
    """
    CreateAccountPage locators
    """
    FIRST_NAME = (By.ID, "customer_firstname")
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')
    EMAIL = (By.ID, 'email')


class CreateAccountPage(BasePage):
    """
    Create Account Page Object
    """

    def choose_gender(self, gender):
        """
        Choose Mr or Mrs
        """
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()

    def enter_first_name(self, first_name):
        """
        Enter First Name
        """
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def get_email_input(self):
        """
        Taking entered e-mail
        :return String
        """
        return self.driver.find_element(*Locators.EMAIL).get_attribute("value")

    def _verify_page(self):
        # TODO: Improve this mechanism!
        sleep(3)
