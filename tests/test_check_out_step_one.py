import time

import pytest

from pages.basepage import URL
from pages.check_out_step_one_page import CheckoutStepOnePage

"""TC_04.01 Make sure that the drop-down menu is present"""


@pytest.mark.smoke
def test_open_checkout_step_one_page(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.open_checkout_step_one_page()


"""TC_04.02 Make sure that the Checkout: Your Information tittle is present"""


def test_checkout_title_is_present(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.checkout_title_is_present()


"""TC_04.03 Make sure that the Swag Labs logo is present"""


def test_swag_labs_logo_is_present_on_checkout_page(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.swag_labs_logo_is_present_on_checkout_page()


"""TC_04.04 Make sure that the registration form is present"""


def test_registration_form_is_present(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.registration_form_is_present()


"""TC_04.05 Make sure that the Continue button is present"""


def test_continue_btn_is_present_on_checkout_page(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.continue_btn_is_present_on_checkout_page()


"""TC_04.06 Make sure that the Continue button is clickable"""


@pytest.mark.smoke
def test_continue_btn_is_clickable(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.continue_btn_is_clickable()


"""TC_04.07 Make sure that the Continue cancel button is present"""


def test_cancel_btn_is_present_on_checkout_page(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.cancel_btn_is_present_on_checkout_page()


"""TC_04.08 Make sure that the Continue cancel button is clickable and redirects user to the shopping cart"""


@pytest.mark.smoke
def test_cancel_btn_is_clickable(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.cancel_btn_is_present_on_checkout_page()


"""TC_04.09 Make sure that user is able to fill all fields and will be redirected to the next page"""


@pytest.mark.smoke
def test_fill_all_registration_form_fields(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.fill_all_registration_form_fields()


"""TC_04.10 Make sure that user is NOT able TO continue registration process if first name field is empty"""


@pytest.mark.smoke
def test_user_can_not_continue_registration_without_first_name(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.don_not_fill_first_name()


"""TC_04.11 Make sure that user is NOT able TO continue registration process if last name field is empty"""


@pytest.mark.smoke
def test_user_can_not_continue_registration_without_last_name(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.don_not_fill_last_name()


"""TC_04.12 Make sure that user is NOT able TO continue registration process if zip/postal code field is empty"""


@pytest.mark.smoke
def test_user_can_not_continue_registration_without_zip_code(driver):
    page = CheckoutStepOnePage(driver, URL)
    page.open_page()
    page.don_not_fill_zip_code()
