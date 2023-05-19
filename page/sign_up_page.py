from selenium.webdriver.common.by import By
from controls.locators import Locators
from page.base_page_driver import BasePage


class SignUpPage(BasePage):
    USER_NAME_LOCATOR = (By.XPATH, Locators.USER_NAME_XPATH)
    USER_LASTNAME_LOCATOR = (By.XPATH, Locators.USER_LASTNAME_XPATH)
    USER_EMAIL_LOCATOR = (By.XPATH, Locators.EMAIL_XPATH)
    SIGUP_PASS_LOCATOR = (By.XPATH, Locators.SIGNUP_PASS_XPATH)
    REPEAT_PASS_LOCATOR = (By.XPATH, Locators.REPEAT_PASS_XPATH)
    REGISTER_BUTTON_LOCATOR = (By.XPATH, Locators.REGISTER_BUTTON)


    def signup(self, name, last_name, email, password, repeat_password):
        self.send_keys(self.USER_NAME_LOCATOR, name)
        self.send_keys(self.USER_LASTNAME_LOCATOR, last_name)
        self.send_keys(self.USER_EMAIL_LOCATOR, email)
        self.send_keys(self.SIGUP_PASS_LOCATOR, password)
        self.send_keys(self.REPEAT_PASS_LOCATOR, repeat_password)
        self.driver.find_element(*self.REGISTER_BUTTON_LOCATOR).click()