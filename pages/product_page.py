from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket_button_click(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_GOOD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        # self.solve_quiz_and_get_code()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_GOOD_TO_BASKET_BTN), "Login form is not presented"

    def should_be_added_correct_mini_price(self):
        price_mini = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.BASKET_MINI_PRICE).text == price_mini, "The book price is not equal in basket mini price"

    def should_be_added_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text == price, "The book price is not equal in basket"

    def should_be_added_correct_title(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_TITLE).text == title, "The book title is not equal in basket"

    def should_be_basket_page(self):
        # self.should_be_login_url()
        self.should_be_add_to_basket_button()

    def should_be_login_url(self):
        assert "?promo=offer" in self.browser.current_url, "Login URL is not correct"

    def should_disappeare_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is appear, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
        


