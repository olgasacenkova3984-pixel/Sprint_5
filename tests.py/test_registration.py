import pytest
from data import RandomUser, InvalidRandomUser
from url import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    # Проверка успешной регистрации
    def test_registration_success(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.name_input).send_keys(RandomUser.name)
        driver.find_element(*Locators.email_input).send_keys(RandomUser.email)
        driver.find_element(*Locators.password_input).send_keys(RandomUser.password)
        driver.find_element(*Locators.button_of_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.header_login))
        assert driver.find_element(*Locators.header_login).text == 'Вход'

    # Проверка ошибки при регистрации с некорректным паролем (менее 6 символов)
    def test_registration_with_short_password(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.name_input).send_keys(InvalidRandomUser.name)
        driver.find_element(*Locators.email_input).send_keys(InvalidRandomUser.email)
        driver.find_element(*Locators.password_input).send_keys(InvalidRandomUser.invalid_password)
        driver.find_element(*Locators.button_of_registration).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.header_incorrect_password))
        assert driver.find_element(*Locators.header_incorrect_password).text == 'Некорректный пароль'