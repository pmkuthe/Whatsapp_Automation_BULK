from click._compat import raw_input
from joblib.numpy_pickle_utils import xrange
from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')
driver.get('https://web.whatsapp.com/')

msg = input('Enter the message:- ')
input('Enter any Key after scanning QR code')
per = int(input('Enter the number of user to be taken:-'))

for i in range(per):
    name = []
    name.append(input('Enter the %s number: '))
    search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
    search_bar.send_keys(format(name).join(name))
    time.sleep(3)

    user_name = driver.find_element_by_xpath("//span[@class='_3NWy8']")
    user_name.click()
    time.sleep(3)

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(format(msg))
    time.sleep(2)

    ''' Sending message button'''
    send_button = driver.find_element_by_xpath("//button[@class='_3M-N-']")
    send_button.click()


