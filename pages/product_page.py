from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_button_click(self):
        """to add an item to the cart"""
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_GOOD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_add_to_basket_button(self):
        """is the add to cart button displayed"""
        assert self.is_element_present(*ProductPageLocators.ADD_GOOD_TO_BASKET_BTN), \
        "Basket button is not presented"

    def should_be_added_correct_mini_price(self):
        """checks if the price of the product matches the price indicated next to the cart icon"""
        price_mini = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.BASKET_MINI_PRICE).text == price_mini, \
        "The book price is not equal in basket mini price"

    def should_be_added_correct_price(self):
        """checks if the price of the product matches the price into the cart"""
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text == price, \
        "The book price is not equal in basket"

    def should_be_added_correct_title(self):
        """checks that a book with the required title has been added to the cart"""
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_TITLE).text == title, \
        "The book title is not equal in basket"

    def should_be_basket_page(self):
        """is the add to cart button displayed"""
        self.should_be_add_to_basket_button()

    def should_be_login_url(self):
        """checks if the url contains the required text"""
        assert "?promo=offer" in self.browser.current_url, "Login URL is not correct"

    def should_disappeare_success_message(self):
        """checks if the message disappears"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is appear, but should not be"

    def should_not_be_success_message(self):
        """checks if the message exists"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
       