#!/usr/bin/zsh



#получение списка компонентов ОС
rm -rf /opt/myscript/ 
mkdir /opt/myscript/
dpkg --list > /opt/myscript/list
#echo /opt/myscript/list | sed (i.+)$ > /opt/myscript/list2
echo /opt/myscript/list | sed -E ?<=^.{20}.+ > /opt/myscript/list2 
cat list2
#получение списка уязвимых компонентов с сайта NVD CVE


#поиск уязвимых компонентов из числа используемых 








