from sys import argv

input = open(argv[1],'r')
for line in input:
	line =line.strip()
	line = line.split(',')
	x = 2
	original = int(line[1])
	new = int(line[1])
	while new<int(line[0]):
		new = original*x
		x+=1
	else:
		print new
