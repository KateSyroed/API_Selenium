from model.sign_up import SignUpPostModel
from model.login import UserLogin
import requests
from driver import Driver
from pages.login_page import LoginPage(BasePage)
from pages.sign_up_page import SignUpPage(BasePage)
from locators import Locators
from base_page import BasePage


class TestAuthentication:
    def setup_class_signup(self):
        self.driver = Driver.get_chrome_driver()
        self.sign_up_page = SignUpPagePage()
        self.garage_page = GaragePage()
        self.session = requests.session()
        register_user = SignUpPostModel("Jon", "Snow", "tes3t5132334ts@rs.fd", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)

    def setup_class_login(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.session = requests.session()
        login_user = UserLogin("tes3t5132334ts@rs.fd", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=login_user.__dict__)

        assert

def test_check_login_window(self):
        self.login_page.get_sign_in_button().click()
        assert self.login_page.get_email_field().is_displayed()

    def test_check_incorrect_email(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("asd123")
        self.login_page.get_remember_me_button().click()
        assert self.login_page.get_login_incorrect_alert().is_displayed()

    def test_check_successful_login(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("test1234ts@rs.fd")
        self.login_page.get_password_field().fill_field("Qwerty123")
        self.login_page.get_login_button().click()
        assert self.garage_page.get_my_profile_button().is_displayed()

    def test_check_login_with_removed_user(self):
        new_user = RegisterPostModel("Jon", "Snow", "teasds3t5132334ts@rs.fd", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=new_user.__dict__)
        self.session.delete("https://qauto2.forstudy.space/api/users")
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("teasds3t5132334ts@rs.fd")
        self.login_page.get_password_field().fill_field("Qwerty123")
        self.login_page.get_login_button().click()
        self.login_page.get_wrong_user_alert().is_displayed()


    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")