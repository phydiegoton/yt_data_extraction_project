# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 01:41:39 2021

@author: Diego
"""

import eps #Es Pafy
from yt_url_research_spanish import vid_urls_spanish
from yt_url_research_english import vid_urls_english
import pandas as pd

vid_urls_spanish.pop(0)# El primer elemento de la lista es NoneType
vid_urls_english.pop(0) #El primer elemento de la lista es NoneType asi que lo quito
vid_urls_spanish=vid_urls_spanish[0:150] #Selecciono la cantidad de videos que quiero coger
vid_urls_english=vid_urls_english[0:150]# Selecciono la cantidad de video en ingles que quiero coger

#Creo las listas de caracteristicas de Pafy
title=[]
rating=[]
viewcount=[]
author=[]
length=[]
duration=[]
likes=[]
description=[] #No funciona en pafy
published=[] #No funciona en pafy
n_comments=[] #No existe en pafy
#Obtengo los dato de los urls en español
for url in vid_urls_spanish,vid_urls_english:
#url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
    for url_0 in url:
        try:
            video = eps.new(url_0)
            title.append(video.title)
            rating.append(video.rating)
            viewcount.append(video.viewcount)
            author.append(video.author)
            length.append(video.length)
            duration.append(video.duration)
            likes.append(video.likes)
            published.append(video.published)
        except:
            continue  
#Creo un Dataframe pasando la info de las listas al DataFrame y genero un Excel con los datos
vid_urls=[]
vid_urls.extend(vid_urls_spanish)
vid_urls.extend(vid_urls_english)
try:
    df=pd.DataFrame()
    df['URL']=vid_urls
    df['Título']=title
    df['Autor']=author
    df['Rating']=rating
    df['Likes']=likes
    df['Visitas']=viewcount
    df['Duración']=duration
    df.to_excel('YT_video_data.xlsx')
except:
    print("Error en las dimensiones de las listas empleadas para crear el DataFrame")