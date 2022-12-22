from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()


def test_guest_can_go_to_login_page(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(1)
    go_to_login_page(browser)
