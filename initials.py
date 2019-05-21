# this program gets title data from user and
# prints the data

# the main function gets a first, middle and
# last name from user, passing them as arguments
# for get_initials functions. Initial name 
# entered and the initials of name printed
def main():
    first = input( "Enter first name: " )
    middle = input( "Enter middle name: " )
    last = input( "Enter last name: " )

    get_initials( first, middle, last )

    print( "Initial name:", first, middle, last )
    print( "Initials:", get_initials( first, middle, last ) )

# the get_initials function gets first, middle,
# last names as arguments and returns a string
# containing each inital 
def get_initials( first, middle, last ):
    initials = ''

    first = first[0].upper() + '.'
    middle = middle[0].upper() + '.'
    last = last[0].upper() + '.'

    initials += first + middle + last

    return initials

# call main function
main()
        
    
    
