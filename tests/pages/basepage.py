from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.saucedemo.com/'

class BasePage:

    def __init__(self, driver, URL):
        self.driver = driver
        self.url = URL

    def open_page(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))