#!/usr/bin/env python

import sys

# for line in sys.stdin:
# 	if len(line) > 1:
# 		numCartao1 = line.split('\t')[0]
# 		numCartao2 = line.strip().split('\t')[1]
# 		temp = numCartao1 + '-' + numCartao2
# 		print "%s\t%s" % (temp,1)

mapa = {}
for line in sys.stdin:
	chave = line.split('\t')[0]
	valor = line.split('\t')[1]