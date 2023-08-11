from selenium.webdriver.common.by import By

class LoginPageLocators:
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    USER_NAME = "standard_user"
    PASSWORD = "secret_sauce"
    USER_NAME_EMPTY = ""
    PASSWORD_EMPTY = ""
    USER_NAME_WRONG = "ABBA"
    PASSWORD_WRONG = "BABBA"

