from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'Basket is not empty'
