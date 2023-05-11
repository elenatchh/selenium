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

#items = soup.find_all("div", {"class": "col-12 col-sm-6 product--description--content--item"})
#print(len(items))

caract = []

div = soup.find('div', class_='product--description--content')

spans = div.find_all('span')
 

for span in spans:
    text = span.get_text(strip=True) # récupère le texte brut sans les balises HTML

    produits = {
      "type" : text, # stocke le texte brut dans le dictionnaire produits
    }
    caract.append(produits)

#wb = Workbook()
#sheet = wb.active
#sheet.append(['carcateristique', text])
#sheet.append(['Alice', 25])
#sheet.append(['Bob', 30])

#wb.save('ficheproduit2.xlsx')

df = pd.DataFrame(caract) # crée le DataFrame Pandas à partir de la liste caract contenant le texte brut
print(df)
#df.to_excel(EXPORT_PATH + 'Ficheproduit1.xlsx', index=False)