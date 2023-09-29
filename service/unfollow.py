# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:23:27 2023

@author: Kakak
"""

import time
import re
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
options = webdriver.FirefoxOptions()
#options.headless = True
options.add_argument("--window-size=1920,1080")
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = webdriver.Firefox(options=options)
browser.get("https://www.instagram.com")

time.sleep(5)
#browser.refresh()
#browser.get_screenshot_as_file(f"screenshot.png")


username = browser.find_element(By.CSS_SELECTOR,"input[name='username']")
password = browser.find_element(By.CSS_SELECTOR,"input[name='password']")

username.clear()
password.clear()
username.send_keys("design.boi_")
password.send_keys("195@asem777")
login = browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

time.sleep(5)
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Profile')]"))).click()
#profile = browser.find_element(By.XPATH,"//span[contains(text(),'Profile')]").click()

time.sleep(5)
following = browser.find_element(By.XPATH,"//a[contains(text(),'following')]").click()

time.sleep(5)
button_unfoll = browser.find_elements(By.CSS_SELECTOR,"button[type='button']")

button_unfoll = browser.find_elements(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div")
i = 0
for click in button_unfoll:
    if i > 0:
        time.sleep(3)
        #button_unfolls = click.find_element(By.XPATH,"//button")
        #browser.execute_script("arguments[0].click();", button_unfolls)
        ActionChains(browser).move_to_element(click).click().perform()
        time.sleep(3)
        confirm = browser.find_element(By.XPATH,"//button[contains(text(),'Unfollow')]").click()
        print("test")
        #browser.get_screenshot_as_file(f"screenshot_" + str(i) +".png")
        time.sleep(3)
        print(str(i))
    i = i + 1
    if i == 4:
        click.send_keys(Keys.PAGE_DOWN).perform()
        button_unfoll = browser.find_elements(By.CSS_SELECTOR,"button[type='button']")
        i = 0
    
    
#wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//href[contains(text(),'following')]"))).click()
