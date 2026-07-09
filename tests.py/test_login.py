import pytest
from data import Credentials
from url import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
# Проверка входа по кнопке «Войти в аккаунт» на главной странице
    def test_login_from_main_page(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_account_button).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.visibility_of_element_located(Locators.order_button))

# Проверка входа через кнопку «Личный кабинет»
    def test_login_with_account_button(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.visibility_of_element_located(Locators.order_button))

# Проверка входа через кнопку в форме регистрации
    def test_login_from_registration_page(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.login_button_register).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.visibility_of_element_located(Locators.order_button))

# Проверка входа через кнопку восстановления пароля
    def test_login_with_forgot_password(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_account_button).click()
        driver.find_element(*Locators.forgot_password_button).click()
        driver.find_element(*Locators.login_button_forgot_password).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.visibility_of_element_located(Locators.order_button))