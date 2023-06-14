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

# options = webdriver.ChromeOptions() 
# # options.headless = True
# options.add_argument('--disable-popup-blocking')
# bot = uc.Chrome(options=options)
# bot.get('https://login.live.com/login.srf')

client = MongoClient(host="mongodb+srv://jatin:jatin123@cluster0.1zrdh.mongodb.net/outlookmail?retryWrites=true&w=majority",tlsCAFile=certifi.where(),connect=False)
collection = client.get_database("outlookmail").get_collection("newmail2")


count = 1
# print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')



    # print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')

try:
    while count <= 3:
        options = webdriver.ChromeOptions() 
# options.headless = True
        options.add_argument('--disable-popup-blocking')
        firstname = (names.get_first_name(gender='male')).lower()
        lastname = (names.get_last_name()).lower()
        email = firstname+'_'+lastname+str(random.randrange(400,2000))+'@outlook.com'
        print(email)
        bot = uc.Chrome(options=options)

        bot.get('https://www.google.com/')
        time.sleep(3)
        bot.get('https://signup.live.com/signup')
        
        # time.sleep(4)

        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="MemberName"]'))).send_keys(email)

        # bot.find_element(By.XPATH, '//*[@id="MemberName"]').send_keys(email)


        # time.sleep(1)

        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()


        # time.sleep(5)
        
        #For Password Imput
        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PasswordInput"]'))).send_keys('Jatin@123')

        # bot.find_element(By.XPATH, '//*[@id="PasswordInput"]').send_keys('Jatin@123')

        

        # time.sleep(1)

        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

        

        # time.sleep(4)
        
        #For Name And Lastname
        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FirstName"]'))).send_keys(firstname)

        # bot.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys(firstname)


        # time.sleep(1)
        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="LastName"]'))).send_keys(lastname)


        # bot.find_element(By.XPATH, '//*[@id="LastName"]').send_keys(lastname)
        

        # time.sleep(1)
        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

        # time.sleep(4)
        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BirthMonth"]/option[6]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="BirthMonth"]/option[6]').click()
        # time.sleep(1)

        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BirthDay"]/option[10]'))).click()

        # bot.find_element(By.XPATH, '//*[@id="BirthDay"]/option[10]').click()
        # time.sleep(1)

        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BirthYear"]'))).send_keys('1993')

        # bot.find_element(By.XPATH, '//*[@id="BirthYear"]').send_keys('1993')
        # time.sleep(1)

        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iSignupAction"]'))).click()

        time.sleep(8)

        try:
            WebDriverWait(bot,7).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()

            data = {'email': email}
            collection.insert_one(data)
            print('Added To DB!!!!!!!!!!!')
            count = count + 1

            bot.quit()

            print("Outlook Done!!!!!!!!!!!!!")

            continue

        
        except:
            pass
        try:
            WebDriverWait(bot,7).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()

            data = {'email': email}
            collection.insert_one(data)
            print('Added To DB!!!!!!!!!!!')
            count = count + 1

            bot.quit()

            print("Outlook Done!!!!!!!!!!!!!")

            continue
        
        except:
            pass

        

        # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

        #OutlookDone? Then ->
        time.sleep(2)
        WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]'))).click()

        time.sleep(10)

        data = {'email': email}
        collection.insert_one(data)
        print('Added To DB!!!!!!!!!!!')
         

        bot.quit()

        print("Outlook Done!!!!!!!!!!!!!")

        continue



        try:
            WebDriverWait(bot,15).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
        
        except:
            pass

        try:
            WebDriverWait(bot,15).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
        
        except:
            pass

        
        time.sleep(10)

        bot.get('https://outlook.live.com/mail/0/')

        try:
            WebDriverWait(bot,15).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Meet Now')]")))
            print('3')
        except:
            bot.get('https://outlook.live.com/mail/0/')
            time.sleep(10)
            pass
        try:
            WebDriverWait(bot,15).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Meet Now')]")))
            print('33')
        except:
            # data = {'email': email}
            # collection.insert_one(data)
            bot.save_screenshot('777.png')
            # sys.exit('Outlook Not Opened')
            time.sleep(2)
            count = count + 1
            bot.quit()
            continue

        # data = {'email': email}
        # collection.insert_one(data)

        count = count + 1

        bot.quit()

        print("Outlook Done!!!!!!!!!!!!!")
except Exception as e:
    print(e)
    time.sleep(10000)

bot.quit()
print("Program Ended")

