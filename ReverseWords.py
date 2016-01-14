from sys import argv

sentence = open(argv[1],'r')

for line in sentence:
	forward = line.split(" ")
	backward =[]
	while len(forward)>0:
		forward[-1] = forward[-1].strip()
		word = str(forward.pop())
		backward.append(word)
	print(' '.join(backward))
