#!/usr/bin/env python

import sys

# for line in sys.stdin:
# 	if len(line) > 1:
# 		numero_cartao = line.strip().split(',')[3].split(":")[1]
# 		cod_veic = line.strip().split(',')[2].split(":")[1]
# 		print "%s\t%s" % (numero_cartao,cod_veic)

for line in sys.stdin:
	if len(line) > 1:
		tempo = line.strip().split(',')[4].split(":")[1].replace("\"","") + ":" +line.strip().split(',')[4].split(":")[2].replace("\"","")
		cod_veic = line.strip().split(',')[2].split(":")[1]
		numero_cartao = line.strip().split(',')[3].split(":")[1]
		print tempo + "-" + cod_veic + "\t" + numero_cartao