from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path="C:/chromedriver/chromedriver.exe")
# service = Service()
browser = webdriver.Chrome(service=service, options=options)
browser.implicitly_wait(10)

url = "http://selenium1py.pythonanywhere.com/"
# url_1 = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

browser.get(url)
print(browser.current_url)
browser.find_element(By.CSS_SELECTOR, "#login_link").click()
print(browser.current_url)
time.sleep(30)
browser.quit()
