# WebDriver waits until the load event fire is returned.

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# # options.add_experimental_option("detach" , True)
# options.page_load_strategy = 'normal'
# driver = webdriver.Chrome(options=options)
# driver.get("http://www.google.com")

# ------------------------------------------------------------------

# WebDriver waits until DOMContentLoaded event fire is returned.

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.page_load_strategy = 'eager'
# driver = webdriver.Chrome(options=options)
# driver.get("http://www.google.com")
# driver.quit()

# WebDriver only waits until the initial page is downloaded.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()



