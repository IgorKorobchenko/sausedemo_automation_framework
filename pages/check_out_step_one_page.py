import time
from .inventorypage import InventoryPage
from .shoppingcart import ShoppingCartPage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators
from locators.locators import DropDownMenu
from locators.locators import ShoppingCart
from locators.locators import CheckOutPageStepOne
from locators.locators import CheckOutPageStepTwo


class CheckoutStepOnePage(ShoppingCartPage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu
    shopping_cart_locators = ShoppingCart
    checkout_step_one_locators = CheckOutPageStepOne
    checkout_step_two_locators = CheckOutPageStepTwo

    def open_checkout_step_one_page(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.checkout_step_one_locators.FIRST_NAME_INPUT_FIELD)

    def checkout_title_is_present(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.checkout_step_one_locators.CHECKOUT_YOUR_INFO_TITLE)

    def swag_labs_logo_is_present_on_checkout_page(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.inventory_locators.SWAG_LABS_LOGO)

    def registration_form_is_present(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.checkout_step_one_locators.FIRST_NAME_INPUT_FIELD)
        assert self.element_is_present(self.checkout_step_one_locators.LAST_NAME_INPUT_FIELD)
        assert self.element_is_present(self.checkout_step_one_locators.ZIP_INPUT_FIELD)

    def continue_btn_is_present_on_checkout_page(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.checkout_step_one_locators.CONTINUE_BTN)

    def continue_btn_is_clickable(self):
        self.checkout_btn_is_clickable()
        self.element_is_clickable(self.checkout_step_one_locators.CONTINUE_BTN).click()
        assert self.element_is_present(self.checkout_step_one_locators.ERROR_MESSAGE)

    def cancel_btn_is_present_on_checkout_page(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.checkout_step_one_locators.CANCEL_BTN)

    def cancel_btn_is_clickable(self):
        self.checkout_btn_is_clickable()
        self.element_is_present(self.checkout_step_one_locators.CANCEL_BTN).click()
        assert self.element_is_present(self.shopping_cart_locators.YOUR_CART_TITLE)

    def fill_all_registration_form_fields(self):
        self.checkout_btn_is_clickable()
        self.element_is_present(self.checkout_step_one_locators.FIRST_NAME_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.FIRST_NAME)
        self.element_is_present(self.checkout_step_one_locators.LAST_NAME_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.LAST_NAME)
        self.element_is_present(self.checkout_step_one_locators.ZIP_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.ZIP_CODE)
        self.element_is_present(self.checkout_step_one_locators.CONTINUE_BTN).click()
        assert self.element_is_present(self.checkout_step_two_locators.CHECKOUT_OVERVIEW_TITLE)

    def don_not_fill_first_name(self):
        self.checkout_btn_is_clickable()
        self.element_is_present(self.checkout_step_one_locators.LAST_NAME_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.LAST_NAME)
        self.element_is_present(self.checkout_step_one_locators.ZIP_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.ZIP_CODE)
        self.element_is_present(self.checkout_step_one_locators.CONTINUE_BTN).click()
        assert self.element_is_present(self.checkout_step_one_locators.ERROR_MESSAGE_FIRST_NAME)

    def don_not_fill_last_name(self):
        self.checkout_btn_is_clickable()
        self.element_is_present(self.checkout_step_one_locators.FIRST_NAME_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.FIRST_NAME)
        self.element_is_present(self.checkout_step_one_locators.ZIP_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.ZIP_CODE)
        self.element_is_present(self.checkout_step_one_locators.CONTINUE_BTN).click()
        assert self.element_is_present(self.checkout_step_one_locators.ERROR_MESSAGE_LAST_NAME)

    def don_not_fill_zip_code(self):
        self.checkout_btn_is_clickable()
        self.element_is_present(self.checkout_step_one_locators.FIRST_NAME_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.FIRST_NAME)
        self.element_is_present(self.checkout_step_one_locators.LAST_NAME_INPUT_FIELD).send_keys(
            self.checkout_step_one_locators.LAST_NAME)
        self.element_is_present(self.checkout_step_one_locators.CONTINUE_BTN).click()
        assert self.element_is_present(self.checkout_step_one_locators.ERROR_MESSAGE_ZIP)













