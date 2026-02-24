import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Calender:

    def test_calender(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://rsuitejs.com/components/date-picker/")
        time.sleep(4)

        calender = driver.find_element(By.XPATH,"//input[@placeholder='Select Date']")
        calender.click()
        time.sleep(3)
        date = driver.find_element(By.XPATH, "//div[contains(@class,'rs-calendar-table-cell-is-today')]")
        date.click()
        time.sleep(3)

