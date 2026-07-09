from selenium.webdriver.common.by import By

class Locators:
    # Локаторы страницы регистрации
    name_input = (By.XPATH, './/label[text() = "Имя"]/following-sibling::input') # Поле ввода Имя
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    button_of_registration = (By.XPATH, './/button[text() = "Зарегистрироваться"]') # Кнопка "Зарегистрироваться"
    header_login = (By.XPATH, './/h2[text() = "Вход"]') # Заголовок "Вход"
    header_incorrect_password = (By.XPATH, './/p[text() = "Некорректный пароль"]') # Сообщение об ошибке "Некорректный пароль"
    
    # Локаторы для входа по кнопке "Войти в аккаунт" на главной странице
    name_input = (By.XPATH, './/label[text() = "Имя"]/following-sibling::input') # Поле ввода Имя
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    login_account_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной странице
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    order_button = (By.XPATH, './/button[text() = "Оформить заказ"]') # Кнопка "Оформить заказ"

    # Локаторы для входа через кнопку "Личный кабинет"
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    login_account_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной странице
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    order_button = (By.XPATH, './/button[text() = "Оформить заказ"]') # Кнопка "Оформить заказ"
    
    # Локаторы для входа через кнопку в форме регистрации
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    login_button_register = By.XPATH, './/a[text() = "Войти"]' #Кнопка "Войти" на странице регистрации
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    order_button = (By.XPATH, './/button[text() = "Оформить заказ"]') # Кнопка "Оформить заказ"

    # Локаторы для входа через кнопку в форме восстановления пароля
    login_account_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной странице
    forgot_password_button = (By.XPATH, './/a[text() = "Восстановить пароль"]') # Кнопка "Восстановить пароль"
    login_button_forgot_password = By.XPATH, './/a[text() = "Войти"]' # Кнопка "Войти" на странице восстановления пароля
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    order_button = (By.XPATH, './/button[text() = "Оформить заказ"]') # Кнопка "Оформить заказ"
    
    # Локаторы для выхода по кнопке "Выйти" в личном кабинете
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    login_account_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной странице 
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    account_button = (By.XPATH, './/p[text() = "Личный Кабинет"]') # Кнопка "Личный кабинет"
    logout_account_button = (By.XPATH, './/button[text() = "Выход"]') # Кнопка "Выход"
    header_login = (By.XPATH, './/h2[text() = "Вход"]') # Заголовок "Вход"

    # Локаторы для перехода по клику на "Личный кабинет"
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    login_account_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной странице 
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    account_button = (By.XPATH, './/p[text() = "Личный Кабинет"]') # Кнопка "Личный кабинет"
    header_profile = (By.XPATH, './/a[text() = "Профиль"]') # Заголовок "Профиль"

    # Локаторы для перехода по клику из "Личного кабинета" в "Конструктор"
    email_input = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # Поле ввода Email
    password_input = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # Поле ввода Пароль
    login_account_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной странице 
    login_button = (By.XPATH, './/button[text() = "Войти"]') # Кнопка "Войти" на странице входа
    account_button = (By.XPATH, './/p[text() = "Личный Кабинет"]') # Кнопка "Личный кабинет"
    constructor_button = By.XPATH, './/p[text() = "Конструктор"]' # Кнопка "Конструктор"
    logo_button = (By.XPATH, './/*[@href = "/"]') # Логотип Stellar Burgers
    collect_a_burger_header = (By.XPATH, './/h1[text() = "Соберите бургер"]') # Заголовок "Соберите бургер"
    
    # Локаторы для перехода между разделами "Конструктора"
    sauces_section = (By.XPATH, './/span[text() = "Соусы"]') # Раздел "Соусы"
    buns_section = (By.XPATH, './/span[text() = "Булки"]') # Раздел "Булки"
    fil_section = (By.XPATH, './/span[text() = "Начинки"]') # Раздел "Начинки"
    selected_section = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') # Активный раздел "Конструктора"