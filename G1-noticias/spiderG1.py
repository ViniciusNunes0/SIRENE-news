# -*- coding: utf-8 -*-
# scrapy runspider spiderG1.py
import scrapy

class GloboSpider(scrapy.Spider):
    name = 'globo'
    def start_requests(self):
        
        urls = []
        for i in range(2,250):
            urls.append('https://g1.globo.com/index/feed/pagina-'+str(i)+'.ghtml')
        urls.append('https://g1.globo.com')   
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.page = response.url.split("/")[-2]
        file = open('links_G1.txt', 'a')
        for noticia in response.css('div.bastian-page'):
            link = str(noticia.css('div.feed-post-body-title a::attr(href)').extract())
            file.write(link)
        file.close()
        
        