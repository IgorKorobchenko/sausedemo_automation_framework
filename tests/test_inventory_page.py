import time

from pages.inventorypage import InventoryPage
from pages.basepage import URL

"""TC_02.01 Make sure that the drop-down menu is present"""


def test_drop_down_menu_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.drop_down_menu_is_present()


"""TC_02.02 Make sure that the Swag Labs logo is present"""


def test_swag_labs_logo_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.swag_labs_logo_is_present()


"""TC_02.03 Make sure that the shopping cart container sign is present"""


def test_shopping_cart_container_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.shopping_cart_container_is_present()


"""TC_02.03.01 Make sure that the user will be redirected to the shopping cart page after clicking on the cart sign """


def test_user_is_able_to_launch_shopping_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.go_to_shopping_cart()


"""TC_02.04 Make sure that the "Products" title is present"""


def test_products_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.products_title_is_present()


"""TC_02.05 Make sure that the filter is present"""


def test_filer_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.filer_is_present()


"""TC_02.06.01 Make sure that the Sauce Labs Backpack image is present"""


def test_backpack_image_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.backpack_image_is_present()


"""TC_02.06.02 Make sure that the Sauce Labs Backpack title is present"""


def test_backpack_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.backpack_title_is_present()


"""TC_02.06.03 Make sure that the Sauce Labs Backpack product description is present"""


def test_backpack_product_description_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.backpack_product_description_is_present()


"""TC_02.06.04 Make sure that the Sauce Labs Backpack price is present"""


def test_backpack_price_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.backpack_price_is_present()


"""TC_02.06.05 Make sure that Add to cart button is present for the Sauce Labs Backpack"""


def test_backpack_add_to_cart_btn_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.backpack_add_btn_is_present()


"""TC_02.06.06 Make sure that the user is able to add the Sauce Labs Backpack to the shopping cart"""


def test_add_backpack_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_backpack_to_cart()


"""TC_02.07.01 Make sure that the Sauce Labs Bike light image is present"""


def test_bike_light_image_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.bike_light_image_is_present()


"""TC_02.07.02 Make sure that the Sauce Labs Bike light title is present"""


def test_bike_light_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.bike_light_title_is_present()


"""TC_02.07.03 Make sure that the Sauce Labs Bike light product description is present"""


def test_bike_light_product_description_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.bike_light_product_description_is_present()


"""TC_02.07.04 Make sure that the Sauce Labs Bike light price is present"""


def test_bike_light_price_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.bike_light_price_is_present()


"""TC_02.07.05 Make sure that Add to cart button is present for the Sauce Labs Bike light"""


def test_bike_light_add_btn_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.bike_light_add_btn_is_present()


"""TC_02.07.06 Make sure that the user is able to add the Sauce Labs Bike light to the shopping cart"""


def test_add_bike_light_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_bike_light_to_cart()


"""TC_02.08.01 Make sure that the Sauce Labs Bolt T-Shirt image is present"""


def test_t_shirt_image_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.t_shirt_image_is_present()


"""TC_02.08.02 Make sure that the Sauce Labs Bolt T-Shirt title is present"""


def test_t_shirt_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.t_shirt_title_is_present()


"""TC_02.08.03 Make sure that the Sauce Labs Bolt T-Shirt product description is present"""


def test_t_shirt_product_description_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.t_shirt_product_description_is_present()


"""TC_02.08.04 Make sure that the Sauce Labs Bolt T-Shirt price is present"""


def test_t_shirt_price_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.t_shirt_price_is_present()


"""TC_02.08.05 Make sure that Add to cart button is present for the Sauce Labs Bolt T-Shirt"""


def test_add_t_shirt_add_btn_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_t_shirt_btn_is_present()


"""TC_02.08.06 Make sure that the user is able to add the Sauce Labs Bolt T-Shirt to the shopping cart"""


def test_add_t_shirt_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_t_shirt_to_cart()


"""TC_02.09.01 Make sure that the Sauce Labs Fleece Jacket image is present"""


def test_fleece_jacket_image_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.fleece_jacket_image_is_present()


"""TC_02.09.02 Make sure that the Sauce Labs Fleece Jacket title is present"""


def test_fleece_jacket_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.t_shirt_title_is_present()


"""TC_02.09.03 Make sure that the Sauce Labs Fleece Jacket product description is present"""


def test_fleece_jacket_product_description_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.fleece_jacket_product_description_is_present()


"""TC_02.09.04 Make sure that the Sauce Labs Fleece Jacket price is present"""


def test_fleece_jacket_price_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.fleece_jacket_price_is_present()


"""TC_02.09.05 Make sure that Add to cart button is present for the Sauce Labs Fleece Jacket"""


