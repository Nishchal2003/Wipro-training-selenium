import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_AlertHandling:
    def test_js_alerts(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)

        simplealt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
        simplealt.click()
        time.sleep(1)

        alt = driver.switch_to.alert
        alt.accept()

        confalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confalt.click()
        time.sleep(1)

        alt = driver.switch_to.alert
        alt.accept()
        prompalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        prompalt.click()
        time.sleep(1)

        alt = driver.switch_to.alert

        alerttext = alt.text
        print(f"The text on the prompt says: {alerttext}")

        alt.send_keys("test hello")
        time.sleep(1)
        alt.accept()

        time.sleep(2)
        driver.quit()