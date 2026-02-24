import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Upload:

    def test_upload(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://jqueryui.com/datepicker/")
        time.sleep(4)

        driver.implicitly_wait(10)

        driver.switch_to.frame(0)

        datepicker = driver.find_element(By.XPATH,"//input[@id='datepicker']")
        datepicker.click()
        time.sleep(3)
        driver.close()