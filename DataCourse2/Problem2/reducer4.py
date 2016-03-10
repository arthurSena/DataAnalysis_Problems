#!/usr/bin/env python

import sys

veic_temp = ''
lista = []

for line in sys.stdin:
	veic = line.split("\t")[0]

	if veic_temp == '':
		veic_temp = veic
		lista.append(veic_temp)
		veic_atual = veic
	elif veic_temp != veic:
		lista.append(veic_temp)
		veic_temp = veic

print len(lista)