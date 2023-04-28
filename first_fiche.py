import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd 
from openpyxl.workbook import Workbook

EXPORT_PATH = "./exports/"

url = "https://eberhardt-pro.fr/armoires-refrigerees/5731-congelateur-electromenager-no-frost-6-tiroirs-238l.html"

s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
#driver.add_argument("headless") #to hide the open-load 


driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

def clean_text(str):
    return str.replace('\n', " ").replace('\t', " ")
#---------- Recupération du titre et de la ref 
for title in soup.find('h1',class_= "h1") : 
      print(title.get_text(strip=True))
for ref in soup.find('p',class_= "d-none") : 
     print(ref.get_text(strip=True))


#---------- Tab et Description du produit 
items = soup.find_all("div", {"class": "col-12 col-sm-6 product--description--content--item"})
#print(items)

item = items[0]
#type = clean_text(item.find('span').get_text(strip=True))
#print(type)
my_spans = items.find("span", recursive=False)
for span in my_spans:
    print(span)

#child et les recup dans un objet : premier enfant = clé deuxieme = valeur 

#caract = []
#for item in items : 
#   type = clean_text(item.find('span').get_text(strip=True))
#   print(type)
#  ans = clean_text(item.find('span').get_text(strip=True))

   # produits = {
    #   "type" : type,
    #}
    #print(caract.append(produits))
#-------- Print to excel 

#df = pd.DataFrame(caract)
#print(df)
#df.to_excel(EXPORT_PATH + 'Fiche_produit1', index=False)