import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
download_google_driver = "https://chromedriver.chromium.org/downloads"
chrome_driver_path = "/Users/dushyant/Downloads/Driver/chromedriver"

# driver = webdriver.chooseAnyBrowser
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://pypi.org")

# browse_project = driver.find_element_by_css_selector(".homepage-banner__browse a")
# or
# browse_project = driver.find_element_by_link_text("browse projects")
# browse_project.click()

search_project = driver.find_element_by_id("search")
search_project.send_keys("Python key")


search_btn = driver.find_element_by_class_name("search-form__button")

# search_btn.click()
# or
search_btn.send_keys(Keys.ENTER)



