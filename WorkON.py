######### Importing libraries #########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
import csv
import time
import runpy
######### Getting emails #########
file = open('emails.txt', 'r')
reader = csv.reader(file)
emails = [row for row in reader]
######### Starting browser #########
options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
browser = webdriver.Chrome(options=options)
######### Going to Ebay SignIn page #########
browser.get(('https://signin.ebay.fr/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.fr%2F'))
time.sleep(10)
# Checking For reCaptcha and starting checking
count=0
captcha = browser.find_elements_by_link_text('ici')
if captcha:
    playsound('captcha.mp3')
    try:
        element = WebDriverWait(browser, 3600).until(
        EC.presence_of_element_located((By.ID, "userid"))
        )
    finally:     
        while len(emails) >= 1:
            if count % 200 == 0:
                print(count, "checked")
            count = count+1
            email = emails[0][0]
            del emails[0]
            time.sleep(1)
            username = browser.find_element_by_name('userid')
            username.clear()
            username.send_keys(email)
            nextButton = browser.find_element_by_id('signin-continue-btn')
            nextButton.click()
            time.sleep(1)
            test = browser.find_elements_by_link_text('Changer de compte')
            if test:
                playsound('detected.mp3')
                valid = open("valid.txt", "a")
                valid.write("\n")
                valid.write(email)
                valid.close()
                print(email)
                back = browser.find_elements_by_link_text('Changer de compte')
                back[0].click()
            error = browser.find_elements_by_id('s0-14-16-25-6-1-1-status')
            if error:
                save = open('emails.txt', 'w')
                for item in emails:
                    save.write(item[0])
                    save.write("\n")
                save.close()
                browser.quit()
                runpy.run_path('WorkON.py')
if not captcha:
    while len(emails)>=1:
        if count % 200 == 0:
            print(count, "checked")
        count = count+1
        email = emails[0][0]
        del emails[0]
        time.sleep(1)
        username = browser.find_element_by_name('userid')
        username.clear()
        username.send_keys(email)
        nextButton = browser.find_element_by_id('signin-continue-btn')
        nextButton.click()
        time.sleep(1)
        test = browser.find_elements_by_link_text('Changer de compte')
        if test:
            playsound('detected.mp3')
            valid = open("valid.txt", "a")
            valid.write("\n")
            valid.write(email)
            valid.close()
            print(email)
            back = browser.find_elements_by_link_text('Changer de compte')
            back[0].click()
        error = browser.find_elements_by_id('s0-14-16-25-6-1-1-status')
        if error:
            save = open('emails.txt', 'w')
            for item in emails:
                save.write(item[0])
                save.write("\n")
            save.close()
            browser.quit()
            runpy.run_path('WorkON.py')
        
