import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='')
driver.get('https://web.whatsapp.com')
driver.implicitly_wait(15)

def spammer(name,message,count):
    driver.find_element_by_css_selector("span[title='" + str(name) + "']").click()
    while count>0:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        time.sleep(1) # Time Delay for each Msg
        count -= 1

    print("Done!")

n = input("Contact Name: ") # name as per in the WhatsApp contact
m = input("Message: ") # message that you want to spam
i = int(input("How many Spam Text: ")) # count of spam message

spammer(n,m,i)