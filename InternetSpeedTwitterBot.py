from selenium import webdriver
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os



PROMISED_DOWN = 1500
PROMISED_UP = 90
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
SPEED_TEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.up = 0.0
        self.down = 0.0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        self.driver.maximize_window()
        start = self.driver.find_element(By.CSS_SELECTOR, value="a .start-text")
        start.click()
        print("Hold on! Just 1 min\nBot on duty..Fetching Results!!!")
        # 1min
        sleep(60)
        self.down = float(
            self.driver.find_element(
                By.XPATH,
                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                      '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        )
        self.up = float(
            self.driver.find_element(
                By.XPATH,
                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                      'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        )
        print("Successfully Fetched Internet Speed")

    def complain_via_twitter(self):
        sleep(5)
        self.driver.get("https://x.com/login")
        sleep(10)
        self.driver.maximize_window()
        email = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                  '/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        )
        sleep(5)
        email.click()
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        sleep(5)
        try:
            password = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                      '/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            )
            sleep(2)
            password.click()
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        except NoSuchElementException:
            # Here there can be a chance of verification
            username = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                      'div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
            )
            sleep(3)
            username.send_keys(TWITTER_USERNAME, Keys.ENTER)
            sleep(3)
            password = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div'
                      '/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            )
            sleep(2)
            password.click()
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        sleep(5)
        tweet = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div'
                  '/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div'
                  '/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        )
        sleep(2)
        message = (f"Hey Internet Provider, why is my internet speed {self.down}"
                   f"down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet.click()
        tweet.send_keys(message)
        post = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]'
                  '/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span'
        )
        sleep(1)
        post.click()
        sleep(2)
        self.driver.quit()
