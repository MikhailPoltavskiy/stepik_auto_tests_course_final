from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoAlertPresentException
import math

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path="C:/chromedriver/chromedriver.exe")
# service = Service()
browser = webdriver.Chrome(service=service, options=options)
browser.implicitly_wait(10)

# url = "http://selenium1py.pythonanywhere.com/"
# url_1 = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

browser.get(url)
# print(browser.current_url)
# browser.find_element(By.CSS_SELECTOR, "#login_link").click()
# print(browser.current_url)
# print(browser.find_element(By.CSS_SELECTOR,'p.price_color').text)
# print(browser.find_element(By.CSS_SELECTOR,'.basket-mini.pull-right.hidden-xs').text)
# print(browser.find_element(By.CSS_SELECTOR,'tr:nth-child(4)>td').text)
# print(browser.find_element(By.CSS_SELECTOR,'.col-sm-6.product_main>h1').text)
browser.find_element(By.CSS_SELECTOR, '.btn.btn-add-to-basket').click()


def solve_quiz_and_get_code():
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


solve_quiz_and_get_code()

input()
# time.sleep(3)
browser.quit()
