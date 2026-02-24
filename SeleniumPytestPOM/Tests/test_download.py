import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Upload:

    def test_upload(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(4)

        alert = driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpg']")
        alert.click()
        time.sleep(2)

        DOWNLOAD_DIR = r"C:\Users\Nikhil\Downloads"
        file_path = os.path.join(DOWNLOAD_DIR,"alert.jpg")
        assert os.path.exists(file_path)

        time.sleep(2)
        driver.close()