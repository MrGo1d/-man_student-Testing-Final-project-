from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time
import pytest


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    LINK = 'http://selenium1py.pythonanywhere.com'
    PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/pl/catalogue/the-shellcoders-handbook_209/'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link=LINK):
        page = LoginPage(browser, link)
        email = str(time.time()) + "@testmail.com"
        password = '1qaz@WSX3edc'
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()      

    def test_user_cant_see_success_message(self, browser, link=PRODUCT_LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, link=PRODUCT_LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_page()
        page.add_to_basket_button_click()
        page.should_be_added_correct_title()
        page.should_be_added_correct_price()


@pytest.mark.add_to_basket_and_get_promo
class TestGuestAddToBasketFromProductPagesAndGetPromo:
    LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), # mark a test that is obviously not working
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

    @pytest.mark.parametrize('link', LINKS)
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_page()
        page.should_be_login_url()
        page.add_to_basket_button_click()
        page.solve_quiz_and_get_code()
        page.should_be_added_correct_title()
        page.should_be_added_correct_price()


@pytest.mark.cant_see_messages
class TestGuestMessagesAddingProductToBasket:
    LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_button_click()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail 
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_button_click()
        page.should_disappeare_success_message()


@pytest.mark.interaction_login_and_basket
class TestGuestInteractionLoginAndBasket:
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    def test_guest_should_see_login_link_on_product_page(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link=LINK):
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.basket_should_be_empty()
        page.empty_basket_should_contain_text()
