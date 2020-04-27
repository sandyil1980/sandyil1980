#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BS
#f = open('xyz.txt','w')
r = requests.get('https://stopgame.ru/review/new/stopchoice')
html = BS(r.content, 'html.parser')
for el in html.select('.lent-block'):
   
    title = el.select('.brief')
    a =  title[0].text
    #b=print (a)
    #c=str(b)
    for i in a:
        f=open('xyz.txt','w')
        f.write(i)
f.close()
#./home/sandy/python/scriptbash





















