from sys import argv

input = open(argv[1],'r')
alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for line in input:
	line = line.lower()
	line = list(line)
	sentence = []
	while len(line)>0:
		if line[-1] in alphabets:
			letter = line.pop()
			sentence.append(letter)
		else:
			line.pop()
			sentence.append(' ')
	new_sentence = []
	while len(sentence)>0:
		bit = sentence.pop()
		new_sentence.append(bit)
	new_sentence = ''.join(new_sentence)
	new_sentence = " ".join(new_sentence.split())
	print new_sentence.strip()
		
