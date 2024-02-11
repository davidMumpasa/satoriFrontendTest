from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

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

        # Find the sign-up button and click it
        loginBtn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-5.m-4 > div > div.text-center.pt-1.mb-5.pb-1.row > button")
        loginBtn.click()
        time.sleep(5)

        popUpOkBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        popUpOkBtn.click()
        time.sleep(2)

        # correct login 

        emailInput = driver.find_element(By.CSS_SELECTOR, "#form1")
        emailInput.clear()
        emailInput.send_keys("david@fluidintellect.com")
        time.sleep(2)  # Adjust sleep time if needed

        passwordInput = driver.find_element(By.CSS_SELECTOR, "#form2")
        passwordInput.clear()
        passwordInput.send_keys("DavidEbula$16")
        time.sleep(2)  # Adjust sleep time if needed
        
        loginBtn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-5.m-4 > div > div.text-center.pt-1.mb-5.pb-1.row > button")
        loginBtn.click()
        time.sleep(5)

    finally:
        # Close the browser
        driver.quit()

try:

    # Navigate to the URL
    driver.get("http://localhost:3000")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root")))

    # Find the register button and click it
    registerBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div > div > div.col-lg-6.align-self-center > div > a.btn.btn-border-base.ml-4.aos-init.aos-animate"))
    )
    registerBtn.click()

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

    # Wait for a moment
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form3"]')))

    # Find the confirm password input field using XPath and enter the same password
    confirmPasswordInput = driver.find_element(By.XPATH, '//*[@id="form3"]')
    confirmPasswordInput.send_keys("your_password")
    time.sleep(2)

    # Wait for a moment
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#flexCheckDefault")))

    # Find the terms and conditions checkbox and click it
    termAndConCheckBox = driver.find_element(By.CSS_SELECTOR, "#flexCheckDefault")
    termAndConCheckBox.click()
    time.sleep(2)

    # Wait for a moment
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-3.m-4 > div > div.text-center.pt-1.mb-2.pb-1.row > button")))

    # Find the sign-up button and click it
    signUpBtn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-3.m-4 > div > div.text-center.pt-1.mb-2.pb-1.row > button")
    signUpBtn.click()
    time.sleep(5)

    # Wait for a few seconds to see the results
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-title"]')))

    # Check Alert
    popUp = driver.find_element(By.XPATH, '//*[@id="swal2-title"]')

    # test password Match
    popUpMessage = driver.find_element(By.XPATH, '//*[@id="swal2-html-container"]')
    # if popUpMessage.text == "You need to be registered to the Academy":

    popUpOkBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
    popUpOkBtn.click()
    time.sleep(2)

    emailInput.clear()
    emailInput.send_keys("chrisva@gmail.com")
    time.sleep(2)
  
    passwordInput.clear()
    passwordInput.send_keys("11111111")
    time.sleep(2)
 
    confirmPasswordInput.clear()
    confirmPasswordInput.send_keys("2222222")
    signUpBtn.click()
    time.sleep(5)
  
    popUpOkBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
    popUpOkBtn.click()

    # User Already Register Test

    emailInput.clear()
    emailInput.send_keys("john.doe@example.com")
    time.sleep(2)  # Adjust sleep time if needed

    passwordInput.clear()
    passwordInput.send_keys("11111111")
    time.sleep(2)  # Adjust sleep time if needed

    confirmPasswordInput.clear()
    confirmPasswordInput.send_keys("11111111")
    time.sleep(2)  # Adjust sleep time if needed

    
    signUpBtn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-3.m-4 > div > div.text-center.pt-1.mb-2.pb-1.row > button")
    signUpBtn.click()
    time.sleep(5)
    
    popUpOkBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
    popUpOkBtn.click()
    time.sleep(5) 


    # Test weak password
    
    emailInput.clear()
    emailInput.send_keys("david@fluidintellect.com")
    time.sleep(2)  # Adjust sleep time if needed

    passwordInput.clear()
    passwordInput.send_keys("11111111")
    time.sleep(2)  # Adjust sleep time if needed

    confirmPasswordInput.clear()
    confirmPasswordInput.send_keys("11111111")
    time.sleep(2)  # Adjust sleep time if needed

    
    signUpBtn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-3.m-4 > div > div.text-center.pt-1.mb-2.pb-1.row > button")
    signUpBtn.click()
    time.sleep(5) 
    
    popUpOkBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
    popUpOkBtn.click()
    time.sleep(2) 

    # test with correct information

    emailInput.clear()
    emailInput.send_keys("david@fluidintellect.com")
    time.sleep(2)  # Adjust sleep time if needed

    passwordInput.clear()
    passwordInput.send_keys("DavidEbula$16")
    time.sleep(2)  # Adjust sleep time if needed

    confirmPasswordInput.clear()
    confirmPasswordInput.send_keys("DavidEbula$16")
    time.sleep(2)  # Adjust sleep time if needed

    
    signUpBtn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.col.mb-5.mt-3.m-4 > div > div.text-center.pt-1.mb-2.pb-1.row > button")
    signUpBtn.click()
    time.sleep(5) 
    
    popUpOkBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
    popUpOkBtn.click()
    time.sleep(2) 

    testLogin()

except Exception as e:
    print(f"Error during the 'test Correct Informations': {e}")



finally:
    # Close the browser
    driver.quit()
