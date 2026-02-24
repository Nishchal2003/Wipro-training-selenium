import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://testautomationpractice.blogspot.com/")

        time.sleep(2)

        checkbox_list = driver.find_elements(By.XPATH, "//div[@class='form-group']//input[@type='checkbox']")
        count = len(checkbox_list)
        print(count)

        for checkbox in checkbox_list:
            time.sleep(1)
            checkbox.click()

        driver.quit()