from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

class InstaFollower:
    
    # Defining constants and starting webpage.
    def __init__(self):
        self.instagram_username = "my_username"
        self.instagram_password = "my_password"
        self.similar_account = "account_to_follow"
        self.chrome_driver_path = "C:\\Users\\falco\\OneDrive\\Desktop\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.driver.get("https://www.instagram.com")
    
    # Logging into Instagram.
    def login(self):
        time.sleep(3)
        username_field = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_field.send_keys(self.instagram_username)

        password_field = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_field.send_keys(self.instagram_password)

        login_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
        login_button.click()
    
    # Handling save login popup.
    def handle_save_login_popup(self):
        time.sleep(3)
        try:
            disable_save_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
            disable_save_button.click()
        except NoSuchElementException:
            pass
    
    # Handling notification popup.
    def handle_notification_popup(self):
        time.sleep(8)
        try:
            disable_notifications_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            disable_notifications_button.click()
        except NoSuchElementException:
            pass
    
    # Searching account to find followers.
    def search_account(self):
        time.sleep(3)
        search_bar = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_bar.send_keys(self.similar_account)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
    
    # Opening table of followers.
    def open_followers_table(self):
        time.sleep(3)
        followers_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers_button.click()
    
    # Scrolling down the table to load more users.
    def scroll(self):
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    
    # Following users.
    def follow(self):
        time.sleep(3)
        extracted_users = self.driver.find_elements_by_css_selector("ul div li div div button")
        for user in extracted_users:
            try:
                time.sleep(1)
                user.click()
            except ElementClickInterceptedException:
                time.sleep(1)
                cancel_button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
                cancel_button.click()

