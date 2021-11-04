from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

code = '366-144-697'
group_url='https://wiseoldman.net/groups/2059'
new_service = Service(r'C:\chrome_driver\chromedriver.exe')
driver = webdriver.Chrome(service=new_service)
driver.get(group_url)

# Click Update All Button
time.sleep(2)
update_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/button")
update_btn.click()

# Types the authentication code into the box
time.sleep(2)
verification_code_box = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[4]/div/input')
verification_code_box.send_keys(code)

# Clicks a different Update All Button
time.sleep(2)
confirm_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div/button[2]')
confirm_btn.click()

time.sleep(2)
driver.quit()
