from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\sudeep\Selenium\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=options , service=serv_obj)
driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("admin123")
driver.find_element(By.NAME, "login").click()

# actual_key = driver.title
# expected_key = "OrangeHRM"
#
# if actual_key == expected_key:
#     print("Login test is passed")
#
# else:
#     print("Login test is failed")

