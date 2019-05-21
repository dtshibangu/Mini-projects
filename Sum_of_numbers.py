# this program will print the sum of values
# from the number.txt file

def main():
    #create varibale for sum
    total = 0

    # opne the file
    numberfile = open( 'numbers.txt', 'r' )

    # read the first line
    number = numberfile.readline()

    # while the line is not at EOF then
    # convert each vlaue to int and add to sum
    while number != '':
        # strip the newline
        number = number.rstrip( '\n' )

        # convert and add to sum
        total += int( number )

        # read the next line
        number = numberfile.readline()

    # close the file
    numberfile.close()

    # print the sum
    print( "The sum of all numbers in 'numbers.txt' is:", total ) 

# call the main function
main()


        

        
