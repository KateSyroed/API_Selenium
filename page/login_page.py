from selenium.webdriver.common.by import By

from model.login import UserLogin
from page.base_page_driver import BasePageWithDriver
from controls.locators import Locators
class LoginPage(BasePageWithDriver):
    USER_LOGIN_LOCATOR = (By.XPATH, Locators.LOGIN_INPUT_XPATH)
    USER_PASSWORD_LOCATOR = (By.XPATH, Locators.PASS_INPUT_XPATH)
    LOGIN_BUTTON_LOCATOR = (By.XPATH, Locators.LOGIN_BUTTON_XPATH)

    def login(self, user_login: UserLogin):
        self.send_keys(self.USER_LOGIN_LOCATOR, user_login.email)
        self.send_keys(self.USER_PASSWORD_LOCATOR, user_login.password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()

    def send_keys(self, locator, text):
        self.clear_and_send_keys(locator, text)