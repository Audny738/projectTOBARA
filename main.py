def main():

	# lista de mintérminos.
	fun = [ 0, 3, 12, 15 ];
	var = 4
	
	Kmap = getKmap( var, fun )

	for i in Kmap:
		
		print( i )

def getKmap( var, fun ):
	
	Kmap = [  ]
	
	for i in range( var ):
		
		Kmap.append( [ ] )
		
		for j in range( var ):
		
			Kmap[ i ].append( 0 )

	for i in fun:
		
		x = ( i ) // var
		
		y = ( i ) % var
		
		Kmap[ y ][ x ] = 1
		
	return Kmap
		
if __name__ == "__main__":

    main()
