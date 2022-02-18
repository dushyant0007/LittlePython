import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
download_google_driver = "https://chromedriver.chromium.org/downloads"
chrome_driver_path = "/Users/dushyant/Downloads/Driver/chromedriver"

# driver = webdriver.chooseAnyBrowser
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.instagram.com/ishangoyaltravel/")

followers = driver.find_element(By.CLASS_NAME,"-nal3 ")
followers.click()

type_username = driver.driver.find_element(By.NAME, "username")
type_username.send_keys("")

# type_password = driver.find_element_by_name("password")
# type_password.send_keys("")

# type_password = driver.find_element_by_class_name("qF0y9")
# type_password.click()


# search_btn = driver.find_elements_by_link_text("Follow")
#
# for every in search_btn:
#     every.click()



