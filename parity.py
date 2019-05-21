# Daniel  Tshibangu
# program identifies 100 random numbers from 1-1000
# as either odd or even

# import the random module
import random

# define odd and even counts, var to hold random numbers
odd_count = 0
even_count = 0
rand_number = 0

# define limits for 100 num and random numbers
LIMIT = 100
RANDOM_LIMIT = 1000

# main function will call te intro function
# then parity function
def main():
    intro()

    parity( even_count, odd_count )


# intro function informs user of program function
def intro():
    input( "Press enter to progress through the prompts." ) 
    input( "Welcome to the parity program!" ) 
    input( "This program takes 100 random numbers," )
    input( "and takes count of which are odd or even." )
    input( "Press enter to continue." ) 


# the parity function separates random
# numbers into odd or even and prints results
def parity( even_count, odd_count ):
    for num in range( 1, LIMIT+1 ):
        rand_number = random.randint( 1, RANDOM_LIMIT )

        if rand_number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print( "\nOut of 100 random numbers,",
           even_count, "are even and",
           odd_count, "are odd." )
    

# calls the main function
main()
