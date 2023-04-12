from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), 'Basket is not emty, but should be empty'


    def empty_basket_should_contain_text(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, 'Basket doesn\'t contain "Your basket is empty" text'
