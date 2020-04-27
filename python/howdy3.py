#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BS
#f = open('xyz.txt','w')
r = requests.get('https://stopgame.ru/review/new/stopchoice')
html = BS(r.content, 'html.parser')
for el in html.select('.lent-block'):
   
    title = el.select('.brief')
    a =  title[0].text
    print (a)



    with open('xyz.txt','w') as f:
        f.writelines("%s\n" % l for l in a)
        f.close()
#./home/sandy/python/scriptbash





















