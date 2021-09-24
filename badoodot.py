from time import sleep
from selenium import webdriver
from logs import mail, password

path = 'your path to the local driver'
driver = webdriver.Chrome(path)
driver.get('https://badoo.com/signin/?f=top')
sleep(5)
search_mail = driver.find_element_by_name('email')
search_mail.send_keys(mail)
sleep(1)

search_password = driver.find_element_by_name('password')
search_password.send_keys(password)
sleep(1)
search_password.submit()
sleep(10)

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/section/p/a').click()
sleep(5)

number = 1
while number != 40:
    try:
        number += 1
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]').click()
        sleep(2)

    except:
        try:
            driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div').click()
        
        except:
            message = 'Привет'
            type_text = driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[1]/div/section/div/div[2]/form/div/div[1]/div/input')
            type_text.send_keys(message)
            sleep(1)
            type_text.submit()
            sleep(1.5)

driver.close()
