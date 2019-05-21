# program displays all unique words in a text file

def main():
    # open a file
    infile = open( 'file.txt', 'r' )

    # create empty set
    unique_words = set()
    string = ''

    # read lines in text file
    line = infile.readline()

    # while line is not blank, keep
    # reading new lines
    while line != '':
        line = line.rstrip('\n' )
        string += Line
        line = infile.readline()

    # put unique words in set
    unique_words = set( string )
    print( unique_words )

# call main function
main()
        

    

        
