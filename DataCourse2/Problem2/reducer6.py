#!/usr/bin/env python

import sys

dupla_temp = ""
dupla_atual = ""
qtd = 0

for line in sys.stdin:
	dupla = line.split('\t')[0]
	val = line.split('\t')[1]

	if dupla_temp == "":
		dupla_temp = dupla
		dupla_atual = dupla
		qtd = int(val)
	elif dupla_temp == dupla:
		qtd = qtd + int(val)
	else:
		print "%s\t%s" % (dupla_temp,qtd)
		qtd = 1
		dupla_temp = dupla
		dupla_atual = dupla

if dupla_atual == dupla_temp:
	print "%s\t%s" % (dupla_temp,qtd)