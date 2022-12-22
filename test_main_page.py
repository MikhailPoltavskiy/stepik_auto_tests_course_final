from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()
