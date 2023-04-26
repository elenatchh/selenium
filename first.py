import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.oanda.com/currency-converter/fr/?from=EUR&to=USD&amount=NaN')
time.sleep(5)

champs_euro = driver.find_element(By.CLASS_NAME, "numberformat").send_keys('34')

champs_euro = send_keys(Keys.RETURN)

