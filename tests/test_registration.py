import pytest
from faker import Faker
from selenium import webdriver
from conftest import driver
from locators import TestLocators
from data import get_sign_up_name_data
from data import get_sign_up_data
from data import Link
class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(f"{Link.BASE_URL}")
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        name_data = get_sign_up_name_data()
        driver.find_element(*TestLocators.NAME).send_keys(name_data())

        email_data, password_data = get_sign_up_data()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email_data)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password_data)
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == f"{Link.BASE_URL}register"

    def test_invalid_password_registration(self, driver):
        driver.get(f"{Link.BASE_URL}")
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        name_data = get_sign_up_name_data()
        driver.find_element(*TestLocators.NAME).send_keys(name_data())

        email_data, password_data = get_sign_up_data()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email_data)

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.find_element(*TestLocators.ERROR).text == "Некорректный пароль"
