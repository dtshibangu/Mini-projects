# this program will generate random numbers
# for lottery then prints them

# import the random module
import random

# define constant varibles
# both up 1 for program limits
PLACE_LIMIT = 8
NUM_LIMIT = 9

def main():
    numbers = []
    lottery_num = ''

    # create for loop that appends
    # 7 random numbers to numbers[]
    for index in range( 1, PLACE_LIMIT ):
        rand_num = random.randint( 1, NUM_LIMIT )
        numbers.append( rand_num )


    # create for loop that connects
    # numbers and prints it all
    for value in numbers:
        # placeholder for numbers
        lottery_num += str( value )

        
    # print number
    print( "Your lottery number is: #", lottery_num,
           sep='' )

# call the main fucntion
main()
        
        
    
