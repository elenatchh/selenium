import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd 
from openpyxl.workbook import Workbook

nb_armoir_looking = 120
EXPORT_PATH = "./exports/"

#------- load and sleep the scrap page 
url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"
#driver = webdriver.Chrome("./chromedriver") DeprecationWarning: executable_path has been deprecated, please pass in a Service object 
s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
#driver.add_argument("headless") to hide the open-load 

driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

def clean_text(str):
    return str.replace('\n', " ").replace('\t', " ")


items = soup.find_all("div", {"class": "thumbnail-container"})
#print(len(items))

item = items[0]
code_art = clean_text(item.find("div", {'class': 'product-reference'}).get_text(strip=True))
#print(code_art)

#-------  retrieve items and sotck it in a list 

list_produits = []

for item in items : 

    title = clean_text(item.find('h2',class_= "h6 product-title mt-2").get_text(strip=True))
    code_art = clean_text(item.find("div", {'class': 'product-reference'}).get_text(strip=True))
    
    produit = {
        "title" : title,
        'code_art':  code_art
    }
    list_produits.append(produit)
#print(list_produits)
#------- Send to CSV

df = pd.DataFrame(list_produits)
print(df)
#df.to_excel(EXPORT_PATH + 'Armoires_Froides_ebe.xlsx', index=False)