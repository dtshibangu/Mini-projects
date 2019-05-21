# this program will display the total sales for
# the days of the week

# DAYS_OF_WEEK is used as a constant for the
# size of the list
DAYS_OF_WEEK = 7

def main():
    # create the list for days of the week
    sales = [0] * DAYS_OF_WEEK

    # define the accumulator
    total = 0.0

    # get the sales for each day of the week
    for index in range( DAYS_OF_WEEK ):
        print( "Enter sales for day", index+1,
               ": ", end='' )
        sales[ index ] = float( input() )

    # Get the total sales for the week
    for value in sales:
        total += value

    # print the values
    print( "The total is: $", format( total, ',.2f'),
           sep='' )

# call the main function
main()
