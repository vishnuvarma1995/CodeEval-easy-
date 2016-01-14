from sys import argv

phrase = open(argv[1],'r')

for line in phrase:
	print line.lower()
