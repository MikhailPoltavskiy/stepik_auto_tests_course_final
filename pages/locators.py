from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')


class LoginPageLocators:
    LOGIN_URL_SUB = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'tr:nth-child(4)>td')
    BASKET_VALUE = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs')
    MSG_PRODUCT_ADD = (By.CSS_SELECTOR, '.alertinner>strong')


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
