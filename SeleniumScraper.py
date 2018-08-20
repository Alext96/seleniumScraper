import random
import urllib.request
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

x = 2

#opens chrome
driver = webdriver.Chrome(r"C:\Users\Swagmaster\PycharmProjects\chromedriver_win32\chromedriver.exe")
driver.get("https://www.spreadshirt.com/quotes+gifts")

#first time requires exiting popus
driver.find_element_by_xpath("""//*[@id="sprd-main"]/div[7]/div[2]/div[2]/div[3]/div[1]/img""").click()
driver.find_element_by_xpath("""//*[@id="articleTileList"]/div[1]/div/a/img""").click()
sleep(3)
driver.find_element_by_xpath("""//*[@id="navigation"]/div[3]/div[2]/span""").click()
img = driver.find_element_by_xpath("""//*[@id="designDetailsPanel"]/div[1]/img""")
driver.back()

#loop for navigating the site
def navigate(x):
    while x < 55:
        x += 1
        #sleep(3)
        driver.find_element_by_xpath("""//*[@id="articleTileList"]/div[""" + str(x) + """]/div/a/img""").click()
        #sleep(3)
        downloadImage(x)
        #sleep(3)
    else:
        exit()

#downloading image, giving it random number
def downloadImage(x):
    img = driver.find_element_by_xpath("""//*[@id="designDetailsPanel"]/div[1]/img""")
    src = img.get_attribute('src')
    name = random.randrange(1, 100000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(src, full_name)
    driver.back()
    navigate(x)


navigate(x)