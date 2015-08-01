# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate
url="http://www.eluniverso.com/files/widgetseu/campeonato/html/2015/nacional/serie_a/fase_2/nw_html_tablasposicionesHTML.html?r=90728021731"
soup = BeautifulSoup(urlopen(url), 'html.parser')
tabla = soup.find("ul")
cont=0
TPos=[]
for i in tabla.find_all("span"):
    if (cont==0):
        t = []
        t.append(i.string)
        cont +=1
    elif (cont<9):
        t.append(i.string)
        cont +=1
    else:
        t.append(i.string)
        TPos.append(t)
        cont=0
print(tabulate(TPos,headers=["Pos","Equipo","PJ","PG","PE","PP","GF","GC","PUNTOS","GD"],tablefmt="fancy_grid"))

#left = soup.find(id="col_left")
#print (left.find_all("ul"))
