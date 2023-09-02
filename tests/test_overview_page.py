from pages.basepage import URL
from pages.over_view_page import OverViewPage

"""TC_05.01 Make sure that the Checkout: Overview tittle is present"""


def test_overview_title_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.overview_title_is_present()


"""TC_05.02 Make sure that the QTY label is present"""


def test_QTY_label_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.QTY_label_is_present()


"""TC_05.03 Make sure that the Description label is present"""


def test_description_label_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.description_label_is_present()


"""TC_05.04 Make sure that product name is present"""


def test_product_name_is_resent(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.product_name_is_resent()


"""TC_05.0 Make sure that product description is present"""


def test_product_description_is_resent(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.product_description_is_resent()


"""TC_05.0 Make sure that product price is present"""


def test_product_price_is_resent(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.product_price_is_resent()


"""TC_05.08 Make sure that product quantity is present"""


def test_product_qty_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.product_qty_is_present()


"""TC_05.09 Make sure that the Payment information tittle is present"""


def test_payment_info_title_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.payment_info_title_is_present()


"""TC_05.10 Make sure that the Shipping information tittle is present"""


def test_shipping_info_title_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.shipping_info_title_is_present()


"""TC_05.11 Make sure that the name of delivery company is present"""


def test_delivery_company_is_present(driver):
    page = OverViewPage(driver, URL)
    page.open_page()
    page.delivery_company_is_present()


"""TC_05.12 Make sure that the Price Total tittle is present"""

"""TC_05.13 Make sure that the item total price is present and correct"""

"""TC_05.14 Make sure that the tax is present and correct"""

"""TC_05.15 Make sure that the total price with tax is present and correct"""

"""TC_05.16 Make sure that the cancel button is present"""

"""TC_05.17 Make sure that the cancel button is clickable and redirects user to the previous page"""

"""TC_05.18 Make sure that the Finish button is present"""

"""TC_05.19 Make sure that the Finish button is clickable and order can be complete"""
