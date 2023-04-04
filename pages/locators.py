from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOG_IN_LINK = (By.NAME, 'login_submit')
    REGESTER_LINK = (By.NAME, 'registration_submit')