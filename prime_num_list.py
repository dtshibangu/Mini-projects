# program lists all prime numbers to 100

# define constants
LIMIT = 100

# main function calls the is_prime function
# and displays the prime numbers
def main():
    intro()
    
    is_prime()

# intro function itroduces program
def intro():
    input( "This program will print all prime numbers 1-100" +
           "\nPress enter to continue." )

# the is_prime fucntion calculates and prints
# all of the prime numbers from 1 - 100
def is_prime():
    for prime_num in range( 1, LIMIT+1 ):
        if prime_num % 2 != 0 and prime_num % 3 != 0:
            print( prime_num, end=', ')

#call main function
main()



