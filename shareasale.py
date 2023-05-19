import time, os
import random
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import sys
from pymongo import MongoClient
import certifi

options = webdriver.ChromeOptions() 
# options.headless = True
options.add_argument('--disable-popup-blocking')
# bot = uc.Chrome(options=options)
# bot.get('https://login.live.com/login.srf')







# print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')



    # print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')

try:


    bot = uc.Chrome(options=options)

    bot.get('https://www.shareasale.com/info/affiliate-login/')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys('GoangTerry')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('dharmikJatin@177')

    time.sleep(5)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div[2]/div/form/div[2]/a'))).click()

    time.sleep(4)

    count = 1

    while count <= 951:

        print(count)


        bot.get(f'https://account.shareasale.com/a-programs.cfm#searchType=basicKeyword&start={count}&order=&resultFilter=&catalog=0&temp=1684234817789')

        time.sleep(10)

        alldata = bot.find_elements(By.CSS_SELECTOR, "div.merId > span")
        # text = alldata.get_attribute('innerText')
        f = open('merchantid.txt','a')

        for i in alldata:
            text = i.get_attribute('innerText')
            data = text + '\n'
            f.write(data)
        

            # print(text)
        f.close()
        count = count + 50

    # '#fullResult1124030 > div > div > div.mGeneral > div.merId > span'

    time.sleep(20000)

    # 'https://account.shareasale.com/a-joinprogram.cfm?merchantID=76815&storeId=0'

    

    

    

    
    



    bot.quit() 
except Exception as e:
    print(e)
    time.sleep(10000)

bot.quit()
print("Program Ended")

