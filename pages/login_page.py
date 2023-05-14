from selenium.webdriver.common.by import By
from base_page_driver import BasePage
from controls.locators import Locators

class LoginPage(BasePage):
    USER_LOGIN_LOCATOR = (By.XPATH, Locators.LOGIN_INPUT_XPATH)
    USER_PASSWORD_LOCATOR = (By.XPATH, Locators.PASS_INPUT_XPATH)
    LOGIN_BUTTON_LOCATOR = (By.XPATH, Locators.LOGIN_BUTTON_XPATH)

    def login(self, username, password):
        self.send_keys(self.USER_LOGIN_LOCATOR, username)
        self.send_keys(self.USER_PASSWORD_LOCATOR, password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()

