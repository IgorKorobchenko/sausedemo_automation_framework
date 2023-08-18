import time

from .basepage import URL, BasePage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators
    inventory_locators = InventoryPageLocators

    def go_to_login_page(self):
        self.driver.get(URL)
        assert self.driver.find_element(self.locators.SWAG_LABS_LOGO)

    def login_form_is_present(self):
        assert self.element_is_present(self.locators.USER_NAME_FIELD)
        assert self.element_is_present(self.locators.PASSWORD_FIELD)
        assert self.element_is_present(self.locators.LOGIN_BTN)

    def login_with_valid_credentials(self):
        self.element_is_present(self.locators.USER_NAME_FIELD).send_keys(self.locators.USER_NAME)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.locators.PASSWORD)
        self.element_is_present(self.locators.LOGIN_BTN).click()
        assert self.element_is_visible(self.inventory_locators.BACKPACK_IMG)

    def login_with_fake_credentials(self):
        self.element_is_present(self.locators.USER_NAME_FIELD).send_keys(self.locators.USER_NAME_WRONG)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.locators.PASSWORD_WRONG)
        self.element_is_present(self.locators.LOGIN_BTN).click()
        assert self.element_is_present(self.locators.USER_NAME_AND_PASSWORD_ARE_REQUIRED)

    def login_with_correct_username_and_wrong_password(self):
        self.element_is_present(self.locators.USER_NAME_FIELD).send_keys(self.locators.USER_NAME)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.locators.PASSWORD_WRONG)
        self.element_is_present(self.locators.LOGIN_BTN).click()
        assert self.element_is_present(self.locators.USER_NAME_AND_PASSWORD_ARE_REQUIRED)

    def login_with_wrong_username_and_correct_password(self):
        self.element_is_present(self.locators.USER_NAME_FIELD).send_keys(self.locators.USER_NAME_WRONG)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.locators.PASSWORD)
        self.element_is_present(self.locators.LOGIN_BTN).click()
        assert self.element_is_present(self.locators.USER_NAME_AND_PASSWORD_ARE_REQUIRED)

    def login_with_empty_username_and_password_fields(self):
        self.element_is_present(self.locators.USER_NAME_FIELD).send_keys(self.locators.USER_NAME_EMPTY)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.locators.PASSWORD_EMPTY)
        self.element_is_present(self.locators.LOGIN_BTN).click()
        assert self.element_is_present(self.locators.USERNAME_IS_REQUIRED_MSG)

    def login_with_correct_username_and_empty_password_field(self):
        self.element_is_present(self.locators.USER_NAME_FIELD).send_keys(self.locators.USER_NAME)
        self.element_is_present(self.locators.PASSWORD_FIELD).send_keys(self.locators.PASSWORD_EMPTY)
        self.element_is_present(self.locators.LOGIN_BTN).click()
        assert self.element_is_present(self.locators.PASSWORD_IS_REQUIRED_MSG)


