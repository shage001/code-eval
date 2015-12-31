import sys

def reverse_words( string ):
	"""
	Reverse a string's words in place by reversing all the letters, then
	reversing all the letters of each word
	"""
	## strings are immutable but we'll fake it ##
	chars = list( string )

	## reverse the whole string ##
	chars = reverse_letters( string, 0, len( string ) - 1 )
	word_start = 0

	## reverese the letters in each word ##
	for i in range ( len( string ) + 1 ):
		if i == len( string ) or chars[i] == ' ':
			chars = reverse_letters( ''.join( chars ), word_start, i - 1 )
			## indicate start of new word ##
			word_start = i + 1

	return ''.join( chars )





def reverse_letters( string, i, j ):
	"""
	Reverse the letters in a string from index i to j
	"""
	chars = list( string )
	while ( i < j ):
		chars[i], chars[j] = chars[j], chars[i]
		i += 1
		j -= 1
	return chars


print( reverse_words( 'hello world' ) )
