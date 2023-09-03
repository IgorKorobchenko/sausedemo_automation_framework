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
from locators.locators import CheckOutCompletePage


class OverViewPage(CheckoutStepOnePage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu
    shopping_cart_locators = ShoppingCart
    checkout_step_one_locators = CheckOutPageStepOne
    checkout_step_two_locators = CheckOutPageStepTwo
    complete_page_locators = CheckOutCompletePage

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

    def price_total_title_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.PRICE_TOTAL_LABEL)

    def item_total_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.ITEM_TOTAL_LABEL)

    def item_price_and_item_total_price_are_correct(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        item_price = self.element_is_present(self.inventory_locators.BACKPACK_PRICE)
        item_total_price = self.element_is_present(self.checkout_step_two_locators.ITEM_PRICE)
        text1 = item_price.text
        text2 = item_total_price.text
        price1 = float(text1.replace('$', ''))
        price2 = float(text2.split(':')[-1].replace('$', ''))
        assert price1 == price2

    def tax_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.TAX_LABEL)

    def total_price_with_tax(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        item_total_price = self.element_is_present(self.checkout_step_two_locators.ITEM_PRICE)
        item_tax = self.element_is_present(self.checkout_step_two_locators.TAX_VALUE)
        text1 = item_total_price.text
        text2 = item_tax.text
        item_total_price_number = float(text1.split(':')[-1].replace('$', ''))
        tax_number = float(text2.split(':')[-1].replace('$', ''))
        total = item_total_price_number + tax_number
        assert total == 32.39

    def cancel_btn_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_one_locators.CANCEL_BTN)

    def cancel_btn_is_clickable(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        self.element_is_clickable(self.checkout_step_one_locators.CANCEL_BTN).click()
        assert self.element_is_clickable(self.inventory_locators.ONESIE_NAME)

    def finish_btn_is_present(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        assert self.element_is_present(self.checkout_step_two_locators.FINISH_BTN)

    def finish_btn_is_clickable(self):
        self.add_backpack_to_cart_and_open_cart()
        self.element_is_clickable(self.shopping_cart_locators.CHECKOUT_BTN).click()
        self.ready_registration_form_and_open_overview_page()
        self.element_is_clickable(self.checkout_step_two_locators.FINISH_BTN).click()
        assert self.element_is_present(self.complete_page_locators.CHECKOUT_COMPLETE_TITLE)











