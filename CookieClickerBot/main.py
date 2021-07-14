from selenium import webdriver
import time

from selenium.common.exceptions import StaleElementReferenceException

# Tracking last purchase time.
last_purchase_time = time.time()

# Setting up chrome driver.
chrome_driver_path = "path"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Obtaining references to cookie-related web elements.
cookie_element = driver.find_element_by_id("cookie")
cookie_balance_element = driver.find_element_by_id("money")

# Obtaining references to purchasing-related web elements.
buy_elements = driver.find_elements_by_css_selector("#store div")
buy_elements.reverse()
buy_ids = [element.get_attribute("id") for element in buy_elements]

# Obtaining references to cost-related web elements.
cost_elements = driver.find_elements_by_css_selector("#store b")
cost_elements.reverse()

# Running clicks and purchases indefinitely.
while True:
    cookie_element.click()

    # Only make a purchase every 5 seconds. Running checks on each iteration is computationally expensive and inefficient.
    if time.time() - last_purchase_time > 5.0:
        try:
            balance = int(cookie_balance_element.text.replace(",", ""))
            cost_elements = driver.find_elements_by_css_selector("#store b")
            cost_elements.reverse()

            # Checking balance against item prices from best item to worst item.
            for index in range(1, len(cost_elements)):
                if int(cost_elements[index].text.split("-")[1].strip().replace(",", "")) < balance:
                    driver.find_element_by_id(buy_ids[index]).click()
                    print("clicked")
                    last_purchase_time = time.time()
                    break
        
        except StaleElementReferenceException:
            pass
