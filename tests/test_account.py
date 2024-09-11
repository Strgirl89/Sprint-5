import pytest

from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAccount:
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        driver.find_element(*TestLocators.NAME).send_keys("Theodore")
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("NISSAN1989")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

    def test_invalid_password_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        driver.find_element(*TestLocators.NAME).send_keys("Theodore")
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("short")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.find_element(*TestLocators.ERROR).text == "Некорректный пароль"

    def test_enter_into_account(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("NISSAN1989")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_enter_into_account2(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("NISSAN1989")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_from_personal_account_to_constructor(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("NISSAN1989")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_from_personal_account_to_logo(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("NISSAN1989")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.HEAD_LOGO).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_from_personal_account_to_exit(self, driver):
        driver.find_element(*TestLocators.ACCOUNT).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("adelbatalova@gmail.com")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("NISSAN1989")
        driver.find_element(*TestLocators.LOG_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.EXIT)
        )
        driver.find_element(*TestLocators.EXIT).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
















