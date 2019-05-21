# This program will prmpt for distance in km
# then convert distace to miles by formula
# miles = kilometers * 0.6214

# define variables
miles = 0.0
kilometers = 0.0

# define miles constant
K_FACTOR = 0.6214

# main will prompt for kilometers,
# use km to miles funtion
# print result
def main():
    kilometers = float( input( "Enter number of kilometers: " ) )

    km_to_miles( kilometers )

    print( format( km_to_miles( kilometers ), '.3f' ) )

# takes argument, returns miles 
def km_to_miles( kilometers ):
    miles = kilometers * K_FACTOR
    return miles

# call main function
main()
