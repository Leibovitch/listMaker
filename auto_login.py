from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username_str = 'noylei31@gmail.com'
password_str = 'darNoy12'

browser = webdriver.Chrome()
browser.get('http://www.mysupermarket.co.il')
knisa = browser.find_element_by_id('SignIn')
knisa.click()
login = WebDriverWait(browser, 15).until(
    EC.presence_of_element_located((By.ID, "Email")))
login.send_keys(username_str)
print(login)
