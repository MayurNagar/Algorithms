from selenium import webdriver
from time import sleep
from getpass import getpass
 
usr=input('Enter Email Id:') 
pwd=getpass('Enter Password:') 
 
driver = webdriver.Chrome()
 
driver.get('https://www.facebook.com/')
 
print ("Opened facebook...")
sleep(1)
 
a = driver.find_element_by_id('email')  #id of email box on fb
a.send_keys(usr)						#sends user input
print ("Email Id entered...")
sleep(1)
 
b =driver.find_element_by_id('pass') #id of password box on fb
b.send_keys(pwd)						#sends user input
print ("Password entered...")
 
c = driver.find_element_by_id('loginbutton')
c.click()							#click on login button
 
print ("Done...")
sleep(10)
driver.quit()