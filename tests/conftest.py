import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

"""Fixture for running tests on Chrome Browser"""


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument("start-maximized")
    options.headless = False
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


"""Fixture for running tests on Safari Browser.
Don't forgot to go to the Develop menu, and turn on the Allow Remote Automation option on your Safari browser"""
# @pytest.fixture(scope='session')
# def driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.headless = False
#     driver = webdriver.Safari()
#     yield driver
#     driver.quit()

"""Fixture for running tests on Firefox Browser"""

# @pytest.fixture(scope='session')
# def driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.headless = False
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager).install())
#     yield driver
#     driver.quit()


"""Fixture for running tests on Edge Browser"""

# @pytest.fixture(scope='session')
# def driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.headless = False
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager).install())
#     yield driver
#     driver.quit()
