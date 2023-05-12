import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

EXPORT_PATH = "../exports/"

# URL de la page des armoires réfrigérées
url = "https://atosafr.fr/category/armoires-refrigerees-atosa/armoires-refrigerees-gn2-1/"
s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
# En-têtes HTTP pour imiter un navigateur web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Obtenir le contenu HTML de la page des armoires réfrigérées
response = requests.get(url, headers=headers)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Récupérer les liens des produits
links = soup.find_all("a", href=True)


# extrayez la valeur de l'attribut "href" de chaque lien
for link in links:
    url = link.get("href")
    print(len(url))

items = soup.find("div", class_= "shop container")
print(items)
