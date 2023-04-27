import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

nb_armoir = 150


url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"
#driver = webdriver.Chrome("./chromedriver") DeprecationWarning: executable_path has been deprecated, please pass in a Service object 
s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
#driver.add_argument("headless")

driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

for h2 in soup.findAll('h2') :
    nom_du_produit = h2.text.strip()

print(nom_du_produit)
