#!/usr/bin/env python

import sys

for line in sys.stdin:
	if len(line) > 1:
		cod_linha = line.strip().split(',')[1].split(":")[1]
		print "%s\t%s" % (cod_linha,1)