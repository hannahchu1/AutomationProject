import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

executable_path = "/Users/hannah/Desktop/HannahC_Final_Automation_Project/chromedriver"

chrome_options = Options()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
wait = WebDriverWait(driver, 10)

# visiting site
driver.get("https://www.chipotle.com/")
time.sleep(1)

# to get to the menu
driver.find_element_by_xpath('//*[@id="cmg-app-content"]/div[1]/div/div[1]/div/div/div/div/div[2]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="menu"]/div/div[3]/div/div[2]/div[1]').click()
time.sleep(7)

# enter location
driver.find_element_by_xpath('/html/body/div[1]/span[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[2]').click()
search = driver.find_element_by_xpath('/html/body/div[1]/span[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[2]/input')
search.send_keys('80 Sutter St, SF, CA')
driver.find_element_by_xpath('/html/body/div[1]/span[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/img').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/span[4]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div[2]/div/div').click()
time.sleep(3)

# enter personal info
name = driver.find_element_by_xpath('/html/body/div[1]/span[8]/div[2]/div/div/div[2]/div[2]/div[5]/div/div[2]/input')
name.send_keys('Potato Chip')
number = driver.find_element_by_xpath('/html/body/div[1]/span[8]/div[2]/div/div/div[2]/div[2]/div[6]/div/div[2]/input')
number.send_keys('4151234567')
driver.find_element_by_xpath('/html/body/div[1]/span[8]/div[2]/div/div/div[2]/div[2]/div[11]/div/div/div').click()
time.sleep(10)

# to order
driver.find_element_by_xpath('//*[@id="cmg-app-content"]/div[1]/div/div/div[2]/div[2]/div[5]/div[3]/div[4]').click()
time.sleep(2)

# meal name
mealName = driver.find_element_by_xpath('/html/body/div[1]/div[5]/span/div[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[2]/input')
mealName.send_keys('Potato')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[5]/span/div[2]/div/div/div/div[3]/div[3]/div/div[3]/div[2]').click()
time.sleep(3)

# checkout
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div[2]/div[3]/div/div').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="guest-info-email"]/div/div[2]/input').send_keys('potatochip.qa21@mail.com')
time.sleep(7)

driver.quit()

# cc info
# card = driver.find_element_by_xpath('//*[@id="cmg-app-content"]/div[1]/div/div/div[2]/div[2]/div/div[6]/div/div[2]/div/form/div[1]/div[1]')
# card.send_keys('4400224400240420')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="cvv"]').send_keys('120')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="exp"]').send_keys('1222')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="postalCode"]').send_keys('94015')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="name"]').send_keys('Potato Chip')