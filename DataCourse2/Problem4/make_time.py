#!/usr/bin/python
import fileinput
import math
import time
import datetime
import os
from os import listdir



path = "/home/arthur/allLines/doc2-20151025/"

allLines = os.listdir("/home/arthur/allLines/doc2-20151025/")


for arq_nome in allLines:
	if "-dist.csv" in arq_nome:
		f = open(path + arq_nome,'r')
		i = 1
		temp_line = []
		conteudo = ""
		for line in f.readlines(): 
				temp = line.strip().split("\t")
				if i == 1:
					temp.append(0.0)
				else:
					t_stamp1 = time.mktime(datetime.datetime.strptime(temp_line[2], "%d\/%m\/%Y %H:%M:%S").timetuple())
					t_stamp2 = time.mktime(datetime.datetime.strptime(temp[2], "%d\/%m\/%Y %H:%M:%S").timetuple())
					resultado = float(temp_line[len(temp_line) - 1]) +  (t_stamp1 - t_stamp2)
					temp.append(resultado)
				temp_line = temp
				temp = [temp[len(temp) - 2], temp[len(temp) - 1]] 
				conteudo = conteudo + '\t'.join(str(e) for e in temp) + "\n"
				i+=1
				
		novo_arq = open(path + arq_nome.replace("-dist.csv","").replace(".csv","") + "-completo.csv" , "w+")
		novo_arq.write(conteudo.strip())
		novo_arq.close()


# i = 1
# temp_line = []
# for line in fileinput.input(): 
# 		temp = line.strip().split("\t")
# 		if i == 1:
# 			temp.append(0.0)
# 		else:
# 			t_stamp1 = time.mktime(datetime.datetime.strptime(temp_line[2], "%d\/%m\/%Y %H:%M:%S").timetuple())
# 			t_stamp2 = time.mktime(datetime.datetime.strptime(temp[2], "%d\/%m\/%Y %H:%M:%S").timetuple())

# 			temp.append(temp_line[len(temp_line) - 1] +  (t_stamp1 - t_stamp2))
# 		print '\t'.join(str(e) for e in temp)
# 		i+=1
# 		temp_line = temp
