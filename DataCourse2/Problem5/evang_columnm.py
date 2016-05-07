#!/usr/bin/env python
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from unidecode import unidecode

f = open('deputados_temas_e_impeachment_v1.1.csv','r')

evang = open('deput_evang_lista.txt','r')

lista_evang = []
for nome in evang.readlines():
		nome_formatado = (nome.strip()).split(" ")[0:2]
		if "(" not in nome_formatado[1]:
			temp1 = nome_formatado[0]
			temp2 = nome_formatado[1] 
			nome_sobrenome = temp1 + temp2
			nome_sobrenome
			lista_evang.append(nome_sobrenome)
		else:
			temp1 = nome_formatado[0]
			nome_sem_sobrenome = temp1
			lista_evang.append(nome_sem_sobrenome)

for line in f.readlines():
	nome_deputado  =  (line.strip()).split(";")[1]
	if "id_dep" in (line.strip()).split(";"):
		print (line.strip()) + ";" + "evangelico"
	elif nome_deputado.upper() in lista_evang:
		print (line.strip()) + ";" + "sim"
	else:
		print (line.strip()) + ";" + "nao"
		
