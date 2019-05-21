# program will calcuate the future value of ones current investment

# define variables
future_val = 0.0
present_val = 0.0
monthly_interest = 0
months = 0

# main function will prompt for present value
# call the future_value function
# and print the results
def main():
    present_val = float( input( "How much is your initial investment? " ) )
    monthly_interest = float( input( "How  much is interest per month? " ) )
    months = int( input( "Enter months withholding your investment: " ) ) 

    future_value( present_val, monthly_interest, months )
    future_val = future_value( present_val, monthly_interest, months )

    print( "\nWithholding $", present_val, sep='')
    print( "for a period of", months, "months" )
    print( "at an interest rate of", monthly_interest,
           "% per month" )
    print( "yields a future value of $", format( future_val, ',.2f' ) )

# the future_value function calculates the
# future value of the initial amount per
# time and interest
def future_value( present_val, monthly_interest, months ):
    future_val = present_val * (( 1 + monthly_interest ) ** months )
    return future_val

# call the main function
main()
