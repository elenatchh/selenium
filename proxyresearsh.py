import requests
from selenium import webdriver
import pandas as pd 
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service

# Obtenir une liste de proxies depuis https://free-proxy-list.net/
response = requests.get("https://free-proxy-list.net/")
proxy_list = pd.read_html(response.text)[0]
proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)

# Créer une liste de proxies à tester
proxies_to_test = list(proxy_list["url"].head(10))

# Tester chaque proxy
for proxy_url in proxies_to_test:
    # Créer un objet Proxy à partir de l'URL du proxy
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_url,
        'sslProxy': proxy_url
    })

    # Créer les options pour Chrome avec le proxy configuré
    chrome_options = webdriver.ChromeOptions()
    proxy.add_to_capabilities(chrome_options.to_capabilities())

    # Créer le navigateur Chrome avec les options de proxy
    s=Service('./chromedriver')
    driver = webdriver.Chrome(options=chrome_options, service=s)

    # Ouvrir https://httpbin.org/ip pour vérifier le proxy
    try:
        driver.get("https://httpbin.org/ip")
        ip = driver.find_element_by_xpath('//pre').text
        print(f"Proxy {proxy_url} returned IP address: {ip}")
    except Exception as e:
        print(f"Error with proxy {proxy_url}: {str(e)}")
    
    # Fermer le navigateur
    driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy, ProxyType

# proxy_url = 'http://8.219.5.240:1080'

# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': proxy_url,
#     'ftpProxy': proxy_url,
#     'sslProxy': proxy_url,
# })

# capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# proxy.add_to_capabilities(capabilities)

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')

# driver = webdriver.Chrome(
#     options=options,
#     desired_capabilities=capabilities,
#     proxy=proxy
# )

# driver.get('https://www.google.com')