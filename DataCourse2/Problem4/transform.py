#!/usr/bin/python

file = open("dados.csv","r")

for line in file.readlines():
	print line.strip() + ',' + line.strip().split(",")[1] + '.' +line.strip().split(",")[2]