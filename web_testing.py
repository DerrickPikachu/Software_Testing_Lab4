from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.nycu.edu.tw/")
driver.maximize_window()

menu = driver.find_element(By.ID, "menu-1-9942884")
information_button = menu.find_element(By.LINK_TEXT, "消息")
information_button.click()

information_list = driver.find_element(By.ID, "-tab")
li_list = information_list.find_elements(By.TAG_NAME, 'li')
li_list[0].click()

content_div = driver.find_element(By.ID, "content")
title = content_div.find_element(By.TAG_NAME, "h1")
print(title.text)
content_ps = content_div.find_elements(By.TAG_NAME, "p")
for p in content_ps:
    print(p.text)

driver.switch_to.new_window('tab')
driver.get("https://google.com")
input_feild = driver.find_element(By.TAG_NAME, "input")
input_feild.send_keys("310553034" + Keys.ENTER)

search_results = driver.find_elements(By.CLASS_NAME, "jtfYYd")
search_link = search_results[1].find_element(By.TAG_NAME, "h3")
print(search_link.text)

# input()