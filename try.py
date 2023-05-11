import requests
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pandas as pd 

# Obtenir une liste de proxies depuis https://free-proxy-list.net/
response = requests.get("https://free-proxy-list.net/")
proxy_list = pd.read_html(response.text)[0]
proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)

# Créer une liste de proxies à utiliser
proxies_to_use = list(proxy_list["url"].head(10))

# Initialiser l'indice du proxy courant
current_proxy_index = 0

# Fonction pour obtenir le proxy courant
def get_current_proxy():
    return proxies_to_use[current_proxy_index]

# Fonction pour passer au proxy suivant
def rotate_proxy():
    global current_proxy_index
    current_proxy_index = (current_proxy_index + 1) % len(proxies_to_use)

# Boucle pour naviguer avec les proxies
for i in range(10):
    # Créer un objet Proxy à partir de l'URL du proxy courant
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': get_current_proxy(),
        'sslProxy': get_current_proxy()
    })

    # Créer les options pour Chrome avec le proxy configuré et la navigation headless activée
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    proxy.add_to_capabilities(chrome_options.to_capabilities())

    # Créer le navigateur Chrome avec les options de proxy et de navigation headless
    driver = webdriver.Chrome(options=chrome_options)

    # Ouvrir la page à naviguer
    driver.get("https://httpbin.org/ip")

    # Passer au proxy suivant
    rotate_proxy()

    # Fermer le navigateur
    driver.quit()