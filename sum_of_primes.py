def prime_sum( n ):
	"""
	Calculate the sum of first n primes
	"""
	prime_sum = 0
	so_far = 0
	i = 1
	while True:
		i += 1
		if is_prime( i ):
			prime_sum += i
			so_far += 1
		if so_far == 1000:
			return prime_sum


def is_prime( n ):
	"""
	Naive primality test
	"""
	for i in range( 2, n ):
		if n % i == 0:
			return False
	return True


print( prime_sum( 1000 ) )
