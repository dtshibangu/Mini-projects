# create a series of numbers that count from 1 to n 


def main():
    # prompt for a number 
    answer = int( input( "Enter a number: " ) ) 

    # print the function output 
=    print( "The total is:", sum_odd_series( answer ) ) 


def sum_odd_series( end ):
    # create accumulator
    odd_tot = 0

    # add numbers between 1 and end to total
    # yet skipping 2 to add by odd numbers 
    for number in range( 1, end+1, 2 ): 
            odd_tot += number 
        
    return odd_tot

# call the main function 
main()


