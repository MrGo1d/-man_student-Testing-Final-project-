from selenium.webdriver.common.by import By


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.ID, 'content_inner')
    EMPTY_BASKET = (By.CLASS_NAME, 'basket-items')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOG_IN_LINK = (By.NAME, 'login_submit')
    REGESTER_LINK = (By.NAME, 'registration_submit')
    REGESTER_LOGIN = (By.NAME, 'registration-email')
    REGESTER_PASSWORD = (By.NAME, 'registration-password1')
    REGESTER_PASSWORD_REPEAT = (By.NAME, 'registration-password2')


class ProductPageLocators():
    ADD_GOOD_TO_BASKET_BTN = (By.CSS_SELECTOR, '#add_to_basket_form .btn')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1') 
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color') 
    MESSAGE_BOOK_TITLE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong') 
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong') 
    BASKET_MINI_PRICE = (By.CLASS_NAME, 'basket-mini')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')

