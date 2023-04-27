import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

nb_armoir = 150

#------- load and sleep the scrap page 
url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"
#driver = webdriver.Chrome("./chromedriver") DeprecationWarning: executable_path has been deprecated, please pass in a Service object 
s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
#driver.add_argument("headless") to hide the open-load 

driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')


#------- find the H2 on the page 
for h2 in soup.findAll('h2') :
    nom_du_produit = h2.text.strip()

#print(nom_du_produit)


#------- Load other pages (next pages)
#------- Send to CSV


