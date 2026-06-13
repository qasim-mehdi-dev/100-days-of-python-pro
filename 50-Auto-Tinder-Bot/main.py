from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/gDFOxXVe6knrWhwF0tUTsYOEfAtPV4et"
FACEBARK_EMAIL = "test@email.com"
FACEBARK_PASSWORD = "Password123"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)

sleep(2)
driver.find_element(By.XPATH, value='//*[text()="Log in"]').click()
sleep(1)
driver.find_element(By.CLASS_NAME, value='btn-facebark').click()

sleep(2)
base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)
print(f"Switched Window: {driver.title}")

email = driver.find_element(By.ID, value='email')
password = driver.find_element(By.ID, value='pass')
email.send_keys(FACEBARK_EMAIL)
password.send_keys(FACEBARK_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(f"Returned to Base Window: {driver.title}")

sleep(3)
driver.find_element(By.XPATH, value='//button[text()="Allow"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="Not interested"]').click()
sleep(1)
driver.find_element(By.XPATH, value='//button[text()="I Accept"]').click()

sleep(1)

for n in range(20):
    driver.execute_script("window.scrollBy(0, 1000);")
    sleep(0.5)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
        print(f"Successfully snapped down and liked dog #{n + 1} 🐶⚡")
    except ElementClickInterceptedException:
        print("Match popup overlay detected! Clearing...")
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
            sleep(0.5)
        except NoSuchElementException:
            pass
    except NoSuchElementException:
        print("Waiting for next dog frame to load into the DOM...")
        sleep(1)

driver.quit()