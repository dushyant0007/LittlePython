import selenium
from selenium import webdriver
download_google_driver = "https://chromedriver.chromium.org/downloads"
chrome_driver_path = "/Users/dushyant/Downloads/Driver/chromedriver"

# driver = webdriver.chooseAnyBrowser
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.flipkart.com/realme-buds-wireless-2-neo-type-c-fast-charge-bass-boost-bluetooth-headset/p/itm342ebcfc6e12b?pid=ACCG65YC8DTGDCNN&lid=LSTACCG65YC8DTGDCNNS3JUO8&marketplace=FLIPKART&q=realme+buds&store=0pm%2Ffcn&srno=s_1_5&otracker=AS_Query_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_2_na_na_na&fm=SEARCH&iid=dce1bf77-192d-4ae2-8ef9-7647d5b07011.ACCG65YC8DTGDCNN.SEARCH&ppt=sp&ppn=sp&ssid=miyagt2eao0000001642254324253&qH=de8dad61d35cd2f1")
# driver.close()// close a tab
# driver.quit() // close whole window

price = driver.find_element_by_class_name("_16Jk6d")


print(price.text)
print(price)
