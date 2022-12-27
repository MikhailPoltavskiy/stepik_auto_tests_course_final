from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_present(self):
        self.should_be_btn_add_to_basket()
        self.should_be_name_product()
        self.should_be_price_product()

    def should_be_product_in_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        assert price_name in self.browser.find_element(
            *ProductPageLocators.MSG_PRODUCT_ADD).text, "Name in basket no correct"
        assert price_product in self.browser.find_element(
            *ProductPageLocators.BASKET_VALUE).text, "Price in basket no correct"

    def should_be_btn_add_to_basket(self):
        # Проверяем, что есть кнопка
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Btn basket is not present"

    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name product is not present"

    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price product is not present"
