#!/usr/bin/env python

import sys

for line in sys.stdin:
	if len(line) > 1:
		veic = line.strip().split(',')[2].split(":")[1]
		print "%s\t%s" % (veic , 1)