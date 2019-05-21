# This program displays property taxes

TAX_FACTOR = 0.0065     #Represents tax factor

# Get the first lot number
print( 'Enter the property lot number' )
print( 'or rnter 0 to end.' )
lot = int( input( 'Lot number: ' ) )

# continue processing as long as the user
# does not enter lot number 0
while lot != 0:
    #Get the property tax
    tax = value * TAX_FACTOR

    #Display the tax
    print( 'Property tax: $', format( tax, '.2f' ), sep=' ' )

    #get the next lot number
    print( 'Enter the next lot number or' )
    print( 'enter 0 to end.' )
    lot = int( input( 'Lot number: ' ) ) 
