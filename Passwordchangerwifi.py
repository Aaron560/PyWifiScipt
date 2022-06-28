#imports all necessary modules and  functions into the project.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import secrets
import string


# Create the webdriver object.
#Also creates a llist of random wifi names to use.
driver = webdriver.Chrome("chromedriver")
random_wifi_names = [
"Rebellious Amish Family",
"Not a Meth Lab",
"Definitely a Meth Lab",
"FBI Surveillance Van 3",
"I am Always Watching",
"Hack of All Trades",
"Russian Hackers",
"LAN-Rover",
"You Will Regret This",
"Clean Your Glasses!",
"Wi-Fi for the Recently Deceased",
"The Promised LAN",
"Reserved for Guests I Hate",
"Open Sesame",
"Jump on the Bandwidth",
"Look Ma, No Wires!",
"I'm Under Your Bed",
"Enter the Dragons Wi-Fi",
"Wi of the Figer",
"Bob DyLAN",
]

#Selects a random wifi name and generates a random password.
NewName = random.choice(random_wifi_names)
NewPass = ''.join([secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16)])


#Redirects To the URL.
driver.get("http://192.168.1.1/1.2.4/login.html")

# MaximizeWindow and waits for 2 seconds.
driver.maximize_window()
time.sleep(2)

#Interacts with the specified Input boxes and overwrites the current data in them with new data,
userName = driver.find_element(By.ID,'username')
userName.click()
userName.send_keys("admin")

passWord = driver.find_element(By.ID,'password')
passWord.click()
passWord.send_keys("XX37Msw3XdGSYMM")

# Obtain button by link ID and clicks.
button = driver.find_element(By.ID,'login-btn')
button.click()
time.sleep(5)


#Interacts with the specified Input boxes and overwrites the current data in them with new data,
wifiName = driver.find_element(By.ID,'ssid_24g')
wifiName.click()
wifiName.send_keys(Keys.CONTROL + "a")
wifiName.send_keys(Keys.DELETE)
wifiName.send_keys(NewName)

wifipassWord = driver.find_element(By.ID,'pwd_24g')
wifipassWord.click()
wifipassWord.send_keys(Keys.CONTROL + "a")
wifipassWord.send_keys(Keys.DELETE)
wifipassWord.send_keys(NewPass)

saveChanges = driver.find_element(By.ID,'save')
saveChanges.click()
time.sleep(5)
confirmChanges = driver.find_element(By.NAME,'confirm')
confirmChanges.click()
driver.close() #It closes the browser window on which the focus is set.

driver.quit() #It basically calls the driver.dispose method which in turn closes all the browser windows and ends the WebDriver session gracefully.