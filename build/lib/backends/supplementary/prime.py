
import random
import math

def modular_pow(base, exponent,modulus):
	result = 1

	while (exponent > 0):
		if (exponent & 1):
			result = (result * base) % modulus
		exponent = exponent >> 1
		base = (base * base) % modulus
	
	return result

def PollardRho( n):
	if (n == 1):
		return n
	if (n % 2 == 0):
		return 2
	x = (random.randint(0, 2) % (n - 2))
	y = x
	c = (random.randint(0, 1) % (n - 1))
	d = 1
	while (d == 1):
		x = (modular_pow(x, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		d = math.gcd(abs(x - y), n)
		if (d == n):
			return PollardRho(n)
	
	return d

