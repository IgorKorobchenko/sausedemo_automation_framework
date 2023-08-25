import time

from pages.basepage import URL
from pages.inventorypage import InventoryPage
from pages.shoppingcart import ShoppingCartPage

"""TC_03.01 Make sure that the drop-down menu is present"""


def test_drop_down_menu_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.drop_down_menu_is_present()


"""TC_03.02 Make sure that the Your cart tittle is present"""


def test_your_cart_title_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.your_cart_title_is_present()


"""TC_03.03 Make sure that the Swag Labs logo is present"""


def test_swab_lab_logo_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.swab_lab_logo_is_present()


"""TC_03.04 Make sure that the shopping cart container is present"""


def test_shopping_cart_container_is_present_in_container(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.shopping_cart_container_is_present_in_container()


"""TC_03.05 Make sure that the QTY label is present"""


def test_QTY_label_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.QTY_label_is_present()

"""TC_03.06 Make sure that the Description label is present"""


def test_description_label_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.description_label_is_present()

"""TC_03.07 Make sure that the Continue Shopping button is present"""



def test_continue_shopping_btn_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.continue_shopping_btn_is_present()


"""TC_03.07.01 Make sure that the Continue Shopping button is clickable and the user will be redirected to the 
inventory page"""


def test_continue_shopping_btn_is_clickable(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.continue_shopping_btn_is_clickable()



"""TC_03.08 Make sure that the Checkout button is present"""


def test_checkout_btn_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.checkout_btn_is_present()

"""TC_03.08.01 Make sure that the Checkout button is clickable and the user will be redirected to the checkout step 
one page"""


def test_checkout_btn_is_clickable(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.checkout_btn_is_clickable()



"""TC_03.09 Make sure that the item section with description, quantity, and price is present on the cart page"""


def test_item_with_dscptn_is_present(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.item_with_dscptn_is_present()


"""TC_03.10 Make sure that the item can be removed from the cart"""

def test_item_can_be_removed(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.item_can_be_removed()

"""TC_03.11 Make sure that the checkout button is not clikable if the cart is empty and the user won't be redirected 
to the step one page """


def test_user_can_NOT_be_redirected_to_step_one(driver):
    page = ShoppingCartPage(driver, URL)
    page.open_page()
    page.user_can_NOT_be_redirected_to_step_one()
    time.sleep(3)