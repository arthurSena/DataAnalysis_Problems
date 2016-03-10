#!/usr/bin/env python

import sys

for line in sys.stdin:
	if len(line) > 1:
		numero_cartao = line.strip().split(',')[3].split(":")[1]
		cod_veic = line.strip().split(',')[2].split(":")[1]
		print "%s\t%s" % (numero_cartao,cod_veic)
