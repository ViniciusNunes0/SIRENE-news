# -*- coding: utf-8 -*-
# scrapy runspider spiderG1.py
import scrapy

class SensacionalistaSpider(scrapy.Spider):
    name = 'Sensacionalista'
    def start_requests(self):
        urls = []
        for i in range(2,100):
            urls.append('https://www.sensacionalista.com.br/pais/page/'+str(i)+'/')
            urls.append('https://www.sensacionalista.com.br/esportes/page/'+str(i)+'/')
            urls.append('https://www.sensacionalista.com.br/entretenimento/page/'+str(i)+'/')
            urls.append('https://www.sensacionalista.com.br/mundo/page/'+str(i)+'/')
            urls.append('https://www.sensacionalista.com.br/digital/page/'+str(i)+'/')
        urls.append('https://www.sensacionalista.com.br/pais/')   
        urls.append('https://www.sensacionalista.com.br/esportes/')
        urls.append('https://www.sensacionalista.com.br/mundo/')
        urls.append('https://www.sensacionalista.com.br/digital/')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file = open('links_Sensacionalista.txt', 'a')
        links = response.css('div.td-block-span6 a::attr(href)').extract()
        for link in links:
            file.write(link+",")
        file.close()
        
        
