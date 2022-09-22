import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get("https://steamcommunity.com/search/users/#text=Nirator") 
#time.sleep(5)
h1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchPersonaInfo')))
#h1 = driver.find_element(By.CLASS_NAME, 'searchPersonaInfo')

htmlFirstProfile = h1.get_attribute('innerHTML').split('href="')[1].split('"')[0].replace("&nbsp", "")

print(htmlFirstProfile) 

driver.close()
options2 = Options()
options2.headless = False
driver2 = webdriver.Firefox(options=options2) 
driver2.get(htmlFirstProfile)  
#time.sleep(5)
#h2 = driver2.find_element(By.XPATH, '//div[@class="profile_header_actions"]')
h2 = WebDriverWait(driver2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'profile_header_actions')))

# h2 = driver.find_elements(By.XPATH, "//a[@class='btn_profile_action btn_medium']")
#h2 = WebDriverWait(driver2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_profile_action')))

print(h2.get_attribute('innerHTML'))

driver2.close()
