#!/usr/bin/python
import fileinput

i = 0

for line in fileinput.input(): 
	if i != 0:

		temp = line.strip().replace("}","").replace("{","").replace('"COD_LINHA":',"").replace('"NOMELINHA":',"").replace('"CODVEICULO":',"").replace('"NUMEROCARTAO":',"").replace('"DTHR":',"").replace("\"","").replace("VEIC:","").replace("LAT:","").replace("LON:","")
		temp = temp.split(",")
		
		# print temp
		lat = temp[1] + "." + temp[2]
		lon = temp[3] + "." + temp[4]
		temp[1] = lat
		temp[2] = lon
		# temp = temp[-2]
		temp.remove(temp[3])
		temp.remove(temp[3])
		# print temp
		print "\t".join(temp[0:len(temp)])
	i += 1
