#!/usr/bin/env python

import sys

numeroCartao_temp = ''
value_temp = 0
numeroAtual = ''

for line in sys.stdin:
	numeroCartao = line.split('\t')[0]
	value = line.split('\t')[1]
	
	if numeroCartao_temp == '':
		numeroCartao_temp = numeroCartao
		value_temp = int(value)
		numeroAtual = numeroCartao
	elif numeroCartao_temp == numeroCartao:
		value_temp = value_temp + int(value)
	else:
		print "%s\t%s" % (numeroCartao_temp, value_temp)
		numeroCartao_temp = numeroCartao
		value_temp = int(value)
		numeroAtual = numeroCartao
if numeroAtual == numeroCartao_temp:
	print "%s\t%s" % (numeroCartao_temp, value_temp)