# this program will print a user specified amount
# of random numbers to the random_numbers.txt file

# import the random module
import random

# state the variables used
num_of_rand = 0
random_num = 0

# state the constants
RAND_MAX = 500

def main():
    # create variable for user input
    num_of_rand = int( input( "Enter amount of random numbers: " ) )

    # open the file
    infile = open( 'random_numbers.txt', 'w' )

    # randomize number, writes to file as number var
    # gets too num_of_rand iterations
    for number in range( 1, num_of_rand+1 ):
        random_num = random.randint( 1, RAND_MAX ) 
        infile.write( str( random_num ) + '\n' )

    # close the file
    infile.close()
    print( "Saved in the random_numbers.txt file." ) 

# call the main function
main()
