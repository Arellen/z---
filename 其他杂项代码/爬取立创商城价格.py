from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://so.szlcsc.com/global.html?k=STM32G070CBT&hot-key=STM32G070CBT')
input = browser.find_element(By.CLASS_NAME, "sch-bd02")
print(input)
input.clear()
input.send_keys("123")
input.send_keys(Keys.RETURN)
print(input.text)
# print(browser.current_url)
# print(browser.get_cookies())
# print(browser.page_source)
