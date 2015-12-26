import sys

def fizz_buzz():
    """
	Classic fizz buzz
	"""
    test_cases = open( sys.argv[1], 'r' )
    for test in test_cases:
        if len( test ) == 0: # ignore empty line
            continue
        else:
            ## read arguments ##
            args = test.split()
            x = int( args[0] )
            y = int( args[1] )
            n = int( args[2] )

            ## count up ##
            out_string = ''
            for i in range( 1, n + 1 ):
                if i % x == 0:
                    out_string += 'F'
                if i % y == 0:
                    out_string += 'B'
                if i % x != 0 and i % y != 0:
                    out_string += str( i )
                out_string += ' '
            print( out_string.strip() )
