import time

from pages.basepage import URL
from pages.check_out_step_one_page import CheckoutStepOnePage

"""TC_04.01 Make sure that the drop-down menu is present"""


def test_open_checkout_step_one_page(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.open_checkout_step_one_page()

"""TC_04.02 Make sure that the Checkout: Your Information tittle is present"""




"""TC_04.03 Make sure that the Swag Labs logo is present"""

"""TC_04.04 Make sure that the address form is present"""

"""TC_04.05 Make sure that the Continue button is present"""

"""TC_04.06 Make sure that the Continue button is clickable and redirects user to the next registration step"""

"""TC_04.07 Make sure that the Continue cancel button is present"""

"""TC_04.08 Make sure that the Continue cancel button is clickable and redirects user to the shopping cart"""

"""TC_04.09 Make sure that user is able to fill all fields and continue registration process on the next page"""

"""TC_04.10 Make sure that user is NOT able TO continue registration process if first name field is empty"""

"""TC_04.11 Make sure that user is NOT able TO continue registration process if last name field is empty"""

"""TC_04.12 Make sure that user is NOT able TO continue registration process if zip/postal code field is empty"""