def test_add_fleece_jacket_btn_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_fleece_jacket_btn_is_present()


"""TC_02.09.06 Make sure that the user is able to add the Sauce Labs Fleece Jacket to the shopping cart"""


def test_add_fleece_jacket_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_fleece_jacket_to_cart()


"""TC_02.10.01 Make sure that the Sauce Labs Onesie image is present"""


def test_onesie_image_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.onesie_image_is_present()


"""TC_02.10.02 Make sure that the Sauce Labs Onesie title is present"""


def test_onesie_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.onesie_title_is_present()


"""TC_02.10.03 Make sure that the Sauce Labs Onesie product description is present"""


def test_onesie_product_description_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.onesie_product_description_is_present()


"""TC_02.10.04 Make sure that the Sauce Labs Onesie price is present"""


def test_onesie_price_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.onesie_price_is_present()


"""TC_02.10.05 Make sure that Add to cart button is present for the Sauce Labs Onesie"""


def test_add_onesie_btn_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_onesie_btn_is_present()


"""TC_02.10.06 Make sure that the user is able to add the Sauce Labs Onesie to the shopping cart"""


def test_add_onesie_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_onesie_to_cart()


"""TC_02.11.01 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) image is present"""


def test_all_things_t_shirt_image_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.all_things_t_shirt_image_is_present()


"""TC_02.11.02 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) title is present"""


def test_all_things_t_shirt_title_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.all_things_t_shirt_title_is_present()


"""TC_02.11.03 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) product description is present"""


def test_all_things_t_shirt_product_description_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.all_things_t_shirt_product_description_is_present()


"""TC_02.11.04 Make sure that the Sauce Labs Test.allThings() T-Shirt(Red) price is present"""


def test_all_things_t_shirt_price_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.all_things_t_shirt_price_is_present()


"""TC_02.11.05 Make sure that Add to cart button is present for the Sauce Labs Test.allThings() T-Shirt(Red)"""


def test_add_all_things_t_shirt_btn_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_all_things_t_shirt_btn_is_present()


"""TC_02.11.06 Make sure that the user is able to add the Sauce Labs Test.allThings() T-Shirt(Red) to the shopping 
cart """


def test_add_all_things_t_shirt_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_all_things_t_shirt_to_cart()


"""TC_02.12.01 Make sure that the Twitter icon is present"""


def test_twitter_icon_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.twitter_icon_is_present()


"""TC_02.12.02 Make sure that the Facebook icon is present"""


def test_facebook_icon_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.facebook_icon_is_present()


"""TC_02.12.03 Make sure that the Linkedin icon is present"""


def test_linkedin_icon_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.linkedin_icon_is_present()


"""TC_02.12.02 Make sure that All rights reserved. Terms of Service|Privacy Policy title is present"""


def test_all_rights_reserved_is_present(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.all_rights_reserved_is_present()


"""TC_02.13.01 Make sure that the badge with the quantity of items appears is present when an item added to the 
shopping cart """


def test_add_one_item_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_one_item_to_cart()


"""TC_02.13.02 Make sure that the badge with the number of items is changed after removing items from the shopping 
cart """


def test_correct_number_of_items_in_cart_after_removing(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.correct_number_of_items_in_cart_when_removed()


"""TC_02.14.01 Make sure that the user is able to add all present items to the shopping cart"""


def test_add_all_items_to_cart(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.add_all_items_to_cart()


"""TC_02.14.02 Make sure that the user is able to remove all present items to the shopping cart"""


def test_remove_all_items(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.remove_all_items()


"""TC_02.15.01 Make sure that all items can be filtered from A to Z"""


def test_sort_items_a_to_z(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.sort_items_a_to_z()


"""TC_02.15.02 Make sure that all items can be filtered from Z to A"""


def test_sort_items_Z_to_A(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.sort_items_Z_to_A()


"""TC_02.15.03 Make sure that all items can be filtered from low to high"""


def test_sort_items_low_to_high(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.sort_items_low_to_high()


"""TC_02.15.03 Make sure that all items can be filtered from high to low"""


def test_sort_items_high_to_low(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.sort_items_high_to_low()


"""TC_02.16.01 Make sure that the drop-down menu can be opened"""


def test_open_drop_down_menu(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.open_drop_down()


"""TC_02.16.02 Make sure that the drop-down menu can be closed"""


def test_close_drop_down(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.close_drop_down()


"""TC_02.16.03 Make sure that the about page can be opened"""


def test_open_about_url(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.open_about_url()

"""TC_02.16.04 Make sure that the user is able to logout"""


def test_log_out(driver):
    page = InventoryPage(driver, URL)
    page.open_page()
    page.log_out()
