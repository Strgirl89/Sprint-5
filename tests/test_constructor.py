import sys
print(sys.path)
from conftest import driver
from selenium import webdriver
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import valid_user_data
from data import Link
class TestConstructor:
    def test_to_click_to_sauces_section(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES)
        )
        driver.find_element(*TestLocators.SAUCES).click()
        assert driver.find_element(*TestLocators.SAUCES2)
    def test_to_click_to_buns_section(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUNS)
        )
        driver.find_element(*TestLocators.SAUCES).click()
        driver.find_element(*TestLocators.BUNS).click()
        assert driver.find_element(*TestLocators.BUNS2)
    def test_to_click_to_fillings_section(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES)
        )
        driver.find_element(*TestLocators.FILLINGS).click()
        assert driver.find_element(*TestLocators.FILLINGS2)

