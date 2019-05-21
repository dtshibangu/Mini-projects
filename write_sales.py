# this program prompts the user for sales amounts
# and writes those amounts to the sales.txt file

def main():
    # get the number of days
    num_days = int( input( "For how many days do " +
                           "you have sales? " ) )

    # open a file
    sales_file = open( 'sales.txt', 'w' )

    # get the amount of sales for each day and write
    # it to file
    for count in range( 1, num_days+1 ):
        # get the sales for each day
        sales = float( input( "Enter the sales for " +
                              str(count) + ': ' ) )

        # write the sales amount to file
        sales_file.write( str(sales) + '\n' )

    # close the file
    sales_file.close()
    print( "Data written to sales.txt" )

# call the main function
main()
