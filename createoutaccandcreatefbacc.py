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

client = MongoClient(host="mongodb+srv://jatin:jatin123@cluster0.1zrdh.mongodb.net/outlookmail?retryWrites=true&w=majority",tlsCAFile=certifi.where(),connect=False)
collection = client.get_database("outlookmail").get_collection("newcreatedoutlookmail")
collection2 = client.get_database("outlookmail").get_collection('mailwithdata2')




# print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')



    # print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')

try:

    firstname = (names.get_first_name(gender='male')).lower()
    lastname = (names.get_last_name()).lower()
    email = firstname+'_'+lastname+str(random.randrange(7598,100000))+'@outlook.com'
    print(email)
    bot = uc.Chrome(options=options)

    bot.get('https://www.google.com/')
    time.sleep(1)
    # bot.get('https://www.shareasale.com/r.cfm?b=363443&u=3595261&m=38014')
    # time.sleep(5)
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

    time.sleep(4)

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
    
    except:
        pass
    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
    
    except:
        pass

    

    # bot.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    #OutlookDone? Then ->
    WebDriverWait(bot,3000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]'))).click()

    time.sleep(5)

    data = {'email': email}
    collection.insert_one(data)
    print('Added To DB!!!!!!!!!!!')

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
    
    except:
        pass

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Continue')]"))).click()
    
    except:
        pass

    
    time.sleep(10)

    bot.get('https://outlook.live.com/mail/0/')

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Meet Now')]")))
        print('3')
    except:
        bot.get('https://outlook.live.com/mail/0/')
        time.sleep(10)
        pass
    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Meet Now')]")))
        print('33')
    except:
        # data = {'email': email}
        # collection.insert_one(data)
        bot.save_screenshot('777.png')
        # sys.exit('Outlook Not Opened')
        time.sleep(2)
        bot.quit()

    bot.execute_script("window.open('');")

    time.sleep(2)

    bot.switch_to.window(bot.window_handles[1])

    

    bot.get('https://en-gb.facebook.com/')

    time.sleep(5)

    bot.save_screenshot('8.png')


    try:


        bot.find_element(By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy').click()

        bot.save_screenshot('9.png')
    except:
        pass
    # WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy'))).click()


    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy'))).click()

    bot.save_screenshot('10.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_email__"]'))).send_keys(email)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_email_confirmation__"]'))).send_keys(email)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="firstname"]'))).send_keys(firstname)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="lastname"]'))).send_keys(lastname)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="reg_passwd__"]'))).send_keys('Jatin@123')


    randdate = random.randint(3,20)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="day"]/option[{randdate}]'))).click()


    randmonth = random.randint(2,9)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="month"]/option[{randmonth}]'))).click()

    randyear = random.randint(28, 34)

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="year"]/option[{randyear}]'))).click()

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[value="2"]'))).click()

    bot.save_screenshot('11.png')

    print('4')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="websubmit"]'))).click()

    
    print('5')


    time.sleep(20)
    bot.save_screenshot('12.png')
    isexit = 0

    
    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Complete these steps in the next 180 days to make sure that you can use this account.')]")))

        print('6')

        print('180 days Text Came. Account not created')

        data = {'email': email, 'fb': 'No', 'firstname': firstname, 'lastname': lastname}

        collection2.insert_one(data)

        # time.sleep(10)

        bot.save_screenshot('13.png')

        # bot.quit()
        
        isexit = 1

        # sys.exit('180 days Text Came. Account not created')
        print('666')
        # sys.exit("Account Not Created 180 days Text Came")

        


        #if 180 days wala msg came then stop here
    # except SystemExit:
    #     sys.exit(1)
    #     print("sys.exit() worked as expected")
    except:
        pass

    if(isexit == 1):
        sys.exit('180 days Text Came. Account not created')

    isotpcame = 0

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Enter the code from your email')]")))

        print('Fb otp page came')

        isotpcame = 1


    except:
        pass

    if(isotpcame == 0):
        data = {'email': email}
        collection.insert_one(data)
        sys.exit('Fb Otp Page Not came. Exiting Code')



    #Going Outlook For OTP Code
    bot.switch_to.window(bot.window_handles[0])

    time.sleep(2)

    bot.get('https://outlook.live.com/mail/0/')

    time.sleep(2)

    
    bot.save_screenshot('133.png')

    print('7')


    elee = WebDriverWait(bot,100).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'is your Facebook confirmation code')]")))

    print('8')

    bot.save_screenshot('14.png')

    ttext = elee.text

    facebookcode = ttext.replace('FB-',"").replace(" is your Facebook confirmation code","")
    
    print(facebookcode)

    time.sleep(1)

    bot.switch_to.window(bot.window_handles[1])

    time.sleep(2)

    ###############NOTEE##########
    #Put This code using send_keys

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="code_in_cliff"]'))).send_keys(facebookcode)

    print('9')

    bot.save_screenshot('15.png')

    WebDriverWait(bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="confirm"]'))).click()
            
    time.sleep(10)
    print('10')

    bot.save_screenshot('16.png')

    try:
        WebDriverWait(bot,10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Allow all cookies')]"))).click()
        print('11')

        bot.save_screenshot('17.png')
    except:
        pass
        
    # Then Click Next
    bot.get('https://www.facebook.com/')

    print("Done Facebook!!!!!!.... Account Created")

   

    data = {'email': email, 'fb': 'Yes', 'firstname': firstname, 'lastname': lastname}

    collection2.insert_one(data)



    bot.quit() 
except Exception as e:
    print(e)
    time.sleep(10000)

bot.quit()
print("Program Ended")

