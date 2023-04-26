import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.oanda.com/currency-converter/fr/?from=EUR&to=USD&amount=NaN')
time.sleep(3)

champs_euro = driver.find_element(By.CLASS_NAME, "numberformat").send_keys('34')



