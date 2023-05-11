from selenium import webdriver
from bs4 import BeautifulSoup

# initialisez le navigateur web
driver = webdriver.Chrome()

# naviguez vers la page
driver.get("https://atosafr.fr/")

# attendez que la page se charge
driver.implicitly_wait(10)

# récupérez le code HTML de la page
html = driver.page_source

# analysez le code HTML avec Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# trouvez tous les éléments "a" avec un attribut "href"
links = soup.find_all("a", href=True)

# extrayez la valeur de l'attribut "href" de chaque lien
for link in links:
    url = link.get("href")
    print(len(url))

# fermez le navigateur
driver.quit()


