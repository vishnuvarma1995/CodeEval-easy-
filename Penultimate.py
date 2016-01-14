from sys import argv

input = open(argv[1],'r')

for line in input:
	line = line.split()
	print line[-2]
