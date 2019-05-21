# this program assigns random numbers to
# a ttwo dimensional list
import random

# constants for rows and columns
ROWS = 3
COLS = 4

def main():
    # create a two-dimensional list
    '''values = [ [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0] ]'''

    # or you could do it this way
    values = [ [0] * 4,
               [0] * 4,
               [0] * 4 ]
               

    # fill the list with ranodm numbers
    for r in range( ROWS ):
        for c in range( COLS ):
            values[r][c] = random.randint( 1, 100 )

    # display the ranodm numbers
    print( values )

# call the main function
main()
