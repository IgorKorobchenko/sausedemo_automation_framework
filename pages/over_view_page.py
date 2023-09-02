import time

from .check_out_step_one_page import CheckoutStepOnePage
from .inventorypage import InventoryPage
from .shoppingcart import ShoppingCartPage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators
from locators.locators import DropDownMenu
from locators.locators import ShoppingCart
from locators.locators import CheckOutPageStepOne
from locators.locators import CheckOutPageStepTwo


class OverViewPage(CheckoutStepOnePage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu
    shopping_cart_locators = ShoppingCart
    checkout_step_one_locators = CheckOutPageStepOne
    checkout_step_two_locators = CheckOutPageStepTwo

    def open_overview_page(self):
        self.fill_all_registration_form_fields()

    def overview_title_is_present(self):
        self.open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.CHECKOUT_OVERVIEW_TITLE)

    def QTY_label_is_present(self):
        self.open_overview_page()
        assert self.element_is_present(self.shopping_cart_locators.QTY_LABEL)

    def description_label_is_present(self):
        self.open_overview_page()
        assert self.element_is_present(self.shopping_cart_locators.QTY_LABEL)

    def product_name_is_resent(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_NAME)

    def product_description_is_resent(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_PRODUCT_DESCRIPTION)

    def product_price_is_resent(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_PRICE)

    def product_qty_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.ONE_ITEM)

    def payment_info_title_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.PAYMENT_INFO_LABEL)

    def shipping_info_title_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.SHIPPING_INFO_TITLE)

    def delivery_company_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.DELIVERY_COMPANY)
