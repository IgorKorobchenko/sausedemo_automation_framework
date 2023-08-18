import allure

from pages.inventorypage import InventoryPage
from pages.basepage import URL

"""TC_02.01 Make sure that the drop-down menu is present"""


#@allure.feature('Test that the drop-down menu is present')
def test_drop_down_menu_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.drop_down_menu_is_present()


"""TC_02.02 Make sure that the Swag Labs logo is present"""


#@allure.feature('Test that the Swag Labs logo is present')
def test_swag_labs_logo_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.swag_labs_logo_is_present()


"""TC_02.03 Make sure that the shopping cart container sign is present"""

"""TC_02.03.01 Make sure that the user will be redirected to the shopping cart page after clicking on the cart sign """

"""TC_02.04 Make sure that the "Products" title is present"""

"""TC_02.05 Make sure that the filter is present"""

"""TC_02.06.01 Make sure that the Sauce Labs Backpack image is present"""

"""TC_02.06.02 Make sure that the Sauce Labs Backpack title is present"""

"""TC_02.06.03 Make sure that the Sauce Labs Backpack product description is present"""

"""TC_02.06.04 Make sure that the Sauce Labs Backpack price is present"""

"""TC_02.06.05 Make sure that Add to cart button is present for the Sauce Labs Backpack"""

"""TC_02.06.06 Make sure that the user is able to add the Sauce Labs Backpack to the shopping cart"""

"""TC_02.06.07 Make sure that the user is able to remove the Sauce Labs Backpack from the shopping cart"""

"""TC_02.07.01 Make sure that the Sauce Labs Bike light image is present"""

"""TC_02.07.02 Make sure that the Sauce Labs Bike light title is present"""

"""TC_02.07.03 Make sure that the Sauce Labs Bike light product description is present"""

"""TC_02.07.04 Make sure that the Sauce Labs Bike light price is present"""

"""TC_02.07.05 Make sure that Add to cart button is present for the Sauce Labs Bike light"""

"""TC_02.07.06 Make sure that the user is able to add the Sauce Labs Bike light to the shopping cart"""

"""TC_02.07.07 Make sure that the user is able to remove the Sauce Labs Bike light from the shopping cart"""

"""TC_02.08.01 Make sure that the Sauce Labs Bolt T-Shirt image is present"""

"""TC_02.08.02 Make sure that the Sauce Labs Bolt T-Shirt title is present"""

"""TC_02.08.03 Make sure that the Sauce Labs Bolt T-Shirt product description is present"""

"""TC_02.08.04 Make sure that the Sauce Labs Bolt T-Shirt price is present"""

"""TC_02.08.05 Make sure that Add to cart button is present for the Sauce Labs Bolt T-Shirt"""

"""TC_02.08.06 Make sure that the user is able to add the Sauce Labs Bolt T-Shirt to the shopping cart"""

"""TC_02.08.07 Make sure that the user is able to remove the Sauce Labs Bolt T-Shirt from the shopping cart"""

"""TC_02.09.01 Make sure that the Sauce Labs Fleece Jacket image is present"""

"""TC_02.09.02 Make sure that the Sauce Labs Fleece Jacket title is present"""

"""TC_02.09.03 Make sure that the Sauce Labs Fleece Jacket product description is present"""

"""TC_02.09.04 Make sure that the Sauce Labs Fleece Jacket price is present"""

"""TC_02.09.05 Make sure that Add to cart button is present for the Sauce Labs Fleece Jacket"""

"""TC_02.09.06 Make sure that the user is able to add the Sauce Labs Fleece Jacket to the shopping cart"""

"""TC_02.09.07 Make sure that the user is able to remove the Sauce Labs Fleece Jacket from the shopping cart"""

"""TC_02.10.01 Make sure that the Sauce Labs Onesie image is present"""

"""TC_02.10.02 Make sure that the Sauce Labs Onesie title is present"""

"""TC_02.10.03 Make sure that the Sauce Labs Onesie product description is present"""

"""TC_02.10.04 Make sure that the Sauce Labs Onesie price is present"""

"""TC_02.10.05 Make sure that Add to cart button is present for the Sauce Labs Onesie"""

"""TC_02.10.06 Make sure that the user is able to add the Sauce Labs Onesie to the shopping cart"""

"""TC_02.10.07 Make sure that the user is able to remove the Sauce Labs Onesie from the shopping cart"""

"""TC_02.11.01 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) image is present"""

"""TC_02.11.02 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) title is present"""

"""TC_02.11.03 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) product description is present"""

"""TC_02.11.04 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) price is present"""

"""TC_02.11.05 Make sure that Add to cart button is present for the Sauce Labs Test.allThings() T-Shirt(Red)"""

"""TC_02.11.06 Make sure that the user is able to add the Sauce Labs Test.allThings() T-Shirt(Red) to the shopping 
cart """

"""TC_02.11.07 Make sure that the user is able to remove the Sauce Labs Test.allThings() T-Shirt(Red) from the 
shopping cart """

"""TC_02.12.01 Make sure that the Twitter icon is present"""

"""TC_02.12.02 Make sure that the Facebook icon is present"""

"""TC_02.12.03 Make sure that the Linkedin icon is present"""

"""TC_02.12.02 Make sure that the Facebook icon is present"""

"""TC_02.12.02 Make sure that All rights reserved. Terms of Service|Privacy Policy title is present"""

"""TC_02.13.01 Make sure that the badge with the quantity of items appears is present when an item added to the 
shopping cart """

"""TC_02.13.02 Make sure that the badge with the number of items is changed after removing items from the shopping 
cart """

"""TC_02.14.01 Make sure that the user is able to add all present items to the shopping cart"""

"""TC_02.14.02 Make sure that the user is able to remove all present items to the shopping cart"""

"""TC_02.15.01 Make sure that all items can be filtered from A to Z"""

"""TC_02.15.02 Make sure that all items can be filtered from Z to A"""

"""TC_02.15.03 Make sure that all items can be filtered from low to high"""

"""TC_02.15.03 Make sure that all items can be filtered from high to low"""

"""TC_02.16.01 Make sure that the drop-down menu can be opened"""

"""TC_02.16.02 Make sure that the drop-down menu can be closed"""

"""TC_02.16.03 Make sure that the about page can be opened"""

"""TC_02.16.04 Make sure that the user is able to logout"""
