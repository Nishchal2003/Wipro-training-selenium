import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_MultiSelectRadio:
        def test_multiradio(self):

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()

            driver.get("https://www.saucedemo.com/")
            name = driver.find_element(By.NAME,"user-name")
            name.send_keys("standard_user")

            password = driver.find_element(By.NAME,"password")
            password.send_keys("secret_sauce")

            login_button = driver.find_element(By.XPATH,"//input[@id='login-button']")
            login_button.click()
            time.sleep(3)