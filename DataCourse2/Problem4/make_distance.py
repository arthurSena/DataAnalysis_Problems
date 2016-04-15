#!/usr/bin/python
import fileinput
import math

def dist(lat1,lon1, lat2, lon2):
	return math.sqrt((float(lat1)-float(lat2))**2 + (float(lon1)-float(lon2))**2)

i = 1
temp_line = []
for line in fileinput.input(): 
		temp = line.strip().split("\t")
		if i == 1:
			temp.append(0.0)
		else:
			temp.append(temp_line[len(temp_line) - 1]+ dist(temp[1],temp[2],temp_line[1], temp_line[2]))
			# x = str(temp[len(temp) - 1])
			# temp[len(temp)-1] = 0
		print '\t'.join(str(e) for e in temp)
		i+=1
		temp_line = temp