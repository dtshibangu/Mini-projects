# this program prompts for a series of numbers
# to be totaled together


def main():
    # create accumulator and prompt for string
    # call string_total function, and
    # print results of accumulator 
    total = 0
    num_input = input( "Enter a string of numbers: " )

    string_total( num_input, total )

    print( "The total is:", string_total( num_input, total ) )

def string_total( num_input, total ):
    # for each number in num_input,
    # convert to int and add to total
    for num in num_input:
        total += int(num)

    return total

# call the main function
main()

    
    
    
