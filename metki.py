#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import io

'''
print ("""Выберите среду сборки
        (1) Windows
        (2) Linux/Unix """)

runit = input ('> ')        #выбор среды сборки
'''
print ("Все пути во всех файлах должны быть вида a/b/c (наклон слэша). Пути латиницей и без пробелов")
print ('Введите адрес слепка файлов до сборки')
AddrIsh = input ('> ')       ##адрес файла с логами proc mon или audit
print ('Введите адрес слепка файлов после сборки')
AddrIshAfter = input ('> ')       ##адрес файла с логами proc mon или audit

print ('Введите адрес файла фикс')
AddrFix = input ('> ')

print ('Введите адрес файла типов файлов')
AddrTipFile = input ('> ')

  

wordfix = 'Каталог'         #идентификатор начала адреса в фиксе
MassAddr = []               #массив адресов
MassAddrTip = []               #массив адресов для типов файлов
MassTi = []
TrSuccess = 'success'       #успешный/неуспешный вызов в audit
StartS = 'name="'           #триггер начала считывания адреса для auditlog
OutAud = '"'                #триггер окончания адреса лога сборки auditlog
OutS = '<'                  #триггер окончания адреса лога сборки или proc mon
OutStart1 = ':'             #триггер начала файла в фикс
OutStart2 = 'drw'
OutStart3 = '-rw'
OutStart4 = './'
OutStop = '/'               #триггер окончания файла в фикс
OutStop1 = ' '
OutStop2 = ';'
OutAddr = 'итого'           #триггер окончания фалов по данному адресу в фикс
OutAddr1 = 'файлов'         #триггер окончания фалов по данному адресу в фикс
Tilda = '~'                 

IspFiles = ['PE32','PE ','ELF','OS/360','a.out','COFF','ECOFF','XCOFF','Mach-O','SOM','AMIGA','Hunk','PEF','CMD','FlexOS','COM','MZ','NE','LE','LX','PIM','XIP','P2','P3','MP','GEOS','DL']         #исполняемые файлы
ArchFiles = ['Zip','7z','7-Zip','WAR','APK','Ar','ARC','ARJ','Ark','Bzip2','Cpio','Cabinet','DAR','Deb','Xar','RAR','RPM','Qcow2','SQX','Snappy','Tar','XZ','EAR','gzip','ISO ','JAR','MDF','Pax','Lzip','GHOST','SAR','Gzip']        #файлы архивов

'''
f = open('netvish.txt','w')           
f.close()
'''
f = open('tipfile.txt','w')            #исходники от proc mon
f.close()  
f = open('redun.txt','w')           #файлы сравнения
f.close()
''''
f = open('biggertip.txt','w')          #избыточные
f.close()
'''


'''
print ('Введите язык компиляции')
word = input ('> ')                                     #какой язык используется (java, c, py ....)'''

print ('''Введите адрес папки с исходниками в логах.
Адрес, который надо отбросить от полного пути.
для сравнения с фиксовскими значениями
Должен иметь вид a/b/c/''')
AddrP = input ('> ')                                    #адрес, который надо отбросить от полного пути. для сравнения с фиксовскими значениями

print (''''Введите адрес папки с исходниками в фикс
Адрес, который надо отбросить от полного пути.
для сравнения со значениями логов
Должен иметь вид a/b/c/''')
AddrPF = input ('> ')                                    #адрес, который надо отбросить от полного пути. для сравнения со значениями audit
FileBefore = []
FileAfter = []



with io.open(AddrFix) as file:                              #адрес файла с фиксом
    for line in file:
        namef = line[(10+len(AddrPF)):len(line)-1]
        #print (namef)
        MassAddr.append(namef)
        #MassAddrTip.append(namef)

        
with io.open(AddrTipFile) as file:                          #адрес файла с типами файлов
    for line in file:

        namef = line[len(AddrPF):line.find(OutStart1)]
        MassAddrTip.append(namef)                           #адреса типов файлов
        tipfileline = line[line.find(OutStart1)+2:len(line)-1]
        MassTi.append(tipfileline)                          #типы файлов



