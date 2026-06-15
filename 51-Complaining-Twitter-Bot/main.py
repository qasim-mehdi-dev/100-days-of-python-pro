from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = os.getenv('Y_EMAIL')
Y_PASSWORD = os.getenv('Y_PASSWORD')
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

class InternetSpeedYBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.geolocation": 2
        })
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        try:
            cookie_accept = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            self.driver.execute_script("arguments[0].click();", cookie_accept)
            time.sleep(2)
        except NoSuchElementException:
            pass

        test_started = False
        attempt = 0

        while not test_started and attempt < 3:
            try:
                attempt += 1
                start_btn = self.driver.find_element(By.CSS_SELECTOR, "a.chScb")
                self.driver.execute_script("arguments[0].click();", start_btn)
                test_started = True
            except NoSuchElementException:
                try:
                    start_btn_fallback = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
                    self.driver.execute_script("arguments[0].click();", start_btn_fallback)
                    test_started = True
                except NoSuchElementException:
                    time.sleep(2)

        for second in range(55, 0, -5):
            time.sleep(5)
            try:
                self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
                self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
            except NoSuchElementException:
                self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
                self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        wait = WebDriverWait(self.driver, 10)
        email_input = wait.until(ec.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys(Y_EMAIL)

        password_input = wait.until(ec.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(Y_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        tweet_compose = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Post text"]')))
        tweet = (f"Hey Internet Provider, why is my speed {self.up}up/{self.down}down? "
                 f"When i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_compose.send_keys(tweet)
        time.sleep(1)

        tweet_button = self.driver.find_element(By.ID, "post-btn")
        tweet_button.click()
        print("Clicked Post Button")
        time.sleep(5)
        time.sleep(3)
        self.driver.quit()

bot = InternetSpeedYBot()
bot.get_internet_speed()
bot.tweet_at_provider()