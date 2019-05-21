# write a program that assigns each word in file to dictionary pairs
# and also add what lines they are found on

def main():
    # create an empty dictionary
    word_index = {}

    # open file
    infile = open( 'this.txt', 'r' )

    get_word_index( infile, word_index )


# the get_word_index file reads each line in file
# adds each word to dictionary and tallies each word
# within file
def get_word_index( file_object, dictionary ):
    # create string to hold each word
    string = ''

    # create counter object to count each line
    index = 0

    # while line is not eof, read each line
    # submit into string
    line = file_object.readline()
    
    while line != '':
        string += line
        line = file_object.readline()

    # split every word in string
    string_list = string.split()

    # add each word to dictionary along with index
    for word in string:
        if '\n' in string:
            index += 1
        dictionary[ word ] = index

if __name__ == "__main__":
    main()
        

    
    
