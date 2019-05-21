# this program will search for records
# in the numbers.txt file

def main():
    # create a bool to use when a match is found
    found = False

    # get the search value
    search = input( "Enter a description to search: " )

    # open the number's file
    numberfile = open( 'numbers.txt', 'r' )

    # read the first record's description field
    numbers = numberfile.readline()

    while numbers != '':
        # strip the newline character
        numbers = numbers.rstrip( '\n' )

        # determine whether this record matches
        # the search value
        if search == numbers:
            print( "NUmber from file:", search )
            # set the found flag to true
            found = True

        # read the next file
        numbers = numberfile.readline()

    # close the file
    numberfile.close()

    # if the search value was not found in the file
    # display a message
    if not found:
        print( "That item was not found in the file." )

# call the main function
main()
           

        
