import json
import requests
# from selenium import webdriver
from seleniumwire import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException

# deshabilitar geolocalizacion en el navegador
geoDisabled = webdriver.FirefoxOptions()
geoDisabled.set_preference("geo.enabled", False)

fp = webdriver.FirefoxProfile()
fp.set_preference("dom.popup_maximum", 0)
browser = webdriver.Firefox(options=geoDisabled, firefox_profile=fp)

# browser.get('https://www.jumbo.com.ar/bebidas/aguas')

# for request in browser.requests:
    # if request.response.status_code == 206:
        # if 'sasCache' in request.path:
        # url = request.url
        # print(
            # request.url,
            # request.response.status_code,
            # request.response.headers,
            # request.body,
            # '\n'
        # )

def parserCategorias(cadena:str):
    string = cadena.split('/')
    result = list(filter(lambda x: x != '', string))
    result.reverse()
    return result[0]

url = 'https://www.jumbo.com.ar/api/catalog_system/pub/products/search/?&fq=C%3a%2f2%2f32%2f&O=OrderByScoreDESC&_from=0&_to=0'
req = requests.get(url)
req_json = req.json()
lista = []
lista.append(url)
for r, q in zip(req_json[0]['categories'], req_json[0]['categoriesIds']):
    lista.append(parserCategorias(r))
    lista.append(parserCategorias(q))


def extraerURL(browser):
    for req in browser.requests:
        if req.status_code == 206:
            url = req.url
            return url


def generarListaAGuardar(lista_urls:str, browser):
    lista_resultante = []
    for link in lista_urls:
        browser.get(link)
        WebDriverWait(browser, timeout=20)
        url = extraerURL(browser)
        solicitud = requests.get(url)
        solicitud_json = solicitud.json()
        lista_a_insertar = []
        lista_a_insertar.append(url)
        for categ, num in zip(solicitud_json[0]['categories'], solicitud_json[0]['categoriesIds']):
            lista_a_insertar.append(parserCategorias(categ))
            lista_a_insertar.append(parserCategorias(num))
        lista_resultante.append(lista_a_insertar)
    return lista_resultante


print(lista)