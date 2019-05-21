# this program will display the number of
# strings stored in the names.txt file

def main():
    # create variable for counting names
    name_count = 0
    
    # open the file
    namefile = open( 'names.txt', 'r' )

    # read the first name
    given_name = namefile.readline()

    while given_name != '':
        # strip the newline
        given_name = given_name.rstrip( '\n' )

        # increase the name counter
        name_count += 1

        # read the next string
        given_name = namefile.readline()

    # close the file
    namefile.close()

    # print the total number of strings
    print( "This file has", name_count, "items." )

# call the main function
main()
