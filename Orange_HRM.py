from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")