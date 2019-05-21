# this program will modify the contents of
# the numbers.txt file

import os   # needed for removing and renaming functions

def main():
    # create a bool to use when match is found
    found = False

    # get a search value
    search = input( "Enter a number to search: " ) 
    replacement = input( "Ener the replacement value: " )  

    # open the file
    numberfile = open( 'numbers.txt', 'r' )

    # open a temporary file for data switch
    tempfile = open( 'temp.txt', 'w' )

    # read a line from the numbers file
    numbers = numberfile.readline()

    # while the line isnt empty, keep scanning lines
    # until at EOF,
    while numbers != '':
        # strip pnewline character
        numbers = numbers.rstrip( '\n' )

        # determine whther this record mathced
        # the search value
        if search == numbers:
            # write the number to the temp file
            tempfile.write( replacement + '\n' )
            
            # set found value to true
            found = True
        else:
            # write orignal record to temp file
            tempfile.write( search + '\n' )

        # read the next number
        numbers = numberfile.readline()

    # close both files
    numberfile.close()
    tempfile.close()

    # delete the original numbers file
    os.remove( 'numbers.txt' )

    # rename the temporary file
    os.rename( 'temp.txt', 'numbers.txt' )

    # if the search value was not found
    if not found:
        print( "That item was not found in the file." )

# call the main function
main()
    
            
    

    
