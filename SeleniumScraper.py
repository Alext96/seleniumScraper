import os
import random
import urllib.request
from time import sleep
import cv2
import numpy as np
import wget
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

x = 1

# opens chrome
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.spreadshirt.com/shop/user/racoon/clothing/t-shirts/?sort=0")

# first time requires exiting popus
sleep(5)
#try:
    #driver.find_element_by_xpath("""//*[@id="sprd-main"]/div[4]/div[2]/div[1]""").click()
#except NoSuchElementException:
#    print("hittade inte 1")
sleep(3)
try:
    driver.find_element_by_xpath("""//*[@id="sprd-main"]/div[6]/div[2]/div/div[3]/div[1]/img""").click()
except NoSuchElementException:
    print("hittade inte usa")
sleep(3)
#try:
    #driver.find_element_by_xpath("""//*[@id="navigation"]/div[3]/div[2]/span""").click()
#except NoSuchElementException:
#    print("hittade inte 2")
#driver.find_element_by_xpath("""//*[@id="navigation"]/div[3]/div[2]/span""").click()
#sleep(3)
#driver.find_element_by_xpath("""//*[@id="navigation"]/div[3]/div[2]/span""").click()
# img = driver.find_element_by_xpath("""//*[@id="d-iO"]""")
#driver.back()
#driver.refresh()


# loop for navigating the site
def navigate(x):
    while x < 70:
        x += 1
        # sleep(3)
        sleep(3)
        try:
            driver.find_element_by_xpath(
                """//*[@id="articleTileList"]/div[""" + str(x) + """]/a/div[3]""").click()
        except NoSuchElementException:
            print("hittade inte 2")
        try:
            driver.find_element_by_xpath(
                """//*[@id="articleTileList"]/div[""" + str(x) + """]/a/div[2]/div[2]""").click()
        except NoSuchElementException:
            print("")

        #driver.find_element_by_xpath("""//*[@id="l-i""" + str(x) + """"]""").click()
        #//*[@id="l-i2"]
        #sleep(3)
        #driver.back()
       # sleep(3)
        #driver.find_element_by_xpath("""//*[@id="articleTileList"]/div[""" + str(x) + """]/a/div[2]/div[2]""").click()
        sleep(3)
        # sleep(2)
        downloadImage(x)
        # sleep(3)
    else:
        exit()


# downloading image, giving it random number
def downloadImage(x):
    #driver.refresh()
    #sleep(3)
    driver.execute_script("window.scrollBy(0, 2300);")
    sleep(4)
    try:
        driver.find_element_by_xpath("""//*[@id="navigation"]/div/div[2]/div[2]/div[1]""").click()
        print("hittade promo")
    except NoSuchElementException:
        print("hittade inte promo")
    except ElementNotInteractableException:
        print("hittade inte promo")
    except ElementClickInterceptedException:
        print("hittade inte promo")
    sleep(2)
    try:
        driver.find_element_by_xpath("""//*[@id="pdp-designer-accordion"]/button""").click()
        print("hittade +")
    except NoSuchElementException:
        print("hittade inte +")
    except ElementNotInteractableException:
        print("hittade inte +")
    except ElementClickInterceptedException:
        print("hittade inte +")
    sleep(2)
    img = driver.find_element_by_xpath("""//*[@id="pdp-designer-section"]/div/pdp-design-info/img""")
    #sleep(3)
    src = img.get_attribute('src')
    name = random.randrange(1, 100000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(src, full_name)
    print("Laddade ned bild " + str(x-1))
    #img = driver.find_element_by_xpath("""//*[@id="d-i14"]""")
    #sleep(3)
  #  src = img.get_attribute('src')
    #name = random.randrange(1, 100000)
   # full_name = str(name) + ".png"
    #wget.download(src, full_name)
    #urllib.request.urlretrieve(src, full_name)
    driver.back()
    navigate(x)

navigate(x)
