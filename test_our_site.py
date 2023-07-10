from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# 1. Зайти на главную страницу
# 2. Открыть страницу login
# 3. Заполнить поле email
# 4. Заполнить поле password
# 5. Нажать кнопку start

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'



# 1.
driver.get(URL)

# login_page_button = driver.find_element(By.ID, 'user-name')
# login_page_button.click()

input_login = driver.find_element(By.ID, 'user-name')
input_password = driver.find_element(By.ID, 'password')
input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)

register_button = driver.find_element(By.ID, 'login-button')
register_button.click()
pass