#!/usr/bin/env python
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from unidecode import unidecode

f = open('deputados_impeachment_evang.csv','r')

deput_pend_jud = open('deput_pend_jud.txt','r')


lista_pend = []
for line in deput_pend_jud.readlines():
	temp = line.strip().split("\t")
	if len(temp) > 1:
		if len(temp[0].split(" ")) == 2:
			lista_pend.append("".join(temp[0].split(" ")))
		elif len(temp[0].split(" ")) > 2:
			nome1 = temp[0].split(" ")[0]
			nome2 = temp[0].split(" ")[1]
			lista_pend.append(nome1 + nome2)		

for line in f.readlines():
	nome_deputado  =  (line.strip()).split(";")[1]
	if "id_dep" in (line.strip()).split(";"):
		print (line.strip()) + ";" + "pendencia"
	elif nome_deputado.upper() in lista_pend:
		print (line.strip()) + ";" + "sim"
	else:
		print (line.strip()) + ";" + "nao"
		
