import time
from .inventorypage import InventoryPage
from .shoppingcart import ShoppingCartPage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators
from locators.locators import DropDownMenu
from locators.locators import ShoppingCart
from locators.locators import CheckOutPageStepOne


class CheckoutStepOnePage(ShoppingCartPage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu
    shopping_cart_locators = ShoppingCart
    checkout_step_one_locators = CheckOutPageStepOne

    def open_checkout_step_one_page(self):
        self.checkout_btn_is_clickable()
        assert self.element_is_present(self.checkout_step_one_locators.CHECKOUT_YOUR_INFO_TITLE)




