#!/usr/bin/env python3

#импорт нужных модулей
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://cve.mitre.org/data/downloads/allitems-cvrf-year-2020.xml')
#html = BS(r.content, 'html.parser')
#for el in html.select('.lent-block'):
    #title = el.select('.lent-title > a')
 #   title = el.select('.brief')
print (r)

#получение списка компонентов ОС


#получение списка уязвимых компонентов с сайта NVD CVE


#поиск уязвимых компонентов из числа используемых 








