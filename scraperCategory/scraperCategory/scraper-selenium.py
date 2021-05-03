from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

# categorias y subcategorias de COTO

driver.get('https://www.cotodigital3.com.ar/sitios/cdigi/browse')

categorias_coto_menu = driver.find_elements_by_xpath('//*[@id="atg_store_catNav"]/li')
categorias = driver.find_elements_by_xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li')

lista_categorias = []
lista_subcategorias = []

categorias_COTO = []
for categoria in categorias_coto_menu:
    link_categoria = categoria.find_element_by_xpath('.//a').text
    if link_categoria != 'Ofertas':
        lista_categorias.append(link_categoria)

for cat in lista_categorias:
    driver.get('https://www.cotodigital3.com.ar/sitios/cdigi/browse')
    categorias = driver.find_elements_by_xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li')
    for categ in categorias:
        enlace = categ.find_element_by_xpath('.//a')
        if cat == enlace.get_attribute('title'):
            enlace.click()
            subcategorias = driver.find_elements_by_xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li')
            for sub in subcategorias:
                link_subcategoria = sub.find_element_by_xpath('.//a').get_attribute('title')
                url_actual = driver.current_url.
                url_crash = url_actual.split('cdigi')
                print('url --> ', url_crash)
                categorias_COTO.append([cat, link_subcategoria])
            break

print(categorias_COTO)
'''
# categorias y subcategorias de DIA

driver.get('https://diaonline.supermercadosdia.com.ar/')

boton_categorias = driver.find_element_by_xpath('//*[@id="home-page"]/div[9]/header/div[5]/div[1]/div/nav/ul/li')
boton_categorias.click()

'''