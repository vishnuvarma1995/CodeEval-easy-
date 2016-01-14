from sys import argv

input = open(argv[1],'r')

for number in input:
	input_number = number.split(" ")
	X = int(input_number[0])
	Y = int(input_number[1])
	N = int(input_number[2])
	count = 0
	output=[]
	while count <= N-1:
		count += 1
		if count%X==0 and count%Y==0:
			output.append('FB')
		elif count%X==0:
			output.append('F')
		elif count%Y==0:
			output.append('B')
		else:
			output.append(str(count))
	print(' '.join(output))
	
input.close
