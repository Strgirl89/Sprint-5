import pytest
from selenium import webdriver

def browser_settings():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--window-size=1920,1080')
    return driver_options

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=browser_settings())
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()