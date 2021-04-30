import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraperCategory.items import CategoriaCoto
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from selenium import webdriver

class CategoriaSpider(CrawlSpider):
    name = 'categorias'

    driver = webdriver('/home/estebanpaz/FOEX-Proyecto-Dets/scrapping-local/chromedriver')

    driver.get('https://www.youtube.com/')

    '''
    allowed_domain = ["https://www.cotodigital3.com.ar"]

    start_urls = ["https://www.cotodigital3.com.ar/sitios/cdigi/browse"]

    rules = [
        Rule(
            LinkExtractor(allow = (),
            restrict_xpaths = ('//*[@id="atg_store_facets"]/div[1]/div/ul/li/a')), 
            callback = 'parse_item',
            follow = False
        )
    ]
    '''


def parse_item(self, response):

    item = CategoriaCoto()

    # item = ItemLoader(item=CategoriaCoto(), response=response)

    # item['categoria'] = response.xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li/a/@title').extract()
    # item['categoria'] = response.xpath('//*[@id="atg_store_refinementAncestorsLastLink"]/text()').extract()
    # item['subcategoria'] = response.xpath('//*[@id="atg_store_facets"]/div[1]/div/ul/li/a/@title').extract()

    # item.add_xpath('categoria', '//*[@id="atg_store_refinementAncestorsLastLink"]/text()')
    # item.add_xpath('subcategoria', '//*[@id="atg_store_facets"]/div[1]/div/ul/li/a/@title')

    yield item
    # item.get_output_value('categoria')
    # return item.load_item()