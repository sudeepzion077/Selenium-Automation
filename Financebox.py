from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\sudeep\Selenium\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=options , service=serv_obj)
driver.maximize_window()

driver.get("http://dev.financebox.in/auth/login")
driver.find_element(By.NAME, "email").send_keys("Test@gmail.com")
driver.find_element(By.NAME, "password").send_keys("3VE%5b9R9Y")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/button/span[1]").click()