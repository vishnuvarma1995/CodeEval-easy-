prime = []

number = 1
while len(prime)<1000:#Determine primes, and add them to list
	number +=1
	if all(number%i for i in range(2,number)):
		prime.append(number)
		
	
x=0
while len(prime)>0:#Sum all numbers in list
	x=x+int(prime.pop())
	
print x
