import time 
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd 
from openpyxl.workbook import Workbook
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import NoSuchWindowException

EXPORT_PATH = "./exports/"

url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"

s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)

driver.get(url)
time.sleep(2)

#def find_product():
  #trouve l'élément HTML contenant les liens des produits
soup = BeautifulSoup(driver.page_source, 'html.parser')
product_list = soup.find("div", {"id": "js-product-list"})

#extrait les liens des produits et stocke-les dans une liste
product_links = []
for link in product_list.find_all("a"):
    product_links.append(link["href"])

#imprime la liste des liens des produits
print(len(product_links))

#clique sur chaque lien de produit individuellement et récupère les informations
caract = []
max_retries = 3 # maximum number of retries
for link in product_links:
    retries = 0
    while retries < max_retries:
        try:
            #clique sur le lien du produit
            driver.get(link)
            time.sleep(2)
            #récupère les informations du produit (à l'aide de BeautifulSoup)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            div = soup.find('div', class_='product--description--content')

            spans = div.find_all('span')
            print(spans)
            text = ""
            for span in spans:
                text += span.get_text(strip=True) + " " # récupère le texte brut sans les balises HTML

            produits = {
              "type" : text, # stocke le texte brut dans le dictionnaire produits
            }
            caract.append(produits)

            #retourne à la page de la liste des produits
            driver.back()
            break
        except NoSuchWindowException:
            retries += 1
            time.sleep(2)
    if retries == max_retries:
        print(f"Failed to get link {link}")

df = pd.DataFrame(caract)
print(df)
#df.to_excel(EXPORT_PATH + 'Armoires_Froides_ebe.xlsx', index=False)

driver.quit()
