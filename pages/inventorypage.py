from .basepage import BasePage, URL
from .loginpage import LoginPage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators
from locators.locators import DropDownMenu


class InventoryPage(LoginPage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu

    def go_to_inventory_page(self):
        self.login_with_valid_credentials()

    def drop_down_menu_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.dropdown_locators.DROP_DOWN_MENU)

    def swag_labs_logo_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_visible(self.inventory_locators.SWAG_LABS_LOGO)




