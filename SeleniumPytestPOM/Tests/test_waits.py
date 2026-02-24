import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

class Test_Waits:

    def test_waits(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://www.selenium.dev/documentation/webdriver/waits/")
        driver.maximize_window()
        driver.implicitly_wait(2)

        # explicit wait
        radio_btn = driver.find_element(By.XPATH,"(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())

        # Custom wait or Fluent Wait
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, poll_frequency=2, ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)
