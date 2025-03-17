import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CookieManager:
    def __init__(self, platform):
        self.platform = platform.lower()
        self.url = "https://www.instagram.com" if self.platform == "instagram" else "https://www.facebook.com"
        self.cookie_file = f"{self.platform}_cookies.pkl"
    
    def save_cookies(self, username, password):
        """ Extracts and saves session cookies for Instagram/Facebook """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in background
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(self.url)
        time.sleep(5)

        # Instagram login
        if self.platform == "instagram":
            driver.find_element("name", "username").send_keys(username)
            driver.find_element("name", "password").send_keys(password)
            driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]/button').click()

        # Facebook login
        elif self.platform == "facebook":
            driver.find_element("id", "email").send_keys(username)
            driver.find_element("id", "pass").send_keys(password)
            driver.find_element("name", "login").click()

        time.sleep(10)  # Wait for login

        # Save Cookies
        with open(self.cookie_file, "wb") as file:
            pickle.dump(driver.get_cookies(), file)

        print(f"✅ {self.platform.capitalize()} cookies saved!")
        driver.quit()

    def load_cookies(self):
        """ Loads session cookies for authentication """
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get(self.url)
        time.sleep(5)

        try:
            with open(self.cookie_file, "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    driver.add_cookie(cookie)

            driver.get(self.url)
            time.sleep(5)
            print(f"✅ Logged into {self.platform.capitalize()} using cookies!")

        except FileNotFoundError:
            print(f"❌ No saved cookies found for {self.platform.capitalize()}. Run save_cookies() first.")

        driver.quit()
