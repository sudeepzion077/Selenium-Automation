from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("http://dev.financebox.in/auth/login")
driver.find_element(By.NAME, "email").send_keys("Test@gmail.com")
driver.find_element(By.NAME, "password").send_keys("3VE%5b9R9Y")
driver.find_element(By.NAME, "Submit").click()

# actual_key = driver.title
# expected_key = "OrangeHRM"
#
# if actual_key == expected_key:
#     print("Login test is passed")
#
# else:
#     print("Login test is failed")
