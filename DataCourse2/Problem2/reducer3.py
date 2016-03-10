#!/usr/bin/env python

import sys

linha_temp = ''
veic_temp = []
linha_atual = ''

for line in sys.stdin:
	linha = line.split("\t")[0]
	veic = line.split("\t")[1]

	if linha_temp == '':
		linha_temp = linha
		veic_temp.append(veic)
		linha_atual = linha
	elif linha_temp == linha:
 		if veic not in veic_temp:
 			veic_temp.append(veic)
 	else:
 		print "%s\t%s" % (linha_temp, len(veic_temp))
 		linha_temp = linha
 		veic_temp = []
 		veic_temp.append(veic)
 		linha_atual = linha

if linha_atual == linha_temp:
	print "%s\t%s" % (linha_temp, len(veic_temp))
