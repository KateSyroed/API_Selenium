from selenium.webdriver.common.by import By
from model.sign_up import SignUpPostModel
from page.base_page_driver import BasePageWithDriver
from controls.locators import Locators
class SignUpPage(BasePageWithDriver):
    USER_NAME_LOCATOR = (By.XPATH, Locators.USER_NAME_XPATH)
    USER_LASTNAME_LOCATOR = (By.XPATH, Locators.USER_LASTNAME_XPATH)
    USER_EMAIL_LOCATOR = (By.XPATH, Locators.EMAIL_XPATH)
    SIGUP_PASS_LOCATOR = (By.XPATH, Locators.SIGNUP_PASS_XPATH)
    REPEAT_PASS_LOCATOR = (By.XPATH, Locators.REPEAT_PASS_XPATH)
    REGISTER_BUTTON_LOCATOR = (By.XPATH, Locators.REGISTER_BUTTON)

    def signup(self, signup_data: SignUpPostModel):
        self.send_keys(self.USER_NAME_LOCATOR, signup_data.name)
        self.send_keys(self.USER_LASTNAME_LOCATOR, signup_data.lastName)
        self.send_keys(self.USER_EMAIL_LOCATOR, signup_data.email)
        self.send_keys(self.SIGUP_PASS_LOCATOR, signup_data.password)
        self.send_keys(self.REPEAT_PASS_LOCATOR, signup_data.repeatPassword)
        self.driver.find_element(*self.REGISTER_BUTTON_LOCATOR).click()

    def send_keys(self, locator, text):
        self.clear_and_send_keys(locator, text)