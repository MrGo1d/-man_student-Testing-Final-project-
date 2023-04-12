from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOG_IN_LINK = (By.NAME, 'login_submit')
    REGESTER_LINK = (By.NAME, 'registration_submit')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_GOOD_TO_BASKET_BTN = (By.CSS_SELECTOR, '#add_to_basket_form .btn')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1') 
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color') 
    MESSAGE_BOOK_TITLE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong') 
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong') 
    BASKET_MINI_PRICE = (By.CLASS_NAME, 'basket-mini')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner strong')

