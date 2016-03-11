#!/usr/bin/env python

import sys

tempo_temp = ""
tempo_autal = ""
cartoes = []


for line in sys.stdin:
	tempo = line.strip().split('\t')[0]
	cartao = line.strip().split('\t')[1]

	if tempo_temp == "":
		tempo_temp = tempo
		tempo_autal = tempo
		cartoes.append(cartao)
	elif tempo_temp == tempo:
		cartoes.append(cartao)
	else:
		print "%s\t%s\t%s" % (tempo , "-".join(cartoes) , len(cartoes))
 		tempo_temp = tempo
		tempo_autal = tempo
		cartoes = []
		cartoes.append(cartao)
if tempo_autal == tempo_temp:
	print "%s\t%s\t%s" % (tempo , "-".join(cartoes) , len(cartoes))

# def check_numCartao(mapa, codV, numC):
# 	for k in mapa.keys():
# 		if k != numC and codV in mapa[k]:
# 			print "%s\t%s" % (numC,k)

# mapa = {}
# mapaFinal = {}

# for line in sys.stdin:
# 	numero_cartao = line.split('\t')[0]
# 	cod_veic = line.split('\t')[1].strip()

# 	if not mapa:
# 		mapa[numero_cartao] = [cod_veic]
# 	else:
# 		if numero_cartao in mapa.keys():
# 			if cod_veic not in mapa[numero_cartao]:
# 				mapa[numero_cartao].append(cod_veic)
# 		else:
# 			mapa[numero_cartao] = [cod_veic]
# 		# check_numCartao(mapa, cod_veic	, numero_cartao)


# for k in mapa.keys():
# 	print "%s\t%s" %(k , mapa[k])
