from sys import argv

input = open(argv[1],'r')


for line in input:
	sum = 0
	line = line.split(',')
	
	while len(line)>0:
		number = int(line.pop())
		sum = sum+number
	print sum
	
	
