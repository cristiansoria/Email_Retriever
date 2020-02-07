from selenium import webdriver
import re
import time
import pandas as pd

browser = webdriver.Chrome("/PATH/chromedriver")
browser.get("https://csus.joinhandshake.com")
button = browser.find_element_by_class_name("sso-button")
button.click()
time.sleep(1)
email = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form/div[1]/div/input")
email.send_keys("$USER")
password = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form/div[2]/div/input")
password.send_keys("$PASSWORD")
login = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form/div[3]/div/button")
login.click()
browser.get("https://csus.joinhandshake.com/employers?ref=content-type-nav")
time.sleep(3)
int_soft = browser.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div/div/form/div/div[1]/div/div[2]/div[15]/div/div[2]/div/div[4]/label/input")
int_soft.click()
time.sleep(3)
ref = webdriver.Chrome("/PATH/chromedriver")
ref.get("https://csus.joinhandshake.com")
button = ref.find_element_by_class_name("sso-button")
button.click()
time.sleep(1)
email = ref.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form/div[1]/div/input")
email.send_keys("$USER")
password = ref.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form/div[2]/div/input")
password.send_keys("$PASSWORD")
login = ref.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form/div[3]/div/button")
login.click()

for c in range(966):
    time.sleep(5)
    print("Page: ", c)
    companies = browser.find_elements_by_class_name("style__heading___jtdKR")
    for i in range(len(companies)):
        text = companies[i].text
        place = 1
        try:
            text = text.strip('\n Follow')
            while (not text[place].isdigit()):
                place+=1
        except:
            pass

        text = text[:place]
        try:
            link = browser.find_element_by_link_text(text).get_attribute("href")
            ref.get(link)
            time.sleep(1)
            email = ref.find_elements_by_class_name("style__text___2ilXR")

            for x in range(len(email)):
                if email[x].text == "Email":
                    text = email[x+1].text
                    # print(text)
                    with open("emails.txt", "a") as FILE:
                        FILE.write(text + ", \n")

        except:
            pass
    try:
        next_page = browser.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div/div/form/div/div[2]/div[3]/div/button[2]")
        next_page.click()
    except:
        pass



