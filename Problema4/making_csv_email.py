#!/usr/bin/python

emails = open("email.txt","r")

linhas = []

for lines in emails:
	print ",".join(lines.strip().split("\t"))
