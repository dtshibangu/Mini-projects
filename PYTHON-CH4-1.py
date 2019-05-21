bugs = 0
total_bugs = 0

for num in range( 1, 5 ):
    if bugs < 0:
        num = num - 1
        print( "Incorrect Input!" )
        bugs = 0
        print( "Enter number of bugs collected: " )

    print( "Day", num ) 
    bugs = int( input( "Enter number of bugs collected: " ) )
    total_bugs += bugs

print( "Total amount of bugs collected:", total_bugs )

