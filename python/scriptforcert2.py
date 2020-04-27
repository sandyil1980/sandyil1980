#!/usr/bin/env python3

#импорт нужных модулей

url = 'https://codeload.github.com/fogleman/Minecraft/zip/master'
 
# downloading with requests
 
# import the requests library
import requests
 
 
# download the file contents in binary format
r = requests.get(url)
 
# open method to open a file on your system and write the contents
with open("minemaster1.zip", "wb") as code:
    code.write(r.content)
 
 
# downloading with urllib
 
# import the urllib library
import urllib
 
# Copy a network object to a local file
urllib.urlretrieve(url, "minemaster.zip")



#html = BS(r.content, 'html.parser')
#for el in html.select('.lent-block'):
    #title = el.select('.lent-title > a')
 #   title = el.select('.brief')


#получение списка компонентов ОС


#получение списка уязвимых компонентов с сайта NVD CVE


#поиск уязвимых компонентов из числа используемых 








