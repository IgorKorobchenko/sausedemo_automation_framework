This is an Automation Framework with Pytest using POM (Page Object Model) design pattern for www.saucedemo.com. 
SauceDemo is a website built by SauceLabs to practice automation testing.
The scope of this project is End-to-End testing  for the target website https://www.saucedemo.com/

Pytest INFO: https://docs.pytest.org/en/7.2.x/

pytest flags

-s - print desired output (pytest -s test_file_name)

-v - show test process' percentage (pytest -v test_file_name)

-m - allow to run tests with specific marks (pytest -m mark_title test_file_name)

How to save or set requirements:
1. To save project requirements run a command: pip freeze>requirements.txt
2. To set run a command: pip install>requirements.txt

ALLURE

Installation:
pip install allure-pytest

1. Create allure:
pytest --alluredir=allure_reports
2. Run tests: pytest 'test name' --alluredir=allure 
3. Generate a report and open it in a browser: allure serve allure_reports
4. Open allure report: allure open <directory>  
5. Clean allure report: allure report clean 
6. Change directory: allure generate old directory-o new directory

Useful links:
1. [About Selenium]:(https://selenium-python.readthedocs.io/)
2. About Pytest: https://pytest.org/en/7.4.x/contents.html
3. About Python: https://www.python.org/

[![GitHub Actions saucedemo](https://github.com/IgorKorobchenko/sausedemo_automation_framework/actions/workflows/actions.yml/badge.svg?branch=main)](https://github.com/IgorKorobchenko/sausedemo_automation_framework/actions/workflows/actions.yml)
