import pytest
from data import Credentials
from url import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructorLogo:
# Проверка перехода по клику из личного кабинета в «Конструктор»
    def test_click_constructor(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_account_button).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.constructor_button))
        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.collect_a_burger_header))
        assert driver.find_element(*Locators.collect_a_burger_header).is_displayed()

# Проверка перехода по клику из личного кабинета на логотип
    def test_click_logo(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_account_button).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.logo_button))
        driver.find_element(*Locators.logo_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.collect_a_burger_header))
        assert driver.find_element(*Locators.collect_a_burger_header).is_displayed()