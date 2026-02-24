import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://trytestingthis.netlify.app/")
time.sleep(4)

title = driver.title
print(title)

url = driver.current_url
print(url)

driver.forward()
time.sleep(2)

driver.refresh()
driver.close()