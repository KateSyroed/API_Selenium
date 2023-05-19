from selenium.webdriver.common.by import By
from page.base_page_driver import BasePageWithDriver
from controls.locators import Locators

class AddCarPage(BasePageWithDriver):
    ADD_CAR_LOCATOR = (By.XPATH, Locators.ADD_CAR_BUTTON_XPATH)
    BRAND_INPUT_LOCATOR = (By.XPATH, Locators.BRAND_INPUT_XPATH)
    MODEL_INPUT_LOCATOR = (By.XPATH, Locators.MODEL_INPUT_XPATH)
    MILEAGE_INPUT_LOCATOR = (By.XPATH, Locators.MILEAGE_INPUT_XPATH)
    ADD_BUTTON_LOCATOR = (By.XPATH, Locators.ADD_BUTTON_XPATH)
    def signup(self, brand, model, mileage):
        self.driver.find_element(*self.ADD_CAR_LOCATOR).click()
        self.send_keys(self.BRAND_INPUT_LOCATOR, brand)
        self.send_keys(self.MODEL_INPUT_LOCATOR, model)
        self.send_keys(self.MILEAGE_INPUT_LOCATOR, mileage)
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def send_keys(self, locator, text):
        pass

    def add_car(self, car_data):
        pass
