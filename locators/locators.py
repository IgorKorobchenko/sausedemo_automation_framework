from selenium.webdriver.common.by import By


class LoginPageLocators:

    SWAG_LABS_LOGO = (By.XPATH, "//div[@class='login_logo']")
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//*[@id='login-button']")
    USER_NAME = "standard_user"
    PASSWORD = "secret_sauce"
    USER_NAME_EMPTY = ""
    PASSWORD_EMPTY = ""
    USER_NAME_WRONG = "ABBA"
    PASSWORD_WRONG = "BABBA"
    PASSWORD_IS_REQUIRED_MSG = (By.XPATH, "//*[text()='Epic sadface: Password is required']")
    USERNAME_IS_REQUIRED_MSG = (By.XPATH, "//*[text()='Epic sadface: Username is required']")
    USER_NAME_AND_PASSWORD_ARE_REQUIRED = (By.XPATH, "//*[text()='Epic sadface: Username and password do not match "
                                                     "any user in this service']")


class DropDownMenu:

    DROP_DOWN_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    ALL_ITEMS = (By.XPATH, "//*[text()='All Items']")
    ABOUT = (By.XPATH, "//a[@id='about_sidebar_link']")
    LOGOUT = (By.XPATH, "//a[@id='logout_sidebar_link']")
    RESET_ALL_APP_STATE = (By.XPATH, "//a[@id='reset_sidebar_link']")
    CLOSE_BTN = (By.XPATH, "//button[text()='Close Menu']")
    ABOUT_URL = 'https://saucelabs.com/'
    ABOUT_SAUSE_LOGO = (By.XPATH, '//*[@src="/images/logo.svg"]')


