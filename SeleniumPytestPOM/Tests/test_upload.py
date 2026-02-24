import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Upload:

    def test_upload(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(4)

        browse = driver.find_element(By.XPATH,"//input[@id='file-upload']")
        browse.send_keys(r"C:\Users\Nikhil\Downloads\upload.txt")
        time.sleep(3)
        upload = driver.find_element(By.XPATH,"//input[@id='file-submit']")

        upload.click()
        time.sleep(2)
        fileupload = driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.close()