import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

"""pytest flags
-s - prints desired output (pytest -s test_file_name)

-v - shows test process' percentage (pytest -v test_file_name)

-m - allows to run tests with specific marks (pytest -m mark_title test_file_name)

for instance: pytest -s -v tests/test_login_page.py --browser chrome

"""

'''Fixture for all browsers'''


@pytest.fixture(params=['chrome'], scope="function", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    options = Options()
    options.add_argument("start-maximized")
    options.headless = False

    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'safari':
        driver = webdriver.Safari()
    elif browser == 'edge':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Browser is not supported: {browser}")

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="define browser: chrome, firefox, safari or edge")


"""Fixture for running tests on Chrome Browser"""

# @pytest.fixture(scope='session')
# def driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.headless = False
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()


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
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     yield driver
#     driver.quit()


"""Fixture for running tests on Edge Browser"""

# @pytest.fixture(scope='session')
# def driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.headless = False
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     yield driver
#     driver.quit()



