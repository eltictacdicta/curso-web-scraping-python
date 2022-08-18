import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath('//h1/text()').get()
        #countries = response.xpath('//td/a/text()').getall() #para sacar el texto de los paises
        countries = response.xpath('//td/a') #para sacar el html a cada uno de los paises

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            #link_absolute = f'https://www.worldometers.info{link}'
            link_absolute = response.urljoin(link)
            #yield scrapy.Request(url=link_absolute)
            yield response.follow(url=link, callback=self.parse_coutry, meta={'country':country_name})

    def parse_coutry(self, response):
        #response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        country = response.request.meta['country']
        rows = response.xpath('(//table[contains(@class,"table")])[1]/tbody/tr')
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            poblation = row.xpath('.//td[2]/strong/text()').get()

            yield{
                'country':country,
                'year':year,
                'poblation':poblation
            }