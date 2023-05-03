import time 
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd 
from openpyxl.workbook import Workbook
from selenium.webdriver.common.proxy import *

#choper un proxi avec requests
# response = requests.get('https://free-proxy-list.net/')
# proxy_list = pd.read_html(response.text)[0]
# proxy_list["url"] = 'http://' + proxy_list["IP Adress"] + ":" + proxy_list["Port"].astype(str)
# proxy_list.head()

# https_proxies = proxy_list[proxy_list["https"] == 'yes']
# https_proxies.count()
# choper un proxi avec selenium 
proxy_url = "192.168.68.129:443"
proxy = Proxy ({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_url,
    'sslProxy': proxy_url,
    'noProxy': ''})

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)
driver.get("https://free-proxy-list.net/")

# EXPORT_PATH = "./exports/"

# url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"

# s=Service('./chromedriver')
# driver = webdriver.Chrome(service=s)

# driver.get(url)
# time.sleep(2)

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# trouve l'élément HTML contenant les liens des produits
# product_list = soup.find("div", {"id": "js-product-list"})

# extrait les liens des produits et stocke-les dans une liste
# product_links = []
# for link in product_list.find_all("a"):
#    product_links.append(link["href"])

# imprime la liste des liens des produits
# print(len(product_links))

# trouve tous les liens de produits sur la page
# product_links = driver.find_elements(By.XPATH, "//a[@id='js-product-list']")

# clique sur chaque lien de produit individuellement et récupère les informations
# for link in product_links:
#     clique sur le lien du produit
#     link.click()

#     récupère les informations du produit (à l'aide de BeautifulSoup)
#     ...
#     caract = []

#     div = soup.find('div', class_='product--description--content')

#     spans = div.find_all('span')
#     for span in spans:
#         text = span.get_text(strip=True) # récupère le texte brut sans les balises HTML

#     produits = {
#       "type" : text, # stocke le texte brut dans le dictionnaire produits
#     }
#     caract.append(produits) 

#     retourne à la page de la liste des produits
#     driver.back()

