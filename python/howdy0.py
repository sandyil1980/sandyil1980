#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BS
#f = open('xyz.txt','w')
r = requests.get('https://stopgame.ru/review/new/stopchoice')
html = BS(r.content, 'html.parser')
for el in html.select('.lent-block'):
    #title = el.select('.lent-title > a')
    title = el.select('.brief')

    print( title[0].text )
   # f = open('xyz.txt','w') 
   # f.write( title[0].text )
   # f.close()





















