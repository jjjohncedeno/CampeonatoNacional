# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate
import sys
try:
    url="http://www.eluniverso.com/files/widgetseu/campeonato/html/" + sys.argv[1] \
       + "/nacional/serie_" + sys.argv[2] + "/" + sys.argv[3] + "/nw_html_tablasposicionesHTML.html?r=90728021731"
    soup = BeautifulSoup(urlopen(url), 'html.parser')

    SoupPart = soup.findAll("span", { "class" : "field-content" })
    #print (SoupPart[25])
    #for i in SoupPart.find_all("span"):
    #    print (i.string)
    #par = soup.find_all("span")
    cont = 0
    t=[]
    for i in SoupPart[24:]:
        if (cont == 0):
            list=[]
            list.append(i.string)
            cont +=1
        elif (cont<3):
            list.append(i.string)
            cont +=1
        else:
            list.append(i.string)
            t.append(list)
            list=[]
            cont=0
    print (tabulate(t,headers=["Local","L","V","Visita"],tablefmt="fancy_grid"))

except:
    print ("Error")
