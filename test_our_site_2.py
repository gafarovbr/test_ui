from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



# 1. Зайти на главную страницу
# 2. Открыть страницу login
# 3. Заполнить поле email
# 4. Заполнить поле password
# 5. Нажать кнопку start

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def open_page(driver, url):
    driver.get(url)


def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

    


driver = get_driver()
open_page(driver, URL)
# login_page_button = driver.find_element(By.ID, 'user-name')
# login_page_button.click()

element_send_keys(driver, 'user-name',LOGIN)
element_send_keys(driver, 'password', PASSWORD)

element_click(driver, 'login-button')
pass