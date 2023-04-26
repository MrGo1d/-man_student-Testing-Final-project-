from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    LANGUAGES = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

    def basket_should_be_empty(self):
        """method checks if the cart is empty"""
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), 'Basket is not emty, but should be empty'

    def empty_basket_should_contain_text(self):
        """method checks if the cart contains text"""
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        text = self.LANGUAGES.get(language)
        assert text in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, f'Basket doesn\'t contain "{text}" text'
