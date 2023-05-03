import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd 
from openpyxl.workbook import Workbook

EXPORT_PATH = "./exports/"

url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"

s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)

driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# trouve l'élément HTML contenant les liens des produits
product_list = soup.find("div", {"id": "js-product-list"})

# extrait les liens des produits et stocke-les dans une liste
#product_links = []
#for link in product_list.find_all("a"):
#    product_links.append(link["href"])

# imprime la liste des liens des produits
#print(len(product_links))

# trouve tous les liens de produits sur la page
product_links = driver.find_elements(By.XPATH, "//a[@class='product-link']")

# clique sur chaque lien de produit individuellement et récupère les informations
for link in product_links:
    # clique sur le lien du produit
    link.click()

    # récupère les informations du produit (à l'aide de BeautifulSoup)
    # ...

    # retourne à la page de la liste des produits
    driver.back()

