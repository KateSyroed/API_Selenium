import requests
from model.edit_car import EditCarPutModel
from model.sign_up import SignUpPostModel
from model.login import UserLogin
from model.add_car import AddCarPostModel
from driver import Driver
from page.car_page import AddCarPage
from page.login_page import LoginPage
from page.sign_up_page import SignUpPage


class TestAddCar:
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = Driver.get_chrome_driver()
        self.driver.get("https://qauto2.forstudy.space/")


        # Create instances of the pages
        self.login_page = LoginPage()
        self.signup_page = SignUpPage()
        self.car_page = AddCarPage()

        # # Perform basic authentication
        # auth_url = "https://qauto2.forstudy.space"
        # Username = "guest"
        # Password = "welcome2qauto"
        # requests.get(auth_url, auth=HTTPBasicAuth(Username, Password))

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
        response = self.session.post("https://qauto2.forstudy.space/api/cars", json=car_data.__dict__)

        # Check the status code
        assert response.status_code == 201, "Success"

        # Check Json response
        expected_car_brand_id = "Audi"
        expected_car_model_id = "R8"
        expected_initial_mileage = 3

        response_json = response.json()

        assert response_json["status"] == expected_status, "Error: wrong 'status'"
        assert response_json["carBrandId"] == expected_car_brand_id, "Error: wrong 'carBrandId'"
        assert response_json["carModelId"] == expected_car_model_id, "Error: wrong 'carModelId'"
        assert response_json["initialMileage"] == expected_initial_mileage, "Error: wrong 'initialMileage'"

        # Car ID
        car_id = response_json["data"]["id"]

        # Test editing the car
        self.test_edit_car(car_id)

        # Test deleting the car
        self.test_delete_car(car_id)

    def test_edit_car(self,car_id):
        self.session = requests.session()
        self.session.get(f"https://qauto2.forstudy.space/api/cars/{car_id}")
        # Modify the car details
        edit_data = EditCarPutModel("Audi", "A6", 3)
        response = self.session.put(f"https://qauto2.forstudy.space/api/cars/{car_id}", json=edit_data.__dict__)

        # Check the status code
        assert response.status_code == 200, "Success"

        # Check Json response
        expected_car_brand_id = "Audi"
        expected_car_model_id = "A6"
        expected_initial_mileage = 3

        response_json = response.json()

        assert response_json["status"] == expected_status, "Error: wrong 'status'"
        assert response_json["carBrandId"] == expected_car_brand_id, "Error: wrong 'carBrandId'"
        assert response_json["carModelId"] == expected_car_model_id, "Error: wrong 'carModelId'"
        assert response_json["initialMileage"] == expected_initial_mileage, "Error: wrong 'initialMileage'"


    def test_delete_car(self,car_id):
        # Add a car
        self.session = requests.session()
        response = self.session.delete(f"https://qauto2.forstudy.space/api/cars/{car_id}")
        assert response.status_code == 200, "Success"
