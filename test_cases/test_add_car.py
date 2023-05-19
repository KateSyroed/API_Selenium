import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.sign_up_page import SignUpPage
from page.login_page import LoginPage
from page.add_car_page import AddCarPage
from model.sign_up import SignUpPostModel
from model.login import UserLogin
from model.add_car import AddCarPostModel

class TestAddCar(unittest.TestCase):

    def setUp(self):
        # Set up the browser instance
        self.driver = webdriver.Firefox()

        # Open the page for signing up
        self.driver.get("https://qauto2.forstudy.space")

        # Create a new user account
        signup_page = SignUpPage(self.driver)
        signup_data = SignUpPostModel("John", "Doe", "johndoe@example.com", "password", "password")
        signup_page.signup(signup_data.name, signup_data.lastName, signup_data.email, signup_data.password, signup_data.repeatPassword)

        # Log in to the website
        login_page = LoginPage(self.driver)
        login_data = UserLogin("johndoe@example.com", "password")
        login_page.login(login_data.email, login_data.password)

    def tearDown(self):
        # Close the browser instance
        self.driver.quit()

    def test_add_car(self):
        # Add a new car
        add_car_page = AddCarPage(self.driver)
        add_car_data = AddCarPostModel("1", "1", "10000")
        add_car_page.add_car(add_car_data.carBrandId, add_car_data.carModelId, add_car_data.mileage)

        # Assert that the car has been added successfully (you can modify this assertion based on your application)
        success_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]")
        self.assertIsNotNone(success_message)

if __name__ == '__main__':
    unittest.main()
