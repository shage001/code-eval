# print( 929 )
# just kidding

def prime_palindrome():
	"""
	Print the largest prime palindrome < 1000
	"""
	for i in range( 1000, 1, -1 ):
		## palindrome check first because it's faster ##
		if is_palindrome( i ) and is_prime( i ):
			return i


def is_palindrome( n ):
	"""
	Palindrome check
	"""
	middle = len( str( n ) ) // 2
	for i in range( middle ):
		if str( n )[i] != str( n )[-i-1]:
			return False
	return True


def is_prime( n ):
	"""
	Naive primality test
	"""
	for i in range( 2, n ):
		if n % i == 0:
			return False
	return True


print( prime_palindrome() )
