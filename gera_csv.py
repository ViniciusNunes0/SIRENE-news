# -*- coding: utf-8 -*-
import csv
import pandas as pd
import re

textos_FAKE = []

for i in range(1,3725,1):
    file = open('sensacionalista/noticias_sensacionalista_'+str(i)+'.txt', 'r', encoding="utf-8")
    textos_FAKE.append(file.read().replace("\n",""))
file.close()

textos_VERDADE = []

for i in range(1,2456,1):
    file = open('G1-noticias/noticias_g1_scrapy_'+str(i)+'.txt', 'r', encoding="utf-8")
    textos_VERDADE.append(file.read().replace("\n",""))
file.close()

texto_verdade_sem_null = []
for noticia in textos_VERDADE:
    if noticia != '' and noticia != None and noticia != '  ':
        texto_verdade_sem_null.append(noticia)

texto_fake_sem_null = []
for noticia in textos_FAKE:
    if noticia != '':
        texto_fake_sem_null.append(noticia)

def limpa_texto(texto):
        texto = re.sub(";", " ", texto)
        texto = re.sub("\n", " ", texto)
        texto = re.sub('“', "", texto)
        texto = re.sub('”', "", texto)        
        texto = re.sub("  ", "", texto)
        
        return texto

dataSet_limpo_verdade = []
for noticia in texto_verdade_sem_null:
    dataSet_limpo_verdade.append(limpa_texto(noticia))

dataSet_limpo_fake = []
for noticia in texto_fake_sem_null:
    dataSet_limpo_fake.append(limpa_texto(noticia))


def dados_dataSet(noticia, classe):    
    datasett = pd.read_csv('noticias-sirene.csv', sep=';')    
    idd = len(datasett)    
    # ATUALZIAÇÃO DO DATASET
    with open('noticias-sirene.csv', 'a', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')       
        spamwriter.writerow([idd, noticia, classe])        
        

for i in range(0,2371,1):
    dados_dataSet(dataSet_limpo_fake[i], 1)
    dados_dataSet(dataSet_limpo_verdade[i], 0)





# DADOS DO ZERO CRIANDO PELA PRIMEIRA VEZ
with open('noticias-sirene.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['id', 'noticia', 'classificacao']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'id': '0', 'noticia': 'noticia teste', 'classificacao': '1'})
    writer.writerow({'id': '1', 'noticia': 'noticia testeeeeeeeeee', 'classificacao': '0'})



fake_br = pd.read_csv('noticias.csv', sep=';', encoding='utf-8')
fake_br.dropna(inplace=True)    

dataset_Sirene = pd.read_csv('noticias-sirene.csv', sep=';', encoding='utf-8')    
dataset_Sirene.dropna(inplace=True)    

fake_br = fake_br.drop(['id'], axis=1)


import nltk
from nltk.corpus import stopwords
from string import punctuation
        
cont_palavras_fake = 0
cont_palavras_verdade = 0

for texto, classe in fake_br.values:
    if(classe == 0):
        print("Verdade ===>", len(nltk.word_tokenize(texto)))
        cont_palavras_verdade = cont_palavras_verdade+len(nltk.tokenize.sent_tokenize(texto))
    else:
        print("fake ===>", len(nltk.word_tokenize(texto)))
        cont_palavras_fake = cont_palavras_fake + len(nltk.tokenize.sent_tokenize(texto))
    
media_palavras_verdade = cont_palavras_verdade/4739
media_palavras_fake = cont_palavras_fake/4739


media_sentencas_verdade = cont_palavras_verdade/7200
media_sentencas_fake = cont_palavras_fake/7200




