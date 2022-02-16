import selenium
from selenium import webdriver
download_google_driver = "https://chromedriver.chromium.org/downloads"
chrome_driver_path = "/Users/dushyant/Downloads/Driver/chromedriver"

# driver = webdriver.chooseAnyBrowser
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://pypi.org")
# driver.close()// close a tab
# driver.quit() // close whole window

# search_bar = driver.find_element_by_name("q")
# or
# search_bar = driver.find_element_by_id("search")
# or
# search_bar = driver.find_element_by_css_selector(".search-form input")
search_bar = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/form')

print(search_bar.get_attribute("placeholder"))

