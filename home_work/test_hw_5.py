from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


# поиск элемента
username = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')
button = driver.find_element(By.CSS_SELECTOR, '#login-button')

if username is None and password is None and button is None:
    print('Элемент не найден')
else:
    print('Элемент найден')