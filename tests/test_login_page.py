import allure

from pages.basepage import URL
from pages.loginpage import LoginPage
import time

"""TC_01.01 Make sure that the login page can be launched"""


@allure.feature('Test that the login page can be launched')
def test_login_page_can_be_launched(driver):
    page = LoginPage(driver, URL)
    page.open_page()


"""TC_01.01.01 Make sure that the login form is present(username field, password field, and login button)"""


@allure.feature('Test that the login form is present(username field, password field, and login button)')
def test_login_form_is_present(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_form_is_present()


"""TC_01.02 Make sure that the user is able to log in with valid credentials"""


@allure.feature('Test that the user is able to log in with valid credentials')
def test_login_with_valid_credentials(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_with_valid_credentials()


"""TC_01.03 Make sure that the user is not able to log in with wrong username and wrong password"""


@allure.feature('Test that the user is not able to log in with wrong username and wrong password')
def test_login_with_fake_credentials(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_with_fake_credentials()


"""TC_01.04 Make sure that the user is not able to log in with correct username and wrong password"""


@allure.feature('Test that the user is not able to log in with correct username and wrong password')
def test_login_with_correct_username_and_wrong_password(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_with_correct_username_and_wrong_password()


"""TC_01.05 Make sure that the user is not able to log in with wrong username and correct password"""


@allure.feature('Test that the user is not able to log in with wrong username and correct password')
def test_login_with_wrong_username_and_correct_password(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_with_wrong_username_and_correct_password()


"""TC_01.06 Make sure that the user is not able to log in with empty username and password fields"""


@allure.feature('Test that the user is not able to log in with empty username and password fields')
def test_login_with_empty_username_and_password_fields(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_with_empty_username_and_password_fields()


"""TC_01.07 Make sure that the user is not able to log in with correct username and empty password field"""


@allure.feature('Test that the user is not able to log in with correct username and empty password field')
def test_login_with_correct_username_and_empty_password_field(driver):
    page = LoginPage(driver, URL)
    page.open_page()
    page.login_with_correct_username_and_empty_password_field()
