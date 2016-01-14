#Write a program which determines the largest prime palindrome less than 1000
prime = []

number = 10
while number<1000:#Determine primes, and add them to list
	number +=1
	if all(number%i for i in range(2,number)):
		prime.append(number)


palindrome =[]
while len(prime)>0:#Determine which primes are also palindromes
	prime_number = str(prime.pop())
	prime_digit = prime_number.split()
	if prime_number[0]==prime_number[-1]:
		palindrome.append(prime_number)
	else:
		pass


while len(palindrome) > 1:#Get the largest palindrome, which is the first value in the list
	palindrome.pop()

largest_palindrome = int(palindrome.pop())
print largest_palindrome
