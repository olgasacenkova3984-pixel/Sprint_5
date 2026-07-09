import pytest
from data import Credentials
from url import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAccount:
# Проверка перехода по клику на «Личный кабинет»
    def test_click_to_personal_account(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_account_button).click()
        driver.find_element(*Locators.email_input).send_keys(Credentials.email)
        driver.find_element(*Locators.password_input).send_keys(Credentials.password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.account_button))
        driver.find_element(*Locators.account_button).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(expected_conditions.visibility_of_element_located(Locators.header_profile))