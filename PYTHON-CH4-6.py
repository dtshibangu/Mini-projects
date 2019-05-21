# program uses loop to display temp table

# state the varibles
fahrenheit = 0.0
celcius = 0.0

# state constants
BASE = 32
RATE = 9/5

# set up format 
print( "Celcius\tFahrenheit" )
print( "----------------------------" ) 

# provide loop for celcius values 
for celcius in range( 0, 21 ):
    #define fahrenheit equation 
    fahrenheit = ( RATE + celcius ) + BASE
    # print ceclius in and fahrenheit output 
    print( celcius, '\t', fahrenheit ) 
