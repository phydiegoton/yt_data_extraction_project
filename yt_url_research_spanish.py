# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:03:52 2021

@author: Diego
"""

from selenium import webdriver
import time
#Variables necesarias

key_ytsearch= "migraña ejercicio"
song = key_ytsearch.replace(" ", "+")
base_url = "https://www.youtube.com" #La base de la página a scrapear
url = 'https://www.youtube.com/results?search_query=' + song
prefs={"profile.default_content_setting_values.notifications":2}
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs",prefs)
    #Inicialiamos el chromedriver
driver=webdriver.Chrome('C:\\Users\\Diego\\CACHARREANDOPY\\chromedriver.exe',chrome_options=chrome_options)
    #Obtenemos la url que queremos scrapear
    
driver.get(url)
    
height = driver.execute_script("return document.documentElement.scrollHeight")
previousHeight = -1

while previousHeight < height:
    previousHeight = height
    driver.execute_script(f'window.scrollTo(0,{height + 5000})')
    time.sleep(5)
    height = driver.execute_script("return document.documentElement.scrollHeight")
    
vidElements = driver.find_elements_by_id('thumbnail')
vid_urls_spanish = []
for v in vidElements:
    vid_urls_spanish.append(v.get_attribute('href'))