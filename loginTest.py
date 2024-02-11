from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from app import driver

def testLogin():

    try:
        # Navigate to the URL
        driver.get("http://localhost:3000")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root")))

        # Find the register button and click it
        loginBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div > div > div.col-lg-6.align-self-center > div > a:nth-child(4)"))
        )
        loginBtn.click()

        # Wait for the registration form to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#form1")))


        # Find the email input field and enter an email address
        emailInput = driver.find_element(By.CSS_SELECTOR, "#form1")
        emailInput.send_keys("test@example.com")
        time.sleep(2)

        # Wait for a moment
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form2")))

        # Find the password input field and enter a password
        passwordInput = driver.find_element(By.CSS_SELECTOR, "#form2")
        passwordInput.send_keys("your_password")
        time.sleep(2)

    finally:
        # Close the browser
        driver.quit()