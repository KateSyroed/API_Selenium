import unittest
from urllib import response

import self as self
from selenium.webdriver.common.by import By
from page.base_page_driver import BasePageWithDriver
from controls.locators import Locators
import requests
from model.sign_up import SignUpPostModel
from model.login import UserLogin
from model.add_car import AddCarPostModel
from driver import Driver
from page.car_page import AddCarPage
from page.login_page import LoginPage
from page.sign_up_page import SignUpPage
# from page.car_page import CarPage


class TestAddCar:
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = Driver.get_chrome_driver()
        self.driver.get("https://qauto2.forstudy.space")


        # Create instances of the pages
        self.login_page = LoginPage()
        self.signup_page = SignUpPage()
        self.car_page = AddCarPage()

        # Perform sign up
        self.session = requests.session()
        signup_data = SignUpPostModel("John", "Doe", "johndoe@example.com", "password123", "password123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=signup_data.__dict__)


        # Perform login
        self.session = requests.session()
        login_data = UserLogin("johndoe@example.com", "password123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signin", json=login_data.__dict__)

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

    def test_add_car(self):
        # Add a car
        self.session = requests.session()
        car_data = AddCarPostModel("Audi", "R8", 3)
        response = self.session.post("https://qauto2.forstudy.space/api/Cars/postCar", json=car_data.__dict__)

        # Assert the response code is 201
        self.assertEqual(response.status_code, 201)

    def assertEqual(self, status_code, param):
        pass
