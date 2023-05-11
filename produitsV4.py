import requests
from bs4 import BeautifulSoup
import pandas as pd

EXPORT_PATH = "./exports/"

# URL de la page des armoires réfrigérées
url = "https://eberhardt-pro.fr/cuisine-professionnelle/29-armoires-refrigerees?page=2"

# En-têtes HTTP pour imiter un navigateur web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Obtenir le contenu HTML de la page des armoires réfrigérées
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Récupérer les liens des produits
product_links = [a['href'] for a in soup.select("#js-product-list a")]

# Récupérer les informations sur chaque produit
products = []
for link in product_links:
    # Obtenir le contenu HTML de la page du produit
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupérer le nom et la description du produit et plus 
    name = soup.find('h1', class_='h1').text.strip()
    ref = soup.find('p', class_='d-none').text.strip()
    description = soup.find('div', class_='product--description--content').text.strip()
    priceht = soup.find('div', class_='current-price').text.strip()
    prixachat = int(priceht) * 0,70 


    # Ajouter le produit à la liste des produits
    products.append({'Nom': name, 'Référence': ref, 'Description': description, 'Price HT': priceht, "Prix achat" : prixachat})

# Créer un DataFrame pandas à partir de la liste des produits
    df = pd.DataFrame(products)
    print(df)

# Exporter le DataFrame dans un fichier Excel
    #df.to_excel(EXPORT_PATH + 'test.xlsx', index=False)

    print("Export terminé !")