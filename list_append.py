# this method demonstrates how the append
# method can be used to add items to a list

def main():
    # First create an empty list
    names_list = []

    # create a variable to control the loop
    again = 'y'

    # add some names to the loop
    while again == 'y':
        # get a name from user
        name = input( "Enter a name: " )

        # append the name to a list
        names_list.append( name )

        # Add another one?
        print( "Do you want to add another name?" )
        again = input( "y = yes, anything else = no: " )
        print()

    # display the names you entered here
    print( "Here are the names that were entered:" )

    for name in names_list:
        print( name )

# call the main function
main()
