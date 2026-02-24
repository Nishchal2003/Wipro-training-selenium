import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        time.sleep(4)

        name = driver.find_element(By.NAME, "username")
        name.send_keys("Admin")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")
        time.sleep(4)

        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()

        time.sleep(4)
        checkbox_list = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//input[@type='checkbox']")
        count = len(checkbox_list)
        print(count)

        for checkbox in checkbox_list:
            time.sleep(1)
            checkbox.click()

        driver.quit()

