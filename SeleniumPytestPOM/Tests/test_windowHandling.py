import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Calender:

    def test_calender(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(4)
        driver.implicitly_wait(10)
        clickhere = driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']")
        clickhere.click()

        windows = driver.window_handles
        print(windows)

        driver.switch_to.window(windows[1])

        text = driver.find_element(By.XPATH,"//h3[contains(text(),'New Window')]")
        print(text.text)
        driver.close()

        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        driver.close()