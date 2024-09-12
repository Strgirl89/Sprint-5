import pytest
from selenium import webdriver
from conftest import driver
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import valid_user_data
from data import Link
class TestAccount:
    def test_enter_into_account(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == f"{Link.BASE_URL}login"

    def test_enter_into_account2(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == f"{Link.BASE_URL}login"

    def test_from_personal_account_to_constructor(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        assert driver.current_url == f"{Link.BASE_URL}"

    def test_from_personal_account_to_logo(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.HEAD_LOGO).click()
        assert driver.current_url == f"{Link.BASE_URL}"

    def test_from_personal_account_to_exit(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(valid_user_data["email"])

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(valid_user_data["password"])
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == f"{Link.BASE_URL}login"
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == f"{Link.BASE_URL}account"
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(TestLocators.EXIT)
        )
        driver.find_element(*TestLocators.EXIT).click()
        assert driver.current_url == f"{Link.BASE_URL}account/profile"
















