import scrapy
import pandas as pd

frases_lista = []

class ParascrapearSpider(scrapy.Spider):
    name = 'parascrapear'
    allowed_domains = ['parascrapear.com']
    start_urls = ['http://parascrapear.com/']

    def parse(self, response):
        print('Parseando ' + response.url)       
        
        next_urls = response.css('a::attr(href)').getall()
        for next_url in next_urls:
            if next_url is not None:
                yield scrapy.Request(response.urljoin(next_url))
        
        frases = response.css('q::text').getall()
        for frase in frases:
            if frase is not frases_lista:
                frases_lista.append(frase)
        df_frases = pd.DataFrame({"Frases":frases_lista})
        df_frases.to_csv("frases.csv",index=False)
    
# Para la ejecución en este tutorial se ha usado el siguiente comando: scrapy runspider --nolog parascrapear.py