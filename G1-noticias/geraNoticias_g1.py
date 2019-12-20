# -*- coding: utf-8 -*-
# scrapy runspider geraNoticias_g1.py

import scrapy

class GloboSpider(scrapy.Spider):
    name = 'globo'
    i = 0 
    
    def start_requests(self):
        file = open('links_G1.txt', 'r', encoding="utf-8")
        links = file.readline()      
        links = links.split(',')
        for url in links:
            yield scrapy.Request(url=url, callback=self.parse)
        file.close()

    def parse(self, response):        
        self.i = self.i+1
        textos = response.css('p.content-text__container::text').extract()
        file = open('noticias_g1_scrapy_'+str(self.i)+'.txt', 'w', encoding="utf-8")        
        file.writelines(textos)
        file.close()
        














#import urllib3   
#from bs4 import BeautifulSoup
#
#file = open('noticias_g1_scrapy.txt', 'r', encoding="utf-8")
#links = file.readlines()
#
#link_noticia = []
#for link in links:
#    link_noticia = link.split(',')
#len(link_noticia)
#
#noticias = []
#http = urllib3.PoolManager()
#for i in range(len(link_noticia) - 1):
#    pagina = http.request('GET', link_noticia[i])
#    if pagina.status == 200:
#        sopa = BeautifulSoup(pagina.data, "html")
#        #sopa.title.string          
#        for tags in sopa(['strong','title','h1','script', 'style', 'a','nav','link', 'span', 'ol','iframe', 'figcaption', 'figure','img', 'li', ]): #limpar lixo das tags
#          tags.decompose()          
#          conteudo = ' '.join(sopa.stripped_strings) #->stripped_strings->remove os espaços em branco
#        
#        conteudo = conteudo+"\n"
#        noticias.append(conteudo)
#
#
#
#file = open('noticias_g1.txt', 'w', encoding="utf-8")
#file.writelines(noticias)
#file.close()
#
#file = open('noticias_g1.txt', 'r', encoding="utf-8")
#noticias_teste = file.readlines()
