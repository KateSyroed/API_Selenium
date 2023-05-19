class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)