s=0
while s<len(MassTi):
    i=0
    while i<len(IspFiles):
        if MassTi[s].find(IspFiles[i])>=0:
            f = open('tipfile.txt','a')
            f.write (AddrPF + MassAddrTip[s] + '   ---: ' + MassTi[s] +'\n')
            f.close()
        i=i+1
    i=0
    while i<len(ArchFiles):
        if MassTi[s].find(ArchFiles[i])>=0:
            f = open('tipfile.txt','a')
            f.write (AddrPF + MassAddrTip[s] + '   ---: ' + MassTi[s] +'\n')
            f.close()
        i=i+1

    s=s+1 


i=0
namef = ''
with io.open(AddrIsh) as file:                          #адрес файла слепка файлов до сборки
    for line in file:
        
        if line == '\n':
            i=0
        elif i<5:
            startline = line[0:3]
            if startline.find(OutStart4)==0:
                namef = line[line.find(OutStart4)+2:line.find(OutStart1)]+'/'
        else:
            startline = line[0:3]
            #print (line)
            if startline.find(OutStart3)==0:
                addrfile = namef + line[line.find('2019')+18:len(line)-1]
                FileBefore.append((line[line.find('2019'):line.find('2019')+18]) + addrfile)

        i=i+1    



i=0
namef = ''
with io.open(AddrIshAfter) as file:                          #адрес файла слепка файлов после
    for line in file:
        #startline = line [0:3]
        if line == '\n':
            i=0
        elif i<5:
            startline = line [0:3]
            if startline.find(OutStart4)==0:
                namef = line[line.find(OutStart4)+2:line.find(OutStart1)]+'/'
        else:
            startline = line [0:3]
            if startline.find(OutStart3)==0:
                addrfile = namef + line[line.find('2019')+18:len(line)-1]
                FileAfter.append((line[line.find('2019'):line.find('2019')+18]) + addrfile)

        i=i+1



MassTi = []



i=0
while i<len(FileBefore):                                      #создание архива задействованных фалйов
    s=0
    n=0
    while s<len(FileAfter):
        if FileBefore[i].find(FileAfter[s])==0:
            n=1
        s=s+1
    if n==1:
        MassTi.append(FileBefore[i])
    i=i+1


i=0
while i<len(MassAddr):                                    #файлы которых нет в папке сборки
    s=0
    n=0
    while s<len(FileBefore):
        sovpadenie = FileBefore[s]
        if  MassAddr[i].find(sovpadenie[18:len(FileBefore[s])])>=0:
            n=1
        s=s+1
    if n==0:
        f = open('netvsborke.txt','a')
        f.write (MassAddr[i] +'\n')
        f.close()
        MassTi.append(MassAddr[i])
    i=i+1
MassTi.append('\n \n')

'''   
i=0
while i<len(MassTi):                                    #избыточные файлы 
    f = open('redun.txt','a')          #избыточные   fields_en.json
    f.write (MassTi[i]+'\n')
    f.close()
    i=i+1
'''

'''
#print (MassAddr)
i=0
while i<len(FileBefore):
    f = open('biggertip.txt','a')          #избыточные
    f.write (FileBefore[i]+'\n')
    f.close()
    i=i+1
'''
i=0
while i<len(FileBefore):                                    #этих файлов нет в исходниках
    s=0
    n=0
    while s<len(MassAddr):
        if  FileBefore[i].find(MassAddr[s])>=0:
            addrfile = FileBefore[i]
            FileBefore[i] = ''
        s=s+1
    if FileBefore[i] != '':
        MassTi.append(addrfile[18:len(addrfile)])
        f = open('netvish.txt','a')
        f.write (FileBefore[i] +'\n')
        f.close()
    i=i+1



   
i=0
while i<len(MassTi):                                    #избыточные файлы
    
    f = open('redun.txt','a')          #избыточные
    f.write (MassTi[i]+'\n')
    f.close()
    i=i+1

    



        
