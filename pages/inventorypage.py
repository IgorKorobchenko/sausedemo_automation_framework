import time

from .basepage import BasePage, URL
from .loginpage import LoginPage
from locators.locators import LoginPageLocators
from locators.locators import InventoryPageLocators
from locators.locators import DropDownMenu
from locators.locators import ShoppingCart


class InventoryPage(LoginPage):
    inventory_locators = InventoryPageLocators
    locators = LoginPageLocators
    dropdown_locators = DropDownMenu
    shopping_cart_locators = ShoppingCart

    def go_to_inventory_page(self):
        self.login_with_valid_credentials()

    def drop_down_menu_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.dropdown_locators.DROP_DOWN_MENU)

    def swag_labs_logo_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_visible(self.inventory_locators.SWAG_LABS_LOGO)

    def shopping_cart_container_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_CONTAINER)

    def go_to_shopping_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.SHOPPING_CART_CONTAINER).click()
        assert self.element_is_present(self.shopping_cart_locators.YOUR_CART_TITLE)

    def products_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.PRODUCTS_TTL)

    def filer_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.OPEN_FILTERS)

    def backpack_image_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_IMG)

    def backpack_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_NAME)

    def backpack_product_description_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_PRODUCT_DESCRIPTION)

    def backpack_price_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_PRICE)

    def backpack_add_btn_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BACKPACK_ADD_TO_CART_BTN)

    def add_backpack_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.BACKPACK_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_BADGE)

    def add_backpack_to_cart_and_open_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.BACKPACK_ADD_TO_CART_BTN).click()
        self.element_is_present(self.inventory_locators.SHOPPING_CART_CONTAINER).click()


    def bike_light_image_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BIKE_LIGHT_IMG)

    def bike_light_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BIKE_LIGHT_NAME)

    def bike_light_product_description_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BIKE_LIGHT_PRODUCT_DESCRIPTION)

    def bike_light_price_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BIKE_LIGHT_PRICE)

    def bike_light_add_btn_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.BIKE_LIGHT_ADD_TO_CART_BTN)

    def add_bike_light_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.BIKE_LIGHT_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_BADGE)

    def t_shirt_image_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_IMG)

    def t_shirt_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_NAME)

    def t_shirt_product_description_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_PRODUCT_DESCRIPTION)

    def t_shirt_price_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_PRICE)

    def add_t_shirt_btn_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_ADD_TO_CART_BTN)

    def add_t_shirt_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_BADGE)

    def fleece_jacket_image_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.FLEECE_JACKET_IMG)

    def fleece_jacket_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.FLEECE_JACKET_NAME)

    def fleece_jacket_product_description_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.FLEECE_JACKET_PRODUCT_DESCRIPTION)

    def fleece_jacket_price_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.FLEECE_JACKET_PRICE)

    def add_fleece_jacket_btn_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.FLEECE_JACKET_ADD_TO_CART_BTN)

    def add_fleece_jacket_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.FLEECE_JACKET_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_BADGE)

    def onesie_image_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.ONESIE_NAME_IMG)

    def onesie_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.ONESIE_NAME)

    def onesie_product_description_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.ONESIE_PRODUCT_DESCRIPTION)

    def onesie_price_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.ONESIE_PRICE)

    def add_onesie_btn_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.ONESIE_NAME_ADD_TO_CART_BTN)

    def add_onesie_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.ONESIE_NAME_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_BADGE)

    def all_things_t_shirt_image_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_IMG)

    def all_things_t_shirt_title_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_NAME)

    def all_things_t_shirt_product_description_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_PRODUCT_DESCRIPTION)

    def all_things_t_shirt_price_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_PRICE)

    def add_all_things_t_shirt_btn_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_ADD_TO_CART_BTN)

    def add_all_things_t_shirt_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_BADGE)

    def twitter_icon_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.TWITTER_LINK)

    def facebook_icon_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.FACEBOOK_LINK)

    def linkedin_icon_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.LINKEDIN_LINK)

    def all_rights_reserved_is_present(self):
        self.go_to_inventory_page()
        assert self.element_is_present(self.inventory_locators.ALL_RIGHTS_RESERVED)

    def add_one_item_to_cart(self):
        self.add_all_things_t_shirt_to_cart()
        self.element_is_present(self.inventory_locators.FLEECE_JACKET_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.TWO_ITEMS_IN_CART)

    def add_all_items_to_cart(self):
        self.go_to_inventory_page()
        self.element_is_present(self.inventory_locators.BACKPACK_ADD_TO_CART_BTN).click()
        self.element_is_present(self.inventory_locators.BIKE_LIGHT_ADD_TO_CART_BTN).click()
        self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_ADD_TO_CART_BTN).click()
        self.element_is_present(self.inventory_locators.FLEECE_JACKET_ADD_TO_CART_BTN).click()
        self.element_is_present(self.inventory_locators.ONESIE_NAME_ADD_TO_CART_BTN).click()
        self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_ADD_TO_CART_BTN).click()
        assert self.element_is_present(self.inventory_locators.SIX_ITEMS_IN_CART)
        self.element_is_present(self.inventory_locators.BACKPACK_REMOVE_BTN)

    def correct_number_of_items_in_cart_when_removed(self):
        self.add_all_items_to_cart()
        self.element_is_present(self.inventory_locators.ONESIE_NAME_REMOVE_BTN).click()
        assert self.element_is_present(self.inventory_locators.FIVE_ITEMS_IN_CART)

    def remove_all_items(self):
        self.add_all_items_to_cart()
        self.element_is_present(self.inventory_locators.BACKPACK_REMOVE_BTN).click()
        time.sleep(1)
        self.element_is_present(self.inventory_locators.BIKE_LIGHT_REMOVE_BTN).click()
        time.sleep(1)
        self.element_is_present(self.inventory_locators.T_SHIRT_BOLT_REMOVE_BTN).click()
        time.sleep(1)
        self.element_is_present(self.inventory_locators.FLEECE_JACKET_REMOVE_BTN).click()
        time.sleep(1)
        self.element_is_present(self.inventory_locators.ONESIE_NAME_REMOVE_BTN).click()
        time.sleep(1)
        self.element_is_present(self.inventory_locators.T_SHIRT_TEST_ALL_THE_THINGS_REMOVE_BTN).click()
        assert self.element_is_present(self.inventory_locators.SHOPPING_CART_CONTAINER)

    def sort_items_a_to_z(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.OPEN_FILTERS).click()
        self.element_is_clickable(self.inventory_locators.NAME_A_Z).click()
        ExpectedResult = []
        list_of_items = self.elements_are_present(self.inventory_locators.INVENTORY_ITEM_NAME)
        for title in list_of_items:
            ExpectedResult.append(title.text)
        ActualResult = sorted(ExpectedResult)
        assert (ExpectedResult == ActualResult)

    def sort_items_Z_to_A(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.OPEN_FILTERS).click()
        self.element_is_clickable(self.inventory_locators.NAME_Z_A).click()
        ExpectedResult = []
        list_of_items = self.elements_are_present(self.inventory_locators.INVENTORY_ITEM_NAME)
        for title in list_of_items:
            ExpectedResult.append(title.text)
        ActualResult = sorted(ExpectedResult, reverse=True)
        assert (ExpectedResult == ActualResult)

    def sort_items_low_to_high(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.OPEN_FILTERS).click()
        self.element_is_clickable(self.inventory_locators.PRICE_LOW_TO_HIGH).click()
        ExpectedResult = []
        list_of_items = self.elements_are_present(self.inventory_locators.INVENTORY_ITEM_PRICE)
        for title in list_of_items:
            ExpectedResult.append(title.text[1::])
        ActualResult = sorted(ExpectedResult, key=float)
        assert (ExpectedResult == ActualResult)

    def sort_items_high_to_low(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.inventory_locators.OPEN_FILTERS).click()
        self.element_is_clickable(self.inventory_locators.PRICE_HIGH_TO_LOW).click()
        ExpectedResult = []
        list_of_items = self.elements_are_present(self.inventory_locators.INVENTORY_ITEM_PRICE)
        for title in list_of_items:
            ExpectedResult.append(title.text[1::])
        ActualResult = sorted(ExpectedResult, key=float, reverse=True)
        assert (ExpectedResult == ActualResult)

    def open_drop_down(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.dropdown_locators.DROP_DOWN_MENU).click()
        assert self.element_is_present(self.dropdown_locators.ABOUT)

    def close_drop_down(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.dropdown_locators.DROP_DOWN_MENU).click()
        self.element_is_clickable(self.dropdown_locators.CLOSE_BTN).click()
        time.sleep(1)
        assert self.element_is_present(self.dropdown_locators.DROP_DOWN_MENU)

    def open_about_url(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.dropdown_locators.DROP_DOWN_MENU).click()
        self.element_is_clickable(self.dropdown_locators.ABOUT).click()
        assert self.element_is_present(self.dropdown_locators.ABOUT_SAUSE_LOGO)

    def log_out(self):
        self.go_to_inventory_page()
        self.element_is_clickable(self.dropdown_locators.DROP_DOWN_MENU).click()
        self.element_is_clickable(self.dropdown_locators.LOGOUT).click()
        assert self.element_is_present(self.locators.SWAG_LABS_LOGO)






















