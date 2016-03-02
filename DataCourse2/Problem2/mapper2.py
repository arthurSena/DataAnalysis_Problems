#!/usr/bin/env python

import sys

for line in sys.stdin:
	if len(line) > 1:
		numeroCartao = line.strip().split(',')[3].split(":")[1]
		print "%s\t%s" % (numeroCartao, 1 )