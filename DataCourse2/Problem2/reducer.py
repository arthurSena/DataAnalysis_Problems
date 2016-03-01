#!/usr/bin/env python

# head -n 1000 doc1-2015102121.txt  | ./mapper.py | sort -k1,1 | ./reducer.py | sort -k2 -n

import sys

value_temp = 0
cod_linha_temp = ''
cod_linha_atual = ''

for line in sys.stdin:
	cod_linha = line.split('\t')[0]
	value = line.split('\t')[1]

	if cod_linha_temp == '':
		cod_linha_temp = cod_linha
		cod_linha_atual = cod_linha
		value_temp = value_temp + int(value) 
	elif cod_linha_temp == cod_linha:
		value_temp = value_temp + int(value)
	else:
		print "%s\t%s" % (cod_linha_temp,value_temp)
		cod_linha_temp	= cod_linha
		value_temp = 0
		cod_linha_atual = cod_linha

if cod_linha_atual == cod_linha_temp:
	print "%s\t%s" % (cod_linha_temp,value_temp)