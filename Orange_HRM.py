from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriveManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(40)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element("username").send_keys("Admin")
# driver.find_element("password").send_keys("admin123")
# driver.find_element("submit").click()
#
# actual_key = driver.title
# expected_key = "OrangeHRM"
#
# if actual_key == expected_key:
#     print("Login test is passed")
#
# else:
#     print("Login test is failed")
