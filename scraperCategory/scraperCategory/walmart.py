import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


geoDisabled = webdriver.FirefoxOptions()
geoDisabled.set_preference("geo.enabled", False)

fp = webdriver.FirefoxProfile()
fp.set_preference("dom.popup_maximum", 0)
browser = webdriver.Firefox(options=geoDisabled, firefox_profile=fp)


browser.get('https://www.walmart.com.ar/')
WebDriverWait(browser, timeout=15)

# categorias = browser.find_element_by_xpath('//*[@id="header-root"]/div/div/div[1]/div/div/nav/button')
# 
# hover_opciones_menu = browser.find_elements_by_xpath('//*[@class="header-categories-nav__dropdown-item"]')
# 
# hover = ActionChains(browser)
# hover.move_to_element(categorias)
# hover.perform()

links_scrapeables = [
    [
        'Almacén',
        'https://www.walmart.com.ar/aceites-y-aderezos',
        'https://www.walmart.com.ar/aceitunas-y-encurtidos',
        'https://www.walmart.com.ar/conservas',
        'https://www.walmart.com.ar/desayuno-y-golosinas',
        'https://www.walmart.com.ar/panificados',
        'https://www.walmart.com.ar/arroz-y-legumbres',
        'https://www.walmart.com.ar/snacks',
        'https://www.walmart.com.ar/sopas-caldos-y-pure',
        'https://www.walmart.com.ar/pastas-y-harinas'
    ],
    [
        'Frescos',
        'https://www.walmart.com.ar/lacteos',
        'https://www.walmart.com.ar/pastas-y-tapas',
        'https://www.walmart.com.ar/carniceria-y-pescaderia',
        'https://www.walmart.com.ar/frutas-y-verduras',
        'https://www.walmart.com.ar/fiambreria',
        'https://www.walmart.com.ar/congelados',
        'https://www.walmart.com.ar/panaderia-y-reposteria'
    ],
    [
        'Bebidas',
        'https://www.walmart.com.ar/aperitivos',
        'https://www.walmart.com.ar/cervezas',
        'https://www.walmart.com.ar/vinos-y-espumantes',
        'https://www.walmart.com.ar/bebidas-blancas-y-licores',
        'https://www.walmart.com.ar/a-base-de-hierbas',
        'https://www.walmart.com.ar/aguas',
        'https://www.walmart.com.ar/gaseosas',
        'https://www.walmart.com.ar/jugos',
        'https://www.walmart.com.ar/isotonicas-y-energizantes'
    ],
    [
        'Perfumería',
        'https://www.walmart.com.ar/cuidado-del-cabello',
        'https://www.walmart.com.ar/cuidado-oral',
        'https://www.walmart.com.ar/cuidado-facial',
        'https://www.walmart.com.ar/proteccion-femenina',
        'https://www.walmart.com.ar/cuidado-del-bebe',
        'https://www.walmart.com.ar/cuidado-del-adulto',
        'https://www.walmart.com.ar/cuidado-corporal'
    ],
    [
        'Limpieza',
        'https://www.walmart.com.ar/desodorante-de-ambientes',
        'https://www.walmart.com.ar/papeles',
        'https://www.walmart.com.ar/limpieza-de-ba%C3%B1o',
        'https://www.walmart.com.ar/limpieza-de-cocina',
        'https://www.walmart.com.ar/limpieza-de-pisos-y-muebles',
        'https://www.walmart.com.ar/limpieza-de-ropa',
        'https://www.walmart.com.ar/lavandina',
        'https://www.walmart.com.ar/limpieza-de-calzado',
        'https://www.walmart.com.ar/accesorios-de-limpieza',
        'https://www.walmart.com.ar/insecticidas'
    ],
    [
        'Bebes y Mamas',
        'https://www.walmart.com.ar/cuidado-del-bebe',
        'https://www.walmart.com.ar/alimentacion-infantil',
        'https://www.walmart.com.ar/paseo-y-viaje',
        'https://www.walmart.com.ar/varios-para-el-bebe',
        'https://www.walmart.com.ar/primera-infancia',
        'https://www.walmart.com.ar/peluches',
        'https://www.walmart.com.ar/cuidado-mama'
    ],
    [
        'Mascotas',
        'https://www.walmart.com.ar/alimento-perro',
        'https://www.walmart.com.ar/alimento-gato',
        'https://www.walmart.com.ar/accesorios-y-otras-mascotas'
    ],
    [
        'Tecnología',
        'https://www.walmart.com.ar/tv-y-video',
        'https://www.walmart.com.ar/audio',
        'https://www.walmart.com.ar/gaming',
        'https://www.walmart.com.ar/telefonia',
        'https://www.walmart.com.ar/informatica',
        'https://www.walmart.com.ar/impresoras'
    ],
    [
        'Electrodomésticos',
        'https://www.walmart.com.ar/climatizacion',
        'https://www.walmart.com.ar/calefaccion',
        'https://www.walmart.com.ar/lavado',
        'https://www.walmart.com.ar/heladeras-y-freezers',
        'https://www.walmart.com.ar/calefones-y-termotanques',
        'https://www.walmart.com.ar/peque%C3%B1o-electro',
        'https://www.walmart.com.ar/cuidado-personal',
        'https://www.walmart.com.ar/cocinas-y-extractores'
    ],
    [
        'Hogar y Bazar',
        'https://www.walmart.com.ar/para-la-cocina',
        'https://www.walmart.com.ar/organizacion-para-la-ropa',
        'https://www.walmart.com.ar/cotillon',
        'https://www.walmart.com.ar/decoracion',
        'https://www.walmart.com.ar/ropa-de-cama-y-ba%C3%B1o',
        'https://www.walmart.com.ar/bolsos-y-valijas',
        'https://www.walmart.com.ar/colchones-y-almohadas',
        'https://www.walmart.com.ar/muebles-de-interior',
        'https://www.walmart.com.ar/para-la-mesa',
        'https://www.walmart.com.ar/moda'
    ],
    [
        'Juguetería',
        'https://www.walmart.com.ar/juegos-de-mesa',
        'https://www.walmart.com.ar/juguetes',
        'https://www.walmart.com.ar/peluches',
        'https://www.walmart.com.ar/primera-infancia',
        'https://www.walmart.com.ar/rodados',
        'https://www.walmart.com.ar/juguetes-varios'
    ],
    [
        'Librería y Ocio',
        'https://www.walmart.com.ar/libreria',
        'https://www.walmart.com.ar/libros',
        'https://www.walmart.com.ar/vuelta-al-cole'
    ],
    [
        'Automotor y Ferretería',
        'https://www.walmart.com.ar/motos',
        'https://www.walmart.com.ar/neumaticos',
        'https://www.walmart.com.ar/alfombras-fundas-y-cobertores-para-auto',
        'https://www.walmart.com.ar/baterias-auto',
        'https://www.walmart.com.ar/lubricantes-y-aditivos-para-auto',
        'https://www.walmart.com.ar/accesorios-para-autos',
        'https://www.walmart.com.ar/herramientas-cajas-y-escaleras',
        'https://www.walmart.com.ar/lamparitas-y-electricidad',
        'https://www.walmart.com.ar/pintureria',
        'https://www.walmart.com.ar/adhesivos'
    ],
    [
        'Aire Libre',
        'https://www.walmart.com.ar/decoracion-y-accesorios-de-jardin',
        'https://www.walmart.com.ar/maquinas-y-herramientas-de-jardin',
        'https://www.walmart.com.ar/macetas-semillas-tierras-y-abonos',
        'https://www.walmart.com.ar/bicicletas',
        'https://www.walmart.com.ar/fitness',
        'https://www.walmart.com.ar/piletas-y-accesorios',
        'https://www.walmart.com.ar/parrillas-y-carbon',
        'https://www.walmart.com.ar/muebles-de-jardin-y-playa',
        'https://www.walmart.com.ar/camping',
        'https://www.walmart.com.ar/otros-deportes'
    ],
]

# para sacar la lista de segmentos

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

enlaces_segmentos = obtenerEnlacesDeCategorias(browser, 'https://www.walmart.com.ar/aceites-y-aderezos', '//*[@class="search-single-navigator"]/h4/a')

print('#### Segmentos ####')
print(enlaces_segmentos)

# para sacar la lista donde estan las subcategorias y segmentos --> //*[@class="bread-crumb"]/ul/li

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

datos_a_guardar = generarListas(browser, subcat_href)