class InventoryPageLocators:

    PRODUCTS_TTL = (By.XPATH, "//span[@class='title']")
    SWAG_LABS_LOGO = (By.XPATH, "//div[text()='Swag Labs']")
    SHOPPING_CART_CONTAINER = (By.ID, "shopping_cart_container")
    SHOPPING_CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    ONE_ITEM_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge' and text()='1']")
    TWO_ITEMS_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge' and text()='2']")
    THREE_ITEMS_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge' and text()='3']")
    FOUR_ITEMS_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge' and text()='4']")
    FIVE_ITEMS_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge' and text()='5']")
    SIX_ITEMS_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge' and text()='6']")

    # Filters:
    NAME_A_Z = (By.CSS_SELECTOR, 'option[value="az"]')
    NAME_Z_A = (By.CSS_SELECTOR, 'option[value="za"]')
    PRICE_LOW_TO_HIGH = (By.CSS_SELECTOR, 'option[value="lohi"]')
    PRICE_HIGH_TO_LOW = (By.CSS_SELECTOR, 'option[value="hilo"]')
    OPEN_FILTERS = (By.XPATH, "//select[@class='product_sort_container']")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    # Items:
    BACKPACK_NAME = (By.XPATH, "//*[text()='Sauce Labs Backpack']")
    BACKPACK_PRODUCT_DESCRIPTION = (By.XPATH, "//*[text()='carry.allTheThings() with the sleek, streamlined Sly Pack "
                                              "that melds uncompromising style with unequaled laptop and tablet "
                                              "protection.']")
    BACKPACK_IMG = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    BACKPACK_ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    BACKPACK_REMOVE_BTN = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']")
    BACKPACK_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[1]")


    BIKE_LIGHT_NAME = (By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    BIKE_LIGHT_PRODUCT_DESCRIPTION = (By.XPATH, "//*[contains(text(), 'A red light')]")
    BIKE_LIGHT_IMG = (By.XPATH, "//img[@alt='Sauce Labs Bike Light']")
    BIKE_LIGHT_ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
    BIKE_LIGHT_REMOVE_BTN = (By.XPATH, "//*[@id='remove-sauce-labs-bike-light']")
    BIKE_LIGHT_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[2]")

    T_SHIRT_BOLT_NAME = (By.XPATH, "//*[text()='Sauce Labs Bolt T-Shirt']")
    T_SHIRT_BOLT_PRODUCT_DESCRIPTION = (By.XPATH, '//*[text()="Get your testing superhero on with the Sauce Labs bolt '
                                                  'T-shirt. From American Apparel, 100% ringspun combed cotton, '
                                                  'heather gray with red bolt."]')
    T_SHIRT_BOLT_IMG = (By.XPATH, "//img[@alt='Sauce Labs Bolt T-Shirt']")
    T_SHIRT_BOLT_ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    T_SHIRT_BOLT_REMOVE_BTN = (By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']")
    T_SHIRT_BOLT_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[3]")

    FLEECE_JACKET_NAME = (By.XPATH, "//*[text()='Sauce Labs Fleece Jacket']")
    FLEECE_JACKET_PRODUCT_DESCRIPTION = (By.XPATH, "//*[contains(text(), 'fleece jacket capable of handling "
                                                   "everything')]")
    FLEECE_JACKET_IMG = (By.XPATH, "//img[@alt='Sauce Labs Fleece Jacket']")
    FLEECE_JACKET_ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
    FLEECE_JACKET_REMOVE_BTN = (By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']")
    FLEECE_JACKET_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[4]")

    ONESIE_NAME = (By.XPATH, "//*[text()='Sauce Labs Onesie']")
    ONESIE_PRODUCT_DESCRIPTION = (By.XPATH, "//*[contains(text(), 'Rib snap infant onesie for the junior automation "
                                            "engineer in development')]")
    ONESIE_NAME_IMG = (By.XPATH, "//img[@alt='Sauce Labs Onesie']")
    ONESIE_NAME_ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")
    ONESIE_NAME_REMOVE_BTN = (By.XPATH, "//*[@id='remove-sauce-labs-onesie']")
    ONESIE_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[5]")

    T_SHIRT_TEST_ALL_THE_THINGS_NAME = (By.XPATH, "//*[text()='Test.allTheThings() T-Shirt (Red)']")
    T_SHIRT_TEST_ALL_THE_THINGS_PRODUCT_DESCRIPTION = (By.XPATH, "//*[text()='This classic Sauce Labs t-shirt is "
                                                                 "perfect to wear when cozying up to your keyboard to "
                                                                 "automate a few tests. Super-soft and comfy ringspun "
                                                                 "combed cotton.']")
    T_SHIRT_TEST_ALL_THE_THINGS_IMG = (By.XPATH, "//img[@alt='Test.allTheThings() T-Shirt (Red)']")
    T_SHIRT_TEST_ALL_THE_THINGS_ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    T_SHIRT_TEST_ALL_THE_THINGS_REMOVE_BTN = (By.XPATH, "//*[@id='remove-test.allthethings()-t-shirt-(red)']")
    T_SHIRT_TEST_ALL_THE_THINGS_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[6]")

    # Footer:
    TWITTER_LINK = (By.XPATH, "//*[@href='https://twitter.com/saucelabs']")
    FACEBOOK_LINK = (By.XPATH, "//*[@href='https://www.facebook.com/saucelabs']")
    LINKEDIN_LINK = (By.XPATH, "//*[@href='https://www.linkedin.com/company/sauce-labs/']")
    ALL_RIGHTS_RESERVED = (By.XPATH, '//*[@class="footer_copy"]')


class ShoppingCart:

    YOUR_CART_TITLE = (By.XPATH, "//*[text()='Your Cart']")
    QTY_LABEL = (By.XPATH, "//*[@class='cart_quantity_label']")
    QTY_FIELD = (By.XPATH, "//div[@class='cart_quantity']")
    DESCRIPTION_LABEL = (By.XPATH, "//*[@class='cart_desc_label']")
    CONTINUE_SHOPPING_BTN = (By.XPATH, '//*[@name="continue-shopping"]')
    CHECKOUT_BTN = (By.XPATH, '//*[@name="checkout"]')
    SWAG_LABS_LOGO = (By.XPATH, "//*[@class= 'app_logo']")


class CheckOutPageStepOne:

    CHECKOUT_YOUR_INFO_TITLE = (By.XPATH, "//*[text()='Checkout: Your Information']")
    CANCEL_BTN = (By.XPATH, "//button[@id='cancel']")
    CONTINUE_BTN = (By.XPATH, "//*[@id='continue']")
    FIRST_NAME_INPUT_FIELD = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME_INPUT_FIELD = (By.XPATH, "//input[@id='last-name']")
    ZIP_INPUT_FIELD = (By.XPATH, "//input[@id='postal-code']")
    ERROR_MESSAGE = (By.XPATH, '//*[text()="Error: First Name is required"]')
    CLOSE_ERROR_MSG_BTN = (By.XPATH, "//*[@class='error-button']")
    FIRST_NAME = "Carl"
    LAST_NAME = "Cox"


class CheckOutPageStepTwo:

    CHECKOUT_OVERVIEW_TITLE = (By.XPATH, "//*[text()='Checkout: Overview']")
    PAYMENT_INFO_LABEL = (By.XPATH, "//*[text()='Payment Information']")
    PAYMENT_NUMBER = (By.XPATH, "//div[@class='summary_value_label'][1]")
    DELIVERY_COMPANY = (By.XPATH, "//*[text()='Free Pony Express Delivery!']")
    PRICE_TOTAL_LABEL = (By.XPATH, "//*[text()='Price Total']")
    ITEM_TOTAL_LABEL = (By.XPATH, "//*[text()='Item total: $']")
    TAX_LABEL = (By.XPATH, "//*[text()='Tax: $']")
    TOTAL_LABEL = (By.XPATH, "//*[text()='Total: $']")
    FINISH_BTN = (By.XPATH, "//*[@id='finish']")


class CheckOutCompletePage:

    CHECKOUT_COMPLETE_TITLE = (By.XPATH, "//*[text()='Checkout: Complete!']")
    CHECKMARK_SIGN = (By.XPATH, "//img[@alt='Pony Express']")
    THANK_YOU_FOR_YOUR_ORDER_TITLE = (By.XPATH, "//h2[text()='Thank you for your order!']")
    YOUR_ORDER_DISPATCHED_TITLE = (By.XPATH, "//*[text()='Your order has been dispatched, and will arrive just as "
                                             "fast as the pony can get there!']")
    BACK_HOME_BTN = (By.XPATH, "//*[@name='back-to-products']")
