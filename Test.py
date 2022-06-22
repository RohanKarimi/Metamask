import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#incognito mode
#chrome_options.add_argument("--incognito")
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

#object of Options class
chrome_options = Options()
print('Setting up metamask extension please wait...')
#set .crx file path of extension
chrome_options.add_extension('metamask.crx')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
time.sleep(5)
# create new Chrome driver object with Metamask extension
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get("https://www.google.com/")
driver.get("chrome://extensions/")

#return all the handle values of opened browser window
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

driver.find_element(By.XPATH, '//button[text()="Get Started"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[text()="Import wallet"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[text()="No Thanks"]').click()
time.sleep(2)

recoveryPhrase = 'large, vague, fall, dynamic, select, large, brother, isolate, hint, wire, emerge, finger'
password = 'TestMeHard666'
inputs = driver.find_element(By.XPATH, '//input')
inputs[0].send_keys(recoveryPhrase)
inputs[1].send_keys(password)
inputs[2].send_keys(password)

driver.find_element(By.CSS_SELECTOR, '.first-time-flow__terms').click()
driver.find_element(By.XPATH, '//button[text()="Import"]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//button[text()="All Done"]').click()

# closing the message popup after all done metamask screen
driver.find_element(By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button').click()
time.sleep(2)
print("Wallet has been imported successfully")


# opening network
networkName=''
print("Changing network")
driver.switch_to.window(driver.window_handles[1])
driver.get('chrome-extension://{}/home.html'.format('EXTENSION_ID'))
print("closing popup")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button').click()
driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
time.sleep(2)
print("opening network dropdown")
elem = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div').click()
time.sleep(2)
all_li = elem.find_elements_by_tag_name("li")
time.sleep(2)
for li in all_li:
    text = li.text
    if (text == networkName):
        li.click()
        print(text, "is selected")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
print("Please provide a valid network name")
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)


driver.quit()