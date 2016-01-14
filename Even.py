from sys import argv

input = open(argv[1], 'r')

for number in input:
	x = int(number)
	if x%2 == 0:
		print '1'
	else:
		print '0'
