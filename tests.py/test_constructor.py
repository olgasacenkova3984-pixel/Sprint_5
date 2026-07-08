import pytest
from url import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:
# Проверка перехода из раздела "Булки" в раздел "Соусы" 
    def test_click_sause_section_constructor(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.sauces_section).click()
        assert driver.find_element(*Locators.selected_section).text == "Соусы"

# Проверка перехода из раздела "Булки" в раздел "Начинки" 
    def test_click_fil_section_constructor(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.fil_section).click()
        assert driver.find_element(*Locators.selected_section).text == "Начинки"

# Проверка перехода из раздела "Соусы" в раздел "Булки" 
    def test_click_buns_section_constructor(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.sauces_section).click()
        driver.find_element(*Locators.buns_section).click()
        assert driver.find_element(*Locators.selected_section).text == "Булки"