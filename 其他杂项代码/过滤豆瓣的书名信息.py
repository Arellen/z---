from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element(By.ID, "q")
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys("ipad")
button = browser.find_element(By.CLASS_NAME, "btn-search")
button.click()