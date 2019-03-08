import random
import urllib.request
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

x = 1

#opens chrome
driver = webdriver.Chrome(r"Z:\Chromedriver\chromedriver.exe")
driver.get("https://www.spreadshirt.com/things+to+do+today")

#first time requires exiting popus

driver.find_element_by_xpath("""//*[@id="sprd-main"]/div[5]/div[2]/div[2]/div[3]/div[1]/img""").click()
sleep(3)
driver.find_element_by_xpath("""//*[@id="navigation"]/div[4]/div[2]/span""").click()
sleep(3)
driver.find_element_by_xpath("""//*[@id="l-i"]""").click()
sleep(3)
#driver.find_element_by_xpath("""//*[@id="navigation"]/div[3]/div[2]/span""").click()
#img = driver.find_element_by_xpath("""//*[@id="d-iO"]""")
driver.back()

#loop for navigating the site
def navigate(x):
    while x < 30:
        x += 1
        #sleep(3)
        driver.find_element_by_xpath("""//*[@id="articleTileList"]/div[""" + str(x) + """]/a/div[1]/div[1]/img""").click()
        #sleep(3)
        downloadImage(x)
        #sleep(3)
    else:
        exit()

#downloading image, giving it random number
def downloadImage(x):
    img = driver.find_element_by_xpath("""//*[@id="d-iZ"]""")
    src = img.get_attribute('src')
    name = random.randrange(1, 100000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(src, full_name)
    driver.back()
    navigate(x)


navigate(x)
