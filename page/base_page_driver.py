from driver import Driver
class BasePageWithDriver:
    def __init__(self):
        self.driver = Driver.get_chrome_driver()

    def clear_and_send_keys(self, locator, text):
            element = self.driver.find_element(*locator)
            element.send_keys(text)

