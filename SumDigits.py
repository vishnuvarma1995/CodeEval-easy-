from sys import argv

input = open(argv[1],'r')

for number in input:#get number in in line of input
	number = str(number)
	digits = list(number)
	if digits[-1] == '\n':#get rid of \n at end of lists
		digits.pop()
	
	
	sum = 0
	while len(digits)>0:
		sum=sum+int(digits[-1])#sum digits
		digits.pop()
	print sum
