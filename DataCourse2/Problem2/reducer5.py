#!/usr/bin/env python

import sys

def check_numCartao(mapa, codV, numC):
	for k in mapa.keys():
		if k != numC and codV in mapa[k]:
			print "%s\t%s" % (numC,k)

mapa = {}
mapaFinal = {}

for line in sys.stdin:
	numero_cartao = line.split('\t')[0]
	cod_veic = line.split('\t')[1].strip()

	if not mapa:
		mapa[numero_cartao] = [cod_veic]
	else:
		if numero_cartao in mapa.keys():
			if cod_veic not in mapa[numero_cartao]:
				mapa[numero_cartao].append(cod_veic)
		else:
			mapa[numero_cartao] = [cod_veic]
		# check_numCartao(mapa, cod_veic	, numero_cartao)


for k in mapa.keys():
	print "%s\t%s" %(k , mapa[k])
