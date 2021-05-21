import json
import requests
from selenium import webdriver
from seleniumwire import webdriver as webdriver_extra
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# deshabilitar geolocalizacion en el navegador
geoDisabled = webdriver.FirefoxOptions()
geoDisabled.set_preference("geo.enabled", False)

fp = webdriver.FirefoxProfile()
fp.set_preference("dom.popup_maximum", 0)
browser = webdriver.Firefox(options=geoDisabled, firefox_profile=fp)
browser_extra = webdriver_extra.Firefox(options=geoDisabled, firefox_profile=fp)
'''
browser.get('https://www.jumbo.com.ar/digital')
WebDriverWait(browser, timeout=20)


btn_categorias = browser.find_element_by_xpath('//*[@id="toggle-menu"]')
btn_categorias.click()

segmentos = browser.find_elements_by_xpath('//*[@id="department-wrapper"]//*[@class="item-link"]//*[@class="text"]')
segmentos_href = browser.find_elements_by_xpath('//*[@id="department-wrapper"]//*[@class="item-link"]')

seg = []
seg_href = []


for s in segmentos:
    if s.text != 'Ofertas':
        seg.append(s.text)


def clickear(browser, lista_href:list):
    lista_categorias = []
    for l in lista_href:
        browser.get(l)
        WebDriverWait(browser, timeout=20)
        categorias = browser.find_elements_by_xpath('//*[@class="search-single-navigator ready"]//*[@class="electro even"]/a')
        for cat in categorias:
            lista_categorias.append(cat.get_attribute('href'))
            print(cat.get_attribute('href'))
        break


def obtenerEnlacesDeCategorias(browser, url:str, xpath:str):
    browser.get(url)
    print('###### URL que se analiza #######')
    print(url)
    WebDriverWait(browser, timeout=20)
    categorias = browser.find_elements_by_xpath(xpath)
    lista_enlaces = []
    if len(categorias) != 0:
        for cat in categorias:
            if cat.get_attribute('href') != None:
                lista_enlaces.append(cat.get_attribute('href'))
    else:
        lista_enlaces.append(url)
    return lista_enlaces


for s in segmentos_href:
    if s.text != 'Ofetas':
        seg_href.append(s.get_attribute('href'))

cat_href = []
xpath = '//*[@class="category-name"]'
for a in seg_href:
    print('ingreso a buscar categorias')
    enlaces = obtenerEnlacesDeCategorias(browser, a, xpath)
    for a in enlaces:
        cat_href.append(a)

xpath = '//*[@id="category-page"]/main/div[2]/div/div[1]/div[1]/div[4]/div/div/div[2]/fieldset[1]/div/a'
subcat_href = []
for a in cat_href:
    print('ingreso a buscar subcategorias')
    enlaces = obtenerEnlacesDeCategorias(browser, a, xpath)
    for a in enlaces:
        subcat_href.append(a)

# print('las subcategorias son ', len(subcat_href))

# generar una lista de listas para usar el scraper

# lista_test = [
    # 'https://www.jumbo.com.ar/electro/aire-acondicionado-y-ventilacion/aire-acondicionado?PS=20',
    # 'https://www.jumbo.com.ar/electro/audio?PS=20'
    # 'https://www.jumbo.com.ar/almacen/libre-de-gluten'
# ]

def generarListas(browser, links:list):
    lista_resultado = []
    # links.remove('https://www.jumbo.com.ar/bebidas/jugos/granadina')
    for a in links:
        print('#### ingreso a generar listas ####')
        print('con el link --> ', a)
        browser.get(a)
        try:
            nombre_segmento = browser.find_element_by_xpath('//*[@id="category-page"]/main/div[1]/div/h3/div/ul/li[2]').text
        except NoSuchElementException:
            try:
                nombre_segmento = browser.find_element_by_xpath('//*[@id="category-page"]/div[17]/div/div/ul/li[3]/strong').text
            except NoSuchElementException:
                nombre_segmento = ''
        try:
            nombre_categoria = browser.find_element_by_xpath('//*[@id="category-page"]/main/div[1]/div/h3/div/ul/li[3]').text
        except NoSuchElementException:
            nombre_categoria = ''
        try:
            nombre_subcategoria = browser.find_element_by_xpath('//*[@id="category-page"]/main/div[1]/div/h3/div/ul/li[4]').text
        except NoSuchElementException:
            nombre_subcategoria = ''
        print('###### DATOS ######')
        print(nombre_segmento)
        print(nombre_categoria)
        print(nombre_subcategoria)
        print('####################')
        if nombre_segmento != '':
            lista_resultado.append([a, nombre_segmento, nombre_categoria, nombre_subcategoria])
    return lista_resultado
'''
# datos_a_guardar = generarListas(browser, subcat_href)

def obtenerNumSubcategoria(cadena:str):
    string = cadena.split('/')
    result = list(filter(lambda x: x != '', string))
    result.pop(0)
    # result.reverse()
    # return result[0]
    return result[0]+'/'+result[1]

def obtenerNumCategoria(cadena:str):
    string = cadena.split('/')
    result = list(filter(lambda x: x != '', string))
    # result.reverse()
    return int(result[0])

def extraerURL(browser):
    for req in browser.requests:
        if req.response.status_code == 206:
            url = req.url
            return url

def generarListaAGuardar(lista_urls:str, browser):
    lista_resultante = []
    # browser.get('https://www.jumbo.com.ar')
    # browser_extra = webdriver_extra.Firefox()
    for link in lista_urls:
        browser.get(link)
        # WebDriverWait(browser, timeout=20)
        url = extraerURL(browser)
        solicitud = requests.get(url)
        solicitud_json = solicitud.json()
        lista_cod_categ = []
        dict_cod_subcateg = []
        # lista_cod_categ.append(url)
        # for categ, num in zip(solicitud_json[0]['categories'], solicitud_json[0]['categoriesIds']):
            # lista_cod_categ.append(parserCategorias(categ))

        print("solicitud_json[0]['categoriesIds'][0] ---> ", solicitud_json[0]['categoriesIds'][0])
        flag = True
        # for categ in solicitud_json[0]['categoriesIds'][0]:
            # cod_categoria = obtenerNumCategoria(categ)
            # print('cod_categoria --> ', cod_categoria)
            # cod_subcategorias = obtenerNumSubcategoria(categ)
            # print('cod_subcategorias --> ', cod_subcategorias)
            # if flag:
                # lista_cod_categ.append(cod_categoria)
                # dict_cod_subcateg.append(cod_subcategorias)
            # elif not cod_categoria in lista_cod_categ:
                # lista_cod_categ.append(cod_categoria)
                # dict_cod_subcateg.append(cod_subcategorias)
            # else:
                # dict_cod_subcateg.append(cod_subcategorias)

    # return lista_resultante
    return lista_cod_categ, dict_cod_subcateg

lista_test = [
    "https://www.jumbo.com.ar/almacen/aceites-y-vinagres",
    "https://www.jumbo.com.ar/almacen/aderezos",
    "https://www.jumbo.com.ar/almacen/arroz-y-legumbres"
]

datos_a_guardar, datos = generarListaAGuardar(lista_test, browser_extra)


with open('categoriasJumbo2.json', 'a', encoding='utf8') as file:
    json.dump(datos_a_guardar, file, indent=4, ensure_ascii=False)

with open('categoriasJumbo2.json', 'a', encoding='utf8') as file:
    json.dump(datos, file, indent=4, ensure_ascii=False)

