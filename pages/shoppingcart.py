import time

from .basepage import BasePage, URL
from .inventorypage import InventoryPage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators
from locators.locators import DropDownMenu
from locators.locators import ShoppingCart
from locators.locators import CheckOutPageStepOne


class ShoppingCartPage(InventoryPage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu
    shopping_cart_locators = ShoppingCart
    checkout_step_one_locators = CheckOutPageStepOne

    def open_shopping_cart(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.SHOPPING_CART_CONTAINER).click()

    def your_cart_title_is_present(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.shopping_cart_locators.YOUR_CART_TITLE)

    def swab_lab_logo_is_present(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.shopping_cart_locators.SWAG_LABS_LOGO)

    def shopping_cart_container_is_present_in_container(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_CONTAINER)

    def QTY_label_is_present(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.shopping_cart_locators.QTY_LABEL)

    def description_label_is_present(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.shopping_cart_locators.DESCRIPTION_LABEL)

    def continue_shopping_btn_is_present(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.shopping_cart_locators.CONTINUE_SHOPPING_BTN)

    def continue_shopping_btn_is_clickable(self):
        self.open_shopping_cart()
        self.element_is_present(self.shopping_cart_locators.CONTINUE_SHOPPING_BTN).click()
        assert self.element_is_present(self.inventory_locators.ONESIE_NAME)

    def checkout_btn_is_present(self):
        self.open_shopping_cart()
        assert self.element_is_present(self.shopping_cart_locators.CHECKOUT_BTN)

    def checkout_btn_is_clickable(self):
        self.open_shopping_cart()
        self.element_is_present(self.shopping_cart_locators.CHECKOUT_BTN).click()
        assert self.element_is_clickable(self.checkout_step_one_locators.CHECKOUT_YOUR_INFO_TITLE)

    def item_with_dscptn_is_present(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.BACKPACK_ADD_TO_CART_BTN).click()
        self.element_is_clickable(self.inventory_locators.SHOPPING_CART_CONTAINER).click()
        assert self.element_is_present(self.inventory_locators.BACKPACK_NAME)
        assert self.element_is_present(self.inventory_locators.BACKPACK_PRODUCT_DESCRIPTION)
        assert self.element_is_present(self.inventory_locators.BACKPACK_PRICE)

    def item_can_be_removed(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.BACKPACK_ADD_TO_CART_BTN).click()
        self.element_is_clickable(self.inventory_locators.SHOPPING_CART_CONTAINER).click()
        self.element_is_present(self.inventory_locators.BACKPACK_REMOVE_BTN).click()
        assert self.element_is_not_visible(self.checkout_step_one_locators.CHECKOUT_YOUR_INFO_TITLE)

    def user_can_NOT_be_redirected_to_step_one(self):
        self.open_shopping_cart()
        self.element_is_present(self.shopping_cart_locators.CHECKOUT_BTN).click()
        assert self.element_is_not_visible(self.checkout_step_one_locators.CHECKOUT_YOUR_INFO_TITLE)








