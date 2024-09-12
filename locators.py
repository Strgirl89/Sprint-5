from selenium.webdriver.common.by import By

class TestLocators:
    LOGIN_LINK = (By.LINK_TEXT, "Личный Кабинет") #Кнопка для входа в личный кабинет
    REGISTER_BUTTON = (By. LINK_TEXT, "Зарегистрироваться") #Кнопка регистрации
    NAME = (By.NAME, "name") #Ввод логина в форме авторизации
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[class="text input__textfield text_type_main-default"]') #Ввод почты в форме авторизации
    PASSWORD_INPUT = (By.NAME, "Пароль") #Ввод пароля в форме авторизации
    LOG_BUTTON = (By.CLASS_NAME, "button_button__33qZ0") #Кнопка входа в "Личный кабинет"
    ERROR = (By.CLASS_NAME, "input__error") #Уведомление о неверном пароле
    ACCOUNT = (By.CLASS_NAME, "button_button_size_large__G21Vg") #Кнопка "Войти в аккаунт"
    CONSTRUCTOR = (By.LINK_TEXT, "Конструктор") #Кнопка "Конструктор"
    HEAD_LOGO = (By.XPATH,'//div/a[@href= "/"]') #Кнопка логотипа "Stellar Burgers"
    EXIT = (By.XPATH, '//button[text()="Выход"]') #Кнопка "Выход"
    BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']") #Кнопка "Булки" на главной
    BUNS2 = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')]//h2[text()='Булки']")
    #Активная секция "Булки"
    SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']") #Кнопка "Соусы" на главной
    SAUCES2 = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')]//h2[text()='Соусы']")
    # Активная секция "Соусы"
    FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']") #Кнопка "Начинки" на главной
    FILLINGS2 = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')]//h2[text()='Начинки']")
    # Активная секция "Начинки"

