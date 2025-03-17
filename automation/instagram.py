from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        time.sleep(5)

        logging.info("Logged into Instagram")

    def start(self, actions):
        self.login("your_username", "your_password")

        if "like" in actions:
            self.auto_like()
        if "comment" in actions:
            self.auto_comment()
        if "follow" in actions:
            self.auto_follow()
        if "message" in actions:
            self.auto_send_messages()

    def auto_like(self):
        logging.info("Liking posts...")
        for _ in range(5):
            try:
                like_button = self.driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Like')]")
                like_button.click()
                time.sleep(2)
            except:
                logging.error("Error while liking post")

    def auto_comment(self):
        logging.info("Commenting on posts...")
        comments = ["Nice!", "Great post!", "Love this!"]
        for comment in comments:
            try:
                comment_box = self.driver.find_element(By.XPATH, "//*[@aria-label='Add a comment…']")
                comment_box.send_keys(comment)
                comment_box.submit()
                time.sleep(2)
            except:
                logging.error("Error while commenting")

    def auto_follow(self):
        logging.info("Following people...")
        # Implement follow logic here

    def auto_send_messages(self):
        logging.info("Sending messages...")
        # Implement message logic here

    def stop(self):
        self.driver.quit()
