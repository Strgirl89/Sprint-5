import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def browser_settings():
    options = Options()
    service = Service(executable_path='/Users/a69b/Sprint-5/sp/chromedriver-win64')
    options.add_argument('--window-size=1920,1080')
    return options, service

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()