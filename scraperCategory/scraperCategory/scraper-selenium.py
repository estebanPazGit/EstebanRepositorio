from selenium import webdriver
import json

driver = webdriver.Firefox()

# categorias y subcategorias de COTO

URL = 'https://www.cotodigital3.com.ar/sitios/cdigi/browse'

driver.get(URL)

categorias_coto_menu = driver.find_elements_by_xpath('//*[@id="atg_store_catNav"]/li')

lista_categorias = []
lista_subcategorias = []

categorias_COTO = []

def formatearURL(url:str):
    '''
    Funcion que formatea la URL de una subcategoria para que pueda ser usada por la spider de COTO
    '''
    url_dividida = url.split('cdigi')
    url_subdiv = url_dividida[1].split('?')
    return url_subdiv[0]

def obtenerSubCategorias(url:str, categoria:str, driverFirefox, guardar=False):
    '''
    Funcion que obtiene las categorias de un segmento, o las subcategorias de una categoria, 
    o para obtener los datos a guardar cuando el ultimo parametro es True
    '''
    driverFirefox.get(url)
    categ_scrapeadas = driverFirefox.find_elements_by_xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li')
    subcategorias_obtenidas = []
    for elem in categ_scrapeadas:
        link_elem = elem.find_element_by_xpath('.//a')
        if link_elem.get_attribute('title') == categoria:
            link_elem.click()
            url_categoria = driverFirefox.current_url
            if guardar:
                categs = driverFirefox.find_elements_by_xpath('//*[@id="atg_store_refinementAncestorsLinkCategory"]/a')
                subcategoria = driverFirefox.find_element_by_xpath('//*[@id="atg_store_refinementAncestorsLastLink"]').text
                categoria_principal = categs[0].text
                if len(categs) < 2:
                    categoria_secundaria = ''
                else:
                    categoria_secundaria = categs[1].text
                print('###### Lo que voy a guardar en categoriasCoto es ######')
                print(categoria_principal)
                print(categoria_secundaria)
                print(subcategoria)
                print(formatearURL(url_categoria))
                print('########################################################')
                return formatearURL(url_categoria), categoria_principal, categoria_secundaria, subcategoria
            subcategorias_scrapeadas = driverFirefox.find_elements_by_xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li')
            for sub_categ in subcategorias_scrapeadas:
                sub_categ_scrapeada = sub_categ.find_element_by_xpath('.//a').get_attribute('title')
                subcategorias_obtenidas.append(sub_categ_scrapeada)
            break
    return subcategorias_obtenidas, url_categoria


# Obtencion de SEGMENTOS
for categoria in categorias_coto_menu:
    link_categoria = categoria.find_element_by_xpath('.//a').text
    if link_categoria != 'Ofertas':
        lista_categorias.append(link_categoria)


# lista, url_actual = obtenerSubCategorias(URL, 'Almacén', driver)
# print('OBTENGO 1')
# print('lista --> ', lista)
# print('URL --> ', url_actual)
# url_a_guardar, catprinc, catsecund, subcateg = obtenerSubCategorias(url_actual, 'Golosinas', driver, guardar=True)
# print('##################')
# print(url_a_guardar)
# print(catprinc)
# print(catsecund)
# print(subcateg)
# lista, url_actual = obtenerSubCategorias(url_actual, 'Golosinas', driver)
# print('OBTENGO 2')
# print('lista --> ', lista)
# print('URL --> ', url_actual)
# obtenerSubCategorias(url_actual, 'Alfajores', driver, guardar=True)

# Recorrido por SEGMENTOS, CATEGORIAS Y SUBCATEGORIAS
for categoria_princ in lista_categorias:
    categorias_secund, url_secund = obtenerSubCategorias(URL, categoria_princ, driver)
    for cat_sec in categorias_secund:
        subcategs, url_categ_secund = obtenerSubCategorias(url_secund, cat_sec, driver)
        for sub in subcategs:
            url_subcateg, categoria_nivel_1, categoria_nivel_2, subcategoria = obtenerSubCategorias(url_categ_secund, sub, driver, guardar=True)
            categorias_COTO.append([url_subcateg, categoria_nivel_1, categoria_nivel_2, subcategoria])


# Guardo los resultados en un JSON
with open('categoriasCoto.json', 'w', encoding='utf8') as file:
    json.dump(categorias_COTO, file, indent=4, ensure_ascii=False)


'''
# categorias y subcategorias de DIA

driver.get('https://diaonline.supermercadosdia.com.ar/')

boton_categorias = driver.find_element_by_xpath('//*[@id="home-page"]/div[9]/header/div[5]/div[1]/div/nav/ul/li')
boton_categorias.click()

'''