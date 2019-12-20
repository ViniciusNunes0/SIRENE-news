# -*- coding: utf-8 -*-
# scrapy runspider geraNoticias_g1.py

import scrapy

class SensacionalistaSpider(scrapy.Spider):
    name = 'sensacionalista'
    i = 0 
    
    def start_requests(self):
        file = open('links_Sensacionalista.txt', 'r', encoding="utf-8")
        links = file.readline()      
        links = links.split(',')
        for url in links:
            yield scrapy.Request(url=url, callback=self.parse)
        file.close()

    def parse(self, response):        
        self.i = self.i+1
        textos = response.css('p ::text').extract()
        file = open('noticias_sensacionalista_'+str(self.i)+'.txt', 'w', encoding="utf-8")        
        file.writelines(textos)
        file.close()
        