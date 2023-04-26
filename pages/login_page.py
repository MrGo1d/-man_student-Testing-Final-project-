from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REGESTER_LOGIN)
        user_password = self.browser.find_element(*LoginPageLocators.REGESTER_PASSWORD)
        user_password_repeat = self.browser.find_element(*LoginPageLocators.REGESTER_PASSWORD_REPEAT)

        login.send_keys(email)
        user_password.send_keys(password)
        user_password_repeat.send_keys(password)
        
        self.browser.find_element(*LoginPageLocators.REGESTER_LINK).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_LINK), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login URL is not correct"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGESTER_LINK), "Registration form is not presented"
