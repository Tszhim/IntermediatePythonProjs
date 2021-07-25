from selenium import webdriver
import time

twitter_username = "Tris25863926"
twitter_password = "seleniumbot9876545678987654567891351351364646"
down_bound = 150.0
up_bound = 10.0

chrome_driver_path = "C:\\Users\\falco\\OneDrive\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def obtain_results():
    try:
        curr_down = float(driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)
        curr_up = float(driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text)
    except ValueError:
        time.sleep(15)
        obtain_results()

    return curr_down, curr_up


driver.get("https://www.speedtest.net/")

time.sleep(1)
init_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
init_button.click()

time.sleep(45)
down, up = obtain_results()

if down < down_bound or up < up_bound:
    driver.get("https://www.twitter.com/")

    time.sleep(1)
    select_login = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div")
    select_login.click()

    time.sleep(1)
    username_field = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    username_field.send_keys(twitter_username)
    password_field = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
    password_field.send_keys(twitter_password)
    login_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
    login_button.click()

    time.sleep(1)
    tweet_field = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
    tweet_field.send_keys(f"Hey RCN, why is my download speed {down} mbps and my upload speed {up} mbps when I pay for {down_bound} mbps download and {up_bound} mbps upload?")
    tweet_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
    tweet_button.click()

    time.sleep(5)
    exit()

exit()